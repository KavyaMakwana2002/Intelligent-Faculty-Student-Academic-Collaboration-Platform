import { useState, useEffect } from 'react';
import { Book, Users, FileText } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import axios from 'axios';

export default function FacultyDashboard() {
  const { user } = useAuth();
  const [stats, setStats] = useState({ assignments_created: 0, materials_uploaded: 0 });

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
      <div className="mb-8">
        <h1 className="text-3xl font-extrabold text-slate-900">Faculty Dashboard</h1>
        <p className="text-slate-500 mt-1 font-medium">Welcome back, Prof. {user?.name}</p>
      </div>
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
