import os

base_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web"
files = {}

# 1. Registration Page
files["src/pages/auth/Register.tsx"] = """import { Link } from 'react-router-dom';
import { Book, ArrowLeft } from 'lucide-react';

export default function Register() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-900 relative overflow-hidden">
      <div className="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=2070')] bg-cover bg-center opacity-20"></div>
      <div className="absolute inset-0 bg-gradient-to-br from-indigo-900/90 via-slate-900/95 to-purple-900/90"></div>
      
      <div className="absolute top-20 left-20 w-72 h-72 bg-indigo-500 rounded-full mix-blend-multiply filter blur-[128px] opacity-40 animate-float"></div>
      
      <div className="relative z-10 w-full max-w-md px-6 animate-fade-in-up">
        <Link to="/" className="inline-flex items-center gap-2 text-indigo-300 hover:text-white mb-8 transition-colors font-medium">
          <ArrowLeft className="w-4 h-4" /> Back to Home
        </Link>
        
        <div className="glass-dark p-10 rounded-3xl">
          <div className="flex justify-center mb-6">
            <div className="w-16 h-16 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-2xl flex items-center justify-center shadow-lg transform -rotate-6">
              <Book className="w-8 h-8 text-white" />
            </div>
          </div>
          
          <h2 className="text-2xl font-bold text-center text-white mb-2">Create Account</h2>
          <p className="text-center text-indigo-200/80 mb-8 font-medium">Join EduConnect AI today.</p>
          
          <div className="space-y-4">
            <div className="p-4 bg-amber-500/10 border border-amber-500/20 rounded-xl">
               <p className="text-amber-400 text-sm text-center font-medium">
                 Registration is disabled in Demo Mode. Please use the <Link to="/login" className="underline font-bold hover:text-amber-300">Login page</Link> to access the platform.
               </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
"""

# 2. Courses
files["src/pages/Courses.tsx"] = """import { Book, Users, Star, ChevronRight } from 'lucide-react';

export default function Courses() {
  const courses = [
    { id: 1, name: "Advanced Web Development", code: "CS401", students: 120, rating: 4.8, color: "from-blue-500 to-indigo-600" },
    { id: 2, name: "Database Management Systems", code: "CS302", students: 85, rating: 4.6, color: "from-emerald-500 to-teal-600" },
    { id: 3, name: "Artificial Intelligence", code: "CS505", students: 150, rating: 4.9, color: "from-purple-500 to-pink-600" },
    { id: 4, name: "Data Structures", code: "CS201", students: 210, rating: 4.5, color: "from-amber-500 to-orange-600" },
  ];

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-slate-900">My Courses</h1>
        <button className="bg-indigo-600 text-white px-5 py-2 rounded-xl font-medium hover:bg-indigo-700 transition shadow-md">Browse Catalog</button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
        {courses.map(course => (
          <div key={course.id} className="bg-white rounded-3xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 overflow-hidden group hover:-translate-y-1">
            <div className={`h-32 bg-gradient-to-r ${course.color} p-6 flex flex-col justify-between relative overflow-hidden`}>
               <div className="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full translate-x-8 -translate-y-8 blur-2xl"></div>
               <span className="bg-white/20 text-white text-xs font-bold px-3 py-1 rounded-full w-fit backdrop-blur-sm">{course.code}</span>
            </div>
            <div className="p-6 relative">
              <div className="w-12 h-12 bg-white rounded-2xl shadow-md absolute -top-6 flex items-center justify-center text-indigo-600">
                <Book className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold text-slate-900 mt-4 mb-2 group-hover:text-indigo-600 transition-colors">{course.name}</h3>
              
              <div className="flex items-center gap-4 text-sm text-slate-500 mt-4">
                <div className="flex items-center gap-1"><Users className="w-4 h-4" /> {course.students}</div>
                <div className="flex items-center gap-1 text-amber-500"><Star className="w-4 h-4 fill-current" /> {course.rating}</div>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-100 flex justify-between items-center">
                 <div className="w-full bg-slate-100 rounded-full h-2 mr-4">
                    <div className="bg-indigo-500 h-2 rounded-full" style={{width: '65%'}}></div>
                 </div>
                 <button className="p-2 text-indigo-600 hover:bg-indigo-50 rounded-full transition"><ChevronRight className="w-5 h-5" /></button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
"""

