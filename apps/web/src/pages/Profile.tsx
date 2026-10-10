import { User, Mail, GraduationCap, ShieldCheck, Briefcase, BookOpen, Clock, Calendar } from 'lucide-react';
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
