#!/usr/bin/env python3
day='11'
part='1'

file='Day '+day+ '/' + '-'.join([day,part]) +'.py'

exec(open(file).read())

# print(bool(not None))

truth=[not 0,not '',not[],not None]