# 3. Materials
files["src/pages/Materials.tsx"] = """import { FileText, Download, FileArchive, Search, Filter } from 'lucide-react';

export default function Materials() {
  const materials = [
    { id: 1, title: "React State Management.pdf", type: "PDF", size: "2.4 MB", course: "CS401", date: "Today" },
    { id: 2, title: "Intro to Neural Networks.pptx", type: "Presentation", size: "15 MB", course: "CS505", date: "Yesterday" },
    { id: 3, title: "SQL Queries Cheatsheet.zip", type: "Archive", size: "1.1 MB", course: "CS302", date: "Oct 5" },
    { id: 4, title: "Graph Algorithms Notes.docx", type: "Document", size: "450 KB", course: "CS201", date: "Oct 1" },
  ];

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-8">
        <h1 className="text-3xl font-bold text-slate-900">Study Materials</h1>
        <div className="flex items-center gap-3 w-full sm:w-auto">
          <div className="relative flex-1 sm:w-64">
            <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
            <input type="text" placeholder="Search files..." className="w-full pl-10 pr-4 py-2 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 text-sm" />
          </div>
          <button className="p-2 border border-slate-200 rounded-xl hover:bg-slate-50 text-slate-600"><Filter className="w-5 h-5" /></button>
        </div>
      </div>

      <div className="bg-white rounded-2xl shadow-sm border border-slate-100 overflow-hidden">
        <table className="w-full text-left border-collapse">
          <thead>
            <tr className="bg-slate-50 border-b border-slate-100 text-slate-500 text-sm">
              <th className="p-4 font-medium">File Name</th>
              <th className="p-4 font-medium hidden md:table-cell">Course</th>
              <th className="p-4 font-medium hidden sm:table-cell">Date Added</th>
              <th className="p-4 font-medium hidden lg:table-cell">Size</th>
              <th className="p-4 font-medium text-right">Action</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            {materials.map(mat => (
              <tr key={mat.id} className="hover:bg-indigo-50/50 transition-colors group">
                <td className="p-4 flex items-center gap-3">
                  <div className="p-2 bg-indigo-100 text-indigo-600 rounded-lg">
                    {mat.type === 'Archive' ? <FileArchive className="w-5 h-5" /> : <FileText className="w-5 h-5" />}
                  </div>
                  <span className="font-medium text-slate-800">{mat.title}</span>
                </td>
                <td className="p-4 hidden md:table-cell">
                   <span className="bg-slate-100 text-slate-600 text-xs px-2 py-1 rounded-md font-semibold">{mat.course}</span>
                </td>
                <td className="p-4 hidden sm:table-cell text-slate-500 text-sm">{mat.date}</td>
                <td className="p-4 hidden lg:table-cell text-slate-500 text-sm">{mat.size}</td>
                <td className="p-4 text-right">
                  <button className="p-2 text-indigo-600 hover:bg-indigo-100 rounded-lg transition-colors inline-flex items-center gap-2 text-sm font-medium">
                    <Download className="w-4 h-4" /> <span className="hidden md:inline">Download</span>
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
"""

