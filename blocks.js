const glob = require('glob');
const path = require('path');
const fs = require('fs');

function Block() {}

Block.prototype.init = function() {
  if(this.init_.length == arguments.length)
    return this.init_.apply(this, arguments);
}

Block.prototype.init_ = function() {}

Block.prototype.call = function() {
  if(this.call_.length == arguments.length)
    return this.call_.apply(this, arguments);
}

function FindAllFiles() {
  Block(this);
}
FindAllFiles.prototype = Object.create(Block.prototype);

FindAllFiles.prototype.init_ = function(dir_path) {
  this.dir_path = dir_path
  this.path_to_text = {}
  const that = this;
  glob.sync(path.join(dir_path, '*')).forEach(function(path_) {
    const text = fs.readFileSync(path_, 'utf8');
    that.path_to_text[path_] = text.toLowerCase();
  });
};

FindAllFiles.prototype.call_ = function(query_string) {
  if(this.dir_path === undefined)
    return;

  let matches = [];
  const query_lower = query_string.toLowerCase();

  const that = this;
  glob.sync(path.join(this.dir_path, '*')).forEach(function(path_) {
    if(path_.indexOf(query_lower) != -1)
      matches.push(path_)

    if(that.path_to_text[path_].indexOf(query_string) != -1)
      matches.push(path_)
  });

  return matches
};

exports.block_classes = [FindAllFiles];
