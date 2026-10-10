import os

base_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web"
files = {}

# 1. index.css (Add animations & custom scrollbar)
files["src/index.css"] = """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  body {
    @apply bg-slate-50 text-slate-900 font-sans antialiased selection:bg-indigo-200 selection:text-indigo-900;
  }
}

@layer utilities {
  .glass {
    @apply bg-white/70 backdrop-blur-lg border border-white/20 shadow-xl;
  }
  .glass-dark {
    @apply bg-slate-900/80 backdrop-blur-xl border border-slate-700/50 shadow-2xl;
  }
  .animate-float {
    animation: float 6s ease-in-out infinite;
  }
  .animate-float-delayed {
    animation: float 6s ease-in-out 3s infinite;
  }
  .animate-fade-in-up {
    animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  }
  .animate-pulse-slow {
    animation: pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite;
  }
}

@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
  100% { transform: translateY(0px); }
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Custom Scrollbar */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}
::-webkit-scrollbar-track {
  background: transparent;
}
::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}
"""

# 2. Landing Page (Stunning Hero, Gradients, Animations)
files["src/pages/Landing.tsx"] = """import { Link } from 'react-router-dom';
import { Book, ChevronRight, Sparkles, Zap, Shield, Users } from 'lucide-react';

export default function Landing() {
  return (
    <div className="min-h-screen bg-slate-50 overflow-hidden relative">
      {/* Background Decorative Blobs */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden -z-10">
        <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-indigo-400/20 rounded-full blur-[120px] animate-pulse-slow"></div>
        <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-purple-400/20 rounded-full blur-[120px] animate-pulse-slow" style={{animationDelay: '2s'}}></div>
      </div>

      <header className="container mx-auto px-6 py-6 flex justify-between items-center relative z-10 animate-fade-in-up">
        <div className="text-2xl font-black text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 flex items-center gap-2">
          <div className="p-2 bg-indigo-600 rounded-xl text-white shadow-lg shadow-indigo-200">
            <Book className="w-6 h-6" />
          </div>
          EduConnect AI
        </div>
        <div className="space-x-4 flex items-center">
          <Link to="/login" className="text-slate-600 hover:text-indigo-600 font-semibold transition-colors">Login</Link>
          <Link to="/register" className="bg-slate-900 text-white px-6 py-2.5 rounded-full font-medium hover:bg-slate-800 transition-all shadow-md hover:shadow-xl hover:-translate-y-0.5">Get Started</Link>
        </div>
      </header>

      <main className="container mx-auto px-6 pt-20 pb-32 flex flex-col items-center text-center relative z-10">
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-indigo-50 border border-indigo-100 text-indigo-700 font-medium text-sm mb-8 animate-fade-in-up" style={{ animationDelay: '0.1s' }}>
          <Sparkles className="w-4 h-4" /> <span>Ganpat University Hackathon 2026</span>
        </div>
        
        <h1 className="text-5xl md:text-7xl font-extrabold text-slate-900 mb-8 tracking-tight max-w-4xl leading-tight animate-fade-in-up" style={{ animationDelay: '0.2s' }}>
          The Future of <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 via-purple-600 to-indigo-600 animate-gradient-x">Academic Collaboration</span>
        </h1>
        
        <p className="text-xl text-slate-600 mb-12 max-w-2xl mx-auto animate-fade-in-up leading-relaxed" style={{ animationDelay: '0.3s' }}>
          A unified, AI-powered platform seamlessly connecting students and faculty. Manage courses, materials, and progress in one beautiful workspace.
        </p>
        
        <div className="flex flex-col sm:flex-row gap-4 animate-fade-in-up" style={{ animationDelay: '0.4s' }}>
          <Link to="/login" className="group relative bg-gradient-to-r from-indigo-600 to-purple-600 text-white px-8 py-4 rounded-full font-bold text-lg hover:shadow-2xl hover:shadow-indigo-500/30 transition-all duration-300 hover:-translate-y-1 overflow-hidden">
            <span className="relative z-10 flex items-center gap-2">
              Launch Demo <ChevronRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </span>
            <div className="absolute inset-0 h-full w-full bg-gradient-to-r from-purple-600 to-indigo-600 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          </Link>
          <a href="#features" className="bg-white text-slate-700 border border-slate-200 px-8 py-4 rounded-full font-bold text-lg hover:bg-slate-50 hover:border-slate-300 transition-all duration-300 shadow-sm hover:shadow-md">
            Explore Features
          </a>
        </div>

        {/* Feature Cards Showcase */}
        <div id="features" className="mt-32 grid grid-cols-1 md:grid-cols-3 gap-8 w-full max-w-6xl animate-fade-in-up" style={{ animationDelay: '0.6s' }}>
          <div className="bg-white p-8 rounded-3xl shadow-xl shadow-slate-200/50 border border-slate-100 text-left hover:-translate-y-2 transition-transform duration-300 relative overflow-hidden group">
            <div className="absolute top-0 right-0 w-32 h-32 bg-blue-50 rounded-bl-full -z-10 transition-transform group-hover:scale-110"></div>
            <div className="w-14 h-14 bg-blue-100 text-blue-600 rounded-2xl flex items-center justify-center mb-6 shadow-inner">
              <Zap className="w-7 h-7" />
            </div>
            <h3 className="text-xl font-bold text-slate-900 mb-3">AI-Powered Insights</h3>
            <p className="text-slate-600 leading-relaxed">Smart analytics to track academic progress and provide personalized recommendations for students.</p>
          </div>
          
          <div className="bg-white p-8 rounded-3xl shadow-xl shadow-slate-200/50 border border-slate-100 text-left hover:-translate-y-2 transition-transform duration-300 relative overflow-hidden group">
             <div className="absolute top-0 right-0 w-32 h-32 bg-indigo-50 rounded-bl-full -z-10 transition-transform group-hover:scale-110"></div>
            <div className="w-14 h-14 bg-indigo-100 text-indigo-600 rounded-2xl flex items-center justify-center mb-6 shadow-inner">
              <Users className="w-7 h-7" />
            </div>
            <h3 className="text-xl font-bold text-slate-900 mb-3">Unified Classrooms</h3>
            <p className="text-slate-600 leading-relaxed">A central hub for discussions, assignments, and real-time announcements bridging the gap between faculty and students.</p>
          </div>

          <div className="bg-white p-8 rounded-3xl shadow-xl shadow-slate-200/50 border border-slate-100 text-left hover:-translate-y-2 transition-transform duration-300 relative overflow-hidden group">
             <div className="absolute top-0 right-0 w-32 h-32 bg-purple-50 rounded-bl-full -z-10 transition-transform group-hover:scale-110"></div>
            <div className="w-14 h-14 bg-purple-100 text-purple-600 rounded-2xl flex items-center justify-center mb-6 shadow-inner">
              <Shield className="w-7 h-7" />
            </div>
            <h3 className="text-xl font-bold text-slate-900 mb-3">Secure & Role-based</h3>
            <p className="text-slate-600 leading-relaxed">Dedicated interfaces and strict access controls for Students, Faculty, and Administrators.</p>
          </div>
        </div>
      </main>
    </div>
  );
}
"""

