import { Bell, CheckCircle, AlertCircle } from 'lucide-react';
export default function Notifications() {
  return (
    <div className="max-w-3xl mx-auto space-y-6 animate-fade-in-up pb-10">
      <h1 className="text-3xl font-extrabold text-slate-900 mb-8 flex items-center gap-3"><Bell className="w-8 h-8 text-amber-500"/> Notifications</h1>
      <div className="space-y-4">
         <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex gap-4">
            <div className="w-12 h-12 bg-indigo-50 text-indigo-600 rounded-full flex items-center justify-center shrink-0"><CheckCircle className="w-6 h-6"/></div>
            <div>
               <h3 className="font-bold text-slate-900">EduConnect Profile Created!</h3>
               <p className="text-slate-500 text-sm mt-1">Welcome to the Intelligent Academic Collaboration Platform.</p>
               <span className="text-xs font-bold text-slate-400 mt-2 block">Just now</span>
            </div>
         </div>
         <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex gap-4 opacity-75">
            <div className="w-12 h-12 bg-rose-50 text-rose-600 rounded-full flex items-center justify-center shrink-0"><AlertCircle className="w-6 h-6"/></div>
            <div>
               <h3 className="font-bold text-slate-900">System Maintenance Scheduled</h3>
               <p className="text-slate-500 text-sm mt-1">The system will be briefly offline for the hackathon judging review.</p>
               <span className="text-xs font-bold text-slate-400 mt-2 block">2 hours ago</span>
            </div>
         </div>
      </div>
    </div>
  );
}
