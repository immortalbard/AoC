from itertools import permutations
import threading, queue

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
    check=0
    relbase=0
    code=icode+[0 for _ in range(10000)]
    output=[]
    while i < len(code):
        abcde=str('0'*(5-len(str(code[i])))+str(code[i]))
        icode=abcde[-2:]
        mode_a=abcde[2]
        mode_b=abcde[1]
        mode_c=abcde[0]
        
        if abcde[-2:]=='99':
            i=len(code)
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

    return(opcode)


if __name__ == '__main__':
    test0=[109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    test1=[1102,34915192,34915192,7,4,7,99,0]
    test2=[104,1125899906842624,99]
    filename = '9.txt'
    code=get_opcode(filename)
    print(intcode(code,[1]))