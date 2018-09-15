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

block_classes = [IsLetter, FindAllFiles, Fibonacci]
