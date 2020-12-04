#!/usr/bin/env python3

def get_input(filename):
  file = open(filename)

  val = file.read().split('\n')

  file.close()

  return val

def find(inlist,val):
  newlist = []

  for i in inlist:
    newlist.append(str(val-int(i)))

  vals =  [value for value in inlist if value in newlist] 

  return int(vals[0])*int(vals[1])



if __name__ == '__main__':
    filename = 'Day 01/1.txt'

    nums = get_input(filename)

    vals = find(nums,2020)

    print(vals)
