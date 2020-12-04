class Star:
    def __init__(self, name):
        self.name = name
        self.lr=''
        self.orbitnum=0

    def name(self):
        return self.name


def getmap(filename):
    file = open(filename)

    coord = file.read().split("\n")

    file.close()

    for i in range(len(coord)):
        coord[i] = coord[i].split(')')
        if len(coord[i])<2:
            coord.remove(coord[i])

    return(coord)

def findstars(starmap):
    stars=[]
    for i in range(len(starmap)):
        if len(starmap[i])<2:
            print(starmap[i])
        else:
            stars.append(starmap[i][0])
            stars.append(starmap[i][1])

    stars=list(dict.fromkeys(stars))
    starlist=[Star(star) for star in stars]

    l=[starmap[x][0] for x in range(len(starmap))]
    r=[starmap[x][1] for x in range(len(starmap))]

    for star in starlist:
        star.lr = (l.count(star.name),r.count(star.name))

    return starlist

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
    filename='6.txt'

    starmap=getmap(filename)
    print(len(starmap))
    starlist=findstars(starmap)
    print(len(starlist),starlist[0].name)
    start=findstart(starmap,starlist)
    end=findend(starmap,starlist)
    print(start,end)
