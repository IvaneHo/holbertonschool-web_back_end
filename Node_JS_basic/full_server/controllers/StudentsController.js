import { readDatabase } from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    const database = process.argv[2];

    readDatabase(database)
      .then((fields) => {
        let response = 'This is the list of our students\n';

        // Trier les clés (CS, SWE) par ordre alphabétique insensible à la casse
        const sortedFields = Object.keys(fields).sort((a, b) =>
          a.toLowerCase().localeCompare(b.toLowerCase())
        );

        sortedFields.forEach((field) => {
          const names = fields[field];
          response += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
        });

        res.status(200).send(response.trim());
      })
      .catch((err) => {
        res.status(500).send(err.message);
      });
  }

  static getAllStudentsByMajor(req, res) {
    const database = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(database)
      .then((fields) => {
        const names = fields[major] || [];
        res.status(200).send(`List: ${names.join(', ')}`);
      })
      .catch((err) => {
        res.status(500).send(err.message);
      });
  }
}

export default StudentsController;
