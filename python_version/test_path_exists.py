import os, shutil

import find_block

def init(block):
  os.mkdir('test_dir')

def test(block):
  return (
    block.call('test_dir') == True and
    block.call('foo_dir') == False
  )

def cleanup():
  shutil.rmtree('test_dir')

if __name__ == '__main__':
  block = find_block.find_block(init, test, cleanup)
  os.mkdir('other_test_dir')
  print block.call('test_dir')
  print block.call('other_test_dir')
  shutil.rmtree('other_test_dir')
