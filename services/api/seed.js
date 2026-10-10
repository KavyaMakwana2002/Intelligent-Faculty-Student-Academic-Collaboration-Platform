const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcryptjs');
const db = new sqlite3.Database('./database.sqlite');

async function seed() {
    console.log("Seeding Database...");
    const salt = await bcrypt.genSalt(10);
    const pass = await bcrypt.hash("password123", salt);

    db.serialize(() => {
        // Clear tables
        db.run('DELETE FROM users');
        db.run('DELETE FROM assignments');
        db.run('DELETE FROM submissions');

        // Faculty
        db.run(`INSERT INTO users (role, name, email, password, identifier) VALUES ('faculty', 'Prof. Smith', 'smith@educonnect.com', '${pass}', 'FAC001')`);
        db.run(`INSERT INTO users (role, name, email, password, identifier) VALUES ('faculty', 'Dr. Patel', 'patel@educonnect.com', '${pass}', 'FAC002')`);

        // Students (Sem 3 BCA)
        for(let i=1; i<=10; i++) {
            db.run(`INSERT INTO users (role, name, email, password, identifier, course, semester) VALUES ('student', 'Student ${i}', 'student${i}@educonnect.com', '${pass}', 'ENR2600${i}', 'bca_hons', '3')`);
        }
        // Students (Sem 1 MCA)
        for(let i=11; i<=15; i++) {
            db.run(`INSERT INTO users (role, name, email, password, identifier, course, semester) VALUES ('student', 'Student ${i}', 'student${i}@educonnect.com', '${pass}', 'ENR260${i}', 'mca', '1')`);
        }

        // Assignments (For Sem 3 BCA)
        const tomorrow = new Date(Date.now() + 86400000).toISOString();
        const yesterday = new Date(Date.now() - 86400000).toISOString();
        
        db.run(`INSERT INTO assignments (title, course, semester, marks, due_date, description, subject, status, faculty_id) VALUES ('Advanced Data Structures', 'bca_hons', '3', 50, '${tomorrow}', 'Implement an AVL tree.', 'Data Structures & Algorithms', 'Published', 2)`);
        db.run(`INSERT INTO assignments (title, course, semester, marks, due_date, description, subject, status, faculty_id) VALUES ('React Dashboard Build', 'bca_hons', '3', 100, '${yesterday}', 'Build a dashboard.', 'Web Development Technologies', 'Published', 2)`);

        console.log("Database Seeded Successfully! Use password: password123 for all users.");
    });
}
seed();