# 3. Login Page (Glassmorphism, beautiful UI)
files["src/pages/auth/Login.tsx"] = """import { useAuth } from '../../contexts/AuthContext';
import { useNavigate, Link } from 'react-router-dom';
import { Book, GraduationCap, Briefcase, ShieldCheck, ArrowLeft } from 'lucide-react';

export default function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleLogin = (role: 'student' | 'faculty' | 'admin') => {
    login(role);
    navigate('/dashboard');
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-900 relative overflow-hidden">
      {/* Background image & gradient overlay */}
      <div className="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=2070')] bg-cover bg-center opacity-20"></div>
      <div className="absolute inset-0 bg-gradient-to-br from-indigo-900/90 via-slate-900/95 to-purple-900/90"></div>
      
      {/* Animated Orbs */}
      <div className="absolute top-20 left-20 w-72 h-72 bg-indigo-500 rounded-full mix-blend-multiply filter blur-[128px] opacity-40 animate-float"></div>
      <div className="absolute bottom-20 right-20 w-72 h-72 bg-purple-500 rounded-full mix-blend-multiply filter blur-[128px] opacity-40 animate-float-delayed"></div>

      <div className="relative z-10 w-full max-w-md px-6 animate-fade-in-up">
        <Link to="/" className="inline-flex items-center gap-2 text-indigo-300 hover:text-white mb-8 transition-colors font-medium">
          <ArrowLeft className="w-4 h-4" /> Back to Home
        </Link>
        
        <div className="glass-dark p-10 rounded-3xl">
          <div className="flex justify-center mb-8">
            <div className="w-20 h-20 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-2xl flex items-center justify-center shadow-lg shadow-indigo-500/30 transform -rotate-6 hover:rotate-0 transition-transform duration-300">
              <Book className="w-10 h-10 text-white" />
            </div>
          </div>
          
          <h2 className="text-3xl font-bold text-center text-white mb-2 tracking-tight">Welcome Back</h2>
          <p className="text-center text-indigo-200/80 mb-10 font-medium">Select your role to access the portal</p>
          
          <div className="space-y-4">
            <button onClick={() => handleLogin('student')} className="group w-full flex items-center justify-between bg-white/5 hover:bg-white/10 border border-white/10 hover:border-indigo-400/50 p-4 rounded-xl text-white transition-all duration-300 hover:shadow-lg hover:shadow-indigo-500/20">
              <div className="flex items-center gap-4">
                <div className="p-2.5 bg-blue-500/20 text-blue-400 rounded-lg group-hover:bg-blue-500 group-hover:text-white transition-colors">
                  <GraduationCap className="w-5 h-5" />
                </div>
                <span className="font-semibold text-lg">Student</span>
              </div>
              <span className="text-xs font-bold px-2 py-1 bg-white/10 rounded text-white/50 group-hover:text-white/90">DEMO</span>
            </button>
            
            <button onClick={() => handleLogin('faculty')} className="group w-full flex items-center justify-between bg-white/5 hover:bg-white/10 border border-white/10 hover:border-purple-400/50 p-4 rounded-xl text-white transition-all duration-300 hover:shadow-lg hover:shadow-purple-500/20">
              <div className="flex items-center gap-4">
                <div className="p-2.5 bg-purple-500/20 text-purple-400 rounded-lg group-hover:bg-purple-500 group-hover:text-white transition-colors">
                  <Briefcase className="w-5 h-5" />
                </div>
                <span className="font-semibold text-lg">Faculty</span>
              </div>
              <span className="text-xs font-bold px-2 py-1 bg-white/10 rounded text-white/50 group-hover:text-white/90">DEMO</span>
            </button>

            <button onClick={() => handleLogin('admin')} className="group w-full flex items-center justify-between bg-white/5 hover:bg-white/10 border border-white/10 hover:border-emerald-400/50 p-4 rounded-xl text-white transition-all duration-300 hover:shadow-lg hover:shadow-emerald-500/20">
              <div className="flex items-center gap-4">
                <div className="p-2.5 bg-emerald-500/20 text-emerald-400 rounded-lg group-hover:bg-emerald-500 group-hover:text-white transition-colors">
                  <ShieldCheck className="w-5 h-5" />
                </div>
                <span className="font-semibold text-lg">Admin</span>
              </div>
              <span className="text-xs font-bold px-2 py-1 bg-white/10 rounded text-white/50 group-hover:text-white/90">DEMO</span>
            </button>
          </div>
          
          <div className="mt-8 pt-6 border-t border-white/10 text-center">
            <p className="text-xs text-white/40">Secured for Ganpat University Hackathon</p>
          </div>
        </div>
      </div>
    </div>
  );
}
"""

