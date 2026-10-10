import os

backend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\services\api"
frontend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web"

# --- 1. ADD SUBMISSIONS TABLE TO DB ---
db_js_path = os.path.join(backend_dir, "db.js")
with open(db_js_path, "r", encoding="utf-8") as f:
    db_content = f.read()

if "submissions" not in db_content:
    db_content = db_content.replace(
        """        db.run(`CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            course TEXT NOT NULL,
            semester TEXT NOT NULL,
            marks INTEGER NOT NULL,
            due_date TEXT NOT NULL,
            description TEXT,
            faculty_id INTEGER,
            status TEXT DEFAULT 'Pending',
            subject TEXT
        )`);""",
        """        db.run(`CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            course TEXT NOT NULL,
            semester TEXT NOT NULL,
            marks INTEGER NOT NULL,
            due_date TEXT NOT NULL,
            description TEXT,
            faculty_id INTEGER,
            status TEXT DEFAULT 'Pending',
            subject TEXT
        )`);

        db.run(`CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assignment_id INTEGER NOT NULL,
            student_id INTEGER NOT NULL,
            file_url TEXT,
            submitted_at TEXT NOT NULL,
            marks_awarded INTEGER,
            status TEXT DEFAULT 'Submitted',
            UNIQUE(assignment_id, student_id)
        )`);"""
    )
    with open(db_js_path, "w", encoding="utf-8") as f: f.write(db_content)


# --- 2. UPDATE ASSIGNMENT CONTROLLER ---
assignment_controller_path = os.path.join(backend_dir, "controllers", "assignmentController.js")
with open(assignment_controller_path, "r", encoding="utf-8") as f:
    ac_content = f.read()

if "submitAssignment" not in ac_content:
    ac_content += """
exports.submitAssignment = (req, res) => {
    const { id: assignment_id } = req.params;
    const { file_url } = req.body;
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
"""
    with open(assignment_controller_path, "w", encoding="utf-8") as f: f.write(ac_content)


# --- 3. UPDATE ROUTES ---
routes_path = os.path.join(backend_dir, "routes", "assignmentRoutes.js")
with open(routes_path, "r", encoding="utf-8") as f:
    routes_content = f.read()

if "submitAssignment" not in routes_content:
    routes_content = routes_content.replace(
        "module.exports = router;",
        "router.post('/:id/submit', auth, assignmentController.submitAssignment);\nrouter.get('/:id/submission', auth, assignmentController.getSubmission);\n\nmodule.exports = router;"
    )
    with open(routes_path, "w", encoding="utf-8") as f: f.write(routes_content)

