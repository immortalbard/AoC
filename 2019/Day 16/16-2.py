#! python3

from itertools import permutations
import threading, queue

def get_input(filename):
    file = open(filename)

    val = file.read()

    file.close()

    lst = [int(i) for i in val]
    start=int(val[0:7])

    return(lst,start)

def pattern(base,length,n):
    base=list(base)
    output=[]
    for i in range(length+1):
        output+=[base[i%4]]*n
        if len(output)>length:
            break
    
    return output[1:(length+1)]

def FFTopt(inp,base,phase,start):
    assert start >= len(inp)/2
    
    output=(inp*10000)[start:]
    length=len(output)
    
    for _ in range(phase):
        cusum=0
        for i in range(length-2,-1,-1):
            cusum+=output[i]
            output[i]=cusum%10
            

    return output[:8]
    
if __name__ == '__main__':
    filename = '16.txt'
    flist,start=get_input(filename)
    # flist0=[1,2,3,4,5,6,7,8]
    # flist1=[int(i) for i in '03036732577212944063491565474664']*10000
    # flist2=[int(i) for i in '02935109699940807407585447034323']*10000
    # flist3=[int(i) for i in '03081770884921959731165446850517']*10000
    # flists=[flist1,flist2,flist3]
    # start1=int('0303673')
    # start2=int('0293510')
    # start3=int('0308177')
    # starts=[start1,start2,start3]
    # # vals=[[int(_) for _ in '84462026'],[int(_) for _ in '78725270'],[int(_) for _ in '53553731']]
    base=[0,1,0,-1]
    phase=100
    check=[]
    # for i in range(3):
    #     check.append(FFT(flists[i],base,phase,starts[i])==vals[i])
       
    # if False not in check:
    #     print(FFT(flist,base,phase,start))
        
    print(FFTopt(flist,base,phase,start))