import os

backend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\services\api"
frontend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web"

# --- BACKEND ---
db_js = """const sqlite3 = require('sqlite3').verbose();
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
            marks INTEGER NOT NULL,
            due_date TEXT NOT NULL,
            description TEXT,
            faculty_id INTEGER,
            status TEXT DEFAULT 'Pending'
        )`);
    }
});

module.exports = db;
"""

auth_middleware_js = """const jwt = require('jsonwebtoken');
const JWT_SECRET = 'hackathon-super-secret-key-2026';

module.exports = (req, res, next) => {
    const token = req.header('Authorization');
    if (!token) return res.status(401).json({ error: 'Access denied. No token provided.' });

    try {
        const decoded = jwt.verify(token.replace('Bearer ', ''), JWT_SECRET);
        req.user = decoded;
        next();
    } catch (ex) {
        res.status(400).json({ error: 'Invalid token.' });
    }
};
"""

auth_controller_js = """const db = require('../db');
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
"""

assignment_controller_js = """const db = require('../db');

exports.createAssignment = (req, res) => {
    const { title, course, semester, marks, dueDate, description } = req.body;
    const faculty_id = req.user.id;

    if (!course || !semester) return res.status(400).json({ error: 'Course and Semester are required' });

    const stmt = db.prepare('INSERT INTO assignments (title, course, semester, marks, due_date, description, faculty_id) VALUES (?, ?, ?, ?, ?, ?, ?)');
    stmt.run([title, course, semester, marks, dueDate, description, faculty_id], function(err) {
        if (err) {
            console.error(err);
            return res.status(500).json({ error: 'Database error' });
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
"""

assignment_routes_js = """const express = require('express');
const router = express.Router();
const auth = require('../middleware/auth');
const assignmentController = require('../controllers/assignmentController');

router.post('/', auth, assignmentController.createAssignment);
router.get('/', auth, assignmentController.getAssignments);

module.exports = router;
"""

index_js = """const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

// Routes
const aiChatRoutes = require('./routes/aiChat');
const authRoutes = require('./routes/authRoutes');
const assignmentRoutes = require('./routes/assignmentRoutes');

app.use('/api/ai-chat', aiChatRoutes);
app.use('/api/auth', authRoutes);
app.use('/api/assignments', assignmentRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Node.js API running on port ${PORT}`);
});
"""

# Write Backend Files
os.makedirs(os.path.join(backend_dir, "middleware"), exist_ok=True)
with open(os.path.join(backend_dir, "db.js"), "w", encoding="utf-8") as f: f.write(db_js)
with open(os.path.join(backend_dir, "middleware", "auth.js"), "w", encoding="utf-8") as f: f.write(auth_middleware_js)
with open(os.path.join(backend_dir, "controllers", "authController.js"), "w", encoding="utf-8") as f: f.write(auth_controller_js)
with open(os.path.join(backend_dir, "controllers", "assignmentController.js"), "w", encoding="utf-8") as f: f.write(assignment_controller_js)
with open(os.path.join(backend_dir, "routes", "assignmentRoutes.js"), "w", encoding="utf-8") as f: f.write(assignment_routes_js)
with open(os.path.join(backend_dir, "index.js"), "w", encoding="utf-8") as f: f.write(index_js)


# --- FRONTEND ---
auth_context_tsx = """import { createContext, useContext, useState, ReactNode, useEffect } from 'react';

type UserRole = 'student' | 'faculty' | 'admin';

interface User {
  id?: number;
  name?: string;
  email?: string;
  role: UserRole;
  course?: string;
  semester?: string;
}

interface AuthContextType {
  user: User | null;
  login: (userData: User, token: string) => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const storedUser = localStorage.getItem('user');
    if (storedUser) {
      setUser(JSON.parse(storedUser));
    }
  }, []);

  const login = (userData: User, token: string) => {
    setUser(userData);
    localStorage.setItem('user', JSON.stringify(userData));
    localStorage.setItem('token', token);
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem('user');
    localStorage.removeItem('token');
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}
"""

