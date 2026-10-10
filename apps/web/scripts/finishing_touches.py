import os
import re

backend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\services\api"
frontend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web"

# --- 1. ADMIN USER API ---
user_controller = """const db = require('../db');

exports.getAllUsers = (req, res) => {
    if (req.user.role !== 'admin') return res.status(403).json({error: 'Admin only'});
    db.all('SELECT id, name, email, role, course, semester, identifier FROM users ORDER BY id DESC', [], (err, rows) => {
        if(err) return res.status(500).json({error: 'DB Error'});
        res.json(rows || []);
    });
};
"""
with open(os.path.join(backend_dir, "controllers", "userController.js"), "w", encoding="utf-8") as f: f.write(user_controller)

user_routes = """const express = require('express');
const router = express.Router();
const auth = require('../middleware/auth');
const userController = require('../controllers/userController');
router.get('/', auth, userController.getAllUsers);
module.exports = router;
"""
with open(os.path.join(backend_dir, "routes", "userRoutes.js"), "w", encoding="utf-8") as f: f.write(user_routes)

# Update index.js
index_path = os.path.join(backend_dir, "index.js")
with open(index_path, "r", encoding="utf-8") as f: idx = f.read()
if "userRoutes" not in idx:
    idx = idx.replace("const authRoutes = require('./routes/authRoutes');", "const authRoutes = require('./routes/authRoutes');\nconst userRoutes = require('./routes/userRoutes');")
    idx = idx.replace("app.use('/api/auth', authRoutes);", "app.use('/api/auth', authRoutes);\napp.use('/api/users', userRoutes);")
    with open(index_path, "w", encoding="utf-8") as f: f.write(idx)

# --- 2. SEED SCRIPT ---
seed_js = """const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcrypt');
const db = new sqlite3.Database('./database.sqlite');

async function seed() {
    console.log("Seeding Database...");
    const salt = await bcrypt.genSalt(10);
    const pass = await bcrypt.hash("password123", salt);

    db.serialize(() => {
        // Clear tables
        db.run('DELETE FROM users');
        db.run('DELETE FROM assignments');
        db.run('DELETE FROM submissions');
        db.run('DELETE FROM materials');

        // Admin
        db.run(`INSERT INTO users (role, name, email, password, position) VALUES ('admin', 'System Admin', 'admin@educonnect.com', '${pass}', 'Dean')`);

        // Faculty
        db.run(`INSERT INTO users (role, name, email, password, identifier) VALUES ('faculty', 'Prof. Smith', 'smith@educonnect.com', '${pass}', 'FAC001')`);
        db.run(`INSERT INTO users (role, name, email, password, identifier) VALUES ('faculty', 'Dr. Patel', 'patel@educonnect.com', '${pass}', 'FAC002')`);

        // Students (Sem 3 BCA)
        for(let i=1; i<=10; i++) {
            db.run(`INSERT INTO users (role, name, email, password, identifier, course, semester) VALUES ('student', 'Student ${i}', 'student${i}@educonnect.com', '${pass}', 'ENR2600${i}', 'bca_hons', '3')`);
        }
        // Students (Sem 1 MCA)
        for(let i=11; i<=15; i++) {
            db.run(`INSERT INTO users (role, name, email, password, identifier, course, semester) VALUES ('student', 'Student ${i}', 'student${i}@educonnect.com', '${pass}', 'ENR260${i}', 'mca', '1')`);
        }

        // Assignments (For Sem 3 BCA)
        const tomorrow = new Date(Date.now() + 86400000).toISOString();
        const yesterday = new Date(Date.now() - 86400000).toISOString();
        
        db.run(`INSERT INTO assignments (title, course, semester, marks, due_date, description, subject, status, faculty_id) VALUES ('Advanced Data Structures', 'bca_hons', '3', 50, '${tomorrow}', 'Implement an AVL tree.', 'Data Structures & Algorithms', 'Published', 2)`);
        db.run(`INSERT INTO assignments (title, course, semester, marks, due_date, description, subject, status, faculty_id) VALUES ('React Dashboard Build', 'bca_hons', '3', 100, '${yesterday}', 'Build a dashboard.', 'Web Development Technologies', 'Published', 2)`);

        console.log("Database Seeded Successfully! Use password: password123 for all users.");
    });
}
seed();
"""
with open(os.path.join(backend_dir, "seed.js"), "w", encoding="utf-8") as f: f.write(seed_js)


