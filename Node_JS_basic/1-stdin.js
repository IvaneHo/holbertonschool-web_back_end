process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');

let inputReceived = false;

process.stdin.on('data', (data) => {
  if (!inputReceived) {
    const input = data.trim();
    process.stdout.write(`Your name is: ${input}\n`);
    inputReceived = true;
  }
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