# 4. Assignments
files["src/pages/Assignments.tsx"] = """import { Clock, CheckCircle, AlertCircle, Plus } from 'lucide-react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

export default function Assignments() {
  const { user } = useAuth();
  
  const assignments = [
    { id: 1, title: "Build a React Dashboard", course: "CS401", due: "Tomorrow, 11:59 PM", status: "Pending", marks: 50 },
    { id: 2, title: "Normalize Database Schema", course: "CS302", due: "Oct 15, 11:59 PM", status: "Submitted", marks: 30 },
    { id: 3, title: "Implement A* Search", course: "CS505", due: "Oct 20, 11:59 PM", status: "Pending", marks: 100 },
  ];

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-slate-900">Assignments</h1>
        {user?.role === 'faculty' && (
          <Link to="/assignments/create" className="bg-indigo-600 text-white px-5 py-2.5 rounded-xl font-medium hover:bg-indigo-700 transition shadow-md flex items-center gap-2">
            <Plus className="w-5 h-5" /> Create Assignment
          </Link>
        )}
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {assignments.map(item => (
          <Link to={`/assignments/${item.id}`} key={item.id} className="bg-white rounded-3xl p-6 shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 group relative overflow-hidden flex flex-col h-full">
            <div className={`absolute top-0 right-0 w-2 h-full ${item.status === 'Pending' ? 'bg-amber-400' : 'bg-emerald-500'}`}></div>
            
            <div className="flex justify-between items-start mb-4">
               <span className="bg-slate-100 text-slate-600 text-xs px-2.5 py-1 rounded-md font-bold uppercase tracking-wider">{item.course}</span>
               {item.status === 'Pending' 
                 ? <span className="flex items-center gap-1 text-xs font-bold text-amber-600 bg-amber-50 px-2 py-1 rounded-md"><AlertCircle className="w-3 h-3" /> Pending</span>
                 : <span className="flex items-center gap-1 text-xs font-bold text-emerald-600 bg-emerald-50 px-2 py-1 rounded-md"><CheckCircle className="w-3 h-3" /> Submitted</span>
               }
            </div>
            
            <h3 className="text-lg font-bold text-slate-900 mb-2 group-hover:text-indigo-600 transition-colors line-clamp-2">{item.title}</h3>
            
            <div className="mt-auto pt-6 flex items-center justify-between text-sm text-slate-500">
               <div className="flex items-center gap-1.5 font-medium"><Clock className="w-4 h-4" /> {item.due}</div>
               <div className="font-bold text-slate-700">{item.marks} pts</div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
"""

# 5. Create Assignment
files["src/pages/CreateAssignment.tsx"] = """import { useState } from 'react';
import { ArrowLeft, Save } from 'lucide-react';
import { Link, useNavigate } from 'react-router-dom';

export default function CreateAssignment() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
      navigate('/assignments');
    }, 1000);
  };

  return (
    <div className="max-w-3xl mx-auto space-y-6 pb-10">
      <Link to="/assignments" className="inline-flex items-center gap-2 text-slate-500 hover:text-indigo-600 transition-colors mb-4 font-medium">
        <ArrowLeft className="w-4 h-4" /> Back to Assignments
      </Link>
      
      <div className="bg-white rounded-3xl shadow-sm border border-slate-100 p-8">
        <h1 className="text-2xl font-bold text-slate-900 mb-8">Create New Assignment</h1>
        
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="space-y-2">
            <label className="text-sm font-semibold text-slate-700">Assignment Title</label>
            <input required type="text" placeholder="e.g. Build a React Dashboard" className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-all" />
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-2">
              <label className="text-sm font-semibold text-slate-700">Course</label>
              <select className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all bg-white">
                <option>CS401 - Web Development</option>
                <option>CS302 - Database Systems</option>
                <option>CS505 - Artificial Intelligence</option>
              </select>
            </div>
            <div className="space-y-2">
              <label className="text-sm font-semibold text-slate-700">Total Marks</label>
              <input required type="number" placeholder="e.g. 100" className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all" />
            </div>
          </div>

          <div className="space-y-2">
            <label className="text-sm font-semibold text-slate-700">Due Date</label>
            <input required type="datetime-local" className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all" />
          </div>

          <div className="space-y-2">
            <label className="text-sm font-semibold text-slate-700">Description / Instructions</label>
            <textarea required rows={5} placeholder="Provide detailed instructions for the students..." className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all resize-none"></textarea>
          </div>

          <div className="pt-6 flex justify-end gap-4">
            <Link to="/assignments" className="px-6 py-3 rounded-xl font-medium text-slate-600 hover:bg-slate-100 transition-colors">Cancel</Link>
            <button type="submit" disabled={loading} className="bg-indigo-600 text-white px-8 py-3 rounded-xl font-medium hover:bg-indigo-700 transition-colors shadow-md flex items-center gap-2">
              {loading ? "Publishing..." : <><Save className="w-5 h-5" /> Publish Assignment</>}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
"""

