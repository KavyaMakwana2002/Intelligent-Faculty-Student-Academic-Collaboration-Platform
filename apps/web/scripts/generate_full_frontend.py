import os
import json

base_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web"

# List of files to generate
files = {}

# 1. AuthContext
files["src/contexts/AuthContext.tsx"] = """import React, { createContext, useContext, useState, ReactNode } from 'react';
import { User } from '../types';

interface AuthContextType {
  user: User | null;
  login: (role: User['role']) => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);

  const login = (role: User['role']) => {
    setUser({ id: '1', name: `Demo ${role}`, email: `${role}@demo.com`, role });
  };

  const logout = () => setUser(null);

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) throw new Error('useAuth must be used within an AuthProvider');
  return context;
}
"""

# 2. Main layout
files["src/components/layout/Layout.tsx"] = """import { Outlet, Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import { LogOut, Book, LayoutDashboard, Settings, User as UserIcon, FileText, MessageSquare, Bell, Calendar, BarChart2 } from 'lucide-react';

export default function Layout() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  return (
    <div className="flex h-screen bg-slate-50">
      <aside className="w-64 bg-white border-r border-slate-200 flex flex-col">
        <div className="p-6 border-b border-slate-200">
          <Link to="/" className="text-2xl font-bold text-indigo-600 flex items-center gap-2">
            <Book className="w-6 h-6" /> EduConnect AI
          </Link>
          <div className="mt-2 text-xs text-slate-500 bg-slate-100 rounded px-2 py-1 inline-block">
            DEMO MODE ({user?.role})
          </div>
        </div>
        
        <nav className="flex-1 overflow-y-auto p-4 space-y-1">
          <Link to="/dashboard" className="flex items-center gap-3 px-3 py-2 text-slate-700 rounded-md hover:bg-slate-100 hover:text-indigo-600">
            <LayoutDashboard className="w-5 h-5" /> Dashboard
          </Link>
          <Link to="/courses" className="flex items-center gap-3 px-3 py-2 text-slate-700 rounded-md hover:bg-slate-100 hover:text-indigo-600">
            <Book className="w-5 h-5" /> Courses
          </Link>
          <Link to="/assignments" className="flex items-center gap-3 px-3 py-2 text-slate-700 rounded-md hover:bg-slate-100 hover:text-indigo-600">
            <FileText className="w-5 h-5" /> Assignments
          </Link>
          <Link to="/materials" className="flex items-center gap-3 px-3 py-2 text-slate-700 rounded-md hover:bg-slate-100 hover:text-indigo-600">
            <FileText className="w-5 h-5" /> Study Materials
          </Link>
          <Link to="/announcements" className="flex items-center gap-3 px-3 py-2 text-slate-700 rounded-md hover:bg-slate-100 hover:text-indigo-600">
            <Bell className="w-5 h-5" /> Announcements
          </Link>
          <Link to="/discussions" className="flex items-center gap-3 px-3 py-2 text-slate-700 rounded-md hover:bg-slate-100 hover:text-indigo-600">
            <MessageSquare className="w-5 h-5" /> Discussions
          </Link>
          <Link to="/calendar" className="flex items-center gap-3 px-3 py-2 text-slate-700 rounded-md hover:bg-slate-100 hover:text-indigo-600">
            <Calendar className="w-5 h-5" /> Calendar
          </Link>
          {user?.role === 'admin' && (
             <Link to="/analytics" className="flex items-center gap-3 px-3 py-2 text-slate-700 rounded-md hover:bg-slate-100 hover:text-indigo-600">
               <BarChart2 className="w-5 h-5" /> Analytics
             </Link>
          )}
        </nav>

        <div className="p-4 border-t border-slate-200">
          <Link to="/profile" className="flex items-center gap-3 px-3 py-2 text-slate-700 rounded-md hover:bg-slate-100">
            <UserIcon className="w-5 h-5" /> Profile
          </Link>
          <Link to="/settings" className="flex items-center gap-3 px-3 py-2 text-slate-700 rounded-md hover:bg-slate-100">
            <Settings className="w-5 h-5" /> Settings
          </Link>
          <button onClick={handleLogout} className="w-full mt-2 flex items-center gap-3 px-3 py-2 text-red-600 rounded-md hover:bg-red-50">
            <LogOut className="w-5 h-5" /> Logout
          </button>
        </div>
      </aside>

      <main className="flex-1 overflow-y-auto">
        <header className="bg-white border-b border-slate-200 px-8 py-4 flex justify-end">
           <Link to="/notifications" className="p-2 text-slate-500 hover:text-indigo-600 rounded-full hover:bg-slate-100">
             <Bell className="w-5 h-5" />
           </Link>
        </header>
        <div className="p-8">
          <Outlet />
        </div>
      </main>
    </div>
  );
}
"""

