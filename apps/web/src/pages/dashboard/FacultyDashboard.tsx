// import { Users, FileText, CheckCircle, Bell } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';

export default function FacultyDashboard() {
  const { user } = useAuth();
  
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-end">
        <h1 className="text-3xl font-bold text-slate-900">Faculty Portal, {user?.name}</h1>
        <button className="bg-indigo-600 text-white px-4 py-2 rounded-lg font-medium hover:bg-indigo-700">
          + Create Assignment
        </button>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <p className="text-sm text-slate-500 font-medium">Courses Managed</p>
          <p className="text-3xl font-bold text-slate-800 mt-2">2</p>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <p className="text-sm text-slate-500 font-medium">Active Assignments</p>
          <p className="text-3xl font-bold text-slate-800 mt-2">5</p>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <p className="text-sm text-slate-500 font-medium">Pending Reviews</p>
          <p className="text-3xl font-bold text-slate-800 mt-2">18</p>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <p className="text-sm text-slate-500 font-medium">Avg Participation</p>
          <p className="text-3xl font-bold text-slate-800 mt-2">92%</p>
        </div>
      </div>
    </div>
  );
}
