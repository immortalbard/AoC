#!/usr/bin/env python3

def get_input(filename):
  file = open(filename)

  val = file.read().split('\n')

  file.close()

  return [val.split(': ') for val in val]

def pwdpass(pwd,val,pos):
  if pwd[int(pos)]==val:
    return True
  else:
    return False

def pwdcheck(pwds):
  passwords=0

  for pwd in pwds:
    pwd[0]=pwd[0].split(' ')
    pwd[0][0]=pwd[0][0].split('-')

    p1=int(pwd[0][0][0])-1
    p2=int(pwd[0][0][1])-1

    if pwdpass(pwd[1],pwd[0][1],p1) ^ pwdpass(pwd[1],pwd[0][1],p2):
      passwords+=1

  return passwords



if __name__ == '__main__':
    filename = 'Day 02/2.txt'

    pwds = get_input(filename)

    vals = pwdcheck(pwds)

    print(vals)