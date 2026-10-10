import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Book, GraduationCap, Briefcase, ArrowLeft, AlertCircle, CheckCircle } from 'lucide-react';
import axios from 'axios';

type RoleType = 'student' | 'faculty' | null;

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
  const [semester, setSemester] = useState('');
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
        identifier,
        course: role === 'student' ? course : undefined,
        semester: role === 'student' ? semester : undefined
      };
      
      await axios.post(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/auth/register`, payload);
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
                  <div>
                    <label className="block text-sm font-medium text-indigo-200 mb-1">
                      {role === 'student' && "Enrollment Number"}
                      {role === 'faculty' && "Faculty ID"}
                    </label>
                    <input type="text" required value={identifier} onChange={e=>setIdentifier(e.target.value)} className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder="ID/Number" />
                  </div>
                <div>
                  <label className="block text-sm font-medium text-indigo-200 mb-1">Phone Number</label>
                  <input type="tel" required value={phone} onChange={e=>setPhone(e.target.value)} className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder="+91 9876543210" />
                </div>
              </div>

              {role === 'student' && (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-indigo-200 mb-1">Course (Program)</label>
                    <select required value={course} onChange={e=>setCourse(e.target.value)} className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500 [&>option]:text-slate-900">
                      <option value="">Select a Program</option>
                      <option value="bca_hons">BCA Hons.</option>
                      <option value="bca_hons_aiml">BCA Hons. AI/ML</option>
                      <option value="bca_hons_cyber">BCA Hons. Cyber Security</option>
                      <option value="mca">MCA</option>
                    </select>
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-indigo-200 mb-1">Semester</label>
                    <select required value={semester} onChange={e=>setSemester(e.target.value)} className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-indigo-500 [&>option]:text-slate-900">
                      <option value="">Select Sem</option>
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
