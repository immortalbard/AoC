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

  def move(self):
    self.x+=3
    self.y+=1

def tobogganride(maps):
  t1=Toboggan(0,0)
  length=len(maps[0])
  trees=0

  while True:
    
    t1.move()

    if t1.y>=len(maps):
      break

    if maps[t1.y][(t1.x)%length]=='#':
      trees+=1
      print('Hit')
    else:
      pass
  
  return trees



if __name__ == '__main__':
    filename = 'Day 03/3.txt'

    map = get_input(filename)
    
    print(tobogganride(map))