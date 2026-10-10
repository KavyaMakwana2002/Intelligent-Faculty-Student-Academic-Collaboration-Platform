import { Outlet, Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import { LogOut, Book, LayoutDashboard, Settings, User as UserIcon, FileText, MessageSquare, Bell, Calendar, BarChart2, Search } from 'lucide-react';
import { cn } from '../../lib/utils';
import AiChatWidget from '../AiChatWidget';

export default function Layout() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  const navItems = [
    { name: 'Dashboard', path: '/dashboard', icon: LayoutDashboard },
    { name: 'Courses', path: '/courses', icon: Book },
    { name: 'Assignments', path: '/assignments', icon: FileText },
    { name: 'Study Materials', path: '/materials', icon: FileText },
    { name: 'Announcements', path: '/announcements', icon: Bell },
    { name: 'Discussions', path: '/discussions', icon: MessageSquare },
    { name: 'Calendar', path: '/calendar', icon: Calendar },
  ];
  
  if (user?.role === 'admin') {
    navItems.push({ name: 'Analytics', path: '/analytics', icon: BarChart2 });
  }

  return (
    <div className="flex h-screen bg-slate-50 overflow-hidden">
      {/* Sidebar */}
      <aside className="w-72 bg-white border-r border-slate-200 flex flex-col shadow-sm relative z-20">
        <div className="p-6">
          <Link to="/" className="text-2xl font-black text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 flex items-center gap-3">
             <div className="p-1.5 bg-indigo-600 rounded-lg text-white shadow-md">
               <Book className="w-5 h-5" />
             </div>
             EduConnect
          </Link>
          <div className="mt-6 flex items-center gap-3 p-3 bg-slate-50 border border-slate-100 rounded-xl">
            <div className="w-10 h-10 rounded-full bg-gradient-to-br from-indigo-100 to-purple-100 border-2 border-white shadow-sm flex items-center justify-center text-indigo-700 font-bold">
               {user?.name?.charAt(0) || 'U'}
            </div>
            <div>
              <p className="font-semibold text-slate-800 text-sm leading-tight">{user?.name}</p>
              <p className="text-xs text-indigo-600 font-medium uppercase tracking-wider">{user?.role} Mode</p>
            </div>
          </div>
        </div>
        
        <nav className="flex-1 overflow-y-auto px-4 py-2 space-y-1.5">
          <p className="px-3 text-xs font-bold text-slate-400 uppercase tracking-wider mb-2 mt-4">Menu</p>
          {navItems.map((item) => {
            const isActive = location.pathname === item.path;
            const Icon = item.icon;
            
            if (item.name === 'Calendar') {
               return (
                 <a 
                   key={item.name}
                   href="/Academic_Calendar.pdf" 
                   target="_blank"
                   rel="noopener noreferrer"
                   className="flex items-center gap-3 px-3 py-2.5 rounded-xl font-medium transition-all duration-200 group text-slate-600 hover:bg-slate-50 hover:text-slate-900"
                 >
                   <Icon className="w-5 h-5 transition-colors text-slate-400 group-hover:text-slate-600" /> 
                   {item.name}
                 </a>
               )
            }
            
            return (
              <Link 
                key={item.name}
                to={item.path} 
                className={cn(
                  "flex items-center gap-3 px-3 py-2.5 rounded-xl font-medium transition-all duration-200 group",
                  isActive 
                    ? "bg-indigo-50 text-indigo-700" 
                    : "text-slate-600 hover:bg-slate-50 hover:text-slate-900"
                )}
              >
                <Icon className={cn("w-5 h-5 transition-colors", isActive ? "text-indigo-600" : "text-slate-400 group-hover:text-slate-600")} /> 
                {item.name}
              </Link>
            )
          })}
        </nav>

        <div className="p-4 border-t border-slate-100">
          <Link to="/profile" className="flex items-center gap-3 px-3 py-2.5 text-slate-600 font-medium rounded-xl hover:bg-slate-50 transition-colors">
            <UserIcon className="w-5 h-5 text-slate-400" /> Profile
          </Link>
          <Link to="/settings" className="flex items-center gap-3 px-3 py-2.5 text-slate-600 font-medium rounded-xl hover:bg-slate-50 transition-colors">
            <Settings className="w-5 h-5 text-slate-400" /> Settings
          </Link>
          <button onClick={handleLogout} className="w-full mt-2 flex items-center gap-3 px-3 py-2.5 text-rose-600 font-medium rounded-xl hover:bg-rose-50 transition-colors">
            <LogOut className="w-5 h-5 text-rose-500" /> Logout
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col h-screen overflow-hidden">
        {/* Header */}
        <header className="bg-white/80 backdrop-blur-md border-b border-slate-200 px-8 py-4 flex justify-between items-center z-10">
           <div className="relative w-96 hidden md:block">
             <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
             <input 
               type="text" 
               placeholder="Search courses, assignments..." 
               className="w-full bg-slate-50 border border-slate-200 rounded-full pl-10 pr-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500 transition-all"
             />
           </div>
           <div className="flex items-center gap-4 ml-auto">
             <button className="relative p-2 text-slate-500 hover:text-indigo-600 rounded-full hover:bg-indigo-50 transition-colors">
               <Bell className="w-5 h-5" />
               <span className="absolute top-1.5 right-1.5 w-2 h-2 bg-rose-500 rounded-full border-2 border-white"></span>
             </button>
           </div>
        </header>
        
        {/* Page Content */}
        <div className="flex-1 overflow-y-auto p-8 animate-fade-in-up">
          <Outlet />
        </div>
      </main>
      <AiChatWidget />
    </div>
  );
}
