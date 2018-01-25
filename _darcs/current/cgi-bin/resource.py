#!/usr/bin/python

import cgitb; cgitb.enable()

import sys, os, cgi

from tempfile import mkstemp
from cStringIO import StringIO

sys.path.append('/home/b/befallen/rdflib-2.0.6/')

from rdflib.URIRef import URIRef
from rdflib.Literal import Literal
from rdflib.Namespace import Namespace
from rdflib.TripleStore import TripleStore

form = cgi.FieldStorage()

def convert(data, informat, outformat, infile=None, outfile=None):
    if infile is None: infile = mkstemp()[1]
    if outfile is None: outfile = mkstemp()[1]

    f = open(infile, 'w')
    f.write(data)
    f.close()

    os.system('/home/h/hastrup/bin/rapper -q -i %s -o %s %s > %s' %
              (informat, outformat, infile, outfile))

    f = open(outfile, 'r')
    data = f.read()
    f.close()

    os.remove(infile)
    os.remove(outfile)

    return data

if not form.has_key('description'):
    print 'Content-Type: text/html\r'
    print '\r'
    print "<H1>Error</H1>"
    print "Please fill in the 'description' field with an appropriate Turtle graph."

else:
    tmpfile = mkstemp()[1]
    data = convert(form['description'].value, 'turtle', 'ntriples', infile=tmpfile)
    
    graph = TripleStore()
    graph.parse(StringIO(data), format='nt')

    thisURI = URIRef('http://%s%s' % (os.environ['HTTP_HOST'],
                                      os.environ['REQUEST_URI']))

    graphNode = URIRef('file://%s' % tmpfile)

    FOAF = Namespace("http://xmlns.com/foaf/0.1/")
    
    try:
        bnode = graph.objects(graphNode, FOAF["primaryTopic"]).next()
    except StopIteration:
        print 'Content-Type: text/plain\r'
        print '\r'
        print 'no primary topic given'

    graph2 = TripleStore()

    for (s,p,o) in graph.triples((None, None, None)):
        if (s,p,o) == (graphNode, FOAF["primaryTopic"], bnode): continue

        if s == bnode: s = thisURI
        if o == bnode: o = thisURI

        graph2.add((s,p,o))

    http_accept = os.environ['HTTP_ACCEPT']
    accepts = []    # pairs (quality, type)

    for acc in http_accept.split(','):
        parts = acc.split(';')
        type = parts[0].strip().lower()
        
        for part in parts[1:]:
            eq = part.find('=')
            if eq >= 0 and part[:eq].strip() == 'q':
                quality = float(part[eq+1:])
                break
            else:
                quality = 1
                break
        else:
            quality = 1

        accepts.append((quality, type))

    accepts.sort()

    for (quality, type) in accepts:
        if type in ['*/*', 'application/*', 'application/x-turtle']:
            content_type = 'application/x-turtle'
            out_format = 'ntriples'
        elif type == 'application/turtle':
            content_type = 'application/turtle'
            out_format = 'ntriples'
        elif type == 'application/rdf+xml':
            content_type = 'application/rdf+xml'
            out_format = 'rdfxml'
        elif type in ['text/*', 'text/html']:
            content_type = 'text/html'
            out_format = 'html'
        elif type == 'text/plain':
            content_type = 'text/plain'
            out_format = 'ntriples'
        else:
            content_type = 'text/html'
            out_format = 'html'

    print 'Content-Type: %s\r' % content_type
    print '\r'
    if out_format != 'html':
        print convert(graph2.serialize(format='xml'), 'rdfxml', out_format)
    else:
        print 'The resource identified by this URI is described'
        print 'by the following RDF graph:'
        print '<p>'
        print '<code>'
        
        text = convert(graph2.serialize(format='xml'), 'rdfxml', 'ntriples')
        text = '&amp;'.join(text.split('&'))
        text = '&lt;'.join(text.split('<'))

        print text

        print '</code>'
