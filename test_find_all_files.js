// This is the only file the user provides

const fs = require('fs');

const nuke_dir = require('rimraf');

const find_block = require('./find_block');

function init_test(block) {
  // Create test directory with a couple test files.
  if(!fs.existsSync('test_dir')) {
    fs.mkdirSync('test_dir');

    fs.writeFileSync('test_dir/1.txt', 'some text');
    fs.writeFileSync('test_dir/2.txt', 'other text');
  }

  // The block should read the contents of the test directory on initialization.
  block.init('test_dir')
}

function arraysEqual(a, b) {
  if (a === b) return true;
  if (a == null || b == null) return false;
  if (a.length != b.length) return false;

  for (var i = 0; i < a.length; ++i) {
    if (a[i] !== b[i]) return false;
  }
  return true;
}

function test(block) {
  return (
    arraysEqual(block.call('some'), ['test_dir/1.txt']) &&
    arraysEqual(block.call('other'), ['test_dir/2.txt']) &&
    arraysEqual(block.call('nothing'), [])
  );
}

function cleanup_test() {
  nuke_dir('test_dir', function(error){});
}

if(require.main === module) {
  console.log(find_block.find_block(init_test, test, cleanup_test));
}