# 3. Landing page
files["src/pages/Landing.tsx"] = """import { Link } from 'react-router-dom';
import { Book, ChevronRight } from 'lucide-react';

export default function Landing() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 to-white flex flex-col">
      <header className="container mx-auto px-6 py-6 flex justify-between items-center">
        <div className="text-2xl font-bold text-indigo-600 flex items-center gap-2">
          <Book className="w-8 h-8" /> EduConnect AI
        </div>
        <div className="space-x-4">
          <Link to="/login" className="text-slate-600 hover:text-indigo-600 font-medium">Login</Link>
          <Link to="/register" className="bg-indigo-600 text-white px-5 py-2 rounded-lg font-medium hover:bg-indigo-700 transition">Register</Link>
        </div>
      </header>

      <main className="flex-1 flex flex-col items-center justify-center text-center px-6">
        <h1 className="text-5xl md:text-6xl font-extrabold text-slate-900 mb-6 tracking-tight">
          Intelligent Academic <span className="text-indigo-600">Collaboration</span>
        </h1>
        <p className="text-xl text-slate-600 mb-10 max-w-2xl mx-auto">
          A centralized platform where students and faculty can manage courses, study materials, assignments, and academic progress seamlessly.
        </p>
        <div className="flex gap-4">
          <Link to="/login" className="bg-indigo-600 text-white px-8 py-4 rounded-xl font-bold text-lg hover:bg-indigo-700 transition flex items-center gap-2 shadow-lg shadow-indigo-200">
            Try Demo Mode <ChevronRight className="w-5 h-5" />
          </Link>
        </div>
        <p className="mt-8 text-sm text-slate-400">Created for Ganpat University Hackathon 2026 (Demo Only)</p>
      </main>
    </div>
  );
}
"""

# 4. Login page
files["src/pages/auth/Login.tsx"] = """import { useAuth } from '../../contexts/AuthContext';
import { useNavigate } from 'react-router-dom';
import { Book } from 'lucide-react';

export default function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleLogin = (role: 'student' | 'faculty' | 'admin') => {
    login(role);
    navigate('/dashboard');
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50 px-4">
      <div className="bg-white p-8 rounded-2xl shadow-xl w-full max-w-md border border-slate-100">
        <div className="flex justify-center mb-6">
          <div className="w-16 h-16 bg-indigo-100 rounded-full flex items-center justify-center">
            <Book className="w-8 h-8 text-indigo-600" />
          </div>
        </div>
        <h2 className="text-2xl font-bold text-center text-slate-900 mb-2">Welcome Back</h2>
        <p className="text-center text-slate-500 mb-8">Select a demo role to continue</p>
        
        <div className="space-y-4">
          <button onClick={() => handleLogin('student')} className="w-full bg-slate-50 hover:bg-indigo-50 text-slate-700 hover:text-indigo-700 border border-slate-200 hover:border-indigo-300 py-3 rounded-lg font-medium transition">
            Login as Student
          </button>
          <button onClick={() => handleLogin('faculty')} className="w-full bg-slate-50 hover:bg-indigo-50 text-slate-700 hover:text-indigo-700 border border-slate-200 hover:border-indigo-300 py-3 rounded-lg font-medium transition">
            Login as Faculty
          </button>
          <button onClick={() => handleLogin('admin')} className="w-full bg-slate-50 hover:bg-indigo-50 text-slate-700 hover:text-indigo-700 border border-slate-200 hover:border-indigo-300 py-3 rounded-lg font-medium transition">
            Login as Admin
          </button>
        </div>
        
        <div className="mt-6 text-center text-xs text-amber-600 bg-amber-50 p-3 rounded-md">
          <strong>DEMO MODE:</strong> Authentication is simulated for the hackathon demo. No credentials required.
        </div>
      </div>
    </div>
  );
}
"""

