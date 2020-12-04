# 2-2.py


#opcode = [1,9,10,3,2,3,11,0,99,30,40,50]

def opcoder(opcode):
    for i in range(len(opcode)):
        set=opcode[i:i+4]
        #print(set)
        if i%4 == 0:
            #print(set)
            #print(i)
            if set[0]==99:
                return(opcode[0])
                break

            elif set[0]==2:
                opcode[set[3]] = opcode[set[1]]*opcode[set[2]]

            elif set[0]==1:
                opcode[set[3]] = opcode[set[1]]+opcode[set[2]]

            else:
                print('error')

def get_opcode(filename):
    file = open(filename)

    opcode = file.read().split(',')

    file.close()

    for i in range(len(opcode)):
        opcode[i] = int(opcode[i])

    return(opcode)

def sentence(noun,verb):
    return 100*int(noun)+int(verb)

if __name__ == "__main__":

    filename = '2-1.txt'

    for noun in range(100):
        for verb in range(100):
            opcode=get_opcode(filename)

            opcode[1] = noun
            opcode[2] = verb

            if opcoder(opcode) == 19690720:
                print(sentence(noun,verb))
