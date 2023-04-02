#! /usr/bin/env python
import sys
for i in sys.stdin:
  line = i.strip()
  num = line.split()
  for j in num:
    print('%s\t%s' % (j,1))