login_tsx = """import { useState } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { useNavigate, Link } from 'react-router-dom';
import { Book, GraduationCap, Briefcase, ShieldCheck, ArrowLeft, AlertCircle } from 'lucide-react';
import axios from 'axios';

type RoleType = 'student' | 'faculty' | 'admin' | null;

export default function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [role, setRole] = useState<RoleType>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const [identifier, setIdentifier] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    
    try {
      const payload = role === 'admin' 
        ? { role, email, password }
        : { role, identifier, password };
        
      const res = await axios.post('http://localhost:5000/api/auth/login', payload);
      
      if (res.data.token) {
        login(res.data.user, res.data.token);
        navigate('/dashboard');
      }
    } catch (err: any) {
      setError(err.response?.data?.error || 'Failed to login. Please check credentials.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-900 relative overflow-hidden">
      <div className="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=2070')] bg-cover bg-center opacity-20"></div>
      <div className="absolute inset-0 bg-gradient-to-br from-indigo-900/90 via-slate-900/95 to-purple-900/90"></div>
      
      <div className="absolute top-20 left-20 w-72 h-72 bg-indigo-500 rounded-full mix-blend-multiply filter blur-[128px] opacity-40 animate-float"></div>
      
      <div className="relative z-10 w-full max-w-md px-6 animate-fade-in-up">
        {role === null ? (
          <Link to="/" className="inline-flex items-center gap-2 text-indigo-300 hover:text-white mb-8 transition-colors font-medium">
            <ArrowLeft className="w-4 h-4" /> Back to Home
          </Link>
        ) : (
          <button onClick={() => { setRole(null); setError(null); }} className="inline-flex items-center gap-2 text-indigo-300 hover:text-white mb-8 transition-colors font-medium">
            <ArrowLeft className="w-4 h-4" /> Back to Roles
          </button>
        )}
        
        <div className="glass-dark p-10 rounded-3xl">
          <div className="flex justify-center mb-8">
            <div className="w-20 h-20 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-2xl flex items-center justify-center shadow-lg transform -rotate-6">
              <Book className="w-10 h-10 text-white" />
            </div>
          </div>
          
          <h2 className="text-3xl font-bold text-center text-white mb-2">{role === null ? "Welcome Back" : `${role.charAt(0).toUpperCase() + role.slice(1)} Login`}</h2>
          
          {error && (
            <div className="bg-red-500/20 border border-red-500/50 text-red-200 p-3 rounded-lg flex items-center gap-2 mb-6 mt-4 text-sm">
              <AlertCircle className="w-4 h-4" /> {error}
            </div>
          )}
          
          {role === null ? (
            <div className="space-y-4 mt-6">
              <button onClick={() => setRole('student')} className="group w-full flex items-center justify-between bg-white/5 p-4 rounded-xl text-white hover:bg-white/10 transition">
                <div className="flex items-center gap-4">
                  <div className="p-2.5 bg-blue-500/20 text-blue-400 rounded-lg"><GraduationCap className="w-5 h-5" /></div>
                  <span className="font-semibold text-lg">Student</span>
                </div>
              </button>
              <button onClick={() => setRole('faculty')} className="group w-full flex items-center justify-between bg-white/5 p-4 rounded-xl text-white hover:bg-white/10 transition">
                <div className="flex items-center gap-4">
                  <div className="p-2.5 bg-purple-500/20 text-purple-400 rounded-lg"><Briefcase className="w-5 h-5" /></div>
                  <span className="font-semibold text-lg">Faculty</span>
                </div>
              </button>
              <button onClick={() => setRole('admin')} className="group w-full flex items-center justify-between bg-white/5 p-4 rounded-xl text-white hover:bg-white/10 transition">
                <div className="flex items-center gap-4">
                  <div className="p-2.5 bg-emerald-500/20 text-emerald-400 rounded-lg"><ShieldCheck className="w-5 h-5" /></div>
                  <span className="font-semibold text-lg">Admin</span>
                </div>
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-5 mt-6">
              <div>
                <label className="block text-sm font-medium text-indigo-200 mb-1">
                  {role === 'student' && "Enrollment Number"}
                  {role === 'faculty' && "Faculty ID"}
                  {role === 'admin' && "Email Address"}
                </label>
                <input 
                  type={role === 'admin' ? "email" : "text"} required 
                  value={role === 'admin' ? email : identifier}
                  onChange={(e) => role === 'admin' ? setEmail(e.target.value) : setIdentifier(e.target.value)}
                  className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-indigo-200 mb-1">Password</label>
                <input type="password" required value={password} onChange={(e) => setPassword(e.target.value)} className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" />
              </div>
              <button type="submit" disabled={loading} className="w-full py-3.5 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl font-bold mt-4 transition">
                {loading ? "Logging in..." : "Login"}
              </button>
            </form>
          )}
        </div>
      </div>
    </div>
  );
}
"""

