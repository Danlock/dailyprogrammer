#I could also delete the punctuation marks from the output... but i wont
#the reddit question's example output was wrong, 
#and subsequently called out in the comments, look there for corrections

#get list of stop words in between alliteration
stopWords = []
with open('stop-words.txt', 'r') as f:
  for line in f.readlines():
    stopWords.append(line.strip())

def outputAlliteration(line):
  #split line along whitespace
  output = set()
  words = line.split()
  previous = words[0]
  words = words[1:]
  cWords = list(words)
  #remove stop words from line, add words if first letter is same
  for w in cWords:
    if w in stopWords:
      words.remove(w)
      continue
    if w[:1].lower() == previous[:1].lower():
      # print(previous)
      output.add(w.lower())
      output.add(previous.lower())
    previous = w
  
  return output

def main():
  #read in the input
  inputText = []
  with open('input.txt','r') as f:
    #first line is number
    for line in f.readlines():
      inputText.append(line.strip())

  numLines = int(inputText[:1][0]) + 1
  inputText = inputText[1:numLines]

  for line in inputText:
    print(' '.join(outputAlliteration(line)))

if __name__ == '__main__':
    main()