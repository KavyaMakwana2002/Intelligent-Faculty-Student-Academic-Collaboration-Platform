import { useState, useEffect } from 'react';
import { Book, Users, FileText, AlertTriangle, Target, User } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import axios from 'axios';

export default function FacultyDashboard() {
  const { user } = useAuth();
  const [insights, setInsights] = useState<any[]>([]);
  const [stats, setStats] = useState({ assignments_created: 0, materials_uploaded: 0 });

  useEffect(() => {
    const fetchStats = async () => {
      try {
         const token = localStorage.getItem('token');
         const res = await axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/analytics/dashboard`, { headers: { Authorization: `Bearer ${token}` } });
         setStats(res.data);
         
         const insightsRes = await axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/analytics/faculty-insights`, { headers: { Authorization: `Bearer ${token}` } });
         setInsights(insightsRes.data);
      } catch (err) {}
    };
    fetchStats();
  }, []);

  return (
    <div className="space-y-6 animate-fade-in-up pb-10">
      <div className="mb-8">
        <h1 className="text-3xl font-extrabold text-slate-900">Faculty Dashboard</h1>
        <p className="text-slate-500 mt-1 font-medium">Welcome back, Prof. {user?.name}</p>
      </div>
      
      {insights.length > 0 && (
          <div className="bg-red-50/50 border border-red-100 rounded-2xl p-6 mb-8 animate-fade-in-up shadow-sm">
            <h2 className="text-xl font-bold text-slate-900 mb-4 flex items-center gap-2">
              <AlertTriangle className="w-5 h-5 text-red-500" />
              Actionable Alerts & Interventions
            </h2>
            <div className="space-y-4">
              {insights.map((insight, idx) => (
                <div key={idx} className="bg-white p-4 rounded-xl border border-red-100 shadow-sm flex items-start gap-4">
                  <div className="p-2 bg-red-100 rounded-lg shrink-0">
                    <User className="w-5 h-5 text-red-600" />
                  </div>
                  <div className="flex-1">
                    <h3 className="font-semibold text-slate-900">{insight.studentName} <span className="text-sm font-normal text-slate-500">({insight.identifier})</span></h3>
                    <p className="text-slate-600 mt-1">{insight.message}</p>
                    <div className="mt-3 inline-flex items-center gap-1.5 px-3 py-1.5 bg-rose-50 text-rose-700 text-sm font-semibold rounded-lg">
                      <Target className="w-4 h-4" />
                      Recommended Action: {insight.action}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="w-14 h-14 bg-indigo-50 text-indigo-600 rounded-2xl flex items-center justify-center"><Book className="w-7 h-7" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase tracking-wider">Assignments</p><h2 className="text-3xl font-black text-slate-900">{stats.assignments_created}</h2></div>
        </div>
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="w-14 h-14 bg-emerald-50 text-emerald-600 rounded-2xl flex items-center justify-center"><FileText className="w-7 h-7" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase tracking-wider">Materials Uploaded</p><h2 className="text-3xl font-black text-slate-900">{stats.materials_uploaded}</h2></div>
        </div>
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="w-14 h-14 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center"><Users className="w-7 h-7" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase tracking-wider">Active Students</p><h2 className="text-3xl font-black text-slate-900">120+</h2></div>
        </div>
      </div>
    </div>
  );
}
