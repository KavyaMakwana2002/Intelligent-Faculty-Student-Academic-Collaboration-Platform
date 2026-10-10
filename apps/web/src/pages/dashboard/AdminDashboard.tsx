// import { useAuth } from '../../contexts/AuthContext';

export default function AdminDashboard() {
  // const { user } = useAuth();
  
  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold text-slate-900">Admin Console</h1>
      <div className="bg-amber-50 text-amber-800 p-4 rounded-lg border border-amber-200">
        <strong>Demo Mode:</strong> Administrative actions are simulated. Real user management will be connected in Phase 2.
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <h2 className="text-sm text-slate-500 font-medium">Total Users</h2>
          <p className="text-3xl font-bold text-slate-800 mt-2">1,245</p>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <h2 className="text-sm text-slate-500 font-medium">Active Courses</h2>
          <p className="text-3xl font-bold text-slate-800 mt-2">48</p>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <h2 className="text-sm text-slate-500 font-medium">System Health</h2>
          <p className="text-3xl font-bold text-emerald-600 mt-2">100%</p>
        </div>
      </div>
    </div>
  );
}