# 4. Layout (Premium Sidebar & Header)
files["src/components/layout/Layout.tsx"] = """import { Outlet, Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import { LogOut, Book, LayoutDashboard, Settings, User as UserIcon, FileText, MessageSquare, Bell, Calendar, BarChart2, Search } from 'lucide-react';
import { cn } from '../../lib/utils';

export default function Layout() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  const navItems = [
    { name: 'Dashboard', path: '/dashboard', icon: LayoutDashboard },
    { name: 'Courses', path: '/courses', icon: Book },
    { name: 'Assignments', path: '/assignments', icon: FileText },
    { name: 'Study Materials', path: '/materials', icon: FileText },
    { name: 'Announcements', path: '/announcements', icon: Bell },
    { name: 'Discussions', path: '/discussions', icon: MessageSquare },
    { name: 'Calendar', path: '/calendar', icon: Calendar },
  ];
  
  if (user?.role === 'admin') {
    navItems.push({ name: 'Analytics', path: '/analytics', icon: BarChart2 });
  }

  return (
    <div className="flex h-screen bg-slate-50 overflow-hidden">
      {/* Sidebar */}
      <aside className="w-72 bg-white border-r border-slate-200 flex flex-col shadow-sm relative z-20">
        <div className="p-6">
          <Link to="/" className="text-2xl font-black text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 flex items-center gap-3">
             <div className="p-1.5 bg-indigo-600 rounded-lg text-white shadow-md">
               <Book className="w-5 h-5" />
             </div>
             EduConnect
          </Link>
          <div className="mt-6 flex items-center gap-3 p-3 bg-slate-50 border border-slate-100 rounded-xl">
            <div className="w-10 h-10 rounded-full bg-gradient-to-br from-indigo-100 to-purple-100 border-2 border-white shadow-sm flex items-center justify-center text-indigo-700 font-bold">
               {user?.name.charAt(0)}
            </div>
            <div>
              <p className="font-semibold text-slate-800 text-sm leading-tight">{user?.name}</p>
              <p className="text-xs text-indigo-600 font-medium uppercase tracking-wider">{user?.role} Mode</p>
            </div>
          </div>
        </div>
        
        <nav className="flex-1 overflow-y-auto px-4 py-2 space-y-1.5">
          <p className="px-3 text-xs font-bold text-slate-400 uppercase tracking-wider mb-2 mt-4">Menu</p>
          {navItems.map((item) => {
            const isActive = location.pathname === item.path;
            const Icon = item.icon;
            return (
              <Link 
                key={item.name}
                to={item.path} 
                className={cn(
                  "flex items-center gap-3 px-3 py-2.5 rounded-xl font-medium transition-all duration-200 group",
                  isActive 
                    ? "bg-indigo-50 text-indigo-700" 
                    : "text-slate-600 hover:bg-slate-50 hover:text-slate-900"
                )}
              >
                <Icon className={cn("w-5 h-5 transition-colors", isActive ? "text-indigo-600" : "text-slate-400 group-hover:text-slate-600")} /> 
                {item.name}
              </Link>
            )
          })}
        </nav>

        <div className="p-4 border-t border-slate-100">
          <Link to="/profile" className="flex items-center gap-3 px-3 py-2.5 text-slate-600 font-medium rounded-xl hover:bg-slate-50 transition-colors">
            <UserIcon className="w-5 h-5 text-slate-400" /> Profile
          </Link>
          <Link to="/settings" className="flex items-center gap-3 px-3 py-2.5 text-slate-600 font-medium rounded-xl hover:bg-slate-50 transition-colors">
            <Settings className="w-5 h-5 text-slate-400" /> Settings
          </Link>
          <button onClick={handleLogout} className="w-full mt-2 flex items-center gap-3 px-3 py-2.5 text-rose-600 font-medium rounded-xl hover:bg-rose-50 transition-colors">
            <LogOut className="w-5 h-5 text-rose-500" /> Logout
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col h-screen overflow-hidden">
        {/* Header */}
        <header className="bg-white/80 backdrop-blur-md border-b border-slate-200 px-8 py-4 flex justify-between items-center z-10">
           <div className="relative w-96 hidden md:block">
             <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
             <input 
               type="text" 
               placeholder="Search courses, assignments..." 
               className="w-full bg-slate-50 border border-slate-200 rounded-full pl-10 pr-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500 transition-all"
             />
           </div>
           <div className="flex items-center gap-4 ml-auto">
             <button className="relative p-2 text-slate-500 hover:text-indigo-600 rounded-full hover:bg-indigo-50 transition-colors">
               <Bell className="w-5 h-5" />
               <span className="absolute top-1.5 right-1.5 w-2 h-2 bg-rose-500 rounded-full border-2 border-white"></span>
             </button>
           </div>
        </header>
        
        {/* Page Content */}
        <div className="flex-1 overflow-y-auto p-8 animate-fade-in-up">
          <Outlet />
        </div>
      </main>
    </div>
  );
}
"""

