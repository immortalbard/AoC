
class Layer:
    def __init__(self, name):
        self.name = name
        self.count=['','','']
        self.num0=self.count[0]
        self.num1=self.count[1]
        self.num2=self.count[2]
        self.layer=[]

    def name(self):
        return self.name

    def __repr__(self):
        return self.name
        
    def __str__(self):
        return self.name
        
    def counted(self):
        self.count[0] = self.name.count('0')
        self.count[1] = self.name.count('1')
        self.count[2] = self.name.count('2')

    def split_layers(self,width,height):
        self.layer=[[self.name[0+x:width+x][k] for k in range(width)] for x in range(0,len(self.name),width)]


def getdata(filename):
    file = open(filename)

    data = file.read()

    file.close()

    return data

def getlayers(data,width,height):
    length=width*height
    layers=list(data[0+i:length+i] for i in range(0, len(data), length))
    layerlist=[Layer(layer) for layer in layers]

    return layerlist


def check(layers):
    checklist=[]
    check0=[]
    for layer in layers:
        layer.counted()
        checklist.append([layer.name]+layer.count)
        check0.append(layer.count[0])
        
    for i in range(len(checklist)):
        if checklist[i][1]==min(check0):
            return checklist[i][2]*checklist[i][3]

def image(layers,width,height,black,white):
    image=[['' for j in range(width)] for i in range(height)]
    for layer in layers:
        layer.split_layers(width,height)
        for l in range(height):
            for k in range(width):
                if layer.layer[l][k]=='0' and image[l][k]=='':
                    image[l][k]=black
                elif layer.layer[l][k]=='1' and image[l][k]=='':
                    image[l][k]=white
                else:
                    pass
    
    return image

if __name__ == "__main__":
    filename='8.txt'

    data=getdata(filename)
    data0='123456789012'
    data1='0222112222120000'
    data2='022222112222221222000000'
    width=25
    height=6
    black=' '
    white=u"\u2588"
    layers=list(getlayers(data,width,height))
    image=image(layers,width,height,black,white)
    for i in range(height):
        print(image[i])