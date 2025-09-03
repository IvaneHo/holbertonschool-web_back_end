process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');

let name = '';

process.stdin.on('readable', () => {
  const chunk = process.stdin.read();
  if (chunk !== null) {
    name += chunk;
  }
});

process.stdin.on('end', () => {
  const cleanedName = name.trim();
  if (cleanedName.length > 0) {
    process.stdout.write(`Your name is: ${cleanedName}\n`);
  }
  process.stdout.write('This important software is now closing\n');
});
