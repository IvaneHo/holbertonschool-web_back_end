const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(request, response) {
    const dbPath = process.argv[2];

    readDatabase(dbPath)
      .then((studentsByField) => {
        let output = 'This is the list of our students\n';

        const sortedFields = Object.keys(studentsByField).sort((a, b) => a.toLowerCase()
          .localeCompare(b.toLowerCase()));

        sortedFields.forEach((field, index) => {
          const list = studentsByField[field];
          output += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
          if (index < sortedFields.length - 1) {
            output += '\n';
          }
        });

        response.status(200).send(output);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const dbPath = process.argv[2];
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(dbPath)
      .then((studentsByField) => {
        const list = studentsByField[major] || [];
        response.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

module.exports = StudentsController;
