const db = require('../db');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

const JWT_SECRET = 'hackathon-super-secret-key-2026';

exports.register = async (req, res) => {
    try {
        const { role, name, email, phone, identifier, course, semester, position, password } = req.body;
        
        if (!role || !name || !email || !password) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        const hashedPassword = await bcrypt.hash(password, 10);
        
        db.get('SELECT * FROM users WHERE email = ? OR identifier = ?', [email, identifier || null], (err, row) => {
            if (err) return res.status(500).json({ error: 'Database error' });
            if (row) return res.status(400).json({ error: 'User with this email or identifier already exists' });
            
            const stmt = db.prepare('INSERT INTO users (role, name, email, phone, identifier, course, semester, position, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)');
            stmt.run([role, name, email, phone, identifier, course, semester, position, hashedPassword], function(err) {
                if (err) return res.status(500).json({ error: 'Failed to register user' });
                res.status(201).json({ message: 'User registered successfully', userId: this.lastID });
            });
            stmt.finalize();
        });
    } catch (err) {
        console.error("Register Error:", err);
        res.status(500).json({ error: 'Server error' });
    }
};

exports.login = (req, res) => {
    try {
        const { role, identifier, email, password } = req.body;
        
        let query, param;
        if (role === 'admin') {
            query = 'SELECT * FROM users WHERE email = ? AND role = ?';
            param = email;
        } else {
            query = 'SELECT * FROM users WHERE identifier = ? AND role = ?';
            param = identifier;
        }

        db.get(query, [param, role], async (err, user) => {
            if (err) return res.status(500).json({ error: 'Database error' });
            if (!user) return res.status(401).json({ error: 'Invalid credentials or user not found' });
            
            const valid = await bcrypt.compare(password, user.password);
            if (!valid) return res.status(401).json({ error: 'Invalid password' });
            
            const token = jwt.sign({ id: user.id, role: user.role, name: user.name, course: user.course, semester: user.semester }, JWT_SECRET, { expiresIn: '1d' });
            res.json({ message: 'Login successful', token, user: { id: user.id, name: user.name, role: user.role, email: user.email, course: user.course, semester: user.semester } });
        });
    } catch (err) {
        console.error("Login Error:", err);
        res.status(500).json({ error: 'Server error' });
    }
};
