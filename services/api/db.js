const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const dbPath = path.join(__dirname, 'database.sqlite');
const db = new sqlite3.Database(dbPath, (err) => {
    if (err) {
        console.error('Error connecting to SQLite DB:', err.message);
    } else {
        console.log('Connected to SQLite database.');
        
        db.run(`CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            identifier TEXT UNIQUE,
            course TEXT,
            semester TEXT,
            position TEXT,
            password TEXT NOT NULL
        )`);
        
        db.run(`CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            course TEXT NOT NULL,
            semester TEXT NOT NULL,
            subject TEXT,
            marks INTEGER NOT NULL,
            due_date TEXT NOT NULL,
            description TEXT,
            topic TEXT DEFAULT 'General',
            faculty_id INTEGER,
            file_url TEXT,
            status TEXT DEFAULT 'Pending'
        )`);
        db.run(`CREATE TABLE IF NOT EXISTS materials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            course TEXT NOT NULL,
            semester TEXT NOT NULL,
            description TEXT,
            file_url TEXT,
            faculty_id INTEGER,
            uploaded_at TEXT
        )`);
    }
});

module.exports = db;
