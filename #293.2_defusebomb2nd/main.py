'''
You have to start with either with a white or a red wire.
If you picked white wire you can either pick another white wire again or you can take an orange one.
If you picked a red wire you have the choice between a black and red wire.
When a second red wire is picked, you can start from rule one again.

Back to the second rule, if you picked another white one you will have to pick a black or red one now
When the red wire is picked, you again go to rule one.
On the other hand if you then picked an orange wire, you can choose between green, orange and black.
When you are at the point where you can choose between green, orange and black and you pick either green or orange you have to choose the other one and then the bomb is defused.
If you ever pick a black wire you will be at the point where you have to choose between green, orange and black

'''
import re

tree = [
  [('W',1),('R',2)],
  [('W',2),('O',3)],
  [('R',0),('B',3)],
  [('B',3),('O',4),('G',5)],
  [('G',6)],
  [('O',6)],
  ]

def main():
  with open('defuse.txt', 'r') as f:
    state = 0
    for line in f.readlines():
      c = line.strip()[:1].upper()
      result = [index for color,index in tree[state] if color == c]
      if len(result) != 1:
        print("Boom!")
        exit()

      state = result.pop(0)
      # print('Now on ',line,'and state ',state)
      if state is 6:
        print("Bomb defused!")
        exit()

  print("Boom!")
  return


if __name__ == '__main__':
    main()