# --- 4. ASSIGNMENT DETAILS UI ---
assignment_details_tsx = """import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { ArrowLeft, Clock, FileText, CheckCircle, UploadCloud, AlertCircle } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import axios from 'axios';

export default function AssignmentDetails() {
  const { id } = useParams();
  const { user } = useAuth();
  
  const [assignment, setAssignment] = useState<any>(null);
  const [submission, setSubmission] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchData();
  }, [id]);

  const fetchData = async () => {
    try {
      const token = localStorage.getItem('token');
      const res = await axios.get(`http://localhost:5000/api/assignments/${id}`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setAssignment(res.data);
      
      if (user?.role === 'student') {
        const subRes = await axios.get(`http://localhost:5000/api/assignments/${id}/submission`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        setSubmission(subRes.data);
      }
    } catch (err: any) {
      setError(err.response?.data?.error || 'Failed to load assignment');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async () => {
    setSubmitting(true);
    try {
      const token = localStorage.getItem('token');
      await axios.post(`http://localhost:5000/api/assignments/${id}/submit`, {
        file_url: 'https://example.com/submission.pdf'
      }, {
        headers: { Authorization: `Bearer ${token}` }
      });
      fetchData();
    } catch (err: any) {
      setError(err.response?.data?.error || 'Failed to submit');
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) return <div className="flex justify-center p-20"><span className="w-10 h-10 border-4 border-indigo-200 border-t-indigo-600 rounded-full animate-spin"></span></div>;

  if (error) return (
    <div className="max-w-3xl mx-auto space-y-6 pb-10">
      <Link to="/assignments" className="inline-flex items-center gap-2 text-slate-500 hover:text-indigo-600 mb-4 font-medium"><ArrowLeft className="w-4 h-4" /> Back to Assignments</Link>
      <div className="bg-red-50 text-red-600 p-6 rounded-3xl border border-red-100 flex items-center gap-4 shadow-sm">
        <AlertCircle className="w-8 h-8" />
        <div><h3 className="font-bold text-lg">Access Denied</h3><p>{error}</p></div>
      </div>
    </div>
  );

  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-10 animate-fade-in-up">
      <Link to="/assignments" className="inline-flex items-center gap-2 text-slate-500 hover:text-indigo-600 mb-4 font-medium transition">
        <ArrowLeft className="w-4 h-4" /> Back to Assignments
      </Link>
      
      <div className="bg-white rounded-3xl shadow-sm border border-slate-100 overflow-hidden">
         <div className="p-8 border-b border-slate-100 bg-slate-50/50">
            <div className="flex justify-between items-start gap-4 mb-4">
               <div>
                 <span className="bg-indigo-100 text-indigo-700 text-xs px-2.5 py-1 rounded-md font-bold uppercase tracking-wider mb-3 inline-block">
                   {assignment.course.replace('_', ' ')} Sem {assignment.semester} • {assignment.subject || 'General'}
                 </span>
                 <h1 className="text-3xl font-extrabold text-slate-900">{assignment.title}</h1>
               </div>
               <div className="text-right">
                  <div className="text-2xl font-black text-indigo-600">{assignment.marks} <span className="text-sm font-medium text-slate-500">pts</span></div>
               </div>
            </div>
            
            <div className="flex items-center gap-6 text-sm text-slate-600 font-medium">
               <div className="flex items-center gap-2 text-amber-600 bg-amber-50 px-3 py-1.5 rounded-lg border border-amber-100">
                  <Clock className="w-4 h-4" /> Due: {new Date(assignment.due_date).toLocaleString()}
               </div>
               <div className="flex items-center gap-2">
                  <FileText className="w-4 h-4" /> Faculty ID: {assignment.faculty_id}
               </div>
            </div>
         </div>
         
         <div className="p-8 space-y-8">
            <div>
               <h3 className="text-lg font-bold text-slate-900 mb-3 border-b border-slate-100 pb-2">Instructions</h3>
               <div className="prose prose-slate max-w-none text-slate-600 whitespace-pre-wrap">
                  {assignment.description}
               </div>
            </div>
         </div>
      </div>
      
      {user?.role === 'student' && (
        <div className="bg-white rounded-3xl shadow-sm border border-slate-100 p-8">
           <h3 className="text-lg font-bold text-slate-900 mb-6 border-b border-slate-100 pb-2">Your Work</h3>
           
           {submission ? (
             <div className="bg-emerald-50 border border-emerald-100 rounded-2xl p-6 text-center space-y-3">
                <div className="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto mb-2">
                   <CheckCircle className="w-8 h-8" />
                </div>
                <h4 className="font-bold text-emerald-800 text-lg">Assignment Submitted</h4>
                <p className="text-emerald-600 text-sm font-medium">Submitted on {new Date(submission.submitted_at).toLocaleString()}</p>
                <button disabled className="mt-4 bg-emerald-600 text-white px-6 py-2.5 rounded-xl font-medium shadow-md opacity-80 cursor-not-allowed">
                   View Submission
                </button>
             </div>
           ) : (
             <div className="border-2 border-dashed border-slate-200 rounded-2xl p-10 text-center hover:bg-slate-50 transition-colors">
                <UploadCloud className="w-12 h-12 text-slate-400 mx-auto mb-4" />
                <h4 className="font-bold text-slate-700 mb-1">Upload your submission</h4>
                <p className="text-slate-500 text-sm mb-6 max-w-sm mx-auto">Click below to submit your assignment. Note: Due to hackathon constraints, this will simulate a file upload.</p>
                <button 
                  onClick={handleSubmit} 
                  disabled={submitting}
                  className="bg-indigo-600 hover:bg-indigo-700 text-white px-8 py-3 rounded-xl font-bold shadow-md transition-all flex items-center gap-2 mx-auto"
                >
                  {submitting ? "Submitting..." : "Submit Assignment"}
                </button>
             </div>
           )}
        </div>
      )}
    </div>
  );
}
"""

with open(os.path.join(frontend_dir, "src/pages/AssignmentDetails.tsx"), "w", encoding="utf-8") as f: f.write(assignment_details_tsx)

print("Updated backend submissions table and built AssignmentDetails UI!")
