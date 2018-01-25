#
# Copyright (c) 2003-2004 by Benja Fallenstein
# 
# This is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
# 
# You should have received a copy of the GNU General
# Public License along with this file; if not, write to the Free
# Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA  02111-1307  USA
# 

#
# Written by Benja Fallenstein
#

import re, os

from add_texture import relative_path

def dbg(s):
    print '[add_navbar]', s

class Tree:
    re_title = re.compile("<title>(.*)</title>")

    def __init__(self, dir):
        self.root = dir
        self.files = []
        self.name = None

        if self.root != '':
            dirlist = os.listdir(self.root);
        else:
            dirlist = os.listdir('.')
            
        dirlist.sort()

        for el in dirlist:
            el = os.path.join(self.root, el)
            if os.path.isdir(el):
                if os.path.exists(os.path.join(el, 'index.rst')):
                    self.addDir(el)
            elif os.path.splitext(el)[1] == '.html':
                self.addFile(el)
    
    def addFile(self, filename, contents=None):
        if contents is None:
            file = open(filename)
            contents = file.read()
            file.close()
        
        match = self.re_title.search(contents)
        if not match:
            dbg(("File %s skipped: It does not contain "
                   "a <title>.") % filename)
            return

        name = match.group(1)
        
        if os.path.basename(filename) == 'index.html':
            self.name = name

        self.files.append([filename, name])

    def addDir(self, dir):
        t = Tree(dir)
        if len(t.files) > 0 or t.name != None:
            self.files.append([dir, t.name, t])

    def prettyprint(self, indent=""):
        for el in self.files:
            dbg("%s%s [%s]" % (indent, el[1],
                               os.path.basename(el[0])))
            if len(el) > 2:
                el[2].prettyprint(indent+"  ")

    def getFiles(self):
        list = []
        for el in self.files:
            if len(el) == 2: list.append(el[0])
            else: list.extend(el[3].getFiles())

def simpleNavbar(tree, filepath, indent=""):
    s = ""
    for el in tree.files:
        if el[0].endswith('index.html'): continue
        if el[0] == filepath or el[0]+"/index.html" == filepath:
            s += '<li class="boxitem">%s' % el[1]
        else:
            s += '<li class="boxitem"><a href="%s">%s</a>' % \
                 (relative_path(filepath, el[0]), el[1])
        if len(el) > 2:
            s += "<ul>\n"
            s += simpleNavbar(el[2], filepath, indent+"&nbsp;&nbsp;")
            s += "</ul>\n"
        s += '</li>\n'
    return s

def getBar(tree, filepath):
    bar = '<!-- NavBar begin -->\n<hr class="footer" />\n'
    bar += '<center class="navigation-title">Navigation</center>\n'
    bar += '<div class="left">\n'
    bar += '<div class="left-bar">\n'
    if filepath == "index.html":
        bar += '<p class="boxhead">%s</p>\n' % tree.name
    else:
        bar += ('<p class="boxhead"><a href="%s">%s'
                '</a></p>\n') \
                % (relative_path(filepath, tree.root),
                   tree.name)
    bar += '<div class="boxcontent"><ul>\n'
    bar += simpleNavbar(tree, filepath=filepath)
    bar += '</ul></div>\n'
    bar += '</div>\n'
    bar += '<div class="logo-bar" style="text-align: center">\n'
    bar += ('<a href="%s"><img src="%s" alt="The Fenfire logo '
            '(a purple flame)"/></a></div>\n') \
            % (relative_path(filepath, tree.root),
               relative_path(filepath, tree.root+'logo.png'))
    bar += '</div>\n<!-- NavBar end -->\n'
    return bar

def insertNavbars(tree, navbarTree=None, singleFile=None):
    if navbarTree == None: navbarTree = tree
    if singleFile:
        file = open(el[0]); s = file.read(); file.close()

        # Tries to find possible existing navbar first and replace that
        i = s.find('<!-- NavBar begin -->'+"\n")
        e = s.find('<!-- NavBar end -->'+"\n") + len('<!-- NavBar end -->'+"\n")
        if (i == -1): 
            i = s.find('<div class="footer">')
            e = i

        s = s[:i] + getBar(navbarTree, el[0]) + s[e:]
        file = open(el[0], 'w')
        file.write(s)
        file.close()
        dbg("Inserted navbar into %s" % filename)

    else:
        for el in tree.files:
            if len(el) == 2:
                file = open(el[0]); s = file.read(); file.close()

                # Tries to find possible existing navbar first and replace that
                i = s.find('<!-- NavBar begin -->'+"\n")
                e = s.find('<!-- NavBar end -->'+"\n") + len('<!-- NavBar end -->'+"\n")
                if (i == -1): 
                    i = s.find('<div class="footer">')
                    e = i

                s = s[:i] + getBar(navbarTree, el[0]) + s[e:]
                file = open(el[0], 'w')
                file.write(s)
                file.close()
                dbg( "Inserted navbar into %s" % el[0])
            else:
                insertNavbars(el[2], navbarTree)

if __name__ == '__main__':
    import sys
    t = Tree('')
    insertNavbars(t)

def postprocess(path):
    t = Tree(path)
    insertNavbars(t)
