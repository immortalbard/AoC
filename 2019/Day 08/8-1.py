
class Layer:
    def __init__(self, name):
        self.name = name
        self.count=['','','']
        self.num0=self.count[0]
        self.num1=self.count[1]
        self.num2=self.count[2]

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

def split_layers(layers,width):
    for i in range(len(layers)):
        layers[i]=list(layers[i][0+x:width+x] for x in range(0,len(layers[i]),width))

    return layers

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


if __name__ == "__main__":
    filename='8.txt'

    data=getdata(filename)
    data0='123456789012'
    print(len(data0),type(data0))
    width=25
    height=6
    layers=list(getlayers(data,width,height))
    print(check(layers))
