#!/usr/bin/env python3

from automaton import Automaton, EPSILON, error, warn
import sys
import pdb



def is_deterministic(a:'Automaton')->bool:
     for nameState in a.statesdict:
      for transition in a.statesdict[nameState].transitions.items():
          if transition[0] == "%":
              return False
          elif len(transition[1]) > 1:
              return False    
      return True
  
  
  
def recognizes(a:'Automaton', word:str)->bool:
  if not is_deterministic(a):
      print("L'automate n'est pas deterministe")
  for (source,symb,dest) in a.transitions :
    state = source
    break
  for i in range(len(word)):
    letter = word[i]
    if letter in str(list(a.statesdict[state].transitions)):
      state = str(list(a.statesdict[state].transitions[letter])[0])
    elif letter != '%':
        return False
  if state in a.acceptstates:
    return True
  return False



if __name__ == "__main__" :
  if len(sys.argv) != 3:
    usagestring = "Usage: {} <automaton-file.af> <word-to-recognize>"
    error(usagestring.format(sys.argv[0]))

  automatonfile = sys.argv[1]  
  word = sys.argv[2]

  a = Automaton("dummy")
  a.from_txtfile(automatonfile)

  if not is_deterministic(a) :
    print("ERROR")
  elif recognizes(a, word):
    print("YES")
  else:
    print("NO")