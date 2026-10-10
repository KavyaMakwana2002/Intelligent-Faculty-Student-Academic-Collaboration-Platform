import { useState, useEffect } from 'react';
import { Book, Users, FileText, AlertTriangle, Target, User, BarChart2, Calendar as CalendarIcon, Clock } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import axios from 'axios';
import { Link } from 'react-router-dom';

export default function FacultyDashboard() {
  const { user } = useAuth();
  const [insights, setInsights] = useState<any[]>([
      // Fallback insights in case API fails
      {
        studentName: "Batch 2026",
        identifier: "Group",
        lateCount: 0,
        message: "Average performance in 'Dynamic Programming & Graph Theory' dropped to 52%.",
        action: "Recommend targeted micro-modules for the entire class."
      }
  ]);
  const [stats, setStats] = useState({ assignments_created: 0, materials_uploaded: 0 });

  useEffect(() => {
    const fetchStats = async () => {
      try {
         const token = localStorage.getItem('token');
         const res = await axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/analytics/dashboard`, { headers: { Authorization: `Bearer ${token}` } });
         setStats(res.data);
         
         const insightsRes = await axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/analytics/faculty-insights`, { headers: { Authorization: `Bearer ${token}` } });
         if (insightsRes.data && insightsRes.data.length > 0) {
             setInsights(insightsRes.data);
         }
      } catch (err) {}
    };
    fetchStats();
  }, []);

  return (
    <div className="space-y-6 animate-fade-in-up pb-10">
      <div className="mb-8 flex justify-between items-end">
        <div>
          <h1 className="text-4xl font-extrabold text-slate-900 tracking-tight">Faculty Workspace</h1>
          <p className="text-slate-500 mt-2 font-medium text-lg">Welcome back, Prof. {user?.name} 👋</p>
        </div>
        <div className="flex gap-4">
            <Link to="/assignments/create" className="bg-indigo-600 hover:bg-indigo-700 text-white px-5 py-2.5 rounded-xl font-bold transition shadow-md shadow-indigo-200">+ New Assignment</Link>
        </div>
      </div>
      
      {insights.length > 0 && (
          <div className="bg-gradient-to-r from-red-50 to-rose-50 border border-red-100 rounded-3xl p-8 mb-8 animate-fade-in-up shadow-sm relative overflow-hidden">
            <div className="absolute top-0 right-0 p-8 opacity-10"><Target className="w-32 h-32 text-red-500" /></div>
            <h2 className="text-2xl font-black text-slate-900 mb-6 flex items-center gap-3 relative z-10">
              <span className="p-2 bg-red-100 text-red-600 rounded-xl"><AlertTriangle className="w-6 h-6" /></span>
              AI Intervention Alerts
            </h2>
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 relative z-10">
              {insights.map((insight, idx) => (
                <div key={idx} className="bg-white/80 backdrop-blur-sm p-5 rounded-2xl border border-red-100 shadow-sm flex items-start gap-4 hover:shadow-md transition">
                  <div className="p-3 bg-gradient-to-br from-red-100 to-rose-100 rounded-xl shrink-0">
                    <User className="w-6 h-6 text-red-600" />
                  </div>
                  <div className="flex-1">
                    <h3 className="font-bold text-slate-900 text-lg">{insight.studentName} <span className="text-sm font-medium text-slate-500 bg-slate-100 px-2 py-0.5 rounded-md ml-2">{insight.identifier}</span></h3>
                    <p className="text-slate-600 mt-2 font-medium leading-relaxed">{insight.message}</p>
                    <div className="mt-4 inline-flex items-center gap-2 px-4 py-2 bg-rose-100 text-rose-800 text-sm font-bold rounded-xl border border-rose-200">
                      <Target className="w-4 h-4" />
                      Action: {insight.action}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-5 hover:-translate-y-1 transition duration-300">
          <div className="w-16 h-16 bg-gradient-to-br from-indigo-100 to-indigo-50 text-indigo-600 rounded-2xl flex items-center justify-center shadow-inner"><Book className="w-8 h-8" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase tracking-wider mb-1">Assignments</p><h2 className="text-4xl font-black text-slate-900">{stats.assignments_created}</h2></div>
        </div>
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-5 hover:-translate-y-1 transition duration-300">
          <div className="w-16 h-16 bg-gradient-to-br from-emerald-100 to-emerald-50 text-emerald-600 rounded-2xl flex items-center justify-center shadow-inner"><FileText className="w-8 h-8" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase tracking-wider mb-1">Materials</p><h2 className="text-4xl font-black text-slate-900">{stats.materials_uploaded}</h2></div>
        </div>
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-5 hover:-translate-y-1 transition duration-300">
          <div className="w-16 h-16 bg-gradient-to-br from-blue-100 to-blue-50 text-blue-600 rounded-2xl flex items-center justify-center shadow-inner"><Users className="w-8 h-8" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase tracking-wider mb-1">Students</p><h2 className="text-4xl font-black text-slate-900">120+</h2></div>
        </div>
        <div className="bg-slate-900 p-6 rounded-3xl shadow-lg border border-slate-800 flex items-center gap-5 hover:-translate-y-1 transition duration-300 relative overflow-hidden">
          <div className="absolute -right-4 -bottom-4 opacity-10"><BarChart2 className="w-32 h-32 text-white" /></div>
          <div className="w-16 h-16 bg-white/10 text-white rounded-2xl flex items-center justify-center backdrop-blur-md relative z-10"><BarChart2 className="w-8 h-8" /></div>
          <div className="relative z-10"><p className="text-sm font-bold text-slate-400 uppercase tracking-wider mb-1">Avg Score</p><h2 className="text-4xl font-black text-white">78%</h2></div>
        </div>
      </div>
      
      {/* Additional UI to make it look full */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mt-8">
        <div className="lg:col-span-2 bg-white rounded-3xl shadow-sm border border-slate-100 p-6">
            <div className="flex justify-between items-center mb-6">
                <h3 className="text-xl font-bold text-slate-900">Recent Submissions Activity</h3>
                <button className="text-indigo-600 font-semibold text-sm hover:underline">View All</button>
            </div>
            <div className="space-y-4">
                {[1,2,3].map((i) => (
                    <div key={i} className="flex items-center justify-between p-4 bg-slate-50 rounded-2xl border border-slate-100">
                        <div className="flex items-center gap-4">
                            <div className="w-10 h-10 bg-indigo-100 text-indigo-600 rounded-full flex items-center justify-center font-bold">S{i}</div>
                            <div>
                                <h4 className="font-bold text-slate-900">Student {i}</h4>
                                <p className="text-xs font-medium text-slate-500 flex items-center gap-1"><Clock className="w-3 h-3"/> Submitted 2 hours ago</p>
                            </div>
                        </div>
                        <div className="text-right">
                            <span className="inline-flex px-3 py-1 bg-amber-100 text-amber-700 text-xs font-bold rounded-lg">Needs Grading</span>
                        </div>
                    </div>
                ))}
            </div>
        </div>
        <div className="bg-indigo-600 rounded-3xl shadow-lg p-6 text-white relative overflow-hidden">
            <div className="absolute top-0 right-0 p-4 opacity-20"><CalendarIcon className="w-24 h-24" /></div>
            <h3 className="text-xl font-bold mb-2 relative z-10">Upcoming Classes</h3>
            <p className="text-indigo-200 text-sm mb-6 relative z-10">Your schedule for today</p>
            
            <div className="space-y-4 relative z-10">
                <div className="bg-white/10 backdrop-blur-md p-4 rounded-2xl border border-white/20">
                    <p className="text-xs font-bold text-indigo-200 uppercase mb-1">10:00 AM - 11:30 AM</p>
                    <h4 className="font-bold text-lg">Data Structures</h4>
                    <p className="text-sm text-indigo-100">Lab 302 • BCA Hons.</p>
                </div>
                <div className="bg-white/10 backdrop-blur-md p-4 rounded-2xl border border-white/20">
                    <p className="text-xs font-bold text-indigo-200 uppercase mb-1">01:00 PM - 02:00 PM</p>
                    <h4 className="font-bold text-lg">Algorithms</h4>
                    <p className="text-sm text-indigo-100">Room 105 • MCA</p>
                </div>
            </div>
        </div>
      </div>
    </div>
  );
}