create_assignment_tsx = """import { useState } from 'react';
import { ArrowLeft, Save, AlertCircle } from 'lucide-react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

export default function CreateAssignment() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const [title, setTitle] = useState('');
  const [course, setCourse] = useState('');
  const [semester, setSemester] = useState('');
  const [marks, setMarks] = useState('');
  const [dueDate, setDueDate] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    
    try {
      const token = localStorage.getItem('token');
      await axios.post('http://localhost:5000/api/assignments', {
        title, course, semester, marks, dueDate, description
      }, {
        headers: { Authorization: `Bearer ${token}` }
      });
      navigate('/assignments');
    } catch (err: any) {
      setError(err.response?.data?.error || 'Failed to create assignment');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-3xl mx-auto space-y-6 pb-10">
      <Link to="/assignments" className="inline-flex items-center gap-2 text-slate-500 hover:text-indigo-600 transition-colors mb-4 font-medium">
        <ArrowLeft className="w-4 h-4" /> Back to Assignments
      </Link>
      
      <div className="bg-white rounded-3xl shadow-sm border border-slate-100 p-8">
        <h1 className="text-2xl font-bold text-slate-900 mb-8">Create New Assignment</h1>
        
        {error && (
            <div className="bg-red-50 text-red-500 p-4 rounded-xl flex items-center gap-2 mb-6">
              <AlertCircle className="w-5 h-5" /> {error}
            </div>
        )}
        
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="space-y-2">
            <label className="text-sm font-semibold text-slate-700">Assignment Title</label>
            <input required value={title} onChange={e=>setTitle(e.target.value)} type="text" placeholder="e.g. Build a React Dashboard" className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-all" />
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-2">
              <label className="text-sm font-semibold text-slate-700">Target Course (Program)</label>
              <select required value={course} onChange={e=>setCourse(e.target.value)} className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all bg-white">
                <option value="">Select Course</option>
                <option value="bca_hons">BCA Hons.</option>
                <option value="bca_hons_aiml">BCA Hons. AI/ML</option>
                <option value="bca_hons_cyber">BCA Hons. Cyber Security</option>
                <option value="mca">MCA</option>
              </select>
            </div>
            <div className="space-y-2">
              <label className="text-sm font-semibold text-slate-700">Target Semester</label>
              <select required value={semester} onChange={e=>setSemester(e.target.value)} className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all bg-white">
                <option value="">Select Semester</option>
                <option value="1">Semester 1</option>
                <option value="2">Semester 2</option>
                <option value="3">Semester 3</option>
                <option value="4">Semester 4</option>
                <option value="5">Semester 5</option>
                <option value="6">Semester 6</option>
                <option value="7">Semester 7</option>
                <option value="8">Semester 8</option>
              </select>
            </div>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-2">
              <label className="text-sm font-semibold text-slate-700">Total Marks</label>
              <input required value={marks} onChange={e=>setMarks(e.target.value)} type="number" placeholder="e.g. 100" className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all" />
            </div>
            <div className="space-y-2">
              <label className="text-sm font-semibold text-slate-700">Due Date</label>
              <input required value={dueDate} onChange={e=>setDueDate(e.target.value)} type="datetime-local" className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all" />
            </div>
          </div>

          <div className="space-y-2">
            <label className="text-sm font-semibold text-slate-700">Description / Instructions</label>
            <textarea required value={description} onChange={e=>setDescription(e.target.value)} rows={5} placeholder="Provide detailed instructions for the students..." className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all resize-none"></textarea>
          </div>

          <div className="pt-6 flex justify-end gap-4">
            <Link to="/assignments" className="px-6 py-3 rounded-xl font-medium text-slate-600 hover:bg-slate-100 transition-colors">Cancel</Link>
            <button type="submit" disabled={loading} className="bg-indigo-600 text-white px-8 py-3 rounded-xl font-medium hover:bg-indigo-700 transition-colors shadow-md flex items-center gap-2">
              {loading ? "Publishing..." : <><Save className="w-5 h-5" /> Publish Assignment</>}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
"""

