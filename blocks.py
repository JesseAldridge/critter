import inspect, os, glob

class Block:
  def init(self, *a):
    pass

  # def init(self, *a):
  #   if len(inspect.getargspec(self.init_).args) == len(a):

  # def init_(self):
  #   pass

class IsLetter(Block):
  def call(self, ch):
    return ch.isalpha()

class FindAllFiles(Block):
  def init(self, dir_path):
    self.dir_path = dir_path
    self.path_to_text = {}
    for path in glob.glob(os.path.join(dir_path, '*')):
      with open(path) as f:
        text = f.read()
      self.path_to_text[path] = text.lower()

  def call(self, query_string):
    matches = []
    query_lower = query_string.lower()

    for path in glob.glob(os.path.join(self.dir_path, '*')):
      if query_lower in path:
        matches.append(path)

      if query_string in self.path_to_text[path]:
        matches.append(path)
    return matches

block_classes = [IsLetter, FindAllFiles]
