import os
import sqlite3
import re

backend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\services\api"
frontend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web"
db_path = os.path.join(backend_dir, 'database.sqlite')

# --- 1. ALTER DATABASE TO ADD SUBJECT ---
try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # Check if subject exists
    c.execute("PRAGMA table_info(assignments)")
    columns = [col[1] for col in c.fetchall()]
    if 'subject' not in columns:
        c.execute("ALTER TABLE assignments ADD COLUMN subject TEXT")
        conn.commit()
    conn.close()
    print("Database updated: Added subject column.")
except Exception as e:
    print(f"DB Error: {e}")

# --- 2. UPDATE BACKEND CONTROLLER ---
assignment_controller_path = os.path.join(backend_dir, "controllers", "assignmentController.js")
with open(assignment_controller_path, "r", encoding="utf-8") as f:
    ac_content = f.read()

if "subject" not in ac_content:
    ac_content = ac_content.replace(
        "const { title, course, semester, marks, dueDate, description } = req.body;",
        "const { title, course, semester, subject, marks, dueDate, description } = req.body;"
    )
    ac_content = ac_content.replace(
        "INSERT INTO assignments (title, course, semester, marks, due_date, description, faculty_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
        "INSERT INTO assignments (title, course, semester, subject, marks, due_date, description, faculty_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    )
    ac_content = ac_content.replace(
        "stmt.run([title, course, semester, marks, dueDate, description, faculty_id]",
        "stmt.run([title, course, semester, subject, marks, dueDate, description, faculty_id]"
    )

if "getAssignmentById" not in ac_content:
    ac_content += """
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
"""
with open(assignment_controller_path, "w", encoding="utf-8") as f: f.write(ac_content)

# --- 3. UPDATE ROUTES ---
routes_path = os.path.join(backend_dir, "routes", "assignmentRoutes.js")
with open(routes_path, "r", encoding="utf-8") as f:
    routes_content = f.read()

if "getAssignmentById" not in routes_content:
    routes_content = routes_content.replace(
        "module.exports = router;",
        "router.get('/:id', auth, assignmentController.getAssignmentById);\n\nmodule.exports = router;"
    )
with open(routes_path, "w", encoding="utf-8") as f: f.write(routes_content)


# --- 4. UPDATE CREATE ASSIGNMENT UI ---
create_assignment_path = os.path.join(frontend_dir, "src/pages/CreateAssignment.tsx")
with open(create_assignment_path, "r", encoding="utf-8") as f:
    ca_content = f.read()

if "const [subject, setSubject] = useState" not in ca_content:
    ca_content = ca_content.replace(
        "const [semester, setSemester] = useState('');",
        "const [semester, setSemester] = useState('');\n  const [subject, setSubject] = useState('');"
    )
    ca_content = ca_content.replace(
        "title, course, semester, marks, dueDate, description",
        "title, course, semester, subject, marks, dueDate, description"
    )
    
    subject_ui = """            <div className="space-y-2 md:col-span-2">
              <label className="text-sm font-semibold text-slate-700">Subject</label>
              <select required value={subject} onChange={e=>setSubject(e.target.value)} className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all bg-white">
                <option value="">Select Subject</option>
                <option value="Data Structures & Algorithms">Data Structures & Algorithms</option>
                <option value="Web Development Technologies">Web Development Technologies</option>
                <option value="Database Management Systems">Database Management Systems</option>
                <option value="Operating Systems">Operating Systems</option>
                <option value="Artificial Intelligence">Artificial Intelligence</option>
                <option value="Cyber Security & Cryptography">Cyber Security & Cryptography</option>
                <option value="Software Engineering">Software Engineering</option>
                <option value="Computer Networks">Computer Networks</option>
              </select>
            </div>"""
    
    ca_content = ca_content.replace(
        """<div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-2">
              <label className="text-sm font-semibold text-slate-700">Target Course (Program)</label>""",
        """<div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-2">
              <label className="text-sm font-semibold text-slate-700">Target Course (Program)</label>"""
    )
    # Add subject UI right after semester div
    ca_content = ca_content.replace(
        """              </select>
            </div>
          </div>""",
        """              </select>
            </div>\n""" + subject_ui + "\n          </div>"
    )
with open(create_assignment_path, "w", encoding="utf-8") as f: f.write(ca_content)


# --- 5. UPDATE ASSIGNMENTS UI ---
assignments_path = os.path.join(frontend_dir, "src/pages/Assignments.tsx")
with open(assignments_path, "r", encoding="utf-8") as f:
    a_content = f.read()

if "item.subject" not in a_content:
    a_content = a_content.replace(
        """<h3 className="text-lg font-bold text-slate-900 mb-2 group-hover:text-indigo-600 transition-colors line-clamp-2">{item.title}</h3>""",
        """<h3 className="text-lg font-bold text-slate-900 mb-1 group-hover:text-indigo-600 transition-colors line-clamp-2">{item.title}</h3>
              <p className="text-sm text-slate-500 mb-3 font-medium">{item.subject || 'General Assignment'}</p>"""
    )
with open(assignments_path, "w", encoding="utf-8") as f: f.write(a_content)

print("Applied strict requirements updates!")
