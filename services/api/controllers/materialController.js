const db = require('../db');

exports.getMaterials = (req, res) => {
    const { role, course, semester, id } = req.user;
    if (role === 'student') {
        db.all('SELECT * FROM materials WHERE course = ? AND semester = ? ORDER BY id DESC', [course, semester], (err, rows) => {
            res.json(rows || []);
        });
    } else if (role === 'faculty') {
        db.all('SELECT * FROM materials WHERE faculty_id = ? ORDER BY id DESC', [id], (err, rows) => {
            res.json(rows || []);
        });
    } else {
        res.json([]);
    }
};

exports.uploadMaterial = (req, res) => {
    const { title, course, semester, description } = req.body;
    const file_url = req.file ? '/uploads/' + req.file.filename : null;
    const faculty_id = req.user.id;
    if (req.user.role !== 'faculty') return res.status(403).json({error: 'Only faculty'});
    
    const uploaded_at = new Date().toISOString();
    const stmt = db.prepare('INSERT INTO materials (title, course, semester, description, file_url, faculty_id, uploaded_at) VALUES (?, ?, ?, ?, ?, ?, ?)');
    stmt.run([title, course, semester, description, file_url, faculty_id, uploaded_at], function(err) {
        if(err) return res.status(500).json({error: 'DB error'});
        res.json({message: 'Uploaded', id: this.lastID});
    });
};
