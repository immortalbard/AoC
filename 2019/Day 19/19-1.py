#! python3

from itertools import permutations
import threading, queue

def get_opcode(filename):
    file = open(filename)

    opcode = file.read().split(',')

    file.close()

    for i in range(len(opcode)):
        opcode[i] = int(opcode[i])

    return(opcode)

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

def intcode(icode,inp):
    i=0
    relbase=0
    code=icode+[0 for _ in range(10000-len(icode))]
    output=[]
    while i < len(code):
        abcde=str('0'*(5-len(str(code[i])))+str(code[i]))
        icode=abcde[-2:]
        mode_a=abcde[2]
        mode_b=abcde[1]
        mode_c=abcde[0]
        
        if abcde[-2:]=='99':
            # print('code[index]= ',code[i],"output= ",output," index= ",i," relbase= ",relbase)
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
                    code[idx_a]=inp.pop()
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

    # print("output= ",output," index= ",i," relbase= ",relbase)
    return output
    
def tractor(code,width,height):
    image=[['' for j in range(width)] for i in range(height)]
    
    for i in range(height):
        for k in range(width):
            output=intcode(code,[i,k])
            if int(output[0])==0:
                image[i][k]=' '
            else:
                image[i][k]='#'
            # print(i,k)
            
    return image


if __name__ == '__main__':
    filename = 'Day 19/19.txt'
    code=get_opcode(filename)
    width,height=50,50
    image=tractor(code,width,height)
    print(sum([image[i].count('#') for i in range(len(image))]))
    # for i in range(height):
    #     print(image[i])