import { useState, useEffect } from 'react';
import { Book, CheckCircle, AlertCircle, Sparkles, Target, AlertTriangle } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import axios from 'axios';
import { Link } from 'react-router-dom';

export default function StudentDashboard() {
  const { user } = useAuth();
  const [recommendations, setRecommendations] = useState<any[]>([]);
  const [stats, setStats] = useState({ pending: 0, completed: 0, overdue: 0 });

  useEffect(() => {
    const fetchStats = async () => {
      try {
         const token = localStorage.getItem('token');
         const res = await axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/analytics/dashboard`, { headers: { Authorization: `Bearer ${token}` } });
         setStats(res.data);
         
         const recRes = await axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/analytics/student-recommendations`, { headers: { Authorization: `Bearer ${token}` } });
         setRecommendations(recRes.data);
      } catch (err) {}
    };
    fetchStats();
  }, []);

  return (
    <div className="space-y-6 animate-fade-in-up pb-10">
      <div className="mb-8 flex justify-between items-end">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-900">Student Dashboard</h1>
          <p className="text-slate-500 mt-1 font-medium">Welcome back, {user?.name}</p>
        </div>
        <Link to="/assignments" className="bg-indigo-600 hover:bg-indigo-700 text-white px-5 py-2.5 rounded-xl font-bold transition">View Assignments</Link>
      </div>

      {recommendations.length > 0 && (
          <div className="bg-indigo-50/50 border border-indigo-100 rounded-2xl p-6 mb-8 animate-fade-in-up shadow-sm">
            <h2 className="text-xl font-bold text-slate-900 mb-4 flex items-center gap-2">
              <Sparkles className="w-5 h-5 text-indigo-500" />
              AI Learning Recommendations
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {recommendations.map((rec, idx) => (
                <div key={idx} className={`bg-white p-5 rounded-xl border shadow-sm ${rec.type === 'alert' ? 'border-red-100' : 'border-indigo-100'}`}>
                  <h3 className={`font-semibold mb-2 flex items-center gap-2 ${rec.type === 'alert' ? 'text-red-700' : 'text-indigo-700'}`}>
                    {rec.type === 'alert' ? <AlertTriangle className="w-4 h-4" /> : <Target className="w-4 h-4" />}
                    {rec.title}
                  </h3>
                  <p className="text-slate-600 text-sm">{rec.message}</p>
                </div>
              ))}
            </div>
          </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4 relative overflow-hidden">
          <div className="absolute top-0 right-0 w-24 h-24 bg-blue-50 rounded-bl-full -mr-8 -mt-8"></div>
          <div className="w-14 h-14 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center relative z-10"><Book className="w-7 h-7" /></div>
          <div className="relative z-10"><p className="text-sm font-bold text-slate-500 uppercase tracking-wider">Pending</p><h2 className="text-3xl font-black text-slate-900">{stats.pending}</h2></div>
        </div>
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4 relative overflow-hidden">
          <div className="absolute top-0 right-0 w-24 h-24 bg-emerald-50 rounded-bl-full -mr-8 -mt-8"></div>
          <div className="w-14 h-14 bg-emerald-50 text-emerald-600 rounded-2xl flex items-center justify-center relative z-10"><CheckCircle className="w-7 h-7" /></div>
          <div className="relative z-10"><p className="text-sm font-bold text-slate-500 uppercase tracking-wider">Completed</p><h2 className="text-3xl font-black text-slate-900">{stats.completed}</h2></div>
        </div>
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4 relative overflow-hidden">
          <div className="absolute top-0 right-0 w-24 h-24 bg-rose-50 rounded-bl-full -mr-8 -mt-8"></div>
          <div className="w-14 h-14 bg-rose-50 text-rose-600 rounded-2xl flex items-center justify-center relative z-10"><AlertCircle className="w-7 h-7" /></div>
          <div className="relative z-10"><p className="text-sm font-bold text-slate-500 uppercase tracking-wider">Overdue</p><h2 className="text-3xl font-black text-slate-900">{stats.overdue}</h2></div>
        </div>
      </div>
    </div>
  );
}
