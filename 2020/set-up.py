#!/usr/bin/env python3

import os

for i in range(1,26):
  path="Day {0:02d}".format(i)
  if not os.path.exists(path):
    os.mkdir(path)

  for p in [1,2]:
    file=path+ '/' + '-'.join([str(i),str(p)]) +'.py'
    f = open(file,'w')
    f.close()
 
print(bool(not None))

truth=[not 0,not '',not[],not None]