# App.tsx complete replacement
files["src/App.tsx"] = """import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import Layout from './components/layout/Layout';
import Landing from './pages/Landing';
import Login from './pages/auth/Login';
import StudentDashboard from './pages/dashboard/StudentDashboard';
import FacultyDashboard from './pages/dashboard/FacultyDashboard';
import AdminDashboard from './pages/dashboard/AdminDashboard';

// Placeholder Pages
const Placeholder = ({ title }: { title: string }) => (
  <div className="bg-white p-8 rounded-xl shadow-sm border border-slate-100 h-full flex flex-col items-center justify-center">
    <h1 className="text-2xl font-bold text-slate-800 mb-2">{title}</h1>
    <p className="text-slate-500">This page is under construction for the demo.</p>
  </div>
);

const Courses = () => <Placeholder title="Courses" />;
const Assignments = () => <Placeholder title="Assignments" />;
const Materials = () => <Placeholder title="Study Materials" />;
const Announcements = () => <Placeholder title="Announcements" />;
const Discussions = () => <Placeholder title="Discussions" />;
const Calendar = () => <Placeholder title="Academic Calendar" />;
const Analytics = () => <Placeholder title="Analytics" />;
const Notifications = () => <Placeholder title="Notifications" />;
const Profile = () => <Placeholder title="Profile" />;
const Settings = () => <Placeholder title="Settings" />;
const NotFound = () => <Placeholder title="404 - Not Found" />;

const ProtectedRoute = ({ children }: { children: React.ReactNode }) => {
  const { user } = useAuth();
  if (!user) return <Navigate to="/login" replace />;
  return <>{children}</>;
};

function AppRoutes() {
  const { user } = useAuth();
  
  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Login />} />
      
      <Route element={<Layout />}>
        <Route path="/dashboard" element={
          <ProtectedRoute>
            {user?.role === 'student' && <StudentDashboard />}
            {user?.role === 'faculty' && <FacultyDashboard />}
            {user?.role === 'admin' && <AdminDashboard />}
          </ProtectedRoute>
        } />
        
        <Route path="/courses" element={<ProtectedRoute><Courses /></ProtectedRoute>} />
        <Route path="/assignments" element={<ProtectedRoute><Assignments /></ProtectedRoute>} />
        <Route path="/materials" element={<ProtectedRoute><Materials /></ProtectedRoute>} />
        <Route path="/announcements" element={<ProtectedRoute><Announcements /></ProtectedRoute>} />
        <Route path="/discussions" element={<ProtectedRoute><Discussions /></ProtectedRoute>} />
        <Route path="/calendar" element={<ProtectedRoute><Calendar /></ProtectedRoute>} />
        <Route path="/analytics" element={<ProtectedRoute><Analytics /></ProtectedRoute>} />
        <Route path="/notifications" element={<ProtectedRoute><Notifications /></ProtectedRoute>} />
        <Route path="/profile" element={<ProtectedRoute><Profile /></ProtectedRoute>} />
        <Route path="/settings" element={<ProtectedRoute><Settings /></ProtectedRoute>} />
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <Router>
        <AppRoutes />
      </Router>
    </AuthProvider>
  );
}
"""

