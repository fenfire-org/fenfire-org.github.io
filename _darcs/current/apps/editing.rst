====================
Browsing and editing
====================

Fenfire can be currently used to browse and edit data in RDF
documents. You can look inside RDF files, follow links to Semantic Web
resources (in RDF/XML or Turtle format), change information locally
and author new content. Fenfire supports RDF/XML and Turtle file
formats.


Looking inside RDF files
========================

Ask us for a prepackaged snapshot version of Fenfire, or follow
the `Getting started`_ notes meant for developers for now.

.. _Getting started: ../doc/devel.html#getting-started

Start a Fenfire snapshot with ``java -jar snapshot.jar some-rdf-file`` 
or one that you compiled yourself with 
``( cd fenfire && make run FILE="some-rdf-file")``. In case of XML
files, please prepend "-xml ". You should see the
browser starting at some item from the file, and a list of properties
connected to that node. 

Keyboard navigation works by first selecting a property with up and
down arrow keys and then following an inverse property left with the
left arrow key or a positive property right with the right arrow key.

Mouse navigation works by left-clicking any node you want to browse
to. If there are more properties than fit the window you can scroll
down by clicking some property line at the bottom to focus it.

In addition to the default PropertyListView, there can be other views
that are able to show surroundings of the current node. In that case,
the right sidebar will list these views and allow you to switch to
them with a mouse click or with a keyboard shortcut (given at the
bottom of the left sidebar).


Following links to Semantic Web resources
=========================================

At the bottom of the left sidebar, there is a keyboard shortcut to
load RDF data from the web. For this to work, the data must be available from
the http URI of the current node or of a node that is linked to the
current node as an ``rdfs:seeAlso`` property. There are some suitable
starting points in demo data that is shown if you *don't* specify a
file name on startup.

For instance, you can navigate to a node that says "Danny's FOAF file"
on it. If you now try to load RDF data from the web, you should get
new links that lead to Daniel Ayers's Friend-of-a-Friend Semantic Web
information. This information contains pointers to more resources that
you can load in the same way.

Another example node says "CaptSolo's blog" on it. This resource is
in HTML but an ``rdfs:seeAlso`` is included to an RSS feed of the same
information. If you choose to load RDF data, the weblog feed is
displayed and you can read the entries.

A third example is "Fenfire project" and for that there is
Description-of-a-Project (DOAP) information available.

If you want to try a resource of your own, you can do that by applying
shortcuts "go to [node]" and "a node given by URI". The latter then
asks you to provide the URI your resource has information on. If the
URI to fetch the data is different, you can add an ``rdfs:seeAlso``
property like there was for the weblog example.


Changing information locally
============================

Whenever Fenfire is running, there is some RDF file it considers
primary and suitable for saves. If you gave file names on startup, the
first of those is taken. Otherwise, a temporary file name has been
designated. Whenever you apply the shortcut to save the graph, this
file is saved with any changes you've made. Even if you've made
changes to information that has been loaded from the web, these
changes are saved to this one and same file.

Whenever a literal property is selected, it can be edited with normal
keys: arrow keys left and right, backspace, letters, numbers etc. If
the text on a node is derived from this literal, it changes at the
same time.

To add a new property, use the keyboard shortcuts to "connect on [prop]
to [node]" or "connect backwards on [prop] to [node]". After this, you
should select a property from the list on the left sidebar by pressing
down Alt and typing the three-letter shortcut given in parentheses
after the property name. The last step is to select the node: To
create a new resource, use "a new node". To create a new literal, use
"a new literal". To use an existing node, browse to that node and use
"this node". You can also type the URI with "a node given by URI".

To remove properties, there are shortcuts similar to following links
that break a link instead.


Authoring new content
=====================

If you start with a new or empty file, Fenfire will create two nodes
for you to begin with. One of them is an initially empty "home" or
"start" node for you, the other represents the file itself and is
used to declare the start node, but can also be used to give any other
metadata about the document. You can use the editing features
described in the previous section to create new content. 

One possible way to proceed is to connect a few new nodes to the start
node with the general ``sl:structLink`` property. You can put text on
them with any text property such as the general ``rdfs:label``. Later,
you can describe connections between the nodes and use more specific
properties if applicable.

Properties that are not on the list yet can be entered with the shortcut 
"a node given by URI" for the first time. You can also create new
properties as new nodes and start to use them as properties with help
of the shortcut "this node".

We don't yet provide any special support for schemas or ontologies,
although you can browse them in RDF format. Considering namespaces,
Fenfire comes with a set of predefined ones and also utilises any
namespaces in the loaded files. If you save a file and would like it
to use additional namespace shorthands, you can edit the definitions
in using some other tool and Fenfire will honour them after that.


