#! python3

from itertools import permutations
import threading, queue

def get_input(filename):
    file = open(filename)

    val = file.read()

    file.close()

    lst = [int(i) for i in val]

    return(lst)

def pattern(base,length,n):
    base=list(base)
    output=[]
    for i in range(length+1):
        output+=[base[i%4]]*n
        if len(output)>length:
            break
    
    return output[1:(length+1)]

def FFT(inp,base,phase):
    output=[inp]
    pat=[]
    for i in range(len(inp)):
        pat.append(pattern(base,len(inp),i+1))
    for i in range(phase):
        out=[]
        for j in range(len(inp)):
            out.append(abs(sum([val*p for val,p in zip(output[i],pat[j])]))%10)
        output.append(out)
            
    return output[-1][0:8]
    
if __name__ == '__main__':
    filename = '16.txt'
    flist=get_input(filename)
    flist0=[1,2,3,4,5,6,7,8]
    flist1=[int(i) for i in '80871224585914546619083218645595']
    flist2=[int(i) for i in '19617804207202209144916044189917']
    flist3=[int(i) for i in '69317163492948606335995924319873']
    base=[0,1,0,-1]
    phase=100
    print(FFT(flist,base,phase))