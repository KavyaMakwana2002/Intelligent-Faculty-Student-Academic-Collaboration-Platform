import { useState } from 'react';
import { ArrowLeft, Save, AlertCircle } from 'lucide-react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

export default function CreateAssignment() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const [title, setTitle] = useState('');
  const [course, setCourse] = useState('');
  const [semester, setSemester] = useState('');
  const [subject, setSubject] = useState('');
  const [file, setFile] = useState<File | null>(null);
  const [marks, setMarks] = useState('');
  const [dueDate, setDueDate] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    
    try {
      const token = localStorage.getItem('token');
      const formData = new FormData();
      formData.append('title', title);
      formData.append('course', course);
      formData.append('semester', semester);
      formData.append('subject', subject);
      formData.append('marks', marks);
      formData.append('due_date', dueDate);
      formData.append('description', description);
      if (file) formData.append('file', file);
      
      await axios.post(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/assignments`, formData, {
        headers: { 
           Authorization: `Bearer ${token}`,
           'Content-Type': 'multipart/form-data'
        }
      });
      navigate('/assignments');
    } catch (err: any) {
      setError(err.response?.data?.error || 'Failed to create assignment');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-3xl mx-auto space-y-6 pb-10">
      <Link to="/assignments" className="inline-flex items-center gap-2 text-slate-500 hover:text-indigo-600 transition-colors mb-4 font-medium">
        <ArrowLeft className="w-4 h-4" /> Back to Assignments
      </Link>
      
      <div className="bg-white rounded-3xl shadow-sm border border-slate-100 p-8">
        <h1 className="text-2xl font-bold text-slate-900 mb-8">Create New Assignment</h1>
        
        {error && (
            <div className="bg-red-50 text-red-500 p-4 rounded-xl flex items-center gap-2 mb-6">
              <AlertCircle className="w-5 h-5" /> {error}
            </div>
        )}
        
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="space-y-2">
            <label className="text-sm font-semibold text-slate-700">Assignment Title</label>
            <input required value={title} onChange={e=>setTitle(e.target.value)} type="text" placeholder="e.g. Build a React Dashboard" className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-all" />
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-2">
              <label className="text-sm font-semibold text-slate-700">Target Course (Program)</label>
              <select required value={course} onChange={e=>setCourse(e.target.value)} className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all bg-white">
                <option value="">Select Course</option>
                <option value="bca_hons">BCA Hons.</option>
                <option value="bca_hons_aiml">BCA Hons. AI/ML</option>
                <option value="bca_hons_cyber">BCA Hons. Cyber Security</option>
                <option value="mca">MCA</option>
              </select>
            </div>
            <div className="space-y-2">
              <label className="text-sm font-semibold text-slate-700">Target Semester</label>
              <select required value={semester} onChange={e=>setSemester(e.target.value)} className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all bg-white">
                <option value="">Select Semester</option>
                <option value="1">Semester 1</option>
                <option value="2">Semester 2</option>
                <option value="3">Semester 3</option>
                <option value="4">Semester 4</option>
                <option value="5">Semester 5</option>
                <option value="6">Semester 6</option>
                <option value="7">Semester 7</option>
                <option value="8">Semester 8</option>
              </select>
            </div>
            <div className="space-y-2 md:col-span-2">
              <label className="text-sm font-semibold text-slate-700">Subject</label>
              <select required value={subject} onChange={e=>setSubject(e.target.value)} className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all bg-white">
                <option value="">Select Subject</option>
                <option value="Data Structures & Algorithms">Data Structures & Algorithms</option>
                <option value="Web Development Technologies">Web Development Technologies</option>
                <option value="Database Management Systems">Database Management Systems</option>
                <option value="Operating Systems">Operating Systems</option>
                <option value="Artificial Intelligence">Artificial Intelligence</option>
                <option value="Cyber Security & Cryptography">Cyber Security & Cryptography</option>
                <option value="Software Engineering">Software Engineering</option>
                <option value="Computer Networks">Computer Networks</option>
              </select>
            </div>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-2">
              <label className="text-sm font-semibold text-slate-700">Total Marks</label>
              <input required value={marks} onChange={e=>setMarks(e.target.value)} type="number" placeholder="e.g. 100" className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all" />
            </div>
            <div className="space-y-2">
              <label className="text-sm font-semibold text-slate-700">Due Date</label>
              <input required value={dueDate} onChange={e=>setDueDate(e.target.value)} type="datetime-local" className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all" />
            </div>
          </div>

          <div className="space-y-2">
            <label className="text-sm font-semibold text-slate-700">Attach PDF (Optional)</label>
            <input type="file" accept=".pdf" onChange={(e) => setFile(e.target.files?.[0] || null)} className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all bg-white" />
          </div>
          
          <div className="space-y-2">
            <label className="text-sm font-semibold text-slate-700">Description / Instructions</label>
            <textarea required value={description} onChange={e=>setDescription(e.target.value)} rows={5} placeholder="Provide detailed instructions for the students..." className="w-full p-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none transition-all resize-none"></textarea>
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
