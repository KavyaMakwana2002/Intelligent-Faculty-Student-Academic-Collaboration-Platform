import { useState, useEffect } from 'react';
import { Users, Shield } from 'lucide-react';
import axios from 'axios';

export default function AdminDashboard() {
  const [users, setUsers] = useState<any[]>([]);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
         const token = localStorage.getItem('token');
         const res = await axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/users`, { headers: { Authorization: `Bearer ${token}` } });
         setUsers(res.data);
      } catch (err) {}
    };
    fetchUsers();
  }, []);

  const students = users.filter(u => u.role === 'student');
  const faculty = users.filter(u => u.role === 'faculty');

  return (
    <div className="space-y-6 animate-fade-in-up">
      <div className="mb-8">
        <h1 className="text-3xl font-extrabold text-slate-900">University Admin Panel</h1>
        <p className="text-slate-500 mt-1 font-medium">Manage all platform users and roles</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="w-14 h-14 bg-indigo-50 text-indigo-600 rounded-2xl flex items-center justify-center"><Users className="w-7 h-7" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase">Total Students</p><h2 className="text-3xl font-black text-slate-900">{students.length}</h2></div>
        </div>
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="w-14 h-14 bg-purple-50 text-purple-600 rounded-2xl flex items-center justify-center"><Shield className="w-7 h-7" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase">Faculty</p><h2 className="text-3xl font-black text-slate-900">{faculty.length}</h2></div>
        </div>
      </div>

      <div className="bg-white rounded-3xl shadow-sm border border-slate-100 p-8">
         <h2 className="text-xl font-bold text-slate-900 mb-6 border-b border-slate-100 pb-4">System Users Directory</h2>
         <div className="overflow-x-auto">
            <table className="w-full text-left">
               <thead>
                  <tr className="text-slate-500 text-sm border-b border-slate-200">
                     <th className="pb-3 font-bold">Name</th>
                     <th className="pb-3 font-bold">Email</th>
                     <th className="pb-3 font-bold">Role</th>
                     <th className="pb-3 font-bold">Identifier (ID)</th>
                     <th className="pb-3 font-bold">Program/Sem</th>
                  </tr>
               </thead>
               <tbody className="divide-y divide-slate-100">
                  {users.map(u => (
                     <tr key={u.id} className="hover:bg-slate-50 transition-colors">
                        <td className="py-4 font-bold text-slate-800">{u.name}</td>
                        <td className="py-4 text-slate-600">{u.email}</td>
                        <td className="py-4"><span className={`px-2 py-1 rounded-md text-xs font-bold uppercase ${u.role === 'admin' ? 'bg-rose-50 text-rose-600' : u.role === 'faculty' ? 'bg-purple-50 text-purple-600' : 'bg-indigo-50 text-indigo-600'}`}>{u.role}</span></td>
                        <td className="py-4 font-mono text-sm text-slate-500">{u.identifier || '-'}</td>
                        <td className="py-4 text-sm font-bold text-slate-600">{u.course ? `${u.course.replace('_',' ').toUpperCase()} (S${u.semester})` : '-'}</td>
                     </tr>
                  ))}
               </tbody>
            </table>
         </div>
      </div>
    </div>
  );
}
