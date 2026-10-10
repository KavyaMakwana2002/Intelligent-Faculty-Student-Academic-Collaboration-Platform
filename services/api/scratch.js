const sqlite3 = require('sqlite3').verbose(); 
const db = new sqlite3.Database('./database.sqlite'); 
db.serialize(() => { 
  db.run(`CREATE TABLE IF NOT EXISTS submissions (id INTEGER PRIMARY KEY AUTOINCREMENT, assignment_id INTEGER NOT NULL, student_id INTEGER NOT NULL, file_url TEXT, submitted_at TEXT NOT NULL, marks_awarded INTEGER, status TEXT DEFAULT 'Submitted', UNIQUE(assignment_id, student_id))`); 
});
console.log("Table created");
