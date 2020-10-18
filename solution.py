testers = ["code", "Braille", "The quick brown fox jumps over the lazy dog",]
import re

def getBraille(code):
  string = ''
  brillesLib = ["000000", "100000", "110000", "100100", "100110", "100010", "110100", "110110", "110010", "010100", "010110", "101000", "111000", "101100", "101110", "101010", "111100", "111110", "111010", "011100", "011110", "101001", "111001", "010111", "101101", "101111", "101011"]
  captialize = "000001"
  def findIndex(code):
    asciiCodes = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for index, letter in enumerate(asciiCodes):
      if letter == code:
        return index

  if re.findall("[a-z\s]", code):
    i = findIndex(code)
    string += brillesLib[i]
  elif re.findall("[A-Z]", code):
    i = findIndex(code.lower())
    string += captialize
    string += brillesLib[i]
  else:
    string += brillesLib[0]
  return string

def getTargetDate(asciiCode):
  output = ''
  for i,letter in enumerate(asciiCode):
    output += getBraille(letter)
    if i == (len(asciiCode) - 1) or i == 54:
      break
  return output

def solution(asciiCode):
  return getTargetDate(asciiCode)
  #print(getTargetDate(asciiCode))

# for i, test in enumerate(testers):
#   solution(test)