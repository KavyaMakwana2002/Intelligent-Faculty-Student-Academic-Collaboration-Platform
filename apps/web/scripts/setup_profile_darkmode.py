import os

frontend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web"

# --- 1. SETTINGS.TSX ---
settings_tsx = """import { useState, useEffect } from 'react';
import { Settings as SettingsIcon, Moon, Sun, Monitor, Shield, Bell, Key, Globe } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';

export default function Settings() {
  const { user } = useAuth();
  
  // Theme state
  const [theme, setTheme] = useState(localStorage.getItem('theme') || 'light');

  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    localStorage.setItem('theme', theme);
  }, [theme]);

  const toggleTheme = (newTheme: string) => {
    setTheme(newTheme);
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-10 animate-fade-in-up">
      <div className="flex items-center gap-4 mb-8">
        <div className="w-14 h-14 bg-indigo-50 text-indigo-600 rounded-2xl flex items-center justify-center shadow-sm border border-indigo-100">
          <SettingsIcon className="w-7 h-7" />
        </div>
        <div>
          <h1 className="text-3xl font-extrabold text-slate-900">Account Settings</h1>
          <p className="text-slate-500 font-medium">Manage your preferences and configurations</p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="md:col-span-1 space-y-2">
          <button className="w-full flex items-center gap-3 p-3 bg-indigo-50 text-indigo-700 rounded-xl font-bold transition">
            <Monitor className="w-5 h-5" /> Appearance
          </button>
          <button className="w-full flex items-center gap-3 p-3 text-slate-600 hover:bg-slate-50 rounded-xl font-medium transition">
            <Bell className="w-5 h-5" /> Notifications
          </button>
          <button className="w-full flex items-center gap-3 p-3 text-slate-600 hover:bg-slate-50 rounded-xl font-medium transition">
            <Key className="w-5 h-5" /> Security
          </button>
          <button className="w-full flex items-center gap-3 p-3 text-slate-600 hover:bg-slate-50 rounded-xl font-medium transition">
            <Globe className="w-5 h-5" /> Language
          </button>
        </div>

        <div className="md:col-span-2 space-y-6">
          <div className="bg-white rounded-3xl p-8 border border-slate-100 shadow-sm">
            <h2 className="text-xl font-bold text-slate-900 mb-6 flex items-center gap-2">
              <Sun className="w-5 h-5 text-amber-500" /> Theme & Appearance
            </h2>
            
            <p className="text-slate-500 mb-6">Choose how the application looks to you. Dark mode is easier on the eyes in low light.</p>
            
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div 
                onClick={() => toggleTheme('light')}
                className={`cursor-pointer border-2 rounded-2xl p-6 flex flex-col items-center justify-center transition-all ${theme === 'light' ? 'border-indigo-500 bg-indigo-50/50' : 'border-slate-200 hover:border-indigo-300'}`}
              >
                <div className="w-16 h-16 bg-white rounded-full flex items-center justify-center shadow-md mb-4">
                  <Sun className="w-8 h-8 text-amber-500" />
                </div>
                <h3 className="font-bold text-slate-900">Light Mode</h3>
                <p className="text-sm text-slate-500 text-center mt-1">Bright and clear for daytime use</p>
              </div>
              
              <div 
                onClick={() => toggleTheme('dark')}
                className={`cursor-pointer border-2 rounded-2xl p-6 flex flex-col items-center justify-center transition-all ${theme === 'dark' ? 'border-indigo-500 bg-indigo-50/50' : 'border-slate-200 hover:border-indigo-300'}`}
              >
                <div className="w-16 h-16 bg-slate-900 rounded-full flex items-center justify-center shadow-md mb-4">
                  <Moon className="w-8 h-8 text-blue-300" />
                </div>
                <h3 className="font-bold text-slate-900">Dark Mode</h3>
                <p className="text-sm text-slate-500 text-center mt-1">Dark backgrounds for low light</p>
              </div>
            </div>
          </div>
          
          <div className="bg-white rounded-3xl p-8 border border-slate-100 shadow-sm">
             <h2 className="text-xl font-bold text-slate-900 mb-4 flex items-center gap-2">
              <Shield className="w-5 h-5 text-emerald-500" /> Account Security
            </h2>
            <div className="flex justify-between items-center py-4 border-b border-slate-100">
               <div>
                 <p className="font-bold text-slate-700">Two-Factor Authentication</p>
                 <p className="text-sm text-slate-500">Add an extra layer of security</p>
               </div>
               <button className="bg-slate-100 hover:bg-slate-200 text-slate-700 px-4 py-2 rounded-lg font-medium transition">Enable</button>
            </div>
            <div className="flex justify-between items-center py-4">
               <div>
                 <p className="font-bold text-slate-700">Change Password</p>
                 <p className="text-sm text-slate-500">Update your account password</p>
               </div>
               <button className="bg-slate-100 hover:bg-slate-200 text-slate-700 px-4 py-2 rounded-lg font-medium transition">Update</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
"""

