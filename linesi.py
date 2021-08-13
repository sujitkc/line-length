#!/usr/bin/python3
import matplotlib.pyplot as plt

def hyphenate(word, length):
  if(len(word) > length):
    w = word[:length - 1] + "-"
    ws = hyphenate(word[length - 1:], length)
    hwords = [w] + ws
  else:
    hwords = [word]
  return hwords
  
def complete_line1(line, lines, word, MaxLength):
  if(line != ""):
    lines.append(line.strip())
  return 0

def complete_line2(line, lines, word, MaxLength):
  l = MaxLength - len(line) - 1
  w = word[:l] + "-"
  line += w
  lines.append(line)
  return l

def make_compute_lines(complete_line):
  def compute_lines(text, MaxLength):
    words = text.split(" ")
    lines = []
    line = ""
    for word in words:
      if(len(line + word) > MaxLength):
        l = complete_line(line, lines, word, MaxLength)
        line = ""
        hwords = hyphenate(word[l:], MaxLength)
        for hw in hwords[:-1]:
          lines.append(hw)
        line = hwords[-1]
      elif(len(line + word) < MaxLength):
        line += (word + " ")
      else:
        line += word
    
    if(line != ""):
      lines.append(line.strip())
    return lines
  return compute_lines

compute_lines = make_compute_lines(complete_line1)

def compute_line_efficiency(text, MaxLength):
  lines = compute_lines(text, MaxLength) 
  line_lengths = [len(line) for line in lines]
  space_used = sum(line_lengths)
  num_lines = len(lines)
  total_space = num_lines * MaxLength
  efficiency = space_used / total_space
  return efficiency

def read_input(fname):
  fin = open(fname, "r")
  text = fin.read()
  fin.close()
  return text

def compute_and_plot(fname, plt):
  # compute
  text = read_input(fname)
  lines = compute_lines(text, 20)
  efficiencies = [(ml, compute_line_efficiency(text, ml)) for ml in range(4, 80)]

  # plot
  plt.plot([ml for (ml, _) in efficiencies], [e for (_, e) in efficiencies])

def t_hyphenate_1():
  w = "hekjhsfsdhfsebwetrewthewbrtewewtrewbrt"
  print(w)
  print(hyphenate(w, 10))

def t_compute_lines(w, l):
  lines = compute_lines(w, l)
  print(w)
  print(lines)

def t_compute_lines_1():
  t_compute_lines("hello hekjhsfsdhfsebwetrewthewbrtewewtrewbrt", 10)

def t_compute_lines_2():
  t_compute_lines("hekjhsfsdhfsebwetrewthewbrtewewtrewbrt", 10)

def t_compute_lines_3():
  text = "Removed the bug from linesi which was causing the first subword of the hyphenated word to appear twice."
  print(text)
  print(compute_lines(text, 10))
  
if __name__ == "__main__":
  t_hyphenate_1()
  t_compute_lines_1()
  t_compute_lines_2()
  t_compute_lines_3()
