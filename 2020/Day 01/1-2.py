#!/usr/bin/env python3

def get_input(filename):
  file = open(filename)

  val = file.read().split('\n')

  file.close()

  return val

def find(inlist,val):

  for i in inlist:
    for j in inlist:
      for k in inlist:
        if int(i)+int(j)+int(k) == val:
          return int(i)*int(j)*int(k)



if __name__ == '__main__':
    filename = 'Day 01/1.txt'

    nums = get_input(filename)

    vals = find(nums,2020)

    print(vals)
