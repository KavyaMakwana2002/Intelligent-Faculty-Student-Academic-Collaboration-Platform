import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { ArrowLeft, Clock, FileText, CheckCircle, UploadCloud, AlertCircle } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import axios from 'axios';

export default function AssignmentDetails() {
  const { id } = useParams();
  const { user } = useAuth();
  
  const [assignment, setAssignment] = useState<any>(null);
  const [submission, setSubmission] = useState<any>(null);
  const [facultySubmissions, setFacultySubmissions] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [file, setFile] = useState<File | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchData();
  }, [id]);

  const fetchData = async () => {
    try {
      const token = localStorage.getItem('token');
      const res = await axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/assignments/${id}`, {
        headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'multipart/form-data' }
      });
      setAssignment(res.data);
      
      if (user?.role === 'student') {
        const subRes = await axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/assignments/${id}/submission`, {
          headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'multipart/form-data' }
        });
        setSubmission(subRes.data);
      } else if (user?.role === 'faculty') {
        const facRes = await axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/assignments/${id}/submissions`, {
          headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'multipart/form-data' }
        });
        setFacultySubmissions(facRes.data);
      }
    } catch (err: any) {
      setError(err.response?.data?.error || 'Failed to load assignment');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async () => {
    setSubmitting(true);
    try {
      const token = localStorage.getItem('token');
      const formData = new FormData();
      if (file) formData.append('file', file);
      
      await axios.post(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/assignments/${id}/submit`, formData, {
        headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'multipart/form-data' }
      });
      fetchData();
    } catch (err: any) {
      setError(err.response?.data?.error || 'Failed to submit');
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) return <div className="flex justify-center p-20"><span className="w-10 h-10 border-4 border-indigo-200 border-t-indigo-600 rounded-full animate-spin"></span></div>;

  if (error) return (
    <div className="max-w-3xl mx-auto space-y-6 pb-10">
      <Link to="/assignments" className="inline-flex items-center gap-2 text-slate-500 hover:text-indigo-600 mb-4 font-medium"><ArrowLeft className="w-4 h-4" /> Back to Assignments</Link>
      <div className="bg-red-50 text-red-600 p-6 rounded-3xl border border-red-100 flex items-center gap-4 shadow-sm">
        <AlertCircle className="w-8 h-8" />
        <div><h3 className="font-bold text-lg">Access Denied</h3><p>{error}</p></div>
      </div>
    </div>
  );

  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-10 animate-fade-in-up">
      <Link to="/assignments" className="inline-flex items-center gap-2 text-slate-500 hover:text-indigo-600 mb-4 font-medium transition">
        <ArrowLeft className="w-4 h-4" /> Back to Assignments
      </Link>
      
      <div className="bg-white rounded-3xl shadow-sm border border-slate-100 overflow-hidden">
         <div className="p-8 border-b border-slate-100 bg-slate-50/50">
            <div className="flex justify-between items-start gap-4 mb-4">
               <div>
                 <span className="bg-indigo-100 text-indigo-700 text-xs px-2.5 py-1 rounded-md font-bold uppercase tracking-wider mb-3 inline-block">
                   {assignment.course.replace('_', ' ')} Sem {assignment.semester} • {assignment.subject || 'General'}
                 </span>
                 <h1 className="text-3xl font-extrabold text-slate-900">{assignment.title}</h1>
               </div>
               <div className="text-right">
                  <div className="text-2xl font-black text-indigo-600">{assignment.marks} <span className="text-sm font-medium text-slate-500">pts</span></div>
               </div>
            </div>
            
            <div className="flex items-center gap-6 text-sm text-slate-600 font-medium">
               <div className="flex items-center gap-2 text-amber-600 bg-amber-50 px-3 py-1.5 rounded-lg border border-amber-100">
                  <Clock className="w-4 h-4" /> Due: {new Date(assignment.due_date).toLocaleString()}
               </div>
               <div className="flex items-center gap-2">
                  <FileText className="w-4 h-4" /> Faculty ID: {assignment.faculty_id}
               </div>
            </div>
         </div>
         
         <div className="p-8 space-y-8">
            <div>
               <h3 className="text-lg font-bold text-slate-900 mb-3 border-b border-slate-100 pb-2">Instructions</h3>
               <div className="prose prose-slate max-w-none text-slate-600 whitespace-pre-wrap">
                  {assignment.description}
                  {assignment.file_url && (
                     <div className="mt-6">
                        <a href={`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}${assignment.file_url}`} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 bg-indigo-50 text-indigo-700 px-4 py-2 rounded-lg font-bold">
                           <FileText className="w-5 h-5" /> View Attached PDF
                        </a>
                     </div>
                  )}
               </div>
            </div>
         </div>
      </div>
      

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
                       <td className="py-4 font-mono text-slate-600 text-sm">{sub.enrollment}
                          {sub.file_url && <a href={`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}${sub.file_url}`} target="_blank" className="block text-indigo-600 text-xs font-bold mt-1 hover:underline">View PDF</a>}
                       </td>
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
                                  await axios.post(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/assignments/submissions/${sub.id}/grade`, {marks}, {headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}});
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
    
      {user?.role === 'student' && (
        <div className="bg-white rounded-3xl shadow-sm border border-slate-100 p-8">
           <h3 className="text-lg font-bold text-slate-900 mb-6 border-b border-slate-100 pb-2">Your Work</h3>
           
           {submission ? (
             <div className="bg-emerald-50 border border-emerald-100 rounded-2xl p-6 text-center space-y-3">
                <div className="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto mb-2">
                   <CheckCircle className="w-8 h-8" />
                </div>
                <h4 className="font-bold text-emerald-800 text-lg">Assignment Submitted</h4>
                <p className="text-emerald-600 text-sm font-medium">Submitted on {new Date(submission.submitted_at).toLocaleString()}</p>
                <button disabled className="mt-4 bg-emerald-600 text-white px-6 py-2.5 rounded-xl font-medium shadow-md opacity-80 cursor-not-allowed">
                   View Submission
                </button>
             </div>
           ) : (
             <div className="border-2 border-dashed border-slate-200 rounded-2xl p-10 text-center hover:bg-slate-50 transition-colors">
                <UploadCloud className="w-12 h-12 text-slate-400 mx-auto mb-4" />
                <h4 className="font-bold text-slate-700 mb-1">Upload your submission</h4>
                <input type="file" accept=".pdf" onChange={e => setFile(e.target.files?.[0] || null)} className="mb-6 border border-slate-200 p-2 rounded-lg" />
                <br/>
                <button 
                  onClick={handleSubmit} 
                  disabled={submitting}
                  className="bg-indigo-600 hover:bg-indigo-700 text-white px-8 py-3 rounded-xl font-bold shadow-md transition-all flex items-center gap-2 mx-auto"
                >
                  {submitting ? "Submitting..." : "Submit Assignment"}
                </button>
             </div>
           )}
        </div>
      )}
    </div>
  );
}
