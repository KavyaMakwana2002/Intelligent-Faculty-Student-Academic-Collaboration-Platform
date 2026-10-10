import { useState } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { useNavigate, Link } from 'react-router-dom';
import { Book, GraduationCap, Briefcase, ArrowLeft, AlertCircle } from 'lucide-react';
import axios from 'axios';

type RoleType = 'student' | 'faculty' | null;

export default function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [role, setRole] = useState<RoleType>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const [identifier, setIdentifier] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    
    try {
      const payload = { role, identifier, password };
        
      const res = await axios.post(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/auth/login`, payload);
      
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
              
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-5 mt-6">
              <div>
                <label className="block text-sm font-medium text-indigo-200 mb-1">
                  {role === 'student' && "Enrollment Number"}
                  {role === 'faculty' && "Faculty ID"}
                  
                </label>
                <input 
                  type="text" required 
                  value={identifier}
                  onChange={(e) => setIdentifier(e.target.value)}
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
