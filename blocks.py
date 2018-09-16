import inspect, os, glob

class Block:
  def init(self, *a):
    if len(inspect.getargspec(self.init_).args) == len(a) + 1:
      return self.init_(*a)

  def init_(self):
    pass

  def call(self, *a):
    if len(inspect.getargspec(self.call_).args) == len(a) + 1:
      return self.call_(*a)

class IsLetter(Block):
  def call_(self, ch):
    return ch.isalpha()

class FindAllFiles(Block):
  def init_(self, dir_path):
    self.dir_path = dir_path
    self.path_to_text = {}
    for path in glob.glob(os.path.join(dir_path, '*')):
      with open(path) as f:
        text = f.read()
      self.path_to_text[path] = text.lower()

  def call_(self, query_string):
    if not hasattr(self, 'dir_path'):
      return

    matches = []
    query_lower = query_string.lower()

    for path in glob.glob(os.path.join(self.dir_path, '*')):
      if query_lower in path:
        matches.append(path)

      if query_string in self.path_to_text[path]:
        matches.append(path)
    return matches

class Fibonacci(Block):
  def call_(self):
    a, b = 1, 1
    while True:
      yield a
      a, b = b, a + b

class Primes(Block):
  def isPrimeNumber(self, n):
      if n==1:
          return False
      for x in range(2,n):
          if n % x == 0:
              return False
      return True

  def call_(self):
      n = 1
      while(True):
          if self.isPrimeNumber(n): yield n
          n += 1

class PathExists(Block):
  def call_(self, path):
    return os.path.exists(path)

block_classes = [IsLetter, FindAllFiles, Fibonacci, Primes, PathExists]
