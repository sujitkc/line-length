def add_word(line, words, MaxLength):
  newline = line + words[0]
  if(len(newline) == MaxLength):
    return newline, words[1:]
  elif(len(newline) < MaxLength):
    if(len(words) > 1):
      return newline + " ", words[1:]
    else:
      return newline, []
  else:
    raise Exception("add_word: resultant line is longer than MaxLength: "\
      + newline)

def is_addable(line, word, MaxLength):
  return len(line + word) <= MaxLength

def hyphenate(line, words, MaxLength):
  l = MaxLength - len(line) - 1
  if(l == 0):
    raise Exception("Hyphenate can't proceed!")
  word = words[0]
  w1 = word[:l] + "-"
  w2 = word[l:]
  newwords = [w1, w2]
  newwords.extend(words[1:])
  return newwords

'''
This loop starts adding the subwords of a hyphenated word from the
next line. Once it is seen the the next word can't be inserted into
the current line in its entirety, the current line is added to the
list of completed lines. Then looping starts just like start.
'''
def loop1(lines, line, words, MaxLength):
  if(words == []):
    if(line != ""):
      return lines + [line]
    return lines
  if(is_addable(line, words[0], MaxLength)):
    newline, newwords = add_word(line, words, MaxLength)
    if(len(newline) == MaxLength):
      return loop1(lines + [newline], "", newwords, MaxLength)
    else:
      return loop1(lines, newline, newwords, MaxLength)
  else:
    if(line == ""):
      newwords = hyphenate(line, words, MaxLength)
      return loop1(lines, line, newwords, MaxLength)
    else:
      return loop1(lines + [line], "", words, MaxLength)

def loop2(lines, line, words, MaxLength):
  if(words == []):
    if(line != ""):
      return lines + [line]
    return lines
  if(is_addable(line, words[0], MaxLength)):
    newline, newwords = add_word(line, words, MaxLength)
    if(len(newline) == MaxLength):
      return loop2(lines + [newline], "", newwords, MaxLength)
    else:
      return loop2(lines, newline, newwords, MaxLength)
  else:
    newwords = hyphenate(line, words, MaxLength)
    return loop2(lines, line, newwords, MaxLength)

def compute_lines(text, MaxLength):
  words = text.split(" ")
  return loop2([], "", words, MaxLength)

def t_add_word_1():
  line = "Hello "
  words = ["World", "and", "others"]
  print(add_word(line, words, 15))

def t_hyphenate_1():
  line = "Hello "
  words = ["Worldand", "others"]
  print(hyphenate(line, words, 10)) 

def t_loop1_1():
  words = ["hello", "hekjhsfsdhfsebwetrewthewbrtewewtrewbrt"]
  print("words = ", str(words))
  print(loop1([], "", words, 10))

def t_loop2_1():
  words = ["hello", "hekjhsfsdhfsebwetrewthewbrtewewtrewbrt"]
  print("words = ", str(words))
  print(loop2([], "", words, 10))

def t_compute_lines_1():
  text = "hello hekjhsfsdhfsebwetrewthewbrtewewtrewbrt"
  print(compute_lines(text, 15))
  
if __name__ == "__main__":
  #t_add_word_1()
  #t_hyphenate_1()
  t_loop1_1()
  t_loop2_1()
  t_compute_lines_1()
