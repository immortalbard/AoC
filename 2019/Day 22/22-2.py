#! python3

# class Deck:
#   def __init__(self, card_num):
#     self.cards = [x for x in range(card_num)]
#     self.length = len(self.cards)

#   def deal(self):
#     self.cards=self.cards[::-1]

#   def cut(self,n):
#     self.cards=self.cards[n:]+self.cards[:n]
  
#   def n_deal(self,n):
#     deck=['' for _ in range(self.length)]
#     for x in range(self.length):
#       # print(x%10,x//n,self.cards[x//n])
#       deck[(x*n)%len(self.cards)]=self.cards[x]
#     self.cards=deck
#     # print(self.cards)

#   def shuffle(self,orders):
#     for order in orders:
#       if order=='deal into new stack':
#         self.deal()
#         # print(deck.cards[2019])
#       elif 'cut ' in order:
#         self.cut(int(order.split(' ')[-1]))
#         # print(deck.cards[2019])
#       elif 'deal with increment ' in order:
#         self.n_deal(int(order.split(' ')[-1]))
#         # print(deck.cards[2019])
#       else:
#         pass
    
#     return(self)
  
    
# def get_orders(filename):
#   file = open(filename)

#   orders = file.read().split('\n')

#   file.close()

#   return orders



# if __name__ == '__main__':
#   filename = '22.txt'
#   orders=get_orders(filename)
#   deck=Deck(119315717514047)
#   for _ in range(101741582076661):
#     shuffled=deck.shuffle(orders)

#   print(shuffled.cards[2019])

INPUT = "Day 22/22.txt"

DECK = 119315717514047
REPEAT = 101741582076661
POSITION = 2020

# The do-nothing shuffle: 0 + 1*x
IDENTITY = [ 0, 1 ]

# Applies shuffle f() to position x
def shuffle_apply(f, x):
    return (f[0] + f[1] * x) % DECK

# Takes shuffle f() and g() and returns the shuffle f(g())
#   f(x) = a + b*x
#   g(x) = c + d*x
#   f(g(x)) = a + b*(c + d*x)
#           = (a + b*c) + b*d*x
#           = f(c) + b*d*x
def shuffle_compose(f, g):
    return [ shuffle_apply(f, g[0]), (f[1] * g[1]) % DECK ]

# Compose a shuffle many times with itself.
#   repeat - how many repetitions to apply
#   f      - the shuffle f()
#   step   - how many repetitions f() currently represents
def shuffle_repeat(repeat, f, step = 1):
    if step > repeat:
        return IDENTITY, repeat
    fN, repeat = shuffle_repeat(repeat, shuffle_compose(f, f), step * 2)
    if step <= repeat:
        fN, repeat = shuffle_compose(f, fN), repeat - step
    return fN, repeat

# Read the input and compose all of the shuffle steps
shuf = IDENTITY
for line in [ s.strip() for s in open(INPUT).readlines() ]:
    f = line.split()
    if line == "deal into new stack":
        shuf = shuffle_compose([ -1, -1 ], shuf)
    elif line.startswith("cut"):
        shuf = shuffle_compose([ -int(f[1]), 1 ], shuf)
    elif line.startswith("deal with increment"):
        shuf = shuffle_compose([ 0, int(f[3]) ], shuf)

# Observation: Repeating the shuffle (DECK - 1) times returns it to
# the original ordering.  While this does not necessarily hold true
# for all deck sizes, it works for the deck size given in Part 2.
# (Experiment idea: What deck sizes does it work for?)
assert(shuffle_repeat(DECK - 1, shuf)[0] == IDENTITY)

# This gives us a way to apply the shuffle in reverse.  If we repeat
# the shuffle (DECK - 1 - n) times, it brings the deck to a state where
# n more shuffles will restore it to factory order.  This is exactly
# the same as reversing the shuffle n times.
shufN, _ = shuffle_repeat(DECK - 1 - REPEAT, shuf)
print(shuffle_apply(shufN, POSITION))