#!/usr/bin/env python3

def get_input(filename):
  file = open(filename)

  val = file.read().split('\n')

  file.close()

  return val

class Toboggan:
  def __init__(self,x0,y0):
    self.x=x0
    self.y=y0

  def move(self,x,y):
    self.x+=x
    self.y+=y

def tobogganride(maps,right,dn):
  t1=Toboggan(0,0)
  length=len(maps[0])
  trees=0

  while True:
    
    t1.move(right,dn)

    if t1.y>=len(maps):
      break

    if maps[t1.y][(t1.x)%length]=='#':
      trees+=1
    else:
      pass
  
  return trees



if __name__ == '__main__':
    filename = 'Day 03/3.txt'

    map = get_input(filename)

    r1d1=tobogganride(map,1,1)
    r3d1=tobogganride(map,3,1)
    r5d1=tobogganride(map,5,1)
    r7d1=tobogganride(map,7,1)
    r1d2=tobogganride(map,1,2)

    check=r1d1*r3d1*r5d1*r7d1*r1d2
    
    print(check)