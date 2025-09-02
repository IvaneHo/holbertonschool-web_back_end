const http = require('http');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n');
      const students = lines.slice(1).filter((line) => line.trim() !== '');

      const report = [];
      report.push(`Number of students: ${students.length}`);

      const fields = {};

      students.forEach((line) => {
        const parts = line.split(',');
        const firstname = parts[0].trim();
        const field = parts[parts.length - 1].trim();

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      for (const [field, names] of Object.entries(fields)) {
        report.push(
          `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`
        );
      }

      resolve(report.join('\n'));
    });
  });
}

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    countStudents(process.argv[2])
      .then((data) => {
        res.end(data);
      })
      .catch(() => {
        res.end('Cannot load the database');
      });
  } else {
    res.end('Not found');
  }
});

app.listen(1245);

module.exports = app;