# Dashboards
files["src/pages/dashboard/StudentDashboard.tsx"] = """import { BookOpen, FileText, Clock, TrendingUp } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';

export default function StudentDashboard() {
  const { user } = useAuth();
  
  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold text-slate-900">Welcome back, {user?.name}!</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="p-3 bg-blue-100 text-blue-600 rounded-lg"><BookOpen className="w-6 h-6" /></div>
          <div>
            <p className="text-sm text-slate-500 font-medium">Enrolled Courses</p>
            <p className="text-2xl font-bold text-slate-800">4</p>
          </div>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="p-3 bg-indigo-100 text-indigo-600 rounded-lg"><FileText className="w-6 h-6" /></div>
          <div>
            <p className="text-sm text-slate-500 font-medium">Pending Assignments</p>
            <p className="text-2xl font-bold text-slate-800">2</p>
          </div>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="p-3 bg-rose-100 text-rose-600 rounded-lg"><Clock className="w-6 h-6" /></div>
          <div>
            <p className="text-sm text-slate-500 font-medium">Upcoming Deadlines</p>
            <p className="text-2xl font-bold text-slate-800">1</p>
          </div>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="p-3 bg-emerald-100 text-emerald-600 rounded-lg"><TrendingUp className="w-6 h-6" /></div>
          <div>
            <p className="text-sm text-slate-500 font-medium">Overall Progress</p>
            <p className="text-2xl font-bold text-slate-800">85%</p>
          </div>
        </div>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <h2 className="text-lg font-bold text-slate-800 mb-4">Recent Announcements</h2>
          <div className="space-y-4">
            <div className="p-4 border border-slate-100 rounded-lg bg-slate-50">
              <h3 className="font-semibold text-slate-800">Hackathon Schedule Updated</h3>
              <p className="text-sm text-slate-500 mt-1">Please review the updated submission guidelines for Phase 1.</p>
            </div>
          </div>
        </div>
        
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <h2 className="text-lg font-bold text-slate-800 mb-4">Recent Study Materials</h2>
          <div className="space-y-4">
             <div className="p-4 border border-slate-100 rounded-lg flex justify-between items-center">
                <div>
                   <h3 className="font-semibold text-slate-800">React State Management Guide</h3>
                   <p className="text-xs text-slate-500 mt-1">CS401 - Web Development</p>
                </div>
                <button className="text-indigo-600 text-sm font-medium hover:underline">View</button>
             </div>
          </div>
        </div>
      </div>
    </div>
  );
}
"""

files["src/pages/dashboard/FacultyDashboard.tsx"] = """import { Users, FileText, CheckCircle, Bell } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';

export default function FacultyDashboard() {
  const { user } = useAuth();
  
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-end">
        <h1 className="text-3xl font-bold text-slate-900">Faculty Portal, {user?.name}</h1>
        <button className="bg-indigo-600 text-white px-4 py-2 rounded-lg font-medium hover:bg-indigo-700">
          + Create Assignment
        </button>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <p className="text-sm text-slate-500 font-medium">Courses Managed</p>
          <p className="text-3xl font-bold text-slate-800 mt-2">2</p>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <p className="text-sm text-slate-500 font-medium">Active Assignments</p>
          <p className="text-3xl font-bold text-slate-800 mt-2">5</p>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <p className="text-sm text-slate-500 font-medium">Pending Reviews</p>
          <p className="text-3xl font-bold text-slate-800 mt-2">18</p>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <p className="text-sm text-slate-500 font-medium">Avg Participation</p>
          <p className="text-3xl font-bold text-slate-800 mt-2">92%</p>
        </div>
      </div>
    </div>
  );
}
"""

files["src/pages/dashboard/AdminDashboard.tsx"] = """import { useAuth } from '../../contexts/AuthContext';

export default function AdminDashboard() {
  const { user } = useAuth();
  
  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold text-slate-900">Admin Console</h1>
      <div className="bg-amber-50 text-amber-800 p-4 rounded-lg border border-amber-200">
        <strong>Demo Mode:</strong> Administrative actions are simulated. Real user management will be connected in Phase 2.
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <h2 className="text-sm text-slate-500 font-medium">Total Users</h2>
          <p className="text-3xl font-bold text-slate-800 mt-2">1,245</p>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <h2 className="text-sm text-slate-500 font-medium">Active Courses</h2>
          <p className="text-3xl font-bold text-slate-800 mt-2">48</p>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <h2 className="text-sm text-slate-500 font-medium">System Health</h2>
          <p className="text-3xl font-bold text-emerald-600 mt-2">100%</p>
        </div>
      </div>
    </div>
  );
}
"""

# main.tsx
files["src/main.tsx"] = """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
"""

for path, content in files.items():
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding='utf-8') as f:
        f.write(content)

print("Full frontend scaffolding completed successfully!")
