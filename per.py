#! /usr/bin/env python3

import sys

# Find persistence values for numbers with the given length
def findper(len):
  res = 1
  max = 0
  for n in gen(len):
    p = per(n)
    if p > max:
      res = n
      max = p
  return res, max

# Find persistence of the given number
def per(n):
  steps = 0
  while len(str(n)) > 1:
    steps +=1
    res = 1
    for d in str(n):
      res *= int(d)
    n = res
  return steps

# Generate all relevant numbers of length n
def gen(n):
  # Relevant numbers can only start with a few options, as we want the smallest
  # Some number combinations would end up multiplying by a number that is better represented as a different set of numbers
  # 2,2 2,3 2,4 and 3,3 are out as 4 6 8 and 9 are better
  # 3,4 is out (2,6 is better)
  # 3,6 is out (2,9 is better)
  # 4,4 is out (2,8 is better)
  # 4,6 is out (3,7 is better)
  # 6,6 is out (4,9 is better)
  # Note that this list automatically ends up searching numbers in numerical order
  for start in ['26', '2', '3', '4', '6', '' ]:
    for end in gen_789s(n-len(start)):
      yield start + end
  # I don't know if there is theory around numbers with 5, but some small numbers do have decent
  # persistence, e.g. 335
  # However if a number contains a 5 and any even digit, it will have a persistence of 2,
  # so we can discard those.
  for start in ['3', '' ]:
    for end in gen_579s(n-len(start)):
      yield start + end
  return 

# Generate all strings of length n that consist of only 5s, 7s and 9s (in order)
def gen_579s(n):
  for n_5 in countdown(n):
    for n_7 in countdown(n - n_5):
      n_9 = (n - n_5 - n_7)
      yield ('5' * n_5) + ('7' * n_7) + ('9' * n_9)

# Generate all strings of length n that consist of only 7s, 8s, and 9s (in order)
def gen_789s(n):
  for n_7 in countdown(n):
    for n_8 in countdown(n - n_7):
      n_9 = (n - n_7 - n_8)
      yield ('7' * n_7) + ('8' * n_8) + ('9' * n_9)

# Count down from n to 0 inclusive
def countdown(n):
  i = n
  while i > -1:
    yield i
    i -= 1 


if __name__ == '__main__':
  n = 230
  while True:
    print(f'Checking {n}', flush=True)
    num, persistence = findper(n)
    # print(f'  NUM {num}')
    # print(f'  PERSISTENCE {persistence}')
    # 11 is the current world record
    if persistence >= 11:
      print(f'  NUM {num}', flush=True)
      print(f'  PERSISTENCE {persistence}', flush=True)
      break
    n+=1
