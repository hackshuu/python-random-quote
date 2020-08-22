import random



def principal():
  
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) -1
  rnd = random.randint(0,last)
  quantidade = rnd
  count = 0;
  while count <=quantidade:
        rnd = random.randint(0,last)
        print(quotes[rnd])
        count = count+1

if __name__== "__main__":
  principal()