assignments_tsx = """import { useState, useEffect } from 'react';
import { Clock, CheckCircle, AlertCircle, Plus, FileText } from 'lucide-react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import axios from 'axios';

export default function Assignments() {
  const { user } = useAuth();
  const [assignments, setAssignments] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAssignments = async () => {
      try {
        const token = localStorage.getItem('token');
        const res = await axios.get('http://localhost:5000/api/assignments', {
          headers: { Authorization: `Bearer ${token}` }
        });
        setAssignments(res.data);
      } catch (err) {
        console.error("Error fetching assignments:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchAssignments();
  }, []);

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold text-slate-900">Assignments</h1>
          {user?.role === 'student' && (
             <p className="text-slate-500 mt-1 font-medium text-sm flex items-center gap-2">
               <span className="bg-indigo-50 text-indigo-700 px-2 py-0.5 rounded uppercase text-xs font-bold">{user.course?.replace('_', ' ')}</span>
               <span className="bg-purple-50 text-purple-700 px-2 py-0.5 rounded uppercase text-xs font-bold">Sem {user.semester}</span>
             </p>
          )}
        </div>
        
        {user?.role === 'faculty' && (
          <Link to="/assignments/create" className="bg-indigo-600 text-white px-5 py-2.5 rounded-xl font-medium hover:bg-indigo-700 transition shadow-md flex items-center gap-2">
            <Plus className="w-5 h-5" /> Create Assignment
          </Link>
        )}
      </div>

      {loading ? (
         <div className="flex justify-center p-10"><span className="w-8 h-8 border-4 border-indigo-200 border-t-indigo-600 rounded-full animate-spin"></span></div>
      ) : assignments.length === 0 ? (
         <div className="bg-slate-50 rounded-3xl p-10 text-center border border-slate-100 flex flex-col items-center">
            <FileText className="w-16 h-16 text-slate-300 mb-4" />
            <h3 className="text-xl font-bold text-slate-700 mb-2">No assignments found</h3>
            <p className="text-slate-500">There are no assignments available for your course and semester yet.</p>
         </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {assignments.map(item => (
            <Link to={`/assignments/${item.id}`} key={item.id} className="bg-white rounded-3xl p-6 shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 group relative overflow-hidden flex flex-col h-full">
              <div className={`absolute top-0 right-0 w-2 h-full ${item.status === 'Pending' ? 'bg-amber-400' : 'bg-emerald-500'}`}></div>
              
              <div className="flex justify-between items-start mb-4">
                 <span className="bg-slate-100 text-slate-600 text-xs px-2.5 py-1 rounded-md font-bold uppercase tracking-wider">{item.course.replace('_', ' ')} S{item.semester}</span>
                 {item.status === 'Pending' 
                   ? <span className="flex items-center gap-1 text-xs font-bold text-amber-600 bg-amber-50 px-2 py-1 rounded-md"><AlertCircle className="w-3 h-3" /> Pending</span>
                   : <span className="flex items-center gap-1 text-xs font-bold text-emerald-600 bg-emerald-50 px-2 py-1 rounded-md"><CheckCircle className="w-3 h-3" /> Submitted</span>
                 }
              </div>
              
              <h3 className="text-lg font-bold text-slate-900 mb-2 group-hover:text-indigo-600 transition-colors line-clamp-2">{item.title}</h3>
              
              <div className="mt-auto pt-6 flex items-center justify-between text-sm text-slate-500">
                 <div className="flex items-center gap-1.5 font-medium"><Clock className="w-4 h-4" /> {new Date(item.due_date).toLocaleDateString()}</div>
                 <div className="font-bold text-slate-700">{item.marks} pts</div>
              </div>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}
"""

with open(os.path.join(frontend_dir, "src/contexts/AuthContext.tsx"), "w", encoding="utf-8") as f: f.write(auth_context_tsx)
with open(os.path.join(frontend_dir, "src/pages/auth/Login.tsx"), "w", encoding="utf-8") as f: f.write(login_tsx)
with open(os.path.join(frontend_dir, "src/pages/CreateAssignment.tsx"), "w", encoding="utf-8") as f: f.write(create_assignment_tsx)
with open(os.path.join(frontend_dir, "src/pages/Assignments.tsx"), "w", encoding="utf-8") as f: f.write(assignments_tsx)

print("Assignments filtering logic created!")
