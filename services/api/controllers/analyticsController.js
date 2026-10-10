const db = require('../db');

exports.getDashboardStats = (req, res) => {
    const { role, course, semester, id } = req.user;
    
    if (role === 'student') {
        db.all('SELECT * FROM assignments WHERE course = ? AND semester = ?', [course, semester], (err, assignments) => {
            db.all('SELECT * FROM submissions WHERE student_id = ?', [id], (err, submissions) => {
                db.get('SELECT COUNT(*) as materials FROM materials WHERE course = ? AND semester = ?', [course, semester], (err, row3) => {
                    
                    const total_assignments = assignments ? assignments.length : 0;
                    const total_submitted = submissions ? submissions.length : 0;
                    
                    let overdue_count = 0;
                    let graded_count = 0;
                    let total_marks_obtained = 0;
                    let total_marks_possible = 0;

                    if (assignments) {
                        assignments.forEach(a => {
                            const sub = submissions?.find(s => s.assignment_id === a.id);
                            if (!sub && new Date(a.due_date) < new Date()) {
                                overdue_count++;
                            }
                            if (sub && sub.status === 'Graded') {
                                graded_count++;
                                total_marks_obtained += (sub.marks_awarded || 0);
                                total_marks_possible += (a.marks || 0);
                            }
                        });
                    }

                    // Risk Calculation
                    let risk_level = 'Low';
                    let risk_reason = 'Great progress on all tasks.';
                    const completion_rate = total_assignments > 0 ? (total_submitted / total_assignments) * 100 : 0;
                    const grade_percentage = total_marks_possible > 0 ? (total_marks_obtained / total_marks_possible) * 100 : 0;

                    if (total_assignments < 2) {
                        risk_level = 'Insufficient Data';
                        risk_reason = 'Not enough assignments published to determine risk.';
                    } else if (completion_rate < 50 || overdue_count > 2) {
                        risk_level = 'High';
                        risk_reason = `High risk due to ${overdue_count} overdue assignments and ${completion_rate.toFixed(0)}% completion rate.`;
                    } else if (completion_rate < 80 || (graded_count > 0 && grade_percentage < 50)) {
                        risk_level = 'Medium';
                        risk_reason = `Medium risk. Completion is at ${completion_rate.toFixed(0)}%. ${graded_count > 0 ? `Current grade average is ${grade_percentage.toFixed(0)}%.` : ''}`;
                    } else {
                        risk_level = 'Low';
                        risk_reason = `Low risk. You have submitted ${total_submitted} out of ${total_assignments} assignments with ${overdue_count} overdue.`;
                    }

                    res.json({
                        assignments_total: total_assignments,
                        assignments_submitted: total_submitted,
                        assignments_pending: total_assignments - total_submitted,
                        materials_total: row3?.materials || 0,
                        overdue_count,
                        completion_rate,
                        grade_percentage,
                        risk_level,
                        risk_reason,
                        graded_count
                    });
                });
            });
        });
    } else if (role === 'faculty') {
        db.get('SELECT COUNT(*) as total FROM assignments WHERE faculty_id = ?', [id], (err, row1) => {
            db.get('SELECT COUNT(*) as materials FROM materials WHERE faculty_id = ?', [id], (err, row2) => {
                 res.json({
                     assignments_created: row1?.total || 0,
                     materials_uploaded: row2?.materials || 0
                 });
            });
        });
    } else {
        res.json({});
    }
};


exports.getFacultyInsights = (req, res) => {
    try {
        db.all('SELECT users.name, users.identifier, COUNT(submissions.id) as late_count FROM users LEFT JOIN submissions ON users.id = submissions.student_id AND submissions.status = "late" WHERE users.role = "student" GROUP BY users.id HAVING late_count >= 1 ORDER BY late_count DESC', [], (err, students) => {
            if (err) return res.status(500).json({ error: 'Database error' });
            
            const insights = students.map(s => {
                let action = "Monitor progress";
                if (s.late_count >= 3) action = "Schedule 1-on-1 tutoring support immediately.";
                else if (s.late_count === 2) action = "Send a warning email regarding deadlines.";
                
                return {
                    studentName: s.name,
                    identifier: s.identifier,
                    lateCount: s.late_count,
                    message: `${s.name} (${s.identifier}) has ${s.late_count} late assignments.`,
                    action: action
                };
            });
            
            // Add a mock topic-wise insight for the demo
            insights.push({
                studentName: "Batch 2026",
                identifier: "Group",
                lateCount: 0,
                message: "Average performance in 'Dynamic Programming & Graph Theory' dropped to 52%.",
                action: "Recommend targeted micro-modules for the entire class."
            });
            
            res.json(insights);
        });
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
};

exports.getStudentRecommendations = (req, res) => {
    try {
        const studentId = req.user.id;
        db.get('SELECT COUNT(*) as late_count FROM submissions WHERE student_id = ? AND status = "late"', [studentId], (err, row) => {
            if (err) return res.status(500).json({ error: 'Database error' });
            
            let recommendations = [];
            
            // Generate dynamic recommendations based on performance
            if (row && row.late_count >= 2) {
                recommendations.push({
                    type: 'alert',
                    title: 'Submission Delays Detected',
                    message: `You have ${row.late_count} late assignments. Please reach out to your faculty for a 1-on-1 mentoring session.`
                });
            }
            
            // Topic-wise mock recommendations based on the Hackathon Problem Statement
            recommendations.push({
                type: 'learning',
                title: 'Targeted Micro-Module: Memoization',
                message: 'Based on your recent assignments in Algorithm Complexity, we recommend reviewing Dynamic Programming & Memoization concepts.'
            });
            
            res.json(recommendations);
        });
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
};
