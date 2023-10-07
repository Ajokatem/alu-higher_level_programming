#!/usr/bin/node
const fs = require('fs');
//PRINT ERROR
fs.writeFile(process.argv[2], process.argv[3], (err, data) => {
  if (err) {
    console.log(err);
  }
});
