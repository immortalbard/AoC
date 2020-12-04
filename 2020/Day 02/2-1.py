#!/usr/bin/env python3

def get_input(filename):
  file = open(filename)

  val = file.read().split('\n')

  file.close()

  return [val.split(': ') for val in val]

def pwdcheck(pwds):
  pwdpass=0

  for pwd in pwds:
    pwd[0]=pwd[0].split(' ')
    pwd[0][0]=pwd[0][0].split('-')

    if int(pwd[0][0][0])<=pwd[1].count(pwd[0][1])<=int(pwd[0][0][1]):
      pwdpass+=1



  return pwdpass



if __name__ == '__main__':
    filename = 'Day 02/2.txt'

    pwds = get_input(filename)

    vals = pwdcheck(pwds)

    print(vals)
