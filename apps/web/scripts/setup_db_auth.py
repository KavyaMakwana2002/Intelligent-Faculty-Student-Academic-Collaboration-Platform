import os
import json

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
        
        // Create users table
        db.run(`CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            identifier TEXT UNIQUE,
            course TEXT,
            position TEXT,
            password TEXT NOT NULL
        )`, (err) => {
            if (err) console.error("Error creating table:", err.message);
        });
    }
});

module.exports = db;
"""

auth_controller_js = """const db = require('../db');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

const JWT_SECRET = 'hackathon-super-secret-key-2026'; // Dummy secret for demo

exports.register = async (req, res) => {
    try {
        const { role, name, email, phone, identifier, course, position, password } = req.body;
        
        if (!role || !name || !email || !password) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        const hashedPassword = await bcrypt.hash(password, 10);
        
        // Check if user exists
        db.get('SELECT * FROM users WHERE email = ? OR identifier = ?', [email, identifier || null], (err, row) => {
            if (err) return res.status(500).json({ error: 'Database error' });
            if (row) return res.status(400).json({ error: 'User with this email or identifier already exists' });
            
            const stmt = db.prepare('INSERT INTO users (role, name, email, phone, identifier, course, position, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?)');
            stmt.run([role, name, email, phone, identifier, course, position, hashedPassword], function(err) {
                if (err) return res.status(500).json({ error: 'Failed to register user' });
                res.status(201).json({ message: 'User registered successfully', userId: this.lastID });
            });
            stmt.finalize();
        });
    } catch (err) {
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
            
            const token = jwt.sign({ id: user.id, role: user.role, name: user.name }, JWT_SECRET, { expiresIn: '1d' });
            res.json({ message: 'Login successful', token, user: { name: user.name, role: user.role, email: user.email } });
        });
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
};
"""

auth_routes_js = """const express = require('express');
const router = express.Router();
const authController = require('../controllers/authController');

router.post('/register', authController.register);
router.post('/login', authController.login);

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

