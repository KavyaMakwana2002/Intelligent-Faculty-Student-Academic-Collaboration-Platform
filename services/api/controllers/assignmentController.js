const db = require('../db');

exports.createAssignment = (req, res) => {
    console.log("RECEIVED BODY:", req.body);
    const { title, course, semester, subject, marks, due_date, dueDate, description, topic } = req.body;
    const faculty_id = req.user.id;
    const file_url = req.file ? '/uploads/' + req.file.filename : null;
    const finalDueDate = due_date || dueDate;

    if (!course || !semester) return res.status(400).json({ error: 'Course and Semester are required' });

    const stmt = db.prepare('INSERT INTO assignments (title, course, semester, marks, due_date, description, faculty_id, subject, file_url, topic) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)');
        stmt.run([title, course, semester, marks, finalDueDate, description, faculty_id, subject, file_url, topic || 'General'], function(err) {
        if (err) {
            console.error(err);
            return res.status(500).json({ error: 'Database error: ' + err.message });
        }
        res.status(201).json({ message: 'Assignment created', id: this.lastID });
    });
    stmt.finalize();
};

exports.getAssignments = (req, res) => {
    const { role, id, course, semester } = req.user;
    
    if (role === 'student') {
        db.all('SELECT * FROM assignments WHERE course = ? AND semester = ?', [course, semester], (err, rows) => {
            if (err) return res.status(500).json({ error: 'Database error' });
            res.json(rows);
        });
    } else if (role === 'faculty') {
        db.all('SELECT * FROM assignments WHERE faculty_id = ?', [id], (err, rows) => {
            if (err) return res.status(500).json({ error: 'Database error' });
            res.json(rows);
        });
    } else {
        db.all('SELECT * FROM assignments', [], (err, rows) => {
            res.json(rows);
        });
    }
};

exports.getAssignmentById = (req, res) => {
    const { id } = req.params;
    const { role, course, semester, id: userId } = req.user;
    
    db.get('SELECT * FROM assignments WHERE id = ?', [id], (err, row) => {
        if (err) return res.status(500).json({ error: 'Database error' });
        if (!row) return res.status(404).json({ error: 'Assignment not found' });
        
        // Security check
        if (role === 'student') {
            if (row.course !== course || String(row.semester) !== String(semester)) {
                return res.status(403).json({ error: 'Access denied: Assignment does not belong to your course or semester' });
            }
        } else if (role === 'faculty') {
            // Faculties can see it if they are the creator or if it's open
            // Strict check: row.faculty_id === userId
            // For now, allow faculty to see all
        }
        
        res.json(row);
    });
};

exports.submitAssignment = (req, res) => {
    const { id: assignment_id } = req.params;
    const file_url = req.file ? '/uploads/' + req.file.filename : req.body.file_url;
    const { role, id: student_id, course, semester } = req.user;
    
    if (role !== 'student') return res.status(403).json({ error: 'Only students can submit assignments' });
    
    // Check if assignment belongs to student
    db.get('SELECT * FROM assignments WHERE id = ?', [assignment_id], (err, row) => {
        if (err || !row) return res.status(404).json({ error: 'Assignment not found' });
        if (row.course !== course || String(row.semester) !== String(semester)) {
            return res.status(403).json({ error: 'Not authorized for this assignment' });
        }
        
        const submitted_at = new Date().toISOString();
        const stmt = db.prepare('INSERT INTO submissions (assignment_id, student_id, file_url, submitted_at) VALUES (?, ?, ?, ?)');
        stmt.run([assignment_id, student_id, file_url, submitted_at], function(err) {
            if (err) return res.status(500).json({ error: 'Already submitted or database error' });
            res.json({ message: 'Assignment submitted successfully' });
        });
    });
};

exports.getSubmission = (req, res) => {
    const { id: assignment_id } = req.params;
    const { id: student_id, role } = req.user;
    if (role !== 'student') return res.json(null);
    db.get('SELECT * FROM submissions WHERE assignment_id = ? AND student_id = ?', [assignment_id, student_id], (err, row) => {
        res.json(row || null);
    });
};

exports.getSubmissionsForAssignment = (req, res) => {
    const { id } = req.params;
    if (req.user.role !== 'faculty') return res.status(403).json({error: 'Unauthorized'});
    
    // Join with users table to get student name
    db.all(`
        SELECT s.*, u.name as student_name, u.identifier as enrollment 
        FROM submissions s 
        JOIN users u ON s.student_id = u.id 
        WHERE s.assignment_id = ?
    `, [id], (err, rows) => {
        if(err) return res.status(500).json({error: err.message});
        res.json(rows || []);
    });
};

exports.gradeSubmission = (req, res) => {
    const { submission_id } = req.params;
    const { marks } = req.body;
    if (req.user.role !== 'faculty') return res.status(403).json({error: 'Unauthorized'});
    
    db.run('UPDATE submissions SET marks_awarded = ?, status = ? WHERE id = ?', [marks, 'Graded', submission_id], function(err) {
        if(err) return res.status(500).json({error: 'DB error'});
        res.json({message: 'Graded successfully'});
    });
};
