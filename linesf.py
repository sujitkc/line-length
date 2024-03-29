def add_word(line, words, MaxLength):
  newline = line + words[0]
  if(len(newline) == MaxLength):
    return newline, words[1:]
  else:
    if(len(words) > 1):
      return newline + " ", words[1:]
    else:
      return newline, []

def is_addable(line, word, MaxLength):
  return len(line + word) <= MaxLength

def hyphenate(line, words, MaxLength):
  l = MaxLength - len(line) - 1
  word = words[0]
  w1, w2 = word[:l] + "-", word[l:]
  newwords = [w1, w2]
  newwords.extend(words[1:])
  return newwords

# This function returns an updated 'words' list by adding the current
# 'line' to lines
def update1(lines, line, words, MaxLength):
  if(line == ""):
    newwords = hyphenate(line, words, MaxLength)
    return lines, line, newwords
  else:
    return lines + [line.strip()], "", words

# This function returns an updated 'words' by hyphenating the first word.
def update2(lines, line, words, MaxLength):
  newwords = hyphenate(line, words, MaxLength)
  return lines, line, newwords

'''
make_loop is a higher order function that returns a function
that stands for the compute_line function parameterised with
the appropriate hyphenation policy.
'''
def make_loop(update):
  def loop(lines, line, words, MaxLength):

    while(True):
      if(words == []):
        if(line != ""):
          return lines + [line]
        return lines
      if(is_addable(line, words[0], MaxLength)):
        newline, newwords = add_word(line, words, MaxLength)
        if(len(newline) == MaxLength):
          lines, line, words = lines + [newline.strip()], "", newwords
          continue
        else:
          lines, line, words = lines, newline, newwords
          continue
      else:
        lines, line, words = update(lines, line, words, MaxLength)
        continue

  return loop

loop = make_loop(update1)

def compute_lines(text, MaxLength):
  words = text.split(" ")
  return loop([], "", words, MaxLength)

def t_add_word_1():
  line = "Hello "
  words = ["World", "and", "others"]
  print(add_word(line, words, 10))

def t_hyphenate_1():
  line = "Hello "
  words = ["Worldand", "others"]
  print(hyphenate(line, words, 10)) 

def t_loop_1():
  words = ["hello", "hekjhsfsdhfsebwetrewthewbrtewewtrewbrt"]
  print("words = ", str(words))
  print(loop([], "", words, 10))

def t_compute_lines_1():
  text = "hello hekjhsfsdhfsebwetrewthewbrtewewtrewbrt"
  print(text)
  print(compute_lines(text, 10))

def t_compute_lines_2():
  text = "Removed the bug from linesi which was causing the first subword of the hyphenated word to appear twice."
  print(text)
  print(compute_lines(text, 10))
  
if __name__ == "__main__":
  t_compute_lines_1()
  t_compute_lines_2()