# 6. Assignment Details
files["src/pages/AssignmentDetails.tsx"] = """import { useState } from 'react';
import { ArrowLeft, UploadCloud, Clock, CheckCircle, FileText } from 'lucide-react';
import { Link, useParams } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

export default function AssignmentDetails() {
  const { id } = useParams();
  const { user } = useAuth();
  const [submitted, setSubmitted] = useState(false);

  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-10">
      <Link to="/assignments" className="inline-flex items-center gap-2 text-slate-500 hover:text-indigo-600 transition-colors mb-4 font-medium">
        <ArrowLeft className="w-4 h-4" /> Back to Assignments
      </Link>
      
      <div className="bg-white rounded-3xl shadow-sm border border-slate-100 overflow-hidden">
        <div className="p-8 border-b border-slate-100 bg-slate-50">
          <div className="flex justify-between items-start mb-4">
             <span className="bg-indigo-100 text-indigo-700 text-xs px-3 py-1.5 rounded-lg font-bold uppercase tracking-wider">CS401 - Web Dev</span>
             <span className="font-bold text-slate-700 bg-white px-4 py-1.5 rounded-lg border border-slate-200 shadow-sm">100 Pts</span>
          </div>
          <h1 className="text-3xl font-extrabold text-slate-900 mb-4">Build a React Dashboard (Demo #{id})</h1>
          <div className="flex items-center gap-4 text-sm font-medium">
             <span className="flex items-center gap-1.5 text-amber-600"><Clock className="w-4 h-4" /> Due: Oct 15, 11:59 PM</span>
          </div>
        </div>

        <div className="p-8">
          <h3 className="text-lg font-bold text-slate-900 mb-4">Instructions</h3>
          <div className="prose prose-slate max-w-none mb-8 text-slate-600">
            <p>Please build a responsive React dashboard using Vite and Tailwind CSS. Ensure it includes at least 3 pages with working routing.</p>
            <p>Submission requirements:</p>
            <ul>
              <li>Provide the GitHub repository link.</li>
              <li>Upload a short PDF report explaining your design choices.</li>
            </ul>
          </div>

          {user?.role === 'student' && (
            <div className="mt-10 border-t border-slate-100 pt-8">
              <h3 className="text-lg font-bold text-slate-900 mb-4">Your Submission</h3>
              
              {!submitted ? (
                <div className="bg-slate-50 border border-slate-200 border-dashed rounded-2xl p-8 text-center hover:bg-slate-100 transition-colors">
                   <div className="w-16 h-16 bg-white rounded-full flex items-center justify-center mx-auto shadow-sm mb-4 text-indigo-600">
                     <UploadCloud className="w-8 h-8" />
                   </div>
                   <p className="font-semibold text-slate-800 mb-1">Click to upload or drag and drop</p>
                   <p className="text-sm text-slate-500 mb-6">PDF, ZIP, or Text files up to 50MB</p>
                   
                   <textarea rows={3} placeholder="Add a comment or link (optional)" className="w-full max-w-lg mx-auto block p-3 mb-4 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none text-left"></textarea>
                   
                   <button onClick={() => setSubmitted(true)} className="bg-indigo-600 text-white px-8 py-2.5 rounded-xl font-medium hover:bg-indigo-700 transition shadow-md">
                     Submit Assignment
                   </button>
                </div>
              ) : (
                <div className="bg-emerald-50 border border-emerald-200 rounded-2xl p-6 flex items-center gap-4">
                   <div className="text-emerald-500"><CheckCircle className="w-10 h-10" /></div>
                   <div>
                     <h4 className="font-bold text-emerald-800 text-lg">Successfully Submitted</h4>
                     <p className="text-emerald-600 text-sm">Your assignment was submitted on Oct 10 at 10:45 AM.</p>
                   </div>
                </div>
              )}
            </div>
          )}

          {user?.role === 'faculty' && (
             <div className="mt-10 border-t border-slate-100 pt-8">
               <h3 className="text-lg font-bold text-slate-900 mb-4">Student Submissions (18/25)</h3>
               <div className="bg-slate-50 border border-slate-200 rounded-2xl p-6 text-center text-slate-500">
                  Submission table will appear here in Phase 2.
               </div>
             </div>
          )}
        </div>
      </div>
    </div>
  );
}
"""

