#! python3
from math import gcd

def get_asteroids(filename):
  file = open(filename)

  rows = file.read().split('\n')

  file.close()

  asteroids=[]

  for y in range(len(rows)):
    for x in range(len(rows[y])):
      if rows[y][x]=='#':
        asteroids.append((x,y))
  
  return(asteroids)

def ray(ast1,ast2):
  dx,dy=ast2[0]-ast1[0],ast2[1]-ast1[1]
  div=abs(gcd(dx,dy))
  return dx//div,dy//div

def best(asteriods):
  station=None
  max_view=0

  for ast in asteroids:
    view_lines=set()

    for a in asteroids:
      if a==ast:
        continue

      view_lines.add(ray(ast,a))

    in_view=len(view_lines)
    if in_view>max_view:
      max_view=in_view
      station=ast

  return max_view

if __name__ == '__main__':
  filename = 'Day 10/10.txt'
  asteroids=get_asteroids(filename)
  max_view=best(asteroids)
  print(max_view)

    
