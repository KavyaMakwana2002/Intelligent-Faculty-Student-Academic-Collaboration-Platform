import { useState, useEffect } from 'react';
import { FileText, Download, Plus } from 'lucide-react';
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
  const [file, setFile] = useState<File | null>(null);

  const fetchMaterials = async () => {
    try {
      const token = localStorage.getItem('token');
      const res = await axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/materials`, { headers: { Authorization: `Bearer ${token}` } });
      setMaterials(res.data);
    } catch (err) {} finally { setLoading(false); }
  };

  useEffect(() => { fetchMaterials(); }, []);

  const handleUpload = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem('token');
      const formData = new FormData();
      formData.append('title', title);
      formData.append('course', course);
      formData.append('semester', semester);
      formData.append('description', description);
      if (file) formData.append('file', file);
      
      await axios.post(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/materials`, formData, { headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'multipart/form-data' } });
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
              <input type="file" required accept=".pdf" onChange={e => setFile(e.target.files?.[0] || null)} className="w-full p-3 border border-slate-200 rounded-xl" />
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
                    <a href={`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}${mat.file_url}`} target="_blank" className="text-indigo-600 font-bold text-sm flex items-center gap-1 group-hover:text-indigo-700"><Download className="w-4 h-4" /> View/Download</a>
                 </div>
              </div>
           ))}
        </div>
      )}
    </div>
  );
}