app.use('/api/ai-chat', aiChatRoutes);
app.use('/api/auth', authRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Node.js API running on port ${PORT}`);
});
"""

# Write Backend Files
os.makedirs(os.path.join(backend_dir, "routes"), exist_ok=True)
os.makedirs(os.path.join(backend_dir, "controllers"), exist_ok=True)

with open(os.path.join(backend_dir, "db.js"), "w", encoding="utf-8") as f: f.write(db_js)
with open(os.path.join(backend_dir, "controllers", "authController.js"), "w", encoding="utf-8") as f: f.write(auth_controller_js)
with open(os.path.join(backend_dir, "routes", "authRoutes.js"), "w", encoding="utf-8") as f: f.write(auth_routes_js)
with open(os.path.join(backend_dir, "index.js"), "w", encoding="utf-8") as f: f.write(index_js)

# --- FRONTEND ---
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

  // Form states
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
        localStorage.setItem('token', res.data.token);
        // Inform context (in real app we'd decode token or use user data)
        login(role!);
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
      <div className="absolute bottom-20 right-20 w-72 h-72 bg-purple-500 rounded-full mix-blend-multiply filter blur-[128px] opacity-40 animate-float-delayed"></div>

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
            <div className="w-20 h-20 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-2xl flex items-center justify-center shadow-lg shadow-indigo-500/30 transform -rotate-6 hover:rotate-0 transition-transform duration-300">
              <Book className="w-10 h-10 text-white" />
            </div>
          </div>
          
          <h2 className="text-3xl font-bold text-center text-white mb-2 tracking-tight">
            {role === null ? "Welcome Back" : `${role.charAt(0).toUpperCase() + role.slice(1)} Login`}
          </h2>
          <p className="text-center text-indigo-200/80 mb-6 font-medium">
            {role === null ? "Select your role to access the portal" : "Enter your credentials below"}
          </p>
          
          {error && (
            <div className="bg-red-500/20 border border-red-500/50 text-red-200 p-3 rounded-lg flex items-center gap-2 mb-6 text-sm">
              <AlertCircle className="w-4 h-4" /> {error}
            </div>
          )}
          
          {role === null ? (
            <div className="space-y-4">
              <button onClick={() => setRole('student')} className="group w-full flex items-center justify-between bg-white/5 hover:bg-white/10 border border-white/10 hover:border-indigo-400/50 p-4 rounded-xl text-white transition-all duration-300 hover:shadow-lg hover:shadow-indigo-500/20">
                <div className="flex items-center gap-4">
                  <div className="p-2.5 bg-blue-500/20 text-blue-400 rounded-lg group-hover:bg-blue-500 group-hover:text-white transition-colors">
                    <GraduationCap className="w-5 h-5" />
                  </div>
                  <span className="font-semibold text-lg">Student</span>
                </div>
              </button>
              
              <button onClick={() => setRole('faculty')} className="group w-full flex items-center justify-between bg-white/5 hover:bg-white/10 border border-white/10 hover:border-purple-400/50 p-4 rounded-xl text-white transition-all duration-300 hover:shadow-lg hover:shadow-purple-500/20">
                <div className="flex items-center gap-4">
                  <div className="p-2.5 bg-purple-500/20 text-purple-400 rounded-lg group-hover:bg-purple-500 group-hover:text-white transition-colors">
                    <Briefcase className="w-5 h-5" />
                  </div>
                  <span className="font-semibold text-lg">Faculty</span>
                </div>
              </button>

              <button onClick={() => setRole('admin')} className="group w-full flex items-center justify-between bg-white/5 hover:bg-white/10 border border-white/10 hover:border-emerald-400/50 p-4 rounded-xl text-white transition-all duration-300 hover:shadow-lg hover:shadow-emerald-500/20">
                <div className="flex items-center gap-4">
                  <div className="p-2.5 bg-emerald-500/20 text-emerald-400 rounded-lg group-hover:bg-emerald-500 group-hover:text-white transition-colors">
                    <ShieldCheck className="w-5 h-5" />
                  </div>
                  <span className="font-semibold text-lg">Admin</span>
                </div>
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-5 animate-fade-in-up" style={{ animationDuration: '0.4s' }}>
              <div>
                <label className="block text-sm font-medium text-indigo-200 mb-1">
                  {role === 'student' && "Enrollment Number"}
                  {role === 'faculty' && "Faculty ID"}
                  {role === 'admin' && "Email Address"}
                </label>
                <input 
                  type={role === 'admin' ? "email" : "text"} 
                  required 
                  value={role === 'admin' ? email : identifier}
                  onChange={(e) => role === 'admin' ? setEmail(e.target.value) : setIdentifier(e.target.value)}
                  className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white placeholder-white/40 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
                  placeholder={role === 'student' ? "e.g. 210001001" : role === 'faculty' ? "e.g. FAC-1042" : "admin@uni.edu"}
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-indigo-200 mb-1">Password</label>
                <input 
                  type="password" 
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white placeholder-white/40 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
                  placeholder="••••••••"
                />
              </div>
              
              <div className="flex justify-between items-center text-sm pt-2">
                <label className="flex items-center gap-2 text-indigo-200 cursor-pointer">
                  <input type="checkbox" className="rounded bg-white/10 border-white/20 text-indigo-600 focus:ring-indigo-500" />
                  Remember me
                </label>
                <a href="#" className="text-indigo-400 hover:text-indigo-300">Forgot password?</a>
              </div>

              <button type="submit" disabled={loading} className="w-full py-3.5 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white rounded-xl font-bold shadow-lg shadow-indigo-500/30 transition-all duration-300 mt-4 flex justify-center items-center">
                {loading ? (
                   <span className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin"></span>
                ) : (
                  "Login"
                )}
              </button>
            </form>
          )}
          
          <div className="mt-8 pt-6 border-t border-white/10 text-center">
            <p className="text-sm text-indigo-200/80">Don't have an account? <Link to="/register" className="text-white font-bold hover:underline">Sign up</Link></p>
          </div>
        </div>
      </div>
    </div>
  );
}
"""

register_tsx = """import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Book, GraduationCap, Briefcase, ShieldCheck, ArrowLeft, AlertCircle, CheckCircle } from 'lucide-react';
import axios from 'axios';

type RoleType = 'student' | 'faculty' | 'admin' | null;

export default function Register() {
  const navigate = useNavigate();
  const [role, setRole] = useState<RoleType>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<boolean>(false);

  // Form states
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [identifier, setIdentifier] = useState(''); // Enrollment, Faculty ID
  const [phone, setPhone] = useState('');
  const [course, setCourse] = useState('');
  const [position, setPosition] = useState(''); // HOD/DEAN
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      setError("Passwords do not match!");
      return;
    }
    
    setLoading(true);
    setError(null);
    
    try {
      const payload = {
        role, name, email, phone, password,
        identifier: role !== 'admin' ? identifier : undefined,
        course: role === 'student' ? course : undefined,
        position: role === 'admin' ? position : undefined
      };
      
      await axios.post('http://localhost:5000/api/auth/register', payload);
      setSuccess(true);
      setTimeout(() => navigate('/login'), 2000);
    } catch (err: any) {
      setError(err.response?.data?.error || 'Registration failed. Try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-900 relative overflow-hidden py-10">
      <div className="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=2070')] bg-cover bg-center opacity-20"></div>
      <div className="absolute inset-0 bg-gradient-to-br from-indigo-900/90 via-slate-900/95 to-purple-900/90"></div>
      
      <div className="absolute top-20 left-20 w-72 h-72 bg-indigo-500 rounded-full mix-blend-multiply filter blur-[128px] opacity-40 animate-float"></div>
      
      <div className="relative z-10 w-full max-w-xl px-6 animate-fade-in-up">
        {role === null ? (
          <Link to="/" className="inline-flex items-center gap-2 text-indigo-300 hover:text-white mb-8 transition-colors font-medium">
            <ArrowLeft className="w-4 h-4" /> Back to Home
          </Link>
        ) : (
          <button onClick={() => { setRole(null); setError(null); }} className="inline-flex items-center gap-2 text-indigo-300 hover:text-white mb-8 transition-colors font-medium">
            <ArrowLeft className="w-4 h-4" /> Back to Roles
          </button>
        )}
        
        <div className="glass-dark p-8 md:p-10 rounded-3xl">
          <div className="flex justify-center mb-6">
            <div className="w-16 h-16 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-2xl flex items-center justify-center shadow-lg transform -rotate-6">
              <Book className="w-8 h-8 text-white" />
            </div>
          </div>
          
          <h2 className="text-3xl font-bold text-center text-white mb-2 tracking-tight">
            {role === null ? "Create an Account" : `${role.charAt(0).toUpperCase() + role.slice(1)} Registration`}
          </h2>
          <p className="text-center text-indigo-200/80 mb-6 font-medium">
            {role === null ? "Choose your role to get started" : "Please fill out the details below"}
          </p>

          {error && (
            <div className="bg-red-500/20 border border-red-500/50 text-red-200 p-3 rounded-lg flex items-center gap-2 mb-6 text-sm">
              <AlertCircle className="w-4 h-4" /> {error}
            </div>
          )}

          {success && (
            <div className="bg-emerald-500/20 border border-emerald-500/50 text-emerald-200 p-3 rounded-lg flex items-center gap-2 mb-6 text-sm">
              <CheckCircle className="w-4 h-4" /> Registration successful! Redirecting to login...
            </div>
          )}
          
          {role === null ? (
            <div className="space-y-4 max-w-md mx-auto">
              <button onClick={() => setRole('student')} className="group w-full flex items-center justify-between bg-white/5 hover:bg-white/10 border border-white/10 hover:border-indigo-400/50 p-4 rounded-xl text-white transition-all duration-300 hover:shadow-lg hover:shadow-indigo-500/20">
                <div className="flex items-center gap-4">
                  <div className="p-2.5 bg-blue-500/20 text-blue-400 rounded-lg group-hover:bg-blue-500 group-hover:text-white transition-colors">
                    <GraduationCap className="w-5 h-5" />
                  </div>
                  <span className="font-semibold text-lg">Student</span>
                </div>
              </button>
              
              <button onClick={() => setRole('faculty')} className="group w-full flex items-center justify-between bg-white/5 hover:bg-white/10 border border-white/10 hover:border-purple-400/50 p-4 rounded-xl text-white transition-all duration-300 hover:shadow-lg hover:shadow-purple-500/20">
                <div className="flex items-center gap-4">
                  <div className="p-2.5 bg-purple-500/20 text-purple-400 rounded-lg group-hover:bg-purple-500 group-hover:text-white transition-colors">
                    <Briefcase className="w-5 h-5" />
                  </div>
                  <span className="font-semibold text-lg">Faculty</span>
                </div>
              </button>

              <button onClick={() => setRole('admin')} className="group w-full flex items-center justify-between bg-white/5 hover:bg-white/10 border border-white/10 hover:border-emerald-400/50 p-4 rounded-xl text-white transition-all duration-300 hover:shadow-lg hover:shadow-emerald-500/20">
                <div className="flex items-center gap-4">
                  <div className="p-2.5 bg-emerald-500/20 text-emerald-400 rounded-lg group-hover:bg-emerald-500 group-hover:text-white transition-colors">
                    <ShieldCheck className="w-5 h-5" />
                  </div>
                  <span className="font-semibold text-lg">Admin</span>
                </div>
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-4 animate-fade-in-up" style={{ animationDuration: '0.4s' }}>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-indigo-200 mb-1">Full Name</label>
                  <input type="text" required value={name} onChange={e=>setName(e.target.value)} className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder="John Doe" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-indigo-200 mb-1">Email Address</label>
                  <input type="email" required value={email} onChange={e=>setEmail(e.target.value)} className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder="john@example.com" />
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {role !== 'admin' && (
                  <div>
                    <label className="block text-sm font-medium text-indigo-200 mb-1">
                      {role === 'student' && "Enrollment Number"}
                      {role === 'faculty' && "Faculty ID"}
                    </label>
                    <input type="text" required value={identifier} onChange={e=>setIdentifier(e.target.value)} className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder="ID/Number" />
                  </div>
                )}
                {role === 'admin' && (
                  <div>
                    <label className="block text-sm font-medium text-indigo-200 mb-1">Position</label>
                    <input type="text" required value={position} onChange={e=>setPosition(e.target.value)} className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder="e.g. HOD / Dean" />
                  </div>
                )}
                <div>
                  <label className="block text-sm font-medium text-indigo-200 mb-1">Phone Number</label>
                  <input type="tel" required value={phone} onChange={e=>setPhone(e.target.value)} className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder="+91 9876543210" />
                </div>
              </div>

              {role === 'student' && (
                <div>
                  <label className="block text-sm font-medium text-indigo-200 mb-1">Course</label>
                  <select required value={course} onChange={e=>setCourse(e.target.value)} className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500 [&>option]:text-slate-900">
                    <option value="">Select a Course</option>
                    <option value="cs">Computer Science (B.Tech)</option>
                    <option value="it">Information Technology (B.Tech)</option>
                    <option value="bca">BCA</option>
                    <option value="mca">MCA</option>
                  </select>
                </div>
              )}

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-indigo-200 mb-1">Password</label>
                  <input type="password" required value={password} onChange={e=>setPassword(e.target.value)} className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder="••••••••" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-indigo-200 mb-1">Confirm Password</label>
                  <input type="password" required value={confirmPassword} onChange={e=>setConfirmPassword(e.target.value)} className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder="••••••••" />
                </div>
              </div>
              
              <button type="submit" disabled={loading} className="w-full py-3.5 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white rounded-xl font-bold shadow-lg shadow-indigo-500/30 transition-all duration-300 mt-6 flex justify-center items-center">
                {loading ? (
                   <span className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin"></span>
                ) : (
                  "Create Account"
                )}
              </button>
            </form>
          )}

          <div className="mt-8 pt-6 border-t border-white/10 text-center">
            <p className="text-sm text-indigo-200/80">Already have an account? <Link to="/login" className="text-white font-bold hover:underline">Sign In</Link></p>
          </div>
        </div>
      </div>
    </div>
  );
}
"""

with open(os.path.join(frontend_dir, "src/pages/auth/Login.tsx"), "w", encoding="utf-8") as f: f.write(login_tsx)
with open(os.path.join(frontend_dir, "src/pages/auth/Register.tsx"), "w", encoding="utf-8") as f: f.write(register_tsx)

print("Database scripts created and Auth forms updated successfully!")
