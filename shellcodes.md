Notes
=====

trap at 0x10
sr = int


Shellcodes
==========

Basic. One nullbyte.
--------------------

push 0x7F
call INT

Basic. No nullbytes:
--------------------

mov #0x1ff, r15
sub #0x180, r15
push r15
call INT
