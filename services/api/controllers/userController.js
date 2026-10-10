const db = require('../db');

exports.getAllUsers = (req, res) => {
    if (req.user.role !== 'admin') return res.status(403).json({error: 'Admin only'});
    db.all('SELECT id, name, email, role, course, semester, identifier FROM users ORDER BY id DESC', [], (err, rows) => {
        if(err) return res.status(500).json({error: 'DB Error'});
        res.json(rows || []);
    });
};
