import { Bell, Megaphone } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';

export default function Announcements() {
  const { user } = useAuth();
  
  const items = [
    { id: 1, title: "Hackathon Phase 1 Deadline Extended", author: "Dr. Smith (Admin)", date: "2 hours ago", content: "The deadline for Phase 1 UI has been extended by 2 hours. Keep building awesome things!" },
    { id: 2, title: "CS401 Midterm Syllabus", author: "Prof. Johnson", date: "Yesterday", content: "Please note that the midterm will cover chapters 1 through 5. Check study materials for the review sheet." },
  ];

  return (
    <div className="space-y-6 max-w-5xl mx-auto">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-slate-900 flex items-center gap-3">
          <Megaphone className="w-8 h-8 text-indigo-600" /> Announcements
        </h1>
        {['faculty', 'admin'].includes(user?.role || '') && (
          <button className="bg-indigo-600 text-white px-5 py-2.5 rounded-xl font-medium hover:bg-indigo-700 transition shadow-md">
            New Announcement
          </button>
        )}
      </div>

      <div className="space-y-6">
        {items.map(item => (
          <div key={item.id} className="bg-white rounded-3xl p-6 md:p-8 shadow-sm border border-slate-100 hover:shadow-md transition-shadow">
            <div className="flex justify-between items-start mb-4">
              <h2 className="text-xl font-bold text-slate-900">{item.title}</h2>
              <span className="flex items-center gap-1.5 text-sm font-medium text-slate-500 bg-slate-50 px-3 py-1 rounded-full"><Bell className="w-3.5 h-3.5" /> {item.date}</span>
            </div>
            <p className="text-sm font-semibold text-indigo-600 mb-4">{item.author}</p>
            <p className="text-slate-600 leading-relaxed bg-slate-50 p-4 rounded-xl border border-slate-100">{item.content}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
