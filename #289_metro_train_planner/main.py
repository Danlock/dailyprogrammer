METRO_DATA = {
  'ZN':'Z,VIOLET,N,VIOLET,6',
  'AN':'A,BLUE,N,BLUE,5',
  'NM':'N,BLUE,M,BLUE,5',
  'AB':'A,GREEN,B,GREEN,2',
  'BC':'B,GREEN,C,GREEN,2',
  'CD':'C,GREEN,D,GREEN,1',
  'DE':'D,GREEN,E,GREEN,1',
  'EF':'E,GREEN,F,GREEN,2',
  'FG':'F,GREEN,G,GREEN,2',
  'GJ':'G,GREEN,J,GREEN,3',
  'JM':'J,GREEN,M,GREEN,3',
  'AD':'A,YELLOW,D,YELLOW,3',
  'DG':'D,YELLOW,G,YELLOW,3',
  'GH':'G,YELLOW,H,YELLOW,2',
  'HI':'H,YELLOW,I,YELLOW,2',
  'IJ':'I,YELLOW,J,YELLOW,1',
  'JK':'J,YELLOW,K,YELLOW,2',
  'KY':'K,YELLOW,L,YELLOW,2',
  'LM':'L,YELLOW,M,YELLOW,1',
  'AA':'A,YELLOW,A,GREEN,2',
  'AA':'A,GREEN,A,BLUE,3',
  'AA':'A,YELLOW,A,BLUE,2.5',
  'DD':'D,YELLOW,D,GREEN,1.5',
  'GG':'G,YELLOW,G,GREEN,1.5',
  'JJ':'J,YELLOW,J,GREEN,1.5',
  'MM':'M,YELLOW,M,GREEN,1.5',
  'MM':'M,GREEN,M,BLUE,2',
  'MM':'M,YELLOW,M,BLUE,1',
  'NN':'N,VIOLET,N,BLUE,2',
}
def optionBuilder(start,sline,change,cline,end):
  if cline and change:
    return 'At %s, take %s line, change at %s and take %s line, then exit at %s' % (start,sline,change,cline,end)
  else:
    return 'At %s, take %s line exit at %s' % (start,sline,end)

def getBeginEndRoutes(start,end):
  b_routes,e_routes = {},{} 
  for k,v in METRO_DATA.items():
    if k[:1] == start:
      b_routes[k] = v
    elif k[1:] == end:
      e_routes[k] = v
  return (b_routes,e_routes)

def getRoute(start,end):
  b_routes,e_routes = getBeginEndRoutes(start,end)

  for k,v in b_routes.items():
    if k[1:] == end: # found it 
      return vW

  return 'unfinished'

def main():
  s = input("Enter start letter. ")
  e = input("Enter end letter. ")
  s = s.upper()
  e = e.upper()
  print(getRoute(s,e))







if __name__ == '__main__':
  main()