const { createServer } = require('node:http');
const countStudents = require('./3-read_file_async');

const app = createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/students') {
    countStudents(process.argv[2])
      .then((data) => {
        res.end(`This is the list of our students\n${data}`);
      })
      .catch((error) => {
        res.end(`This is the list of our students\n${error.message}`);
      });
  } else {
    res.end('Hello Holberton School!');
  }
});

app.listen(1245);
module.exports = app;
