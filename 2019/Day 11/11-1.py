#! python3

BLACK, WHITE=0,1
LEFT, RIGHT=0,1
NORTH, SOUTH, EAST, WEST='NSEW'
dirmap={NORTH:(WEST,EAST),SOUTH:(EAST,WEST),EAST:(NORTH,SOUTH),WEST:(SOUTH,NORTH)}
movemap={NORTH:(-1,0),SOUTH:(+1,0),EAST:(0,+1),WEST:(0,-1)}

from collections import defaultdict

def get_opcode(filename):
  file = open(filename)

  opcode = file.read().split(',')

  file.close()

  for i in range(len(opcode)):
      opcode[i] = int(opcode[i])

  return(opcode+[0 for _ in range(10000-len(opcode))])

def get_index(index,mode,relbase):
  global code
  if mode=='0':
    return code[index]
  elif mode=='1':
    return index
  elif mode=='2':
    return relbase+code[index]
  else:
    return ValueError

def get_data(index,mode,relbase):
  global code
  foo=get_index(index,mode,relbase)
  return code[foo]

def intcode(inp,index,relbase):
  global code
  i=index
  output=[]
  while i<len(code):
    abcde=str('0'*(5-len(str(code[i])))+str(code[i]))
    icode=abcde[-2:]
    mode_a=abcde[2]
    mode_b=abcde[1]
    mode_c=abcde[0]
    a=get_data(i+1,mode_a,relbase)
    b=get_data(i+2,mode_b,relbase)
    c=get_index(i+3,mode_c,relbase)
    
    if abcde[-2:]=='99':
      print('code[index]= ',code[i],"output= ",output," index= ",i," relbase= ",relbase)
      return None,index,relbase
    
    if icode in ['01','02','07','08']:
      code[c] = a+b if icode=='01' else a*b if icode=='02' else 1 if (icode=='07' and a<b) else 1 if (icode=='08' and a==b) else 0
      i+=4
    
    elif icode in ['03','04','09']:
      idx_a=get_index(i+1,mode_a,relbase)
      if icode=='03':
        code[idx_a]=inp.pop()
      elif icode=='04':
        output.append(a)
        if len(output)==2:
        #   # i+=2
        #   # print("output= ",output," index= ",i," relbase= ",relbase)
          return output,i,relbase
      elif icode=='09':
        relbase+=a
        # print(relbase)
      i+=2
        
    elif icode in ['05','06']:
      i=b if (icode=='05' and a!=0) or (icode=='06' and a==0) else i+3

def robot(color_start):
  location=(0,0)
  bearing=NORTH
  grid=defaultdict(lambda: BLACK)
  grid[location]=color_start
  
  check=0
  index=0
  relbase=0
  
  while True:
    output,index,relbase=intcode([grid[location]],index,relbase)

    if not output or check>5000000:
      break

    if check%1902==0:
      print('start loop #:',check)
      print('i:',index,'\nlocation:',location)

    color,turn=output
    grid[location]=color
    bearing=dirmap[bearing][turn]
    dx,dy=movemap[bearing]
    location=(location[0]+dx,location[1]+dy)

    check+=1
    

  print(len(grid),check)
  return(grid)
    
def image(image):
  minj=min(x for x,_ in image)
  maxj=max(x for x,_ in image)
  mini=min(y for _,y in image)
  maxi=max(y for _,y in image)

  height = maxi - mini + 1
  width  = maxj - minj + 1
  pic    = [([' '] * width) for _ in range(height)]

  for i in range(height):
    for j in range(width):
      if [mini + i, minj + j] in image:
        pic[i][j] = '#'

  pic = ''.join(''.join(x) for x in pic)
  
  return pic

if __name__ == '__main__':
  filename = 'Day 11/11.txt'
  
  code=get_opcode(filename)
  panel_image=robot(BLACK)

  # print(panel_image)
  # print(image(panel_image))
  # 'LRZECGFE'