const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcryptjs');
const db = new sqlite3.Database('./database.sqlite');

async function addKrisha() {
    const salt = await bcrypt.genSalt(10);
    const pass = await bcrypt.hash("krisha123", salt);

    db.serialize(() => {
        // As a student
        db.run(`INSERT INTO users (role, name, email, password, identifier, course, semester) VALUES ('student', 'Krisha', 'krisha@educonnect.com', '${pass}', 'krisha', 'bca_hons', '3')`);
        
        // As an admin just in case she needs admin access, but with different email
        db.run(`INSERT INTO users (role, name, email, password, position) VALUES ('admin', 'Krisha Admin', 'admin.krisha@educonnect.com', '${pass}', 'Dean')`);

        console.log("Krisha added back!");
    });
}
addKrisha();
