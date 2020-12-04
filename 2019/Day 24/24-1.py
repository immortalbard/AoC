#! python3

from pprint import pprint
   
def get_bugs(filename):
  file = open(filename)

  orders = file.read().split('\n')

  file.close()

  bugs=[[order[i] for i in range(len(order))] for order in orders]

  return bugs

def adjacent(ar,x,y):
  dir={'up':[y-1,x],'down':[y+1,x],'left':[y,x-1],'right':[y,x+1]}
  adj=['up','down','left','right']
  for key in dir.keys():
    i=adj.index(key)
    try:
      adj[i]=ar[dir[key][0]][dir[key][1]]
    except IndexError:
      adj[i]='.'
    finally:
      if key in ['up','left'] and (x==0 or y==0):
        adj[i]='.' if (y==0 and key=='up') else '.' if (x==0 and key=='left') else adj[i]
        
  return adj

def Conway(ar):
  arr=[i[:] for i in ar]

  for y in range(5):
    for x in range(5):
      test=adjacent(ar,x,y)
      if ar[y][x]=='#' and test.count('#')!=1:
        arr[y][x]='.'
      elif ar[y][x]=='.' and (test.count('#')==1 or test.count('#')==2):
        arr[y][x]='#'

  return(arr)

if __name__ == '__main__':
  path='Day 24/'
  filename = '24.txt'
  bugs=get_bugs(path+filename)
  layout=[bugs]

  while True:
    bugs=Conway(bugs)
    if bugs in layout:
      pprint(bugs)
      break
    else:
      layout.append(bugs)

  flatten = [item for sublist in bugs for item in sublist]
  val=[2**i for i, e in enumerate(flatten) if e == '#']
  print(sum(val))

