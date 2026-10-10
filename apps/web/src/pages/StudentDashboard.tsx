import { useState, useEffect } from 'react';
import { Book, Clock, CheckCircle, FileText } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';

import axios from 'axios';

export default function StudentDashboard() {
  const { user } = useAuth();
  const [stats, setStats] = useState<any>({ assignments_total: 0, assignments_submitted: 0, assignments_pending: 0, materials_total: 0, risk_level: '', risk_reason: '', completion_rate: 0, grade_percentage: 0, graded_count: 0 });

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const token = localStorage.getItem('token');
        const res = await axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/analytics/dashboard`, { headers: { Authorization: `Bearer ${token}` } });
        setStats(res.data);
      } catch (err) {}
    };
    fetchStats();
  }, []);

  return (
    <div className="space-y-6 animate-fade-in-up">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-8">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-900">Welcome back, {user?.name?.split(' ')[0] || 'Student'}!</h1>
          <p className="text-slate-500 mt-1 font-medium text-sm flex items-center gap-2">
            <span className="bg-indigo-50 text-indigo-700 px-2.5 py-1 rounded-md uppercase tracking-wider text-xs font-bold">{user?.course?.replace('_', ' ')}</span>
            <span className="bg-purple-50 text-purple-700 px-2.5 py-1 rounded-md uppercase tracking-wider text-xs font-bold">Sem {user?.semester}</span>
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="w-14 h-14 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center"><Book className="w-7 h-7" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase tracking-wider">Total Assignments</p><h2 className="text-3xl font-black text-slate-900">{stats.assignments_total}</h2></div>
        </div>
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="w-14 h-14 bg-amber-50 text-amber-600 rounded-2xl flex items-center justify-center"><Clock className="w-7 h-7" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase tracking-wider">Pending Tasks</p><h2 className="text-3xl font-black text-slate-900">{stats.assignments_pending}</h2></div>
        </div>
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="w-14 h-14 bg-emerald-50 text-emerald-600 rounded-2xl flex items-center justify-center"><CheckCircle className="w-7 h-7" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase tracking-wider">Submitted</p><h2 className="text-3xl font-black text-slate-900">{stats.assignments_submitted}</h2></div>
        </div>
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="w-14 h-14 bg-purple-50 text-purple-600 rounded-2xl flex items-center justify-center"><FileText className="w-7 h-7" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase tracking-wider">Study Materials</p><h2 className="text-3xl font-black text-slate-900">{stats.materials_total}</h2></div>
        </div>
      </div>
      
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-6">
         <div className="bg-indigo-600 rounded-3xl p-8 text-white shadow-md relative overflow-hidden flex flex-col justify-center">
            <div className="absolute right-0 bottom-0 opacity-10"><Book className="w-48 h-48 transform translate-x-1/4 translate-y-1/4" /></div>
            <h2 className="text-2xl font-bold mb-2 relative z-10">EduConnect AI Assistant</h2>
            <p className="text-indigo-100 mb-6 relative z-10 max-w-sm">Got a doubt? Ask our smart AI assistant for help with your semester topics.</p>
            <button className="bg-white text-indigo-600 px-6 py-3 rounded-xl font-bold w-fit shadow-lg hover:shadow-xl transition-all relative z-10">Try it now (Bottom Right)</button>
         </div>
                  <div className="bg-white rounded-3xl p-8 shadow-sm border border-slate-100 flex flex-col justify-center">
            <h3 className="text-lg font-bold text-slate-900 mb-6 flex items-center gap-2">
              <div className={`w-3 h-3 rounded-full ${stats.risk_level === 'High' ? 'bg-red-500 animate-pulse' : stats.risk_level === 'Medium' ? 'bg-amber-500' : stats.risk_level === 'Low' ? 'bg-emerald-500' : 'bg-slate-300'}`}></div>
              Academic Progress & Risk Indicator
            </h3>
            
            <div className="mb-6">
               <div className="flex justify-between items-end mb-2">
                  <span className="font-bold text-slate-700">Assignment Completion</span>
                  <span className="text-xl font-black text-indigo-600">{stats.completion_rate?.toFixed(0) || 0}%</span>
               </div>
               <div className="w-full bg-slate-100 rounded-full h-3 mb-1 overflow-hidden">
                  <div className="bg-indigo-600 h-3 rounded-full transition-all duration-1000" style={{ width: `${Math.min(100, stats.completion_rate || 0)}%` }}></div>
               </div>
               <p className="text-xs text-slate-500 font-medium">{stats.assignments_submitted} of {stats.assignments_total} submitted</p>
            </div>

            <div className={`p-4 rounded-2xl border ${stats.risk_level === 'High' ? 'bg-red-50 border-red-100' : stats.risk_level === 'Medium' ? 'bg-amber-50 border-amber-100' : stats.risk_level === 'Low' ? 'bg-emerald-50 border-emerald-100' : 'bg-slate-50 border-slate-100'}`}>
               <div className="flex justify-between items-center mb-2">
                  <p className={`font-bold text-sm uppercase tracking-wider ${stats.risk_level === 'High' ? 'text-red-700' : stats.risk_level === 'Medium' ? 'text-amber-700' : stats.risk_level === 'Low' ? 'text-emerald-700' : 'text-slate-600'}`}>
                    Risk Level: {stats.risk_level || 'Calculating...'}
                  </p>
                  {stats.graded_count > 0 && <span className="bg-white px-2 py-1 rounded-md text-xs font-bold shadow-sm">Avg Grade: {stats.grade_percentage?.toFixed(0)}%</span>}
               </div>
               <p className={`text-sm ${stats.risk_level === 'High' ? 'text-red-600' : stats.risk_level === 'Medium' ? 'text-amber-600' : stats.risk_level === 'Low' ? 'text-emerald-600' : 'text-slate-500'}`}>
                  {stats.risk_reason || 'Loading data...'}
               </p>
            </div>
         </div>
      </div>
    </div>
  );
}
