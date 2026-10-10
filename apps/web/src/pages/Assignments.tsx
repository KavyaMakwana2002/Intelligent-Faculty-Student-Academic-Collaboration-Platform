import { useState, useEffect } from 'react';
import { Clock, CheckCircle, AlertCircle, Plus, FileText } from 'lucide-react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import axios from 'axios';

type FilterType = 'All' | 'Pending' | 'Submitted' | 'Overdue';

export default function Assignments() {
  const { user } = useAuth();
  const [assignments, setAssignments] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeFilter, setActiveFilter] = useState<FilterType>('All');

  useEffect(() => {
    const fetchAssignments = async () => {
      try {
        const token = localStorage.getItem('token');
        const res = await axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/assignments`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        
        // If student, we need to know which ones they submitted to calculate status correctly.
        // For hackathon sake, we'll fetch submissions to map status
        let assignmentsData = res.data;
        if (user?.role === 'student') {
           const subPromises = assignmentsData.map((a: any) => 
               axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/assignments/${a.id}/submission`, {
                   headers: { Authorization: `Bearer ${token}` }
               }).catch(() => ({ data: null }))
           );
           const subs = await Promise.all(subPromises);
           
           assignmentsData = assignmentsData.map((a: any, index: number) => {
               const sub = subs[index].data;
               let status = 'Pending';
               if (sub) {
                  status = 'Submitted';
               } else if (new Date(a.due_date) < new Date()) {
                  status = 'Overdue';
               }
               return { ...a, derived_status: status };
           });
        }
        
        setAssignments(assignmentsData);
      } catch (err) {
        console.error("Error fetching assignments:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchAssignments();
  }, [user]);

  const filteredAssignments = assignments.filter(item => {
    if (activeFilter === 'All') return true;
    if (user?.role === 'student') {
        return item.derived_status === activeFilter;
    }
    return true; // Faculty doesn't filter by student status easily in this view
  });

  return (
    <div className="space-y-6 animate-fade-in-up">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-8">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-900">Assignments</h1>
          {user?.role === 'student' && (
             <p className="text-slate-500 mt-1 font-medium text-sm flex items-center gap-2">
               <span className="bg-indigo-50 text-indigo-700 px-2.5 py-1 rounded-md uppercase tracking-wider text-xs font-bold">{user.course?.replace('_', ' ')}</span>
               <span className="bg-purple-50 text-purple-700 px-2.5 py-1 rounded-md uppercase tracking-wider text-xs font-bold">Sem {user.semester}</span>
             </p>
          )}
        </div>
        
        {user?.role === 'faculty' && (
          <Link to="/assignments/create" className="bg-indigo-600 text-white px-5 py-2.5 rounded-xl font-bold hover:bg-indigo-700 transition shadow-md flex items-center gap-2">
            <Plus className="w-5 h-5" /> Create Assignment
          </Link>
        )}
      </div>

      {user?.role === 'student' && (
        <div className="flex overflow-x-auto gap-2 pb-2 hide-scrollbar mb-6">
          {(['All', 'Pending', 'Submitted', 'Overdue'] as FilterType[]).map(filter => (
            <button
              key={filter}
              onClick={() => setActiveFilter(filter)}
              className={`px-5 py-2 rounded-xl font-bold text-sm whitespace-nowrap transition-all ${activeFilter === filter ? 'bg-slate-800 text-white shadow-md' : 'bg-white text-slate-600 hover:bg-slate-100 border border-slate-200'}`}
            >
              {filter} {filter !== 'All' && `(${assignments.filter(a => a.derived_status === filter).length})`}
            </button>
          ))}
        </div>
      )}

      {loading ? (
         <div className="flex justify-center p-20"><span className="w-10 h-10 border-4 border-indigo-200 border-t-indigo-600 rounded-full animate-spin"></span></div>
      ) : filteredAssignments.length === 0 ? (
         <div className="bg-white rounded-3xl p-16 text-center border border-slate-100 shadow-sm flex flex-col items-center">
            <div className="w-24 h-24 bg-slate-50 rounded-full flex items-center justify-center mb-6">
              <FileText className="w-10 h-10 text-slate-300" />
            </div>
            <h3 className="text-2xl font-bold text-slate-800 mb-2">No assignments found</h3>
            <p className="text-slate-500 max-w-md mx-auto">
              {activeFilter === 'All' 
                ? "There are no published assignments available for your course and semester yet."
                : `You don't have any ${activeFilter.toLowerCase()} assignments.`}
            </p>
         </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredAssignments.map(item => (
            <Link to={`/assignments/${item.id}`} key={item.id} className="bg-white rounded-3xl p-6 shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 group relative flex flex-col h-full transform hover:-translate-y-1">
              <div className={`absolute top-0 right-0 w-2 h-full rounded-r-3xl ${
                  item.derived_status === 'Pending' ? 'bg-amber-400' : 
                  item.derived_status === 'Submitted' ? 'bg-emerald-500' : 
                  item.derived_status === 'Overdue' ? 'bg-red-500' : 'bg-indigo-500'
              }`}></div>
              
              <div className="flex justify-between items-start mb-4 pr-4">
                 <span className="bg-slate-100 text-slate-600 text-xs px-2.5 py-1 rounded-md font-bold uppercase tracking-wider">
                   {item.course.replace('_', ' ')} S{item.semester}
                 </span>
                 
                 {user?.role === 'student' && (
                   item.derived_status === 'Pending' ? <span className="flex items-center gap-1 text-xs font-bold text-amber-600 bg-amber-50 px-2.5 py-1 rounded-md border border-amber-100"><AlertCircle className="w-3.5 h-3.5" /> Pending</span> :
                   item.derived_status === 'Submitted' ? <span className="flex items-center gap-1 text-xs font-bold text-emerald-600 bg-emerald-50 px-2.5 py-1 rounded-md border border-emerald-100"><CheckCircle className="w-3.5 h-3.5" /> Submitted</span> :
                   <span className="flex items-center gap-1 text-xs font-bold text-red-600 bg-red-50 px-2.5 py-1 rounded-md border border-red-100"><AlertCircle className="w-3.5 h-3.5" /> Overdue</span>
                 )}
              </div>
              
              <h3 className="text-xl font-bold text-slate-900 mb-1 group-hover:text-indigo-600 transition-colors line-clamp-2 pr-4">{item.title}</h3>
              <p className="text-sm text-slate-500 mb-4 font-medium">{item.subject || 'General Assignment'}</p>
              
              <div className="mt-auto pt-6 border-t border-slate-50 flex items-center justify-between text-sm pr-4">
                 <div className={`flex items-center gap-1.5 font-bold ${item.derived_status === 'Overdue' ? 'text-red-500' : 'text-slate-500'}`}>
                   <Clock className="w-4 h-4" /> {new Date(item.due_date).toLocaleDateString()}
                 </div>
                 <div className="font-black text-slate-800 bg-slate-50 px-3 py-1 rounded-lg">{item.marks} pts</div>
              </div>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}