# 7. Announcements
files["src/pages/Announcements.tsx"] = """import { Bell, Megaphone } from 'lucide-react';
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
"""

# 8. Discussions
files["src/pages/Discussions.tsx"] = """import { MessageSquare, ThumbsUp, Reply } from 'lucide-react';

export default function Discussions() {
  return (
    <div className="space-y-6 max-w-5xl mx-auto">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-slate-900 flex items-center gap-3">
          <MessageSquare className="w-8 h-8 text-indigo-600" /> Course Discussions
        </h1>
        <button className="bg-indigo-600 text-white px-5 py-2.5 rounded-xl font-medium hover:bg-indigo-700 transition shadow-md">
          Ask a Question
        </button>
      </div>

      <div className="bg-white rounded-3xl p-6 md:p-8 shadow-sm border border-slate-100">
        <div className="flex gap-4">
           <div className="w-12 h-12 bg-indigo-100 rounded-full flex-shrink-0 flex items-center justify-center text-indigo-600 font-bold">JD</div>
           <div className="flex-1">
              <div className="flex justify-between items-start">
                 <div>
                   <h3 className="font-bold text-slate-900 text-lg">Error when running React app</h3>
                   <p className="text-xs text-slate-500 font-medium">John Doe • CS401 • 3 hours ago</p>
                 </div>
                 <span className="bg-emerald-100 text-emerald-700 text-xs px-2 py-1 rounded font-bold">Resolved</span>
              </div>
              <p className="mt-4 text-slate-600">I am getting a "Vite plugin not found" error when trying to run the app. Any ideas?</p>
              
              <div className="mt-4 flex items-center gap-4 text-sm">
                 <button className="flex items-center gap-1.5 text-slate-500 hover:text-indigo-600 font-medium"><ThumbsUp className="w-4 h-4" /> 4 Likes</button>
                 <button className="flex items-center gap-1.5 text-slate-500 hover:text-indigo-600 font-medium"><Reply className="w-4 h-4" /> 2 Replies</button>
              </div>

              {/* Reply */}
              <div className="mt-6 ml-6 p-4 bg-slate-50 border border-slate-100 rounded-2xl flex gap-4">
                 <div className="w-8 h-8 bg-purple-100 rounded-full flex-shrink-0 flex items-center justify-center text-purple-600 font-bold text-xs">PJ</div>
                 <div>
                    <p className="text-xs text-slate-500 font-medium mb-1">Prof. Johnson • 1 hour ago</p>
                    <p className="text-sm text-slate-700">Make sure you ran <code>npm install</code> before running the dev server.</p>
                 </div>
              </div>
           </div>
        </div>
      </div>
    </div>
  );
}
"""

# 9. Generic Placeholder for Analytics, Calendar, Notifications, Profile, Settings, NotFound
generic_placeholder = """import { {icon} } from 'lucide-react';

export default function {name}() {
  return (
    <div className="flex flex-col items-center justify-center h-[70vh] text-center animate-fade-in-up">
      <div className="w-24 h-24 bg-indigo-50 text-indigo-600 rounded-3xl flex items-center justify-center mb-6 shadow-sm border border-indigo-100 transform rotate-3">
        <{icon} className="w-12 h-12" />
      </div>
      <h1 className="text-3xl font-extrabold text-slate-900 mb-4">{title}</h1>
      <p className="text-slate-500 max-w-md text-lg">This section is currently under construction for Phase 2 of the hackathon.</p>
    </div>
  );
}
"""

files["src/pages/Analytics.tsx"] = generic_placeholder.replace("{name}", "Analytics").replace("{title}", "Platform Analytics").replace("{icon}", "BarChart2")
files["src/pages/Calendar.tsx"] = generic_placeholder.replace("{name}", "Calendar").replace("{title}", "Academic Calendar").replace("{icon}", "Calendar")
files["src/pages/Notifications.tsx"] = generic_placeholder.replace("{name}", "Notifications").replace("{title}", "Your Notifications").replace("{icon}", "Bell")
files["src/pages/Profile.tsx"] = generic_placeholder.replace("{name}", "Profile").replace("{title}", "User Profile").replace("{icon}", "UserIcon")
files["src/pages/Settings.tsx"] = generic_placeholder.replace("{name}", "Settings").replace("{title}", "Account Settings").replace("{icon}", "Settings")