# --- 3. ADMIN DASHBOARD ---
admin_dash = """import { useState, useEffect } from 'react';
import { Users, Shield, Book, Award } from 'lucide-react';
import axios from 'axios';

export default function AdminDashboard() {
  const [users, setUsers] = useState<any[]>([]);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
         const token = localStorage.getItem('token');
         const res = await axios.get('http://localhost:5000/api/users', { headers: { Authorization: `Bearer ${token}` } });
         setUsers(res.data);
      } catch (err) {}
    };
    fetchUsers();
  }, []);

  const students = users.filter(u => u.role === 'student');
  const faculty = users.filter(u => u.role === 'faculty');

  return (
    <div className="space-y-6 animate-fade-in-up">
      <div className="mb-8">
        <h1 className="text-3xl font-extrabold text-slate-900">University Admin Panel</h1>
        <p className="text-slate-500 mt-1 font-medium">Manage all platform users and roles</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="w-14 h-14 bg-indigo-50 text-indigo-600 rounded-2xl flex items-center justify-center"><Users className="w-7 h-7" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase">Total Students</p><h2 className="text-3xl font-black text-slate-900">{students.length}</h2></div>
        </div>
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="w-14 h-14 bg-purple-50 text-purple-600 rounded-2xl flex items-center justify-center"><Shield className="w-7 h-7" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase">Faculty</p><h2 className="text-3xl font-black text-slate-900">{faculty.length}</h2></div>
        </div>
      </div>

      <div className="bg-white rounded-3xl shadow-sm border border-slate-100 p-8">
         <h2 className="text-xl font-bold text-slate-900 mb-6 border-b border-slate-100 pb-4">System Users Directory</h2>
         <div className="overflow-x-auto">
            <table className="w-full text-left">
               <thead>
                  <tr className="text-slate-500 text-sm border-b border-slate-200">
                     <th className="pb-3 font-bold">Name</th>
                     <th className="pb-3 font-bold">Email</th>
                     <th className="pb-3 font-bold">Role</th>
                     <th className="pb-3 font-bold">Identifier (ID)</th>
                     <th className="pb-3 font-bold">Program/Sem</th>
                  </tr>
               </thead>
               <tbody className="divide-y divide-slate-100">
                  {users.map(u => (
                     <tr key={u.id} className="hover:bg-slate-50 transition-colors">
                        <td className="py-4 font-bold text-slate-800">{u.name}</td>
                        <td className="py-4 text-slate-600">{u.email}</td>
                        <td className="py-4"><span className={`px-2 py-1 rounded-md text-xs font-bold uppercase ${u.role === 'admin' ? 'bg-rose-50 text-rose-600' : u.role === 'faculty' ? 'bg-purple-50 text-purple-600' : 'bg-indigo-50 text-indigo-600'}`}>{u.role}</span></td>
                        <td className="py-4 font-mono text-sm text-slate-500">{u.identifier || '-'}</td>
                        <td className="py-4 text-sm font-bold text-slate-600">{u.course ? `${u.course.replace('_',' ').toUpperCase()} (S${u.semester})` : '-'}</td>
                     </tr>
                  ))}
               </tbody>
            </table>
         </div>
      </div>
    </div>
  );
}
"""
with open(os.path.join(frontend_dir, "src/pages/AdminDashboard.tsx"), "w", encoding="utf-8") as f: f.write(admin_dash)

# Update App.tsx for Admin route
app_path = os.path.join(frontend_dir, "src/App.tsx")
with open(app_path, "r", encoding="utf-8") as f: app_content = f.read()
if "AdminDashboard" not in app_content:
    app_content = app_content.replace(
        "import FacultyDashboard from './pages/FacultyDashboard';",
        "import FacultyDashboard from './pages/FacultyDashboard';\nimport AdminDashboard from './pages/AdminDashboard';"
    )
    app_content = app_content.replace(
        "{user?.role === 'student' ? <StudentDashboard /> : <FacultyDashboard />}",
        "{user?.role === 'admin' ? <AdminDashboard /> : user?.role === 'student' ? <StudentDashboard /> : <FacultyDashboard />}"
    )
    with open(app_path, "w", encoding="utf-8") as f: f.write(app_content)


