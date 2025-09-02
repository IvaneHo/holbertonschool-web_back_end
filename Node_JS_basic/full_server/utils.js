import fs from 'fs';

export function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n').slice(1).filter((l) => l.trim() !== '');
      const fields = {};

      lines.forEach((line) => {
        const parts = line.split(',');
        const firstname = parts[0].trim();
        const field = parts[parts.length - 1].trim();

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      resolve(fields);
    });
  });
}
