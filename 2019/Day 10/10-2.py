#! python3
from math import gcd
from math import atan2,pi as PI

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

def manhattan(ast1,ast2):
  x1,y1=ast1[0],ast1[1]
  x2,y2=ast2[0],ast2[1]
  return abs(x2-x1)+abs(y2-y1)

def angle(ast1,ast2):
  x1,y1=ast1[0],ast1[1]
  x2,y2=ast2[0],ast2[1]
  rad=atan2(y2-y1,x2-x1)+PI
  rad=rad%(2*PI)-PI/2
  return rad if rad>=0 else 2*PI+rad

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

  return max_view,station

def blast(asteroids,station,n):
  closest={}

  for ast in asteroids:
    if ast==station:
      continue
    
    r=ray(station,ast)
    m=manhattan(station,ast)

    if r not in closest or m<closest[r][1]:
      closest[r]=(ast,m)

  ordered=sorted(closest.values(),key=lambda am: angle(station,am[0]))
  x,y=ordered[n-1][0]
  ans=100*x+y

  return(ans)

if __name__ == '__main__':
  filename = 'Day 10/10.txt'
  asteroids=get_asteroids(filename)
  max_view,station=best(asteroids)
  ans=blast(asteroids,station,200)
  print(ans)

    
