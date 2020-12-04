#! python3

class Deck:
  def __init__(self, card_num):
    self.cards = [x for x in range(card_num)]
    self.length = len(self.cards)

  def deal(self):
    self.cards=self.cards[::-1]

  def cut(self,n):
    self.cards=self.cards[n:]+self.cards[:n]
  
  def n_deal(self,n):
    deck=['' for _ in range(self.length)]
    for x in range(self.length):
      # print(x%10,x//n,self.cards[x//n])
      deck[(x*n)%len(self.cards)]=self.cards[x]
    self.cards=deck
    # print(self.cards)
    
def get_orders(filename):
  file = open(filename)

  orders = file.read().split('\n')

  file.close()

  return orders

def shuffle(deck,orders):
  for order in orders:
    print(order)
    if order=='deal into new stack':
      deck.deal()
      # print(deck.cards[2019])
    elif 'cut ' in order:
      deck.cut(int(order.split(' ')[-1]))
      # print(deck.cards[2019])
    elif 'deal with increment ' in order:
      deck.n_deal(int(order.split(' ')[-1]))
      # print(deck.cards[2019])
    else:
      pass
  
  return(deck)


if __name__ == '__main__':
  filename = '22.txt'
  orders=get_orders(filename)
  deck=Deck(10007)
  shuffled=shuffle(deck,orders)

  print(shuffled.cards.index(2019))