# --- 2. PROFILE.TSX ---
profile_tsx = """import { User, Mail, GraduationCap, Phone, ShieldCheck, Briefcase, BookOpen, Clock, Calendar } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';

export default function Profile() {
  const { user } = useAuth();
  
  if (!user) return null;

  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-10 animate-fade-in-up">
      <div className="bg-white rounded-3xl overflow-hidden border border-slate-100 shadow-sm">
        {/* Cover Photo */}
        <div className="h-48 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 relative">
           <div className="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1557683316-973673baf926?q=80&w=2029&auto=format&fit=crop')] opacity-30 mix-blend-overlay"></div>
        </div>
        
        {/* Profile Info */}
        <div className="px-8 pb-8 relative">
           <div className="flex justify-between items-end -mt-16 mb-6">
              <div className="w-32 h-32 bg-white p-2 rounded-full shadow-lg relative z-10">
                 <div className="w-full h-full bg-slate-100 rounded-full flex items-center justify-center overflow-hidden">
                    <User className="w-16 h-16 text-slate-400" />
                 </div>
              </div>
              <button className="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-2.5 rounded-xl font-medium transition shadow-md">
                 Edit Profile
              </button>
           </div>
           
           <div>
             <h1 className="text-3xl font-extrabold text-slate-900">{user.name}</h1>
             <p className="text-slate-500 font-medium flex items-center gap-2 mt-1 uppercase tracking-wider text-sm">
               {user.role === 'admin' ? <ShieldCheck className="w-4 h-4 text-emerald-500" /> : user.role === 'faculty' ? <Briefcase className="w-4 h-4 text-purple-500" /> : <GraduationCap className="w-4 h-4 text-blue-500" />}
               {user.role} Account
             </p>
           </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="md:col-span-2 bg-white p-8 rounded-3xl border border-slate-100 shadow-sm">
           <h2 className="text-xl font-bold text-slate-900 mb-6 border-b border-slate-100 pb-4">Personal Information</h2>
           
           <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
             <div>
               <p className="text-sm text-slate-500 mb-1">Full Name</p>
               <p className="font-bold text-slate-800 text-lg">{user.name}</p>
             </div>
             <div>
               <p className="text-sm text-slate-500 mb-1">Email Address</p>
               <p className="font-bold text-slate-800 text-lg flex items-center gap-2">
                 <Mail className="w-4 h-4 text-indigo-500" /> {user.email}
               </p>
             </div>
             
             {user.course && (
               <div>
                 <p className="text-sm text-slate-500 mb-1">Course / Program</p>
                 <p className="font-bold text-slate-800 text-lg flex items-center gap-2">
                   <BookOpen className="w-4 h-4 text-indigo-500" /> {user.course.replace('_', ' ').toUpperCase()}
                 </p>
               </div>
             )}
             
             {user.semester && (
               <div>
                 <p className="text-sm text-slate-500 mb-1">Current Semester</p>
                 <p className="font-bold text-slate-800 text-lg flex items-center gap-2">
                   <Clock className="w-4 h-4 text-indigo-500" /> Semester {user.semester}
                 </p>
               </div>
             )}
             
             {user.role === 'admin' && (
               <div>
                 <p className="text-sm text-slate-500 mb-1">Position / Department</p>
                 <p className="font-bold text-slate-800 text-lg flex items-center gap-2">
                   <ShieldCheck className="w-4 h-4 text-emerald-500" /> System Administrator
                 </p>
               </div>
             )}
             
             <div>
               <p className="text-sm text-slate-500 mb-1">Account Created</p>
               <p className="font-bold text-slate-800 text-lg flex items-center gap-2">
                 <Calendar className="w-4 h-4 text-indigo-500" /> {new Date().toLocaleDateString()}
               </p>
             </div>
           </div>
        </div>

        <div className="md:col-span-1 space-y-6">
           <div className="bg-gradient-to-br from-indigo-600 to-purple-600 p-8 rounded-3xl shadow-md text-white relative overflow-hidden">
              <div className="absolute -right-10 -bottom-10 opacity-20">
                 <GraduationCap className="w-40 h-40" />
              </div>
              <h2 className="text-xl font-bold mb-2 relative z-10">EduConnect AI</h2>
              <p className="text-indigo-100 text-sm mb-6 relative z-10">You are a registered {user.role} member of the Intelligent Faculty-Student Academic Collaboration Platform.</p>
              <div className="bg-white/20 backdrop-blur-sm p-4 rounded-xl relative z-10">
                 <p className="text-xs text-indigo-100 uppercase tracking-wider font-bold mb-1">Status</p>
                 <p className="font-bold text-lg flex items-center gap-2"><div className="w-2.5 h-2.5 bg-emerald-400 rounded-full animate-pulse"></div> Active</p>
              </div>
           </div>
        </div>
      </div>
    </div>
  );
}
"""

