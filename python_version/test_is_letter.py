import find_block

def init(block):
  pass

def test(block):
  return (
    block.call('a') == True and
    block.call('1') == False and
    block.call('#') == False
  )

def cleanup():
  pass

if __name__ == '__main__':
  block = find_block.find_block(init, test, cleanup)
  print 'x:', block.call('x')
  print '2:', block.call('2')
