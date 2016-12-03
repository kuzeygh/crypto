#!/usr/bin/python3
import functools
import string

def xorcrypt(key, cipher):
  return ''.join([chr(key ^ x) for x in cipher])

def asciiUpper(text):
  for c in text:
    i = string.ascii_lowercase.find(c)
    if i == -1:
      yield c
    else:
      yield c.upper()

def alphaCount(text):
  counts = [0] * 256
  for c in asciiUpper(text):
    counts[ord(c)] += 1
  return counts

def dist(count1, count2):
  diffs = map(lambda x, y: abs(x - y), count1, count2)
  return sum(diffs)

def expectedCounts(total):
  freqs = [0] * 256
  freqs[ord('A')] = total *  8.167 / 100.0
  freqs[ord('B')] = total *  1.492 / 100.0
  freqs[ord('C')] = total *  2.782 / 100.0
  freqs[ord('D')] = total *  4.253 / 100.0
  freqs[ord('E')] = total * 12.702 / 100.0
  freqs[ord('F')] = total *  2.228 / 100.0
  freqs[ord('G')] = total *  2.015 / 100.0
  freqs[ord('H')] = total *  6.094 / 100.0
  freqs[ord('I')] = total *  6.966 / 100.0
  freqs[ord('J')] = total *  0.153 / 100.0
  freqs[ord('K')] = total *  0.772 / 100.0
  freqs[ord('L')] = total *  4.025 / 100.0
  freqs[ord('M')] = total *  2.406 / 100.0
  freqs[ord('N')] = total *  6.749 / 100.0
  freqs[ord('O')] = total *  7.507 / 100.0
  freqs[ord('P')] = total *  1.929 / 100.0
  freqs[ord('Q')] = total *  0.095 / 100.0
  freqs[ord('R')] = total *  5.987 / 100.0
  freqs[ord('S')] = total *  6.327 / 100.0
  freqs[ord('T')] = total *  9.056 / 100.0
  freqs[ord('U')] = total *  2.758 / 100.0
  freqs[ord('V')] = total *  0.978 / 100.0
  freqs[ord('W')] = total *  2.360 / 100.0
  freqs[ord('X')] = total *  0.150 / 100.0
  freqs[ord('Y')] = total *  1.974 / 100.0
  freqs[ord('Z')] = total *  0.074 / 100.0
  return freqs

def main():
  msg = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
  cipher = bytes.fromhex(msg)
  print("cipher: ", cipher)

  engCount = expectedCounts(len(cipher))
  minDist = 999999
  bestPlain = ''
  for key in range(256):
    plain = xorcrypt(key, cipher)
    currCount = alphaCount(plain)
    currDist = dist(currCount, engCount)
    if currDist < minDist:
      minDist = currDist
      bestCount = currCount
      bestPlain = plain

  print(bestPlain)
  print(minDist)
  print(bestCount)

if __name__ == "__main__":
  main()
