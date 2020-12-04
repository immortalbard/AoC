def doubles(num):
    numlist=str(num)
    
    for i in range(len(numlist)):
        if i==len(numlist)-1:
            return False
        elif numlist[i]==numlist[i+1]:
            return True

def increase(num):
    ascending = ''.join(sorted(str(num)))
    if int(ascending)==num:
        return True
    else:
        return False

def check(num):
    if doubles(num) and increase(num):
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