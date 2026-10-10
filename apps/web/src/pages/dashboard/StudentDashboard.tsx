import { BookOpen, FileText, Clock, TrendingUp, ChevronRight, PlayCircle } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';

export default function StudentDashboard() {
  const { user } = useAuth();
  
  return (
    <div className="space-y-8 max-w-7xl mx-auto pb-12">
      {/* Welcome Banner */}
      <div className="bg-gradient-to-r from-indigo-900 to-purple-900 rounded-3xl p-8 text-white shadow-xl shadow-indigo-900/20 relative overflow-hidden">
        <div className="absolute top-0 right-0 w-64 h-64 bg-white opacity-5 rounded-full blur-3xl translate-x-1/2 -translate-y-1/2"></div>
        <div className="relative z-10 flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
          <div>
            <h1 className="text-3xl font-extrabold mb-2">Welcome back, {user?.name}! 👋</h1>
            <p className="text-indigo-200 text-lg max-w-xl">You have 2 pending assignments due this week. Keep up the great work, your overall progress is up by 4%!</p>
          </div>
          <button className="bg-white text-indigo-900 px-6 py-3 rounded-xl font-bold hover:bg-indigo-50 transition-colors shadow-lg flex items-center gap-2">
            View Assignments <ChevronRight className="w-4 h-4" />
          </button>
        </div>
      </div>
      
      {/* Stats Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 hover:shadow-md hover:-translate-y-1 transition-all duration-300 group">
          <div className="flex items-center justify-between mb-4">
            <div className="p-3 bg-blue-50 text-blue-600 rounded-xl group-hover:bg-blue-600 group-hover:text-white transition-colors"><BookOpen className="w-6 h-6" /></div>
            <span className="text-xs font-bold text-emerald-600 bg-emerald-50 px-2 py-1 rounded-md">+1 New</span>
          </div>
          <p className="text-sm text-slate-500 font-medium">Enrolled Courses</p>
          <p className="text-3xl font-bold text-slate-800 mt-1">4</p>
        </div>
        
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 hover:shadow-md hover:-translate-y-1 transition-all duration-300 group">
          <div className="flex items-center justify-between mb-4">
            <div className="p-3 bg-amber-50 text-amber-600 rounded-xl group-hover:bg-amber-500 group-hover:text-white transition-colors"><FileText className="w-6 h-6" /></div>
            <span className="text-xs font-bold text-amber-600 bg-amber-50 px-2 py-1 rounded-md">Action needed</span>
          </div>
          <p className="text-sm text-slate-500 font-medium">Pending Tasks</p>
          <p className="text-3xl font-bold text-slate-800 mt-1">2</p>
        </div>
        
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 hover:shadow-md hover:-translate-y-1 transition-all duration-300 group">
          <div className="flex items-center justify-between mb-4">
            <div className="p-3 bg-rose-50 text-rose-600 rounded-xl group-hover:bg-rose-500 group-hover:text-white transition-colors"><Clock className="w-6 h-6" /></div>
          </div>
          <p className="text-sm text-slate-500 font-medium">Upcoming Deadlines</p>
          <p className="text-3xl font-bold text-slate-800 mt-1">1</p>
        </div>
        
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 hover:shadow-md hover:-translate-y-1 transition-all duration-300 group relative overflow-hidden">
          <div className="absolute bottom-0 right-0 w-24 h-24 bg-emerald-500/10 rounded-tl-full"></div>
          <div className="flex items-center justify-between mb-4">
            <div className="p-3 bg-emerald-50 text-emerald-600 rounded-xl group-hover:bg-emerald-500 group-hover:text-white transition-colors"><TrendingUp className="w-6 h-6" /></div>
          </div>
          <p className="text-sm text-slate-500 font-medium">Overall Progress</p>
          <div className="flex items-end gap-2 mt-1">
             <p className="text-3xl font-bold text-slate-800">85%</p>
             <span className="text-emerald-500 text-sm font-semibold mb-1">+4%</span>
          </div>
        </div>
      </div>
      
      {/* Sections */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="bg-white p-7 rounded-3xl shadow-sm border border-slate-100">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-xl font-bold text-slate-900">Recent Announcements</h2>
            <button className="text-sm font-semibold text-indigo-600 hover:text-indigo-800">View All</button>
          </div>
          <div className="space-y-4">
            <div className="p-5 border border-slate-100 rounded-2xl bg-gradient-to-r from-slate-50 to-white hover:border-indigo-100 transition-colors cursor-pointer group">
              <div className="flex justify-between items-start">
                <h3 className="font-bold text-slate-800 group-hover:text-indigo-700 transition-colors">Hackathon Schedule Updated</h3>
                <span className="text-xs font-medium text-slate-400 bg-white px-2 py-1 rounded border border-slate-100">2h ago</span>
              </div>
              <p className="text-sm text-slate-600 mt-2 leading-relaxed">Please review the updated submission guidelines for Phase 1. The deadline has been extended by 2 hours.</p>
            </div>
            <div className="p-5 border border-slate-100 rounded-2xl bg-gradient-to-r from-slate-50 to-white hover:border-indigo-100 transition-colors cursor-pointer group">
              <div className="flex justify-between items-start">
                <h3 className="font-bold text-slate-800 group-hover:text-indigo-700 transition-colors">Welcome to EduConnect</h3>
                <span className="text-xs font-medium text-slate-400 bg-white px-2 py-1 rounded border border-slate-100">1d ago</span>
              </div>
              <p className="text-sm text-slate-600 mt-2 leading-relaxed">Welcome to the new AI powered portal. We hope you enjoy the new seamless experience!</p>
            </div>
          </div>
        </div>
        
        <div className="bg-white p-7 rounded-3xl shadow-sm border border-slate-100">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-xl font-bold text-slate-900">Latest Study Materials</h2>
            <button className="text-sm font-semibold text-indigo-600 hover:text-indigo-800">Browse Library</button>
          </div>
          <div className="space-y-4">
             <div className="p-4 border border-slate-100 rounded-2xl flex items-center gap-4 hover:bg-slate-50 transition-colors cursor-pointer group">
                <div className="w-12 h-12 bg-rose-50 text-rose-500 rounded-xl flex items-center justify-center group-hover:bg-rose-500 group-hover:text-white transition-colors">
                  <PlayCircle className="w-6 h-6" />
                </div>
                <div className="flex-1">
                   <h3 className="font-bold text-slate-800 group-hover:text-indigo-700 transition-colors">React Advanced Patterns</h3>
                   <p className="text-xs text-slate-500 mt-0.5">CS401 • Video Lecture • 45m</p>
                </div>
                <button className="p-2 text-slate-400 hover:text-indigo-600 transition-colors"><ChevronRight className="w-5 h-5" /></button>
             </div>
             
             <div className="p-4 border border-slate-100 rounded-2xl flex items-center gap-4 hover:bg-slate-50 transition-colors cursor-pointer group">
                <div className="w-12 h-12 bg-blue-50 text-blue-500 rounded-xl flex items-center justify-center group-hover:bg-blue-500 group-hover:text-white transition-colors">
                  <FileText className="w-6 h-6" />
                </div>
                <div className="flex-1">
                   <h3 className="font-bold text-slate-800 group-hover:text-indigo-700 transition-colors">Database Normalization PDF</h3>
                   <p className="text-xs text-slate-500 mt-0.5">CS302 • PDF Document • 2.4MB</p>
                </div>
                <button className="p-2 text-slate-400 hover:text-indigo-600 transition-colors"><ChevronRight className="w-5 h-5" /></button>
             </div>
          </div>
        </div>
      </div>
    </div>
  );
}
