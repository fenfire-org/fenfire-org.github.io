=====================
Developer information
=====================

Fenfire is a Free Software project. Anyone is free to look into what 
we're doing. If the project `vision`_ attracts you, we welcome you 
to collaboration. 

.. contents::


Developer resources
===================

* Official source code in `Darcs`_ repositories under http://himalia.it.jyu.fi/darcs:
  alph, callgl, depends, fenfire, libvob, navidoc, storm

* Mailing lists: `fenfire-dev`_ for developers and users;
  `fencommits`_ for automatic notification of commits to the
  Darcs repositories

* IRC discussion on channel #fenfire at Freenode servers (eg. irc.freenode.net)
  and `discussion logs`_

* compiled versions of `documentation from CVS`_ (not updated at the moment!)
    * information on `subprojects`_
    * `Proposals for enhancing Fenfire`_
    * `Javadocs`_ of source code


Getting started
===============

We use `Darcs`_ for source code version control, so you should have it
installed first. Programming language is mostly Java so you should
have a `suitable Java`_ compiler and runtime installed, but there are
optional pieces written in C, C++, Perl and Jython (Python running in
Java) as well. We use the `GNU Make`_ to build the project, if you
don't have it you'll have to type the compile and run commands
yourself.

* To get a fresh copy of the official repositories, "darcs get" each 
  repository, for instance in shell:

  ``for d in alph callgl depends fenfire libvob navidoc storm; do 
  darcs get http://himalia.it.jyu.fi/darcs/$d ; done``

* To get updates, "darcs pull" in each repository, for instance:

  ``for d in alph callgl depends fenfire libvob navidoc storm; do ( 
  cd "$d" && darcs pull ) done``

* To compile Java code, "make" or "make java" in each directory in the order, 
  for instance:

  ``for d in navidoc storm alph libvob fenfire; do 
  ( cd "$d" && make java ) done``

* To start the applications, "make run*" in some repository, for instance:

  ``( cd fenfire && make run )``


Old resources
=============

The following resources contain historical stuff, they're not in active use.

Fenfire project page `at Savannah`_
    * List of `mailing lists`_, including the old `gzz-dev`_,
      the old `fenfire-commits`_, and `fenfire-rdf-discuss`_ which was
      never really used
    * pre-2004 browsable source code `in CVS`_

`Old IRC logs`_ (from IRCNet, not in use after 2003)



.. _vision: ../vision.html

.. _suitable Java: java.html

.. _Darcs: http://abridgegame.org/darcs/
.. _GNU Make: http://www.gnu.org/software/make/make.html

.. _discussion logs: http://fenfire.org/irc/fenfire
.. _Old IRC logs: http://himalia.it.jyu.fi/irc
.. _documentation from CVS: http://himalia.it.jyu.fi/ffdoc/fenfire
.. _subprojects: http://himalia.it.jyu.fi/ffdoc/fenfire/projects.gen.html
.. _Proposals for enhancing Fenfire: http://himalia.it.jyu.fi/ffdoc/fenfire/pegboard
.. _Javadocs: http://himalia.it.jyu.fi/ffdoc/fenfire/javadoc

.. _at Savannah: http://savannah.nongnu.org/projects/fenfire
.. _in CVS: http://savannah.nongnu.org/cgi-bin/viewcvs/fenfire
.. _mailing lists: http://savannah.nongnu.org/mail/?group=fenfire
.. _fenfire-dev: http://mail.nongnu.org/mailman/listinfo/fenfire-dev
.. _fencommits: http://lists.jyu.fi/mailman/listinfo/fencommits
.. _fenfire-rdf-discuss: http://mail.nongnu.org/mailman/listinfo/fenfire-rdf-discuss
.. _fenfire-commits: http://mail.nongnu.org/mailman/listinfo/fenfire-commits
.. _gzz-dev: http://mail.nongnu.org/mailman/listinfo/gzz-dev
