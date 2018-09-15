import blocks

def find_block(init, test, cleanup):
  for block_class in blocks.block_classes:
    block = block_class()
    try:
      init(block)
      if test(block):
        return block
    finally:
      cleanup()
