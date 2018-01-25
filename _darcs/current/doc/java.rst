================
Java information
================

Most of Fenfire has been written as a Java application to achieve
platform independency. To use Fenfire software, you need a
sufficiently advanced Java runtime. At the moment, `Sun's JRE`_ 1.4 or
the latest `Kaffe`_ are enough. To compile Fenfire from source code,
`Sun's JDK`_ 1.4 or latest `Jikes`_ are enough.


Runtime
=======

The development versions of Fenfire use ``java`` from system ``PATH``
by default, but you can change this by setting variable ``JAVA`` in
the environment or by adding the setting to ``make`` commands.

`Kaffe`_ is a good implementation of Java as Free Software. If it's not
installed as ``java``, you can give command ``export JAVA=kaffe``.

If you run Debian, you can install Kaffe with 

``apt-get install kaffe``

When you try to find out what's going on or want to report a problem
to us, see the version of the runtime you are using by

``java -fullversion``

or if you have set ``JAVA``

``$JAVA -fullversion``


Compiler
========

The build system of Fenfire uses ``javac`` from system ``PATH`` by
default. To use another compiler or set options, define variable
``JAVAC`` in the environment or in the ``make`` command lines.

The Java compiler that comes with Kaffe doesn't understand all our
code, but the best compiler called `Jikes`_ does and is also Free
Software. If you have Debian, installation can be done with

``apt-get install jikes``

To use Jikes as the compiler, give command

``export JAVAC="jikes +Z0"``

In addition, Jikes needs to know where the basic Java library is
found. For Debian and Kaffe this is
``/usr/share/kaffe-common/lib/rt.jar`` so give command

``export BOOTCLASSPATH=/usr/share/kaffe-common/lib/rt.jar``

But on Debian, there is an even better way to use Jikes with
Kaffe. You can install a package called ``jikes-kaffe``, which takes
care of the Java library when you set the Java compiler as

``export JAVAC="jikes-kaffe +Z0"``


.. _Sun's JRE: http://java.sun.com/getjava/
.. _Sun's JDK: http://java.sun.com/j2se

.. _Kaffe: http://www.kaffe.org/
.. _Jikes: http://jikes.sourceforge.net/