# Not found
files["src/pages/NotFound.tsx"] = """import { Link } from 'react-router-dom';

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-slate-50 text-center px-4">
      <h1 className="text-9xl font-black text-slate-200 mb-4">404</h1>
      <h2 className="text-3xl font-bold text-slate-800 mb-6">Page Not Found</h2>
      <p className="text-slate-500 mb-8 max-w-md">The page you are looking for doesn't exist or has been moved.</p>
      <Link to="/" className="bg-indigo-600 text-white px-8 py-3 rounded-xl font-bold hover:bg-indigo-700 transition shadow-md">
        Go Back Home
      </Link>
    </div>
  );
}
"""

# App.tsx Update
files["src/App.tsx"] = """import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import Layout from './components/layout/Layout';
import Landing from './pages/Landing';
import Login from './pages/auth/Login';
import Register from './pages/auth/Register';
import StudentDashboard from './pages/dashboard/StudentDashboard';
import FacultyDashboard from './pages/dashboard/FacultyDashboard';
import AdminDashboard from './pages/dashboard/AdminDashboard';
import Courses from './pages/Courses';
import Assignments from './pages/Assignments';
import CreateAssignment from './pages/CreateAssignment';
import AssignmentDetails from './pages/AssignmentDetails';
import Materials from './pages/Materials';
import Announcements from './pages/Announcements';
import Discussions from './pages/Discussions';
import Calendar from './pages/Calendar';
import Analytics from './pages/Analytics';
import Notifications from './pages/Notifications';
import Profile from './pages/Profile';
import Settings from './pages/Settings';
import NotFound from './pages/NotFound';

const ProtectedRoute = ({ children }: { children: React.ReactNode }) => {
  const { user } = useAuth();
  if (!user) return <Navigate to="/login" replace />;
  return <>{children}</>;
};

function AppRoutes() {
  const { user } = useAuth();
  
  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      
      <Route element={<Layout />}>
        <Route path="/dashboard" element={
          <ProtectedRoute>
            {user?.role === 'student' && <StudentDashboard />}
            {user?.role === 'faculty' && <FacultyDashboard />}
            {user?.role === 'admin' && <AdminDashboard />}
          </ProtectedRoute>
        } />
        
        <Route path="/courses" element={<ProtectedRoute><Courses /></ProtectedRoute>} />
        <Route path="/assignments" element={<ProtectedRoute><Assignments /></ProtectedRoute>} />
        <Route path="/assignments/create" element={<ProtectedRoute><CreateAssignment /></ProtectedRoute>} />
        <Route path="/assignments/:id" element={<ProtectedRoute><AssignmentDetails /></ProtectedRoute>} />
        <Route path="/materials" element={<ProtectedRoute><Materials /></ProtectedRoute>} />
        <Route path="/announcements" element={<ProtectedRoute><Announcements /></ProtectedRoute>} />
        <Route path="/discussions" element={<ProtectedRoute><Discussions /></ProtectedRoute>} />
        <Route path="/calendar" element={<ProtectedRoute><Calendar /></ProtectedRoute>} />
        <Route path="/analytics" element={<ProtectedRoute><Analytics /></ProtectedRoute>} />
        <Route path="/notifications" element={<ProtectedRoute><Notifications /></ProtectedRoute>} />
        <Route path="/profile" element={<ProtectedRoute><Profile /></ProtectedRoute>} />
        <Route path="/settings" element={<ProtectedRoute><Settings /></ProtectedRoute>} />
      </Route>
      
      {/* 404 Catch All */}
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <Router>
        <AppRoutes />
      </Router>
    </AuthProvider>
  );
}
"""

for path, content in files.items():
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding='utf-8') as f:
        f.write(content)
        
print("All 14 pages generated and App.tsx updated successfully!")