# --- 4. POLISHED LANDING PAGE ---
landing_tsx = """import { ArrowRight, Bot, BookOpen, Sparkles, ShieldCheck } from 'lucide-react';
import { Link } from 'react-router-dom';

export default function Landing() {
  return (
    <div className="min-h-screen bg-[#0f172a] text-white overflow-hidden relative">
      {/* Animated Background Gradients */}
      <div className="absolute top-[-20%] left-[-10%] w-[50%] h-[50%] bg-indigo-600/30 blur-[120px] rounded-full animate-pulse-slow pointer-events-none"></div>
      <div className="absolute bottom-[-20%] right-[-10%] w-[50%] h-[50%] bg-purple-600/30 blur-[120px] rounded-full animate-pulse-slow pointer-events-none" style={{animationDelay: '2s'}}></div>

      {/* Navbar */}
      <nav className="relative z-10 flex justify-between items-center p-8 max-w-7xl mx-auto">
        <div className="flex items-center gap-3">
           <div className="w-12 h-12 bg-gradient-to-br from-indigo-500 to-purple-500 rounded-xl flex items-center justify-center shadow-lg shadow-indigo-500/30">
              <BookOpen className="w-6 h-6 text-white" />
           </div>
           <span className="text-2xl font-black tracking-tight">EduConnect <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-purple-400">AI</span></span>
        </div>
        <div className="flex gap-4">
          <Link to="/login" className="px-6 py-2.5 font-bold text-slate-300 hover:text-white transition">Sign In</Link>
          <Link to="/register" className="bg-white text-slate-900 px-6 py-2.5 rounded-full font-bold hover:scale-105 transition-transform shadow-xl">Get Started</Link>
        </div>
      </nav>

      {/* Hero Section */}
      <main className="relative z-10 flex flex-col items-center text-center px-4 pt-20 pb-32 max-w-5xl mx-auto animate-fade-in-up">
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-300 font-bold text-sm mb-8">
           <Sparkles className="w-4 h-4" /> Ganpat University Hackathon 2026 (PS-04)
        </div>
        
        <h1 className="text-6xl md:text-8xl font-black tracking-tighter mb-8 leading-[1.1]">
          The Future of <br/>
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-purple-400 to-pink-400">Academic Collaboration</span>
        </h1>
        
        <p className="text-xl text-slate-400 mb-12 max-w-2xl font-medium leading-relaxed">
          An intelligent platform uniting faculty and students with smart assignments, AI doubt-solving, explainable risk indicators, and secure workflows.
        </p>
        
        <div className="flex flex-col sm:flex-row gap-4">
          <Link to="/register" className="bg-gradient-to-r from-indigo-600 to-purple-600 px-8 py-4 rounded-full font-bold text-lg hover:scale-105 transition-transform shadow-lg shadow-indigo-500/25 flex items-center justify-center gap-2">
            Explore Platform <ArrowRight className="w-5 h-5" />
          </Link>
        </div>

        {/* Glassmorphism Feature Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-24 text-left w-full">
           <div className="glass-dark p-8 rounded-3xl relative overflow-hidden group">
              <div className="absolute top-0 right-0 w-32 h-32 bg-indigo-500/10 rounded-full blur-2xl group-hover:bg-indigo-500/20 transition-all"></div>
              <Bot className="w-10 h-10 text-indigo-400 mb-6" />
              <h3 className="text-xl font-bold mb-2">AI Study Assistant</h3>
              <p className="text-slate-400">Context-aware AI helping students resolve doubts instantly based on course materials.</p>
           </div>
           <div className="glass-dark p-8 rounded-3xl relative overflow-hidden group">
              <div className="absolute top-0 right-0 w-32 h-32 bg-purple-500/10 rounded-full blur-2xl group-hover:bg-purple-500/20 transition-all"></div>
              <ShieldCheck className="w-10 h-10 text-purple-400 mb-6" />
              <h3 className="text-xl font-bold mb-2">Secure Submissions</h3>
              <p className="text-slate-400">Role-based access control ensuring students only see what belongs to their semester.</p>
           </div>
           <div className="glass-dark p-8 rounded-3xl relative overflow-hidden group">
              <div className="absolute top-0 right-0 w-32 h-32 bg-pink-500/10 rounded-full blur-2xl group-hover:bg-pink-500/20 transition-all"></div>
              <BookOpen className="w-10 h-10 text-pink-400 mb-6" />
              <h3 className="text-xl font-bold mb-2">Risk Indicators</h3>
              <p className="text-slate-400">Predictive analytics warning students of overdue tasks before they fail.</p>
           </div>
        </div>
      </main>
    </div>
  );
}
"""
with open(os.path.join(frontend_dir, "src/pages/Landing.tsx"), "w", encoding="utf-8") as f: f.write(landing_tsx)


