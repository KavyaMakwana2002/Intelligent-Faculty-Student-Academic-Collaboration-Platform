import { useAuth } from '../../contexts/AuthContext';
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
