#!/usr/bin/env python3

day='3'
part='2'

if len(day)<2:
  file = 'Day 0'+day+'/'+'-'.join([day,part])+'.py'
else:
  file='Day '+day+ '/' + '-'.join([day,part]) +'.py'

exec(open(file).read())

# print(bool(not None))

truth=[not 0,not '',not[],not None]
