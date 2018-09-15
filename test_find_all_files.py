import os, shutil, glob

import find_block

def init(block):
  # Create test directory with a couple test files.
  if not os.path.exists('test_dir'):
    os.mkdir('test_dir')
    with open('test_dir/1.txt', 'w') as f:
      f.write('some text')
    with open('test_dir/2.txt', 'w') as f:
      f.write('other text')

  # The block should read the contents of the test directory on initialization.
  block.init('test_dir')

def test(block):
  return (
    block.call('some') == ['test_dir/1.txt'] and
    block.call('other') == ['test_dir/2.txt'] and
    block.call('nothing') == []
  )

def cleanup():
  shutil.rmtree('test_dir')

if __name__ == '__main__':
  print find_block.find_block(init, test, cleanup)
