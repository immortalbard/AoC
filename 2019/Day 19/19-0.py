#! python3

from itertools import permutations
import threading, queue

def get_opcode(filename):
  file = open(filename)

  opcode = file.read().split(',')

  file.close()

  for i in range(len(opcode)):
    opcode[i] = int(opcode[i])

  return(opcode+[0 for _ in range(10000)])

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
  # print('f',foo)
  # try:
  #   print(code[foo])
  # except:
  #   print('out of bounds on',index,mode,relbase,code[index])
  return code[foo]

def intcode(code,inp):
  
  i=0
  relbase=0
  output=[]
  while i<len(code):
    abcde=str('0'*(5-len(str(code[i])))+str(code[i]))
    print(i)
    icode=abcde[-2:]
    mode_a=abcde[2]
    mode_b=abcde[1]
    mode_c=abcde[0]
    a=get_data(i+1,mode_a,relbase)
    
    if icode=='99':
      print('code[index]= ',code[i],"output= ",output," index= ",i," relbase= ",relbase)
      return None
    
    elif icode in ['03','04','09']:
      idx_a=get_index(i+1,mode_a,relbase)
      if icode=='03':
        code[idx_a]=inp.pop()
      elif icode=='04':
        output.append(a)
        return output
      elif icode=='09':
        relbase+=a
        # print('relbase',relbase)
      i+=2
    
    elif icode in ['05','06']:
      b=get_data(i+2,mode_b,relbase)
      i=b if (icode=='05' and a!=0) or (icode=='06' and a==0) else i+3
        
    elif icode in ['01','02','07','08']:
      b=get_data(i+2,mode_b,relbase)
      c=get_index(i+3,mode_c,relbase)
      code[c]=a+b if icode=='01' else a*b if icode=='02' else 1 if (icode=='07' and a<b) else 1 if (icode=='08' and a==b) else 0
      i+=4
   
def tractor(code,width,height):
  image=[['' for j in range(width)] for i in range(height)]
  
  for i in range(height):
    for k in range(width):
      output=intcode(code,[i,k])
      if int(output[0])==0:
        image[i][k]=' '
      else:
        image[i][k]='#'
      print(i,k)
          
  return image


if __name__ == '__main__':
  filename = 'Day 19/19.txt'
  code=get_opcode(filename)
  width,height=50,50
  image=tractor(code,width,height)
  print(sum([image[i].count('#') for i in range(len(image))]))
  # for i in range(height):
  #     print(image[i])