# --- 3. INDEX.CSS ---
index_css_addition = """
/* DARK MODE OVERRIDES */
html.dark body {
  background-color: #0f172a;
  color: #f8fafc;
}

html.dark .bg-white {
  background-color: #1e293b;
  border-color: #334155;
  color: #f8fafc;
}

html.dark .text-slate-900, 
html.dark .text-slate-800, 
html.dark .text-slate-700 {
  color: #f8fafc;
}

html.dark .text-slate-600, 
html.dark .text-slate-500 {
  color: #cbd5e1;
}

html.dark .border-slate-100, 
html.dark .border-slate-200 {
  border-color: #334155;
}

html.dark .bg-slate-50, 
html.dark .bg-slate-100 {
  background-color: #0f172a;
}

html.dark .bg-indigo-50 {
  background-color: rgba(79, 70, 229, 0.2);
}

html.dark .bg-white\\/50 {
  background-color: rgba(30, 41, 59, 0.5);
}

html.dark input, 
html.dark select, 
html.dark textarea {
  background-color: #0f172a !important;
  color: #f8fafc !important;
  border-color: #334155 !important;
}

html.dark .glass {
  background-color: rgba(30, 41, 59, 0.7);
  border-color: rgba(255, 255, 255, 0.1);
}
"""

# Write files
with open(os.path.join(frontend_dir, "src/pages/Settings.tsx"), "w", encoding="utf-8") as f: f.write(settings_tsx)
with open(os.path.join(frontend_dir, "src/pages/Profile.tsx"), "w", encoding="utf-8") as f: f.write(profile_tsx)

# Append to index.css if not already there
with open(os.path.join(frontend_dir, "src/index.css"), "r", encoding="utf-8") as f:
    css_content = f.read()

if "DARK MODE OVERRIDES" not in css_content:
    with open(os.path.join(frontend_dir, "src/index.css"), "a", encoding="utf-8") as f:
        f.write(index_css_addition)

print("Profile and Dark Mode implemented!")
