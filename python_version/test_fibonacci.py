import itertools

import find_block

def init(block):
  pass

def test(block):
  actual = []
  expected = [1,1,2,3,5,8,13]
  iter_ = block.call()
  if not iter_:
    return False
  for val in iter_:
    actual.append(val)
    if len(actual) == len(expected):
      break
  return actual == expected

def cleanup():
  pass

if __name__ == '__main__':
  block = find_block.find_block(init, test, cleanup)
  for x in itertools.islice(block.call(), 0, 10):
    print x
