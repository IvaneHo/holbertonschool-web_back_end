const express = require('express');
const fs = require('fs');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];
const app = express();

app.get('/', (req, res) => {
  res.type('text/plain');
  res.status(200).send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.type('text/plain');
  res.write('This is the list of our students\n');

  countStudents(database)
    .then(() => {
      fs.readFile(database, 'utf-8', (err, data) => {
        if (err) {
          res.end('Cannot load the database');
          return;
        }

        const lines = data.split('\n').filter((line) => line.trim() !== '');
        if (lines.length <= 1) {
          res.end('Number of students: 0');
          return;
        }

        const students = lines.slice(1);
        const fields = {};
        let total = 0;

        for (const line of students) {
          const parts = line.split(',');
          if (parts.length >= 4) {
            const firstname = parts[0].trim();
            const field = parts[3].trim();
            if (!fields[field]) fields[field] = [];
            fields[field].push(firstname);
            total += 1;
          }
        }

        res.write(`Number of students: ${total}\n`);
        for (const [field, names] of Object.entries(fields)) {
          res.write(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`);
        }
        res.end();
      });
    })
    .catch(() => {
      res.end('Cannot load the database');
    });
});

app.listen(1245);

module.exports = app;
