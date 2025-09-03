const fs = require('fs');

function countStudents(path) {
  let file;
  try {
    file = fs.readFileSync(path, 'utf-8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = file.trim().split('\n');
  const students = lines.slice(1).filter((line) => line.trim() !== '');

  console.log(`Number of students: ${students.length}`);

  const groups = {};

  for (const line of students) {
    const parts = line.split(',');
    const firstname = parts[0];
    const field = parts[3];

    if (!groups[field]) {
      groups[field] = [];
    }
    groups[field].push(firstname);
  }

  for (const field in groups) {
    if (Object.prototype.hasOwnProperty.call(groups, field)) {
      const list = groups[field].join(', ');
      console.log(
        `Number of students in ${field}: ${groups[field].length}. List: ${list}`,
      );
    }
  }
}

module.exports = countStudents;
