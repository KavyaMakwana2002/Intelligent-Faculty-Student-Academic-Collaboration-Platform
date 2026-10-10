import os

base_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web"
files = {}

# 1. Landing Page Update
files["src/pages/Landing.tsx"] = """import { Link } from 'react-router-dom';
import { Book, ChevronRight, Sparkles, Zap, Shield, Users } from 'lucide-react';

export default function Landing() {
  return (
    <div className="min-h-screen bg-slate-50 overflow-hidden relative">
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
          <Link to="/register" className="bg-slate-900 text-white px-6 py-2.5 rounded-full font-medium hover:bg-slate-800 transition-all shadow-md hover:shadow-xl hover:-translate-y-0.5">Sign Up</Link>
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

# 2. Login Page Update
files["src/pages/auth/Login.tsx"] = """import { useState } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { useNavigate, Link } from 'react-router-dom';
import { Book, GraduationCap, Briefcase, ShieldCheck, ArrowLeft } from 'lucide-react';

type RoleType = 'student' | 'faculty' | 'admin' | null;

export default function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [role, setRole] = useState<RoleType>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    // Simulate API call
    setTimeout(() => {
      login(role!);
      navigate('/dashboard');
    }, 1000);
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
          <button onClick={() => setRole(null)} className="inline-flex items-center gap-2 text-indigo-300 hover:text-white mb-8 transition-colors font-medium">
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
          <p className="text-center text-indigo-200/80 mb-10 font-medium">
            {role === null ? "Select your role to access the portal" : "Enter your credentials below"}
          </p>
          
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
                  className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white placeholder-white/40 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
                  placeholder={role === 'student' ? "e.g. 210001001" : role === 'faculty' ? "e.g. FAC-1042" : "admin@uni.edu"}
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-indigo-200 mb-1">Password</label>
                <input 
                  type="password" 
                  required 
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

# 3. Register Page Update
files["src/pages/auth/Register.tsx"] = """import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Book, GraduationCap, Briefcase, ShieldCheck, ArrowLeft } from 'lucide-react';

type RoleType = 'student' | 'faculty' | 'admin' | null;

export default function Register() {
  const navigate = useNavigate();
  const [role, setRole] = useState<RoleType>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setTimeout(() => {
      // In demo, redirect to login after successful registration
      navigate('/login');
    }, 1500);
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
          <button onClick={() => setRole(null)} className="inline-flex items-center gap-2 text-indigo-300 hover:text-white mb-8 transition-colors font-medium">
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
          <p className="text-center text-indigo-200/80 mb-10 font-medium">
            {role === null ? "Choose your role to get started" : "Please fill out the details below"}
          </p>
          
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
                  <input type="text" required className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder="John Doe" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-indigo-200 mb-1">Email Address</label>
                  <input type="email" required className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder="john@example.com" />
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-indigo-200 mb-1">
                    {role === 'student' && "Enrollment Number"}
                    {role === 'faculty' && "Faculty ID"}
                    {role === 'admin' && "Position (HOD/DEAN)"}
                  </label>
                  <input type="text" required className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder={role === 'admin' ? "e.g. HOD" : "ID/Number"} />
                </div>
                <div>
                  <label className="block text-sm font-medium text-indigo-200 mb-1">Phone Number</label>
                  <input type="tel" required className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder="+91 9876543210" />
                </div>
              </div>

              {role === 'student' && (
                <div>
                  <label className="block text-sm font-medium text-indigo-200 mb-1">Course</label>
                  <select required className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500 [&>option]:text-slate-900">
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
                  <input type="password" required className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder="••••••••" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-indigo-200 mb-1">Confirm Password</label>
                  <input type="password" required className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder="••••••••" />
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

for path, content in files.items():
    full_path = os.path.join(base_dir, path)
    with open(full_path, "w", encoding='utf-8') as f:
        f.write(content)
        
print("Auth flows updated successfully!")