# 5. Student Dashboard (Premium Cards & Gradients)
files["src/pages/dashboard/StudentDashboard.tsx"] = """import { BookOpen, FileText, Clock, TrendingUp, ChevronRight, PlayCircle } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';

export default function StudentDashboard() {
  const { user } = useAuth();
  
  return (
    <div className="space-y-8 max-w-7xl mx-auto pb-12">
      {/* Welcome Banner */}
      <div className="bg-gradient-to-r from-indigo-900 to-purple-900 rounded-3xl p-8 text-white shadow-xl shadow-indigo-900/20 relative overflow-hidden">
        <div className="absolute top-0 right-0 w-64 h-64 bg-white opacity-5 rounded-full blur-3xl translate-x-1/2 -translate-y-1/2"></div>
        <div className="relative z-10 flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
          <div>
            <h1 className="text-3xl font-extrabold mb-2">Welcome back, {user?.name}! 👋</h1>
            <p className="text-indigo-200 text-lg max-w-xl">You have 2 pending assignments due this week. Keep up the great work, your overall progress is up by 4%!</p>
          </div>
          <button className="bg-white text-indigo-900 px-6 py-3 rounded-xl font-bold hover:bg-indigo-50 transition-colors shadow-lg flex items-center gap-2">
            View Assignments <ChevronRight className="w-4 h-4" />
          </button>
        </div>
      </div>
      
      {/* Stats Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 hover:shadow-md hover:-translate-y-1 transition-all duration-300 group">
          <div className="flex items-center justify-between mb-4">
            <div className="p-3 bg-blue-50 text-blue-600 rounded-xl group-hover:bg-blue-600 group-hover:text-white transition-colors"><BookOpen className="w-6 h-6" /></div>
            <span className="text-xs font-bold text-emerald-600 bg-emerald-50 px-2 py-1 rounded-md">+1 New</span>
          </div>
          <p className="text-sm text-slate-500 font-medium">Enrolled Courses</p>
          <p className="text-3xl font-bold text-slate-800 mt-1">4</p>
        </div>
        
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 hover:shadow-md hover:-translate-y-1 transition-all duration-300 group">
          <div className="flex items-center justify-between mb-4">
            <div className="p-3 bg-amber-50 text-amber-600 rounded-xl group-hover:bg-amber-500 group-hover:text-white transition-colors"><FileText className="w-6 h-6" /></div>
            <span className="text-xs font-bold text-amber-600 bg-amber-50 px-2 py-1 rounded-md">Action needed</span>
          </div>
          <p className="text-sm text-slate-500 font-medium">Pending Tasks</p>
          <p className="text-3xl font-bold text-slate-800 mt-1">2</p>
        </div>
        
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 hover:shadow-md hover:-translate-y-1 transition-all duration-300 group">
          <div className="flex items-center justify-between mb-4">
            <div className="p-3 bg-rose-50 text-rose-600 rounded-xl group-hover:bg-rose-500 group-hover:text-white transition-colors"><Clock className="w-6 h-6" /></div>
          </div>
          <p className="text-sm text-slate-500 font-medium">Upcoming Deadlines</p>
          <p className="text-3xl font-bold text-slate-800 mt-1">1</p>
        </div>
        
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 hover:shadow-md hover:-translate-y-1 transition-all duration-300 group relative overflow-hidden">
          <div className="absolute bottom-0 right-0 w-24 h-24 bg-emerald-500/10 rounded-tl-full"></div>
          <div className="flex items-center justify-between mb-4">
            <div className="p-3 bg-emerald-50 text-emerald-600 rounded-xl group-hover:bg-emerald-500 group-hover:text-white transition-colors"><TrendingUp className="w-6 h-6" /></div>
          </div>
          <p className="text-sm text-slate-500 font-medium">Overall Progress</p>
          <div className="flex items-end gap-2 mt-1">
             <p className="text-3xl font-bold text-slate-800">85%</p>
             <span className="text-emerald-500 text-sm font-semibold mb-1">+4%</span>
          </div>
        </div>
      </div>
      
      {/* Sections */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="bg-white p-7 rounded-3xl shadow-sm border border-slate-100">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-xl font-bold text-slate-900">Recent Announcements</h2>
            <button className="text-sm font-semibold text-indigo-600 hover:text-indigo-800">View All</button>
          </div>
          <div className="space-y-4">
            <div className="p-5 border border-slate-100 rounded-2xl bg-gradient-to-r from-slate-50 to-white hover:border-indigo-100 transition-colors cursor-pointer group">
              <div className="flex justify-between items-start">
                <h3 className="font-bold text-slate-800 group-hover:text-indigo-700 transition-colors">Hackathon Schedule Updated</h3>
                <span className="text-xs font-medium text-slate-400 bg-white px-2 py-1 rounded border border-slate-100">2h ago</span>
              </div>
              <p className="text-sm text-slate-600 mt-2 leading-relaxed">Please review the updated submission guidelines for Phase 1. The deadline has been extended by 2 hours.</p>
            </div>
            <div className="p-5 border border-slate-100 rounded-2xl bg-gradient-to-r from-slate-50 to-white hover:border-indigo-100 transition-colors cursor-pointer group">
              <div className="flex justify-between items-start">
                <h3 className="font-bold text-slate-800 group-hover:text-indigo-700 transition-colors">Welcome to EduConnect</h3>
                <span className="text-xs font-medium text-slate-400 bg-white px-2 py-1 rounded border border-slate-100">1d ago</span>
              </div>
              <p className="text-sm text-slate-600 mt-2 leading-relaxed">Welcome to the new AI powered portal. We hope you enjoy the new seamless experience!</p>
            </div>
          </div>
        </div>
        
        <div className="bg-white p-7 rounded-3xl shadow-sm border border-slate-100">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-xl font-bold text-slate-900">Latest Study Materials</h2>
            <button className="text-sm font-semibold text-indigo-600 hover:text-indigo-800">Browse Library</button>
          </div>
          <div className="space-y-4">
             <div className="p-4 border border-slate-100 rounded-2xl flex items-center gap-4 hover:bg-slate-50 transition-colors cursor-pointer group">
                <div className="w-12 h-12 bg-rose-50 text-rose-500 rounded-xl flex items-center justify-center group-hover:bg-rose-500 group-hover:text-white transition-colors">
                  <PlayCircle className="w-6 h-6" />
                </div>
                <div className="flex-1">
                   <h3 className="font-bold text-slate-800 group-hover:text-indigo-700 transition-colors">React Advanced Patterns</h3>
                   <p className="text-xs text-slate-500 mt-0.5">CS401 • Video Lecture • 45m</p>
                </div>
                <button className="p-2 text-slate-400 hover:text-indigo-600 transition-colors"><ChevronRight className="w-5 h-5" /></button>
             </div>
             
             <div className="p-4 border border-slate-100 rounded-2xl flex items-center gap-4 hover:bg-slate-50 transition-colors cursor-pointer group">
                <div className="w-12 h-12 bg-blue-50 text-blue-500 rounded-xl flex items-center justify-center group-hover:bg-blue-500 group-hover:text-white transition-colors">
                  <FileText className="w-6 h-6" />
                </div>
                <div className="flex-1">
                   <h3 className="font-bold text-slate-800 group-hover:text-indigo-700 transition-colors">Database Normalization PDF</h3>
                   <p className="text-xs text-slate-500 mt-0.5">CS302 • PDF Document • 2.4MB</p>
                </div>
                <button className="p-2 text-slate-400 hover:text-indigo-600 transition-colors"><ChevronRight className="w-5 h-5" /></button>
             </div>
          </div>
        </div>
      </div>
    </div>
  );
}
"""

for path, content in files.items():
    full_path = os.path.join(base_dir, path)
    with open(full_path, "w", encoding='utf-8') as f:
        f.write(content)

print("CSS and Premium UI applied successfully!")
