
#opcode = [1,9,10,3,2,3,11,0,99,30,40,50]

def opcoder(opcode):
    for i in range(len(opcode)):
        set=opcode[i:i+4]
        if i%4 == 0:
            #print(set)
            #print(i)
            if set[0]==99:
                break
            elif set[0]==2:
                opcode[set[3]] = opcode[set[1]]*opcode[set[2]]

            elif set[0]==1:
                opcode[set[3]] = opcode[set[1]]+opcode[set[2]]

            else:
                print('error')


    print(opcode[0])

if __name__ == "__main__":
    filename = '2-1.txt'

    file = open(filename)

    opcode = file.read().split(',')

    file.close()

    print(len(opcode))

    for i in range(len(opcode)):
        opcode[i] = int(opcode[i])

    opcode[1] = 12
    opcode[2] = 2

    opcoder(opcode)
