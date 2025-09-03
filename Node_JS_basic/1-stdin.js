// 1-stdin.js
process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');

process.stdin.on('data', (data) => {
  const name = data.trim();
  process.stdout.write(`Your name is: ${name}\n`);
  process.stdin.end(); // <-- important : force la fin du flux
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
