'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Star:
    def __init__(self, name):
        self.name = name
        self.lr=''
        self.orbitnum=0
        self.orbitpath=[]
        
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

def findorbit(starmap,start,star):
    #find someway to make this work. Basic theory is
    #if I can find and end star then count back to start star
    #Each star gets orbitnum, sum them, return that.
    # print(star.name)
    starx=star.name
    while starx!=start:
        for i in range(len(starmap)):
            if starmap[i][1]==starx:
                star.orbitnum+=1
                starx=starmap[i][0]
                star.orbitpath.append(starx)
                break
            
def intersect(lst1,lst2):
    lst3=[value for value in lst1 if value in lst2]
    return lst3[1:]

if __name__ == "__main__":
    filename='6.txt'
    
    starmap=getmap(filename)
    print(starmap[0])
    starlist=findstars(starmap)
    # print(starlist[0].name)
    start=findstart(starmap,starlist)
    end=findend(starmap,starlist)
    # print(start,end)
    orbits=0
    xfer=[]
    for star in starlist:
        findorbit(starmap,start,star)
        orbits+=star.orbitnum
        if star.name == 'YOU' or star.name=='SAN':
            xfer.append(star.orbitpath)
            
    print(orbits)

    # pathmax=max(len(xfer[0]),len(xfer[1]))
    # pathmin=min(len(xfer[0]),len(xfer[1]))

    # for i in range(2):
    #     if len(xfer[i])==pathmin:
    #         difflist=['']*(pathmax-pathmin)
    #         print(difflist)
    #         xfer[i]+=(difflist)
    
    intersection=intersect(xfer[0],xfer[1])
    print(intersection)
    print(list(set(xfer[1])-set(xfer[0])))
    a=len(xfer[0])-len(intersection)
    b=len(xfer[1])-len(intersection)
    print(a+b)