# --- 5. CALENDAR & NOTIFICATIONS UI ---
calendar_tsx = """import { Calendar as CalIcon, Clock } from 'lucide-react';
export default function Calendar() {
  return (
    <div className="max-w-4xl mx-auto space-y-6 animate-fade-in-up pb-10">
      <h1 className="text-3xl font-extrabold text-slate-900 mb-8">Academic Calendar</h1>
      <div className="bg-white rounded-3xl shadow-sm border border-slate-100 p-8">
         <div className="grid grid-cols-7 gap-4 mb-4 text-center font-bold text-slate-500 text-sm">
            <div>Mon</div><div>Tue</div><div>Wed</div><div>Thu</div><div>Fri</div><div>Sat</div><div>Sun</div>
         </div>
         <div className="grid grid-cols-7 gap-4">
            {Array.from({length: 30}).map((_, i) => (
               <div key={i} className={`h-24 rounded-2xl border ${i===15 ? 'bg-indigo-50 border-indigo-200' : 'border-slate-100'} p-2 hover:border-indigo-300 transition-colors relative group`}>
                  <span className={`font-bold ${i===15 ? 'text-indigo-600' : 'text-slate-700'}`}>{i+1}</span>
                  {i===15 && <div className="mt-2 text-[10px] font-bold bg-indigo-600 text-white p-1 rounded-md leading-tight">Hackathon Submission</div>}
                  {i===18 && <div className="mt-2 text-[10px] font-bold bg-rose-500 text-white p-1 rounded-md leading-tight">Assignment Due</div>}
               </div>
            ))}
         </div>
      </div>
    </div>
  );
}
"""
with open(os.path.join(frontend_dir, "src/pages/Calendar.tsx"), "w", encoding="utf-8") as f: f.write(calendar_tsx)

notif_tsx = """import { Bell, CheckCircle, AlertCircle } from 'lucide-react';
export default function Notifications() {
  return (
    <div className="max-w-3xl mx-auto space-y-6 animate-fade-in-up pb-10">
      <h1 className="text-3xl font-extrabold text-slate-900 mb-8 flex items-center gap-3"><Bell className="w-8 h-8 text-amber-500"/> Notifications</h1>
      <div className="space-y-4">
         <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex gap-4">
            <div className="w-12 h-12 bg-indigo-50 text-indigo-600 rounded-full flex items-center justify-center shrink-0"><CheckCircle className="w-6 h-6"/></div>
            <div>
               <h3 className="font-bold text-slate-900">EduConnect Profile Created!</h3>
               <p className="text-slate-500 text-sm mt-1">Welcome to the Intelligent Academic Collaboration Platform.</p>
               <span className="text-xs font-bold text-slate-400 mt-2 block">Just now</span>
            </div>
         </div>
         <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex gap-4 opacity-75">
            <div className="w-12 h-12 bg-rose-50 text-rose-600 rounded-full flex items-center justify-center shrink-0"><AlertCircle className="w-6 h-6"/></div>
            <div>
               <h3 className="font-bold text-slate-900">System Maintenance Scheduled</h3>
               <p className="text-slate-500 text-sm mt-1">The system will be briefly offline for the hackathon judging review.</p>
               <span className="text-xs font-bold text-slate-400 mt-2 block">2 hours ago</span>
            </div>
         </div>
      </div>
    </div>
  );
}
"""
with open(os.path.join(frontend_dir, "src/pages/Notifications.tsx"), "w", encoding="utf-8") as f: f.write(notif_tsx)

print("All finishing touches built!")
