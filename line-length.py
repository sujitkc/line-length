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
    
def compute_lines(text, max_line_length):
  words = text.split(" ")
#  avg_wlen = sum([len(w) for w in words]) / len(words)
#  print("Average word length = ", avg_wlen)

  lines = []
  curr_line = ""
  for word in words:
    if(len(curr_line + word) > max_line_length):
      lines.append(curr_line.strip())
      curr_line = ""
    if(curr_line == "" and (len(word) > max_line_length)):
      hwords = hyphenate(word, max_line_length)
      for hw in hwords[:-1]:
        lines.append(hw)
      curr_line = hwords[-1]
    else:
      curr_line += (word + " ")
  if(curr_line != ""):
    lines.append(curr_line.strip())
#  print(lines)
#  print(max_line_length, " : ", [len(line) for line in lines])
  return lines

def compute_line_efficiency(text, max_line_length):
  lines = compute_lines(text, max_line_length) 
  line_lengths = [len(line) for line in lines]
  space_used = sum(line_lengths)
  num_lines = len(lines)
  total_space = num_lines * max_line_length
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

if __name__ == "__main__":

  inputs = ["data/bolshevik.txt", "data/pigeons.txt"]
  fig = plt.figure()
  plt.xlabel("line length")
  plt.ylabel("efficiency")

  for inp in inputs:
    print("Plotting ", inp)
    compute_and_plot(inp, plt)
  
  plt.show()
  fig.savefig("plot.png", bbox_inches="tight")
