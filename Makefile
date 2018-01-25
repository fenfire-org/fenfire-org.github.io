RST2HTML=LC_ALL=C rst2html

PAPER_FILES = $(shell find * -name "*.rst"|bash paper_ids.sh http://fenfire.org/ papers/ -paper.gen.jpg)


RST = $(shell find . -path './_darcs' -prune -or -path './manuscripts' -prune -o -name '*.rst')



all: rst doap.rdfxml

rst: $(patsubst %.rst,%.html,$(RST))
	python add_texture.py
	python add_navbar.py

%.html: %.rst
	$(RST2HTML) $< $@

doap.rdfxml: doap.turtle
	# rapper is in Debian package raptor-utils
	rapper -q -i turtle -o rdfxml doap.turtle > doap.rdfxml




papers: $(PAPER_FILES)

%-paper.gen.jpg:
#	- (cd `dirname $@` && make -C ../../libvob runjython DBG="lava/bgfilegen.py `basename $*`")
	make -C ../libvob runjython DBG="lava/bgfilegen.py `basename $*`"
	convert -quality 70 ../libvob/`basename $*`-paper.gen.png papers/`basename $*`-paper.gen.jpg

dbg:
	echo $(PAPER_FILES)
