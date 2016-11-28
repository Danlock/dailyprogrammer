'''
If you cut a white cable you can't cut white or black cable.
If you cut a red cable you have to cut a green one
If you cut a black cable it is not allowed to cut a white, green or orange one
If you cut a orange cable you should cut a red or black one
If you cut a green one you have to cut a orange or white one
If you cut a purple cable you can't cut a purple, green, orange or white cable


Can:
R > G
O > R || B
G > O || W
Derived:
W > !(W || B)
B > !(W || G || O)
P > !(P || G || O || W)

Cant:
W /> W || B
B /> W || G || O
P /> P || G || O || W 
'''
#key CAN cut values
rules = dict({
  'R': ['G'],
  'O': ['R','B'],
  'G': ['O','W'],
  'W': ['P','G','O','R'],
  'B': ['P','B','R'],
  'P': ['B','R'],
})

def main():
  with open('defuse.txt', 'r') as f:
    colors = []
    last = None
    for line in f.readlines():
      c = line.strip()[:1].upper()
      colors.append(c)
      if last is not None:
        if c not in rules[last]:
          print("Boom!")
          exit()
      last = c
  print("Bomb defused!")
  return

if __name__ == '__main__':
    main()