from itertools import permutations
import threading, queue


def moder(seti,opcode):
    
    modes=[ x for x in seti[0][0:2]]
    for i in range(len(modes)):
        if int(modes[-1-i])==0 and len(seti)!=len(modes):
            foo=opcode[seti[i+1]]
            seti[i+1]=foo
    
    return(seti)

def TEST(amp_name,opcode,inpf,outputf):
    i=0
    check=0
    code=opcode
    while i < len(code):
        #print(code[i])
        abcde=str('0'*(4-len(str(code[i])))+str(code[i]))
        icode=abcde[-2:]
        if abcde[-2:]=='99':
            i=len(code)
            break
        
        if icode in ['01','02','07','08']:
            seti=code[i:i+4]
            seti[0]=abcde
            moder(seti,code)
            if icode=='01':
                code[seti[3]] = seti[1]+seti[2]
                
            elif icode=='02':
                code[seti[3]]=seti[1]*seti[2]
                
            elif icode=='07':
                if seti[1]<seti[2]:
                    code[seti[3]]=1
                else:
                    code[seti[3]]=0
                
            elif icode=='08':
                if seti[1]==seti[2]:
                    code[seti[3]]=1
                else:
                    code[seti[3]]=0
            i+=4
        
        elif icode in ['03','04']:
            seti=code[i:i+2]
            seti[0]=abcde
            moder(seti,code)
            if icode=='03':
                code[seti[1]]=inpf()
                
            elif icode=='04':
                outputf(code[seti[1]])
            i+=2
            
        elif icode in ['05','06']:
            seti=code[i:i+3]
            seti[0]=abcde
            moder(seti,code)
            if icode=='05' and seti[1]!=0:
                i=seti[2]
            elif icode=='06' and seti[1]==0:
                i=seti[2]
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

def amp(name,opcode,inqueue,outqueue):
    def outthing(x):
        # print("Spitting %d out of amp %d" % (name,x))
        outqueue.put_nowait(x)
    TEST(name,opcode,lambda: inqueue.get(True, 2),outthing)

def max_thrust(code):
    # WE DO NOT UNDERSTAND THIS FUTURE ME, https://www.reddit.com/r/adventofcode/comments/e7a4nj/2019_day_7_solutions/fa22s5d?utm_source=share&utm_medium=web2x
    max_thrust=-1000
    for ordering in permutations(range(5,10)):
        queues = [queue.Queue() for _ in range (6)]
        for (ique, order) in zip(queues, ordering):
            ique.put(order)
        queues[0].put(0)
        threads=[]
        for i in range(5):
            threads.append(threading.Thread(target=amp, args=(i,code,queues[i],queues[(i+1) % 5])))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        last_out= queues[0].get_nowait()
        max_thrust=max(max_thrust,last_out)
    return(max_thrust)


if __name__ == '__main__':
    filename = '7.txt'
    code=get_opcode(filename)
    print(max_thrust(code))

