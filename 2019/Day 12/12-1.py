#! python3

import re

class Moon:
    def __init__(self,name,x0,y0,z0):
        self.name=name
        self.x=x0
        self.y=y0
        self.z=z0
        self.position=[self.x,self.y,self.z]
        self.pi=[x0,y0,z0]
        self.vx=0
        self.vy=0
        self.vz=0
        self.velocity=[self.vx,self.vy,self.vz]
        self.PE=sum(map(abs,self.position))
        self.KE=sum(map(abs,self.velocity))
        self.total_energy=0
        
    def __repr__(self):
        return 'Moon %s is at <%d,%d,%d> traveling at <%d,%d,%d>.' %(self.name,self.x,self.y,self.z,self.vx,self.vy,self.vz)
        
    def update_position(self):
        self.x=self.position[0]
        self.y=self.position[1]
        self.z=self.position[2]
        self.PE=sum(map(abs,self.position))
        
    def update_velocity(self,vx,vy,vz):
        self.velocity=[a+b for a,b in zip(self.velocity,[vx,vy,vz])]
        self.vx=self.velocity[0]
        self.vy=self.velocity[1]
        self.vz=self.velocity[2]
        self.KE=sum(map(abs,self.velocity))

    def move(self):
        self.position=[a+b for a,b in zip(self.position,self.velocity)]
        self.total_energy=self.PE*self.KE
        
    def gravity(self,other):
        for i in range(3):
            if self.position[i]<other.position[i]:
                self.velocity[i]+=1
            elif self.position[i]>other.position[i]:
                self.velocity[i]-=1

    def getEnergy(self):
        self.KE=sum(map(abs,self.velocity))
        self.PE=sum(map(abs,self.position))
        self.total_energy=self.PE*self.KE
        return self.total_energy
        
def get_moons(filename):
    file = open(filename)

    val = file.read().split('\n')

    file.close()
    
    exp=re.compile(r'-?\d+')
    coor=[list(map(int,exp.findall(line))) for line in val]

    Io=Moon('Io',coor[0][0],coor[0][1],coor[0][2])
    Europa=Moon('Europa',coor[1][0],coor[1][1],coor[1][2])
    Ganymede=Moon('Ganymede',coor[2][0],coor[2][1],coor[2][2])
    Callisto=Moon('Callisto',coor[3][0],coor[3][1],coor[3][2])

    return [Io,Europa,Ganymede,Callisto]
    
def step(moons):
    
    xs=[moon.x for moon in moons]
    ys=[moon.y for moon in moons]
    zs=[moon.z for moon in moons]
    
    for moon in moons:
        # print(moon.position,dx,dy,dz,moon.velocity)
        dx=len([i for i in xs if moon.x<i])-len([i for i in xs if moon.x>i])
        dy=len([i for i in ys if i>moon.y])-len([i for i in ys if i<moon.y])
        dz=len([i for i in zs if i>moon.z])-len([i for i in zs if i<moon.z])
        moon.update_velocity(dx,dy,dz)
        
    for moon in moons:
        moon.move()
        moon.update_position()

def track(moons,n):
    i=0
    while i<n:
        # print('step: ',i)
        for m in moons:
            for o in moons:
                if m==o:
                    continue
                m.gravity(o)
                
        for moon in moons:
            moon.move()
            moon.update_position()
        
        i+=1
        
def get_TotalEnergy(moons):
    TE=0
    for moon in moons:
        TE+=moon.getEnergy()

    
    return TE
    
    
if __name__ == '__main__':
    filename='12.txt'
    moons=get_moons(filename)
    # print(Io.PE)
    
    # Io=Moon('Io',-8,-10,0)
    # Europa=Moon('Europa',5,5,10)
    # Ganymede=Moon('Ganymede',2,-7,3)
    # Callisto=Moon('Callisto',9,-8,-3)
    # moons=[Io,Europa,Ganymede,Callisto]

    track(moons,1000)
    print(get_TotalEnergy(moons))
