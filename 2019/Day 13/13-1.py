#! python3

from collections import defaultdict

empty,wall,block,paddle,ball=0,1,2,3,4

def get_index(code,index,mode,relbase):
    if mode=='0':
        return code[index]
    elif mode=='1':
        return index
    elif mode=='2':
        return relbase+code[index]
    else:
        return ValueError

def get_data(code,index,mode,relbase):
    foo=get_index(code,index,mode,relbase)
    return code[foo]

def intcode(code,inp):
  i=0
  check=0
  relbase=0

  output=[]
  while i < len(code):
    abcde=str('0'*(5-len(str(code[i])))+str(code[i]))
    icode=abcde[-2:]
    mode_a=abcde[2]
    mode_b=abcde[1]
    mode_c=abcde[0]
    
    if abcde[-2:]=='99':
      return output
  
    if icode in ['01','02','07','08']:
      a=get_data(code,i+1,mode_a,relbase)
      b=get_data(code,i+2,mode_b,relbase)
      c=get_index(code,i+3,mode_c,relbase)
      if icode=='01':
        code[c] = a+b
          
      elif icode=='02':
        code[c]=a*b
          
      elif icode=='07':
        if a<b:
          code[c]=1
        else:
          code[c]=0
          
      elif icode=='08':
        if a==b:
          code[c]=1
        else:
          code[c]=0
      i+=4
  
    elif icode in ['03','04','09']:
      idx_a=get_index(code,i+1,mode_a,relbase)
      val_a=get_data(code,i+1,mode_a,relbase)
      if icode=='03':
        code[idx_a]=inp[0]
      elif icode=='04':
        output.append(val_a)
        
        
      elif icode=='09':
        relbase+=val_a
      i+=2
      
    elif icode in ['05','06']:
      a=get_data(code,i+1,mode_a,relbase)
      b=get_data(code,i+2,mode_b,relbase)
      if icode=='05' and a!=0:
        i=b
      elif icode=='06' and a==0:
        i=b
      else:
        i+=3

  return code[0]

def get_opcode(filename):
  file = open(filename)

  opcode = file.read().split(',')

  file.close()

  for i in range(len(opcode)):
    opcode[i] = int(opcode[i])

  return opcode+[0 for _ in range(10000-len(opcode))] 

def cabinet(code):
  grid=defaultdict(lambda: EMPTY)

  output=intcode(code,[])
    
  for i in range(0,len(output),3):
    x,y,tile=output[i:i+3]
    grid[(x,y)]=tile

  return(grid)


if __name__ == '__main__':
  filename = 'Day 13/13.txt'
  code=get_opcode(filename)
  grid=cabinet(code)

  bricks=list(grid.values()).count(2)
  print(bricks)




