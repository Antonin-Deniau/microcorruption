#!/usr/bin/env python
import os, sys

if len(sys.argv) == 2:
  dump = open(sys.argv[1], "r")

  OFFSET_PADDING = "000"
  OFFSET_END = 5
  DUMP_BEGGIN = 8
  DUMP_END = 47
  DISPLAY_BEGIN = 51

  res = ""
  for line in dump:
    if "*" in line and len(line) <= 12:
      continue
    res += ("{}{} {}  {}".format(OFFSET_PADDING, line[:OFFSET_END], line[DUMP_BEGGIN:DUMP_END], line[DISPLAY_BEGIN:]))

  open('./dumped', 'w').close()
  f = open("./dumped", "a")
  f.write(res)
  f.flush()
  os.system("cat ./dumped | xxd -r > ./a.out")

else:
  print("Usage create_dump.py <dump>")

