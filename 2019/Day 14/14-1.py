#! python3

class Rxn:
    def __init__(self,rxnts,prods):
        self.rxnts=rxnts
        self.prods=prods


def getrxns(filename):
    file = open(filename)

    rxns = file.read().split("\n")

    file.close()

    for i in range(len(rxns)):
        rxns[i] = rxns[i].split(' => ')
        if len(rxns[i])<2:
            rxns.remove(coord[i])
            
        rxns[i][0]=rxns[i][0].split(', ')
        rxns[i][1]=rxns[i][1].split(', ')

    return(rxns)

def findchems(rxns):
    chemlist=[]
    for i in range(len(rxns)):
        if len(rxns[i])<2:
            print(rxns[i])
        else:
            chemlist+=[rxns[i][0][_].split(' ')[1] for _ in range(len(rxns[i][0]))]
            chemlist+=[rxns[i][1][_].split(' ')[1] for _ in range(len(rxns[i][1]))]


    chems=list(dict.fromkeys(chemlist))
    # chemlist=[Star(star) for star in stars]

    # l=[starmap[x][0] for x in range(len(starmap))]
    # r=[starmap[x][1] for x in range(len(starmap))]

    # for star in starlist:
    #     star.lr = (l.count(star.name),r.count(star.name))

    return chems

def findstart(starmap,starlist):
    for star in starlist:
        if star.lr == (1,0):
            start=star.name
    return start

def findend(starmap,starlist):
    end=[]

    for star in starlist:
        if star.lr == (0,1):
            end.append(star.name)
    return end

def findorbits(starmap,starlist,start,end):
    #find someway to make this work. Basic theory is
    #if I can find and end star then count back to start star
    #Each star gets orbitnum, sum them, return that.
    pass

if __name__ == "__main__":
    filename='Day 14/14.txt'

    rxns=getrxns(filename)
    
    for rxn in rxns:
      if 'FUEL' in rxn[1][0]:
        fuelrxn=rxn

    for rxt in
    
    chems=findchems(rxns)
    print(chems)
