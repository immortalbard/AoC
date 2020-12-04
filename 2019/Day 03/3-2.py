#! python3


class Wire:
  def __init__(self, name):
    self.name = name
    self.x = 0
    self.y = 0
    self.coord = []

  def move(self, inst):
    dx = int(
        inst[1:]) if 'R' in inst else -int(inst[1:]) if 'L' in inst else 0
    dy = int(
        inst[1:]) if 'U' in inst else -int(inst[1:]) if 'D' in inst else 0

    coords = [
        (self.x, y) for y in range(self.y, self.y + dy, int(dy / abs(dy)))
    ] if dx == 0 else [
        (x, self.y) for x in range(self.x, self.x + dx, int(dx / abs(dx)))
    ] if dy == 0 else []
    self.coord += coords

    self.x += dx
    self.y += dy


def get_wires(filename):
  file = open(filename)

  val = file.read().split('\n')

  file.close()

  wires = [val.split(',') for val in val]

  wire1 = Wire('A')
  for inst in wires[0]:
      wire1.move(inst)
  wire2 = Wire('B')
  for inst in wires[1]:
      wire2.move(inst)
  print('Wires loaded')
  return wire1, wire2


def Manhattan_dist(a, b):
  return int(abs(int(a)) + abs(int(b)))


def short(wire1, wire2):
  cross = list(set(wire1.coord).intersection(wire2.coord))
  dist = {}

  for i in cross:
    dist[i]=Manhattan_dist(i[0],i[1])

  del dist[(0,0)]

  return dist

def first(wire1,wire2):
  dist=short(wire1,wire2)
  foo=[]
  for key in dist.keys():
    foo.append(wire1.coord.index(key)+wire2.coord.index(key))

  return(min(foo))


if __name__ == '__main__':
  filename = '3.txt'
  wire1, wire2 = get_wires(filename)
  first=first(wire1,wire2)
  print(first)

