def doubles(num):
    numlist=str(num)
    
    for i in range(len(numlist)):
        if i==len(numlist)-1:
            return False
        elif numlist[i]==numlist[i+1]:
            return True

def check2(num):
    numstr=str(num)
    numdict={0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
    numsplit=[int(x) for x in numstr]
    
    for i in range(10):
        numdict[i]=numsplit.count(i)
    
    numlist=list(numdict.values())
    while 0 in numlist:
        numlist.remove(0)

    if 2 in numlist:
        return True
    else:
        return False
    
def increase(num):
    ascending = ''.join(sorted(str(num)))
    if int(ascending)==num:
        return True
    else:
        return False

def check(num):
    if doubles(num) and increase(num) and check2(num):
        return True
    else:
        return False

start=246540
end=787419

possible=[]

if __name__ == '__main__':
    test0=111122
    test1=112233
    test2=123444

    print([check(test0), check(test1), check(test2)])
    
    for i in range(start,end,1):
        if check(i):
            possible.append(i)
        
    print(len(possible))