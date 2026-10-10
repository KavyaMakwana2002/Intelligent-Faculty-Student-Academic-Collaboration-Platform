import os

frontend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web"

# --- 1. DASHBOARDS ---
student_dash = """import { useState, useEffect } from 'react';
import { Book, Clock, CheckCircle, FileText, Bell } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import { Link } from 'react-router-dom';
import axios from 'axios';

export default function StudentDashboard() {
  const { user } = useAuth();
  const [stats, setStats] = useState({ assignments_total: 0, assignments_submitted: 0, assignments_pending: 0, materials_total: 0 });

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const token = localStorage.getItem('token');
        const res = await axios.get('http://localhost:5000/api/analytics/dashboard', { headers: { Authorization: `Bearer ${token}` } });
        setStats(res.data);
      } catch (err) {}
    };
    fetchStats();
  }, []);

  return (
    <div className="space-y-6 animate-fade-in-up">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-8">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-900">Welcome back, {user?.name.split(' ')[0]}!</h1>
          <p className="text-slate-500 mt-1 font-medium text-sm flex items-center gap-2">
            <span className="bg-indigo-50 text-indigo-700 px-2.5 py-1 rounded-md uppercase tracking-wider text-xs font-bold">{user?.course?.replace('_', ' ')}</span>
            <span className="bg-purple-50 text-purple-700 px-2.5 py-1 rounded-md uppercase tracking-wider text-xs font-bold">Sem {user?.semester}</span>
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="w-14 h-14 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center"><Book className="w-7 h-7" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase tracking-wider">Total Assignments</p><h2 className="text-3xl font-black text-slate-900">{stats.assignments_total}</h2></div>
        </div>
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="w-14 h-14 bg-amber-50 text-amber-600 rounded-2xl flex items-center justify-center"><Clock className="w-7 h-7" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase tracking-wider">Pending Tasks</p><h2 className="text-3xl font-black text-slate-900">{stats.assignments_pending}</h2></div>
        </div>
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="w-14 h-14 bg-emerald-50 text-emerald-600 rounded-2xl flex items-center justify-center"><CheckCircle className="w-7 h-7" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase tracking-wider">Submitted</p><h2 className="text-3xl font-black text-slate-900">{stats.assignments_submitted}</h2></div>
        </div>
        <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex items-center gap-4">
          <div className="w-14 h-14 bg-purple-50 text-purple-600 rounded-2xl flex items-center justify-center"><FileText className="w-7 h-7" /></div>
          <div><p className="text-sm font-bold text-slate-500 uppercase tracking-wider">Study Materials</p><h2 className="text-3xl font-black text-slate-900">{stats.materials_total}</h2></div>
        </div>
      </div>
      
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-6">
         <div className="bg-indigo-600 rounded-3xl p-8 text-white shadow-md relative overflow-hidden flex flex-col justify-center">
            <div className="absolute right-0 bottom-0 opacity-10"><Book className="w-48 h-48 transform translate-x-1/4 translate-y-1/4" /></div>
            <h2 className="text-2xl font-bold mb-2 relative z-10">EduConnect AI Assistant</h2>
            <p className="text-indigo-100 mb-6 relative z-10 max-w-sm">Got a doubt? Ask our smart AI assistant for help with your semester topics.</p>
            <button className="bg-white text-indigo-600 px-6 py-3 rounded-xl font-bold w-fit shadow-lg hover:shadow-xl transition-all relative z-10">Try it now (Bottom Right)</button>
         </div>
         <div className="bg-white rounded-3xl p-8 shadow-sm border border-slate-100">
            <h3 className="text-lg font-bold text-slate-900 mb-6 flex items-center gap-2"><Bell className="w-5 h-5 text-amber-500" /> Recent Announcements</h3>
            <div className="space-y-4">
               <div className="p-4 bg-slate-50 rounded-2xl border border-slate-100"><p className="font-bold text-slate-800">Welcome to Hackathon 2026!</p><p className="text-sm text-slate-500">Problem Statement PS-04 is live.</p></div>
            </div>
         </div>
      </div>
    </div>
  );
}
"""

faculty_dash = """import { useState, useEffect } from 'react';
import { Book, Users, FileText, CheckCircle } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import axios from 'axios';

export default function FacultyDashboard() {
  const { user } = useAuth();
  const [stats, setStats] = useState({ assignments_created: 0, materials_uploaded: 0 });

  useEffect(() => {
    const fetchStats = async () => {
      try {
         const token = localStorage.getItem('token');
         const res = await axios.get('http://localhost:5000/api/analytics/dashboard', { headers: { Authorization: `Bearer ${token}` } });
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
"""

with open(os.path.join(frontend_dir, "src/pages/StudentDashboard.tsx"), "w", encoding="utf-8") as f: f.write(student_dash)
with open(os.path.join(frontend_dir, "src/pages/FacultyDashboard.tsx"), "w", encoding="utf-8") as f: f.write(faculty_dash)


# --- 2. MATERIALS COMPONENT ---
materials_tsx = """import { useState, useEffect } from 'react';
import { FileText, Download, Plus, Search } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import axios from 'axios';

export default function Materials() {
  const { user } = useAuth();
  const [materials, setMaterials] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  // Upload Form States (Faculty only)
  const [showForm, setShowForm] = useState(false);
  const [title, setTitle] = useState('');
  const [course, setCourse] = useState('');
  const [semester, setSemester] = useState('');
  const [description, setDescription] = useState('');

  const fetchMaterials = async () => {
    try {
      const token = localStorage.getItem('token');
      const res = await axios.get('http://localhost:5000/api/materials', { headers: { Authorization: `Bearer ${token}` } });
      setMaterials(res.data);
    } catch (err) {} finally { setLoading(false); }
  };

  useEffect(() => { fetchMaterials(); }, []);

  const handleUpload = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem('token');
      await axios.post('http://localhost:5000/api/materials', {
         title, course, semester, description, file_url: 'https://example.com/notes.pdf'
      }, { headers: { Authorization: `Bearer ${token}` } });
      setShowForm(false);
      fetchMaterials();
    } catch (err) { alert('Upload failed'); }
  };

  return (
    <div className="space-y-6 animate-fade-in-up">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-900">Study Materials</h1>
          <p className="text-slate-500 font-medium mt-1">Access notes, PDFs, and resources</p>
        </div>
        {user?.role === 'faculty' && (
          <button onClick={() => setShowForm(!showForm)} className="bg-indigo-600 text-white px-5 py-2.5 rounded-xl font-bold flex items-center gap-2 hover:bg-indigo-700">
            <Plus className="w-5 h-5" /> Upload Material
          </button>
        )}
      </div>

      {showForm && user?.role === 'faculty' && (
        <div className="bg-white p-8 rounded-3xl shadow-sm border border-slate-100 mb-8">
           <h2 className="text-xl font-bold mb-6">Upload New Resource</h2>
           <form onSubmit={handleUpload} className="space-y-4">
              <input required value={title} onChange={e=>setTitle(e.target.value)} type="text" placeholder="Title (e.g. Chapter 1 Notes)" className="w-full p-3 border border-slate-200 rounded-xl" />
              <div className="grid grid-cols-2 gap-4">
                 <select required value={course} onChange={e=>setCourse(e.target.value)} className="w-full p-3 border border-slate-200 rounded-xl">
                   <option value="">Course</option><option value="bca_hons">BCA Hons.</option><option value="mca">MCA</option>
                 </select>
                 <select required value={semester} onChange={e=>setSemester(e.target.value)} className="w-full p-3 border border-slate-200 rounded-xl">
                   <option value="">Semester</option><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option>
                 </select>
              </div>
              <textarea required value={description} onChange={e=>setDescription(e.target.value)} placeholder="Description..." className="w-full p-3 border border-slate-200 rounded-xl"></textarea>
              <button type="submit" className="bg-emerald-600 text-white px-6 py-2.5 rounded-xl font-bold">Publish Material</button>
           </form>
        </div>
      )}

      {loading ? (
         <div className="flex justify-center p-20"><span className="w-10 h-10 border-4 border-indigo-200 border-t-indigo-600 rounded-full animate-spin"></span></div>
      ) : materials.length === 0 ? (
         <div className="bg-white p-16 text-center rounded-3xl border border-slate-100"><p className="text-slate-500 font-bold">No materials found for your semester.</p></div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
           {materials.map(mat => (
              <div key={mat.id} className="bg-white p-6 rounded-3xl border border-slate-100 shadow-sm flex flex-col h-full group hover:shadow-md transition">
                 <div className="w-12 h-12 bg-rose-50 text-rose-500 rounded-xl flex items-center justify-center mb-4"><FileText className="w-6 h-6" /></div>
                 <h3 className="font-bold text-lg text-slate-900 mb-2">{mat.title}</h3>
                 <p className="text-sm text-slate-500 mb-4 line-clamp-2">{mat.description}</p>
                 <div className="mt-auto pt-4 border-t border-slate-50 flex justify-between items-center">
                    <span className="text-xs font-bold text-slate-400">{new Date(mat.uploaded_at).toLocaleDateString()}</span>
                    <button className="text-indigo-600 font-bold text-sm flex items-center gap-1 group-hover:text-indigo-700"><Download className="w-4 h-4" /> Download</button>
                 </div>
              </div>
           ))}
        </div>
      )}
    </div>
  );
}
"""
with open(os.path.join(frontend_dir, "src/pages/Materials.tsx"), "w", encoding="utf-8") as f: f.write(materials_tsx)


# --- 3. AI CHAT WIDGET ---
ai_chat_tsx = """import { useState, useRef, useEffect } from 'react';
import { MessageSquare, X, Send, Bot, Sparkles } from 'lucide-react';
import axios from 'axios';

export default function AiChatWidget() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<{sender: 'user'|'ai', text: string}[]>([{sender: 'ai', text: 'Hi! I am EduConnect AI. How can I help with your semester today?'}]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const endRef = useRef<HTMLDivElement>(null);

  useEffect(() => { endRef.current?.scrollIntoView({ behavior: 'smooth' }); }, [messages]);

  const handleSend = async () => {
    if(!input.trim()) return;
    setMessages(prev => [...prev, {sender: 'user', text: input}]);
    setInput('');
    setLoading(true);
    
    try {
       const res = await axios.post('http://localhost:5000/api/ai-chat', { message: input });
       setMessages(prev => [...prev, {sender: 'ai', text: res.data.reply}]);
    } catch(err) {
       setMessages(prev => [...prev, {sender: 'ai', text: 'Oops! AI Service is currently offline.'}]);
    } finally { setLoading(false); }
  };

  return (
    <>
      {/* FAB */}
      <button onClick={() => setIsOpen(true)} className={`fixed bottom-8 right-8 w-16 h-16 bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded-full shadow-2xl flex items-center justify-center hover:scale-110 transition-all z-50 ${isOpen ? 'scale-0 opacity-0' : 'scale-100 opacity-100'}`}>
        <Sparkles className="w-8 h-8" />
      </button>

      {/* Chat Window */}
      <div className={`fixed bottom-8 right-8 w-96 h-[32rem] bg-white rounded-3xl shadow-2xl border border-slate-100 flex flex-col z-50 transition-all duration-300 origin-bottom-right ${isOpen ? 'scale-100 opacity-100' : 'scale-0 opacity-0 pointer-events-none'}`}>
         {/* Header */}
         <div className="bg-gradient-to-r from-indigo-600 to-purple-600 p-4 rounded-t-3xl flex justify-between items-center text-white">
            <div className="flex items-center gap-3">
               <div className="w-10 h-10 bg-white/20 rounded-full flex items-center justify-center backdrop-blur-sm"><Bot className="w-6 h-6" /></div>
               <div><h3 className="font-bold leading-tight">EduConnect AI</h3><p className="text-xs text-indigo-100"><div className="w-2 h-2 bg-emerald-400 rounded-full inline-block mr-1"></div>Online</p></div>
            </div>
            <button onClick={() => setIsOpen(false)} className="p-2 hover:bg-white/20 rounded-full transition"><X className="w-5 h-5" /></button>
         </div>
         
         {/* Messages */}
         <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-slate-50">
            {messages.map((m, i) => (
               <div key={i} className={`flex ${m.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
                  <div className={`max-w-[80%] p-3 rounded-2xl text-sm ${m.sender === 'user' ? 'bg-indigo-600 text-white rounded-br-sm' : 'bg-white text-slate-700 border border-slate-100 rounded-bl-sm shadow-sm'}`}>
                     {m.text}
                  </div>
               </div>
            ))}
            {loading && <div className="flex justify-start"><div className="bg-white p-3 rounded-2xl rounded-bl-sm border border-slate-100 shadow-sm text-slate-400 text-xs flex gap-1"><span className="animate-bounce">•</span><span className="animate-bounce delay-75">•</span><span className="animate-bounce delay-150">•</span></div></div>}
            <div ref={endRef}></div>
         </div>
         
         {/* Input */}
         <div className="p-4 bg-white border-t border-slate-100 rounded-b-3xl flex gap-2">
            <input value={input} onChange={e=>setInput(e.target.value)} onKeyDown={e=>e.key==='Enter' && handleSend()} type="text" placeholder="Ask AI a doubt..." className="flex-1 bg-slate-50 border border-slate-200 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm" />
            <button onClick={handleSend} disabled={loading} className="w-10 h-10 bg-indigo-600 text-white rounded-xl flex items-center justify-center hover:bg-indigo-700 transition disabled:opacity-50"><Send className="w-4 h-4" /></button>
         </div>
      </div>
    </>
  );
}
"""
with open(os.path.join(frontend_dir, "src/components/AiChatWidget.tsx"), "w", encoding="utf-8") as f: f.write(ai_chat_tsx)


# --- 4. INCLUDE WIDGET IN LAYOUT ---
layout_path = os.path.join(frontend_dir, "src/components/layout/Layout.tsx")
with open(layout_path, "r", encoding="utf-8") as f: layout_content = f.read()
if "AiChatWidget" not in layout_content:
    layout_content = layout_content.replace(
        "import { cn } from '../../lib/utils';",
        "import { cn } from '../../lib/utils';\nimport AiChatWidget from '../AiChatWidget';"
    )
    layout_content = layout_content.replace(
        "      </main>\n    </div>",
        "      </main>\n      <AiChatWidget />\n    </div>"
    )
    with open(layout_path, "w", encoding="utf-8") as f: f.write(layout_content)


# --- 5. FACULTY GRADING (Update AssignmentDetails.tsx) ---
# We will inject the Faculty Submissions View into AssignmentDetails
ad_path = os.path.join(frontend_dir, "src/pages/AssignmentDetails.tsx")
with open(ad_path, "r", encoding="utf-8") as f: ad_content = f.read()

if "facultySubmissions" not in ad_content:
    ad_content = ad_content.replace("const [submission, setSubmission] = useState<any>(null);", "const [submission, setSubmission] = useState<any>(null);\n  const [facultySubmissions, setFacultySubmissions] = useState<any[]>([]);")
    
    fetch_data_block = """      if (user?.role === 'student') {
        const subRes = await axios.get(`http://localhost:5000/api/assignments/${id}/submission`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        setSubmission(subRes.data);
      }"""
    fetch_data_block_new = fetch_data_block + """ else if (user?.role === 'faculty') {
        const facRes = await axios.get(`http://localhost:5000/api/assignments/${id}/submissions`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        setFacultySubmissions(facRes.data);
      }"""
    ad_content = ad_content.replace(fetch_data_block, fetch_data_block_new)
    
    faculty_ui = """
      {user?.role === 'faculty' && (
        <div className="bg-white rounded-3xl shadow-sm border border-slate-100 p-8">
           <h3 className="text-xl font-bold text-slate-900 mb-6 border-b border-slate-100 pb-4 flex items-center gap-2"><CheckCircle className="w-5 h-5 text-indigo-500" /> Student Submissions</h3>
           
           {facultySubmissions.length === 0 ? (
             <div className="text-center p-10 text-slate-500 font-medium">No submissions yet for this assignment.</div>
           ) : (
             <div className="overflow-x-auto">
               <table className="w-full text-left">
                 <thead>
                   <tr className="border-b border-slate-200 text-slate-500 text-sm">
                     <th className="pb-3 font-bold">Student Name</th>
                     <th className="pb-3 font-bold">Enrollment</th>
                     <th className="pb-3 font-bold">Submitted At</th>
                     <th className="pb-3 font-bold">Status</th>
                     <th className="pb-3 font-bold text-right">Grade (Marks)</th>
                   </tr>
                 </thead>
                 <tbody className="divide-y divide-slate-100">
                   {facultySubmissions.map(sub => (
                     <tr key={sub.id} className="hover:bg-slate-50 transition-colors">
                       <td className="py-4 font-bold text-slate-800">{sub.student_name}</td>
                       <td className="py-4 font-mono text-slate-600 text-sm">{sub.enrollment}</td>
                       <td className="py-4 text-sm text-slate-500">{new Date(sub.submitted_at).toLocaleString()}</td>
                       <td className="py-4">
                          <span className={`px-2 py-1 rounded-md text-xs font-bold ${sub.status === 'Graded' ? 'bg-emerald-50 text-emerald-600' : 'bg-amber-50 text-amber-600'}`}>{sub.status}</span>
                       </td>
                       <td className="py-4 text-right">
                          {sub.status === 'Graded' ? (
                             <span className="font-bold text-lg text-indigo-600">{sub.marks_awarded} / {assignment.marks}</span>
                          ) : (
                             <div className="flex justify-end gap-2">
                               <input type="number" id={`marks-${sub.id}`} max={assignment.marks} className="w-20 p-2 border border-slate-200 rounded-lg text-center font-bold" placeholder="Score" />
                               <button onClick={async () => {
                                  const marks = (document.getElementById(`marks-${sub.id}`) as HTMLInputElement).value;
                                  if(!marks) return;
                                  await axios.post(`http://localhost:5000/api/assignments/submissions/${sub.id}/grade`, {marks}, {headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}});
                                  fetchData();
                               }} className="bg-indigo-600 text-white px-4 py-2 rounded-lg font-bold text-sm hover:bg-indigo-700">Grade</button>
                             </div>
                          )}
                       </td>
                     </tr>
                   ))}
                 </tbody>
               </table>
             </div>
           )}
        </div>
      )}
    """
    
    ad_content = ad_content.replace(
        "      {user?.role === 'student' && (",
        faculty_ui + "\n      {user?.role === 'student' && ("
    )
    with open(ad_path, "w", encoding="utf-8") as f: f.write(ad_content)

print("Frontend features built!")
