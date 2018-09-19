const blocks = require('./blocks');

exports.find_block = function(init_test, test, cleanup_test) {
  for(var i = 0; i < blocks.block_classes.length; i++) {
    const block = new blocks.block_classes[i]();
    try {
      init_test(block);
      if(test(block)) {
        return block;
      }
    }
    finally {
      cleanup_test();
    }
  }
};
