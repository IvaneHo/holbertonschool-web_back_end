const fs = require('fs');

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }
      const lines = data
        .trim()
        .split('\n')
        .filter((line) => line.trim() !== '');

      const header = lines.shift().split(',');
      const firstnameIndex = header.indexOf('firstname');
      const fieldIndex = header.indexOf('field');

      const studentsByField = {};

      lines.forEach((line) => {
        const parts = line.split(',');
        const firstname = parts[firstnameIndex];
        const field = parts[fieldIndex];

        if (firstname && field) {
          if (!studentsByField[field]) {
            studentsByField[field] = [];
          }
          studentsByField[field].push(firstname);
        }
      });

      resolve(studentsByField);
    });
  });
}

module.exports = readDatabase;
