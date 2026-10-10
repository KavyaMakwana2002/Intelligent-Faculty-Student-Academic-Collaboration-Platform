import os
import re

backend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\services\api"
frontend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web"

# Create uploads folder
uploads_dir = os.path.join(backend_dir, "uploads")
os.makedirs(uploads_dir, exist_ok=True)

# 1. Create upload middleware
upload_js = """const multer = require('multer');
const path = require('path');
const storage = multer.diskStorage({
    destination: (req, file, cb) => cb(null, 'uploads/'),
    filename: (req, file, cb) => cb(null, Date.now() + path.extname(file.originalname))
});
module.exports = multer({ storage });
"""
with open(os.path.join(backend_dir, "middleware", "upload.js"), "w", encoding="utf-8") as f:
    f.write(upload_js)

# 2. Update index.js to serve uploads
index_path = os.path.join(backend_dir, "index.js")
with open(index_path, "r", encoding="utf-8") as f: idx_content = f.read()
if "express.static" not in idx_content:
    idx_content = idx_content.replace(
        "app.use(express.json());",
        "app.use(express.json());\nconst path = require('path');\napp.use('/uploads', express.static(path.join(__dirname, 'uploads')));"
    )
    with open(index_path, "w", encoding="utf-8") as f: f.write(idx_content)

# 3. DB Schema modification (assignments table needs file_url column if not exists)
# wait, assignments table doesn't have file_url. Let's add it via ALTER TABLE.
db_path = os.path.join(backend_dir, "db.js")
with open(db_path, "r", encoding="utf-8") as f: db_content = f.read()
if "ALTER TABLE assignments ADD COLUMN file_url TEXT" not in db_content:
    db_content = db_content.replace(
        "db.run(`ALTER TABLE assignments ADD COLUMN subject TEXT`, (err) => {",
        "db.run(`ALTER TABLE assignments ADD COLUMN file_url TEXT`, (err) => {});\n        db.run(`ALTER TABLE assignments ADD COLUMN subject TEXT`, (err) => {"
    )
    # Also update the CREATE TABLE for future
    if "subject TEXT\n" in db_content and "file_url TEXT" not in db_content.split("CREATE TABLE IF NOT EXISTS assignments")[1].split(")")[0]:
        db_content = db_content.replace("subject TEXT\n            )", "subject TEXT,\n                file_url TEXT\n            )")
    with open(db_path, "w", encoding="utf-8") as f: f.write(db_content)

# 4. Update Backend Routes
ar_path = os.path.join(backend_dir, "routes", "assignmentRoutes.js")
with open(ar_path, "r", encoding="utf-8") as f: ar_content = f.read()
if "upload.single('file')" not in ar_content:
    ar_content = "const upload = require('../middleware/upload');\n" + ar_content
    ar_content = ar_content.replace("router.post('/', auth, assignmentController.createAssignment);", "router.post('/', auth, upload.single('file'), assignmentController.createAssignment);")
    ar_content = ar_content.replace("router.post('/:id/submit', auth, assignmentController.submitAssignment);", "router.post('/:id/submit', auth, upload.single('file'), assignmentController.submitAssignment);")
    with open(ar_path, "w", encoding="utf-8") as f: f.write(ar_content)

mr_path = os.path.join(backend_dir, "routes", "materialRoutes.js")
with open(mr_path, "r", encoding="utf-8") as f: mr_content = f.read()
if "upload.single('file')" not in mr_content:
    mr_content = "const upload = require('../middleware/upload');\n" + mr_content
    mr_content = mr_content.replace("router.post('/', auth, materialController.uploadMaterial);", "router.post('/', auth, upload.single('file'), materialController.uploadMaterial);")
    with open(mr_path, "w", encoding="utf-8") as f: f.write(mr_content)

# 5. Update Backend Controllers
ac_path = os.path.join(backend_dir, "controllers", "assignmentController.js")
with open(ac_path, "r", encoding="utf-8") as f: ac_content = f.read()
if "const file_url = req.file" not in ac_content:
    # Update createAssignment
    ac_content = ac_content.replace(
        "const { title, course, semester, marks, due_date, description, subject } = req.body;",
        "const { title, course, semester, marks, due_date, description, subject } = req.body;\n    const file_url = req.file ? '/uploads/' + req.file.filename : null;"
    )
    ac_content = ac_content.replace(
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    )
    ac_content = ac_content.replace(
        "[title, course, semester, marks, due_date, description, faculty_id, subject]",
        "[title, course, semester, marks, due_date, description, faculty_id, subject, file_url]"
    )
    ac_content = ac_content.replace(
        "faculty_id INTEGER,\n            status TEXT DEFAULT 'Pending',\n            subject TEXT",
        "faculty_id INTEGER,\n            status TEXT DEFAULT 'Pending',\n            subject TEXT,\n            file_url TEXT"
    )
    ac_content = ac_content.replace(
        "subject TEXT)`)",
        "subject TEXT, file_url TEXT)`)"
    )
    # The above replace for query might fail if it doesn't match exactly. Let's use regex:
    ac_content = re.sub(
        r"const stmt = db\.prepare\('INSERT INTO assignments \([^)]+\) VALUES \([^)]+\)'\);[\s\S]*?stmt\.run\(\[.*?\]",
        "const stmt = db.prepare('INSERT INTO assignments (title, course, semester, marks, due_date, description, faculty_id, subject, file_url) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)');\n        stmt.run([title, course, semester, marks, due_date, description, faculty_id, subject, file_url]",
        ac_content
    )
    
    # Update submitAssignment
    ac_content = ac_content.replace(
        "const { file_url } = req.body;",
        "const file_url = req.file ? '/uploads/' + req.file.filename : req.body.file_url;"
    )
    with open(ac_path, "w", encoding="utf-8") as f: f.write(ac_content)

mc_path = os.path.join(backend_dir, "controllers", "materialController.js")
with open(mc_path, "r", encoding="utf-8") as f: mc_content = f.read()
if "const file_url = req.file" not in mc_content:
    mc_content = mc_content.replace(
        "const { title, course, semester, description, file_url } = req.body;",
        "const { title, course, semester, description } = req.body;\n    const file_url = req.file ? '/uploads/' + req.file.filename : null;"
    )
    with open(mc_path, "w", encoding="utf-8") as f: f.write(mc_content)


# --- FRONTEND CHANGES ---

# 1. CreateAssignment.tsx
ca_path = os.path.join(frontend_dir, "src/pages/CreateAssignment.tsx")
with open(ca_path, "r", encoding="utf-8") as f: ca_content = f.read()
if "const [file, setFile] = useState<File | null>(null);" not in ca_content:
    ca_content = ca_content.replace("const [subject, setSubject] = useState('');", "const [subject, setSubject] = useState('');\n  const [file, setFile] = useState<File | null>(null);")
    
    # Replace axios POST
    axios_old = """      await axios.post('http://localhost:5000/api/assignments', {
        title, course, semester, subject, marks: Number(marks), due_date: dueDate, description
      }, {
        headers: { Authorization: `Bearer ${token}` }
      });"""
    axios_new = """      const formData = new FormData();
      formData.append('title', title);
      formData.append('course', course);
      formData.append('semester', semester);
      formData.append('subject', subject);
      formData.append('marks', marks);
      formData.append('due_date', dueDate);
      formData.append('description', description);
      if (file) formData.append('file', file);
      
      await axios.post('http://localhost:5000/api/assignments', formData, {
        headers: { 
           Authorization: `Bearer ${token}`,
           'Content-Type': 'multipart/form-data'
        }
      });"""
    ca_content = ca_content.replace(axios_old, axios_new)
    
    # Add file input UI
    ui_old = """            <div>
              <label className="block text-sm font-bold text-slate-700 mb-2">Instructions</label>"""
    ui_new = """            <div>
              <label className="block text-sm font-bold text-slate-700 mb-2">Attach PDF (Optional)</label>
              <input type="file" accept=".pdf" onChange={(e) => setFile(e.target.files?.[0] || null)} className="w-full p-3 border border-slate-200 rounded-xl" />
            </div>
            <div>
              <label className="block text-sm font-bold text-slate-700 mb-2">Instructions</label>"""
    ca_content = ca_content.replace(ui_old, ui_new)
    with open(ca_path, "w", encoding="utf-8") as f: f.write(ca_content)


# 2. AssignmentDetails.tsx
ad_path = os.path.join(frontend_dir, "src/pages/AssignmentDetails.tsx")
with open(ad_path, "r", encoding="utf-8") as f: ad_content = f.read()
if "const [file, setFile] = useState<File | null>(null);" not in ad_content:
    ad_content = ad_content.replace("const [submitting, setSubmitting] = useState(false);", "const [submitting, setSubmitting] = useState(false);\n  const [file, setFile] = useState<File | null>(null);")
    
    # Replace submit handler
    submit_old = """      await axios.post(`http://localhost:5000/api/assignments/${id}/submit`, {
        file_url: 'https://example.com/submission.pdf'
      }, {"""
    submit_new = """      const formData = new FormData();
      if (file) formData.append('file', file);
      
      await axios.post(`http://localhost:5000/api/assignments/${id}/submit`, formData, {"""
    ad_content = ad_content.replace(submit_old, submit_new)
    
    # Also update headers
    ad_content = ad_content.replace("headers: { Authorization: `Bearer ${token}` }", "headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'multipart/form-data' }")
    
    # Update UI to include file input
    ui_old = """                <UploadCloud className="w-12 h-12 text-slate-400 mx-auto mb-4" />
                <h4 className="font-bold text-slate-700 mb-1">Upload your submission</h4>
                <p className="text-slate-500 text-sm mb-6 max-w-sm mx-auto">Click below to submit your assignment. Note: Due to hackathon constraints, this will simulate a file upload.</p>
                <button 
                  onClick={handleSubmit} """
    ui_new = """                <UploadCloud className="w-12 h-12 text-slate-400 mx-auto mb-4" />
                <h4 className="font-bold text-slate-700 mb-1">Upload your submission</h4>
                <input type="file" accept=".pdf" onChange={e => setFile(e.target.files?.[0] || null)} className="mb-6 border border-slate-200 p-2 rounded-lg" />
                <br/>
                <button 
                  onClick={handleSubmit} """
    ad_content = ad_content.replace(ui_old, ui_new)
    
    # Show PDF link if assignment has file_url
    if "assignment.description}" in ad_content:
       ad_content = ad_content.replace("{assignment.description}", """{assignment.description}
                  {assignment.file_url && (
                     <div className="mt-6">
                        <a href={`http://localhost:5000${assignment.file_url}`} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 bg-indigo-50 text-indigo-700 px-4 py-2 rounded-lg font-bold">
                           <FileText className="w-5 h-5" /> View Attached PDF
                        </a>
                     </div>
                  )}""")

    # Show PDF link for student submissions in faculty view
    if "sub.enrollment}</td>" in ad_content:
        ad_content = ad_content.replace("<td className=\"py-4 font-mono text-slate-600 text-sm\">{sub.enrollment}</td>", """<td className="py-4 font-mono text-slate-600 text-sm">{sub.enrollment}
                          {sub.file_url && <a href={`http://localhost:5000${sub.file_url}`} target="_blank" className="block text-indigo-600 text-xs font-bold mt-1 hover:underline">View PDF</a>}
                       </td>""")
    
    with open(ad_path, "w", encoding="utf-8") as f: f.write(ad_content)


# 3. Materials.tsx
mat_path = os.path.join(frontend_dir, "src/pages/Materials.tsx")
with open(mat_path, "r", encoding="utf-8") as f: mat_content = f.read()
if "const [file, setFile] = useState<File | null>(null);" not in mat_content:
    mat_content = mat_content.replace("const [description, setDescription] = useState('');", "const [description, setDescription] = useState('');\n  const [file, setFile] = useState<File | null>(null);")
    
    axios_old = """      await axios.post('http://localhost:5000/api/materials', {
         title, course, semester, description, file_url: 'https://example.com/notes.pdf'
      }, { headers: { Authorization: `Bearer ${token}` } });"""
    axios_new = """      const formData = new FormData();
      formData.append('title', title);
      formData.append('course', course);
      formData.append('semester', semester);
      formData.append('description', description);
      if (file) formData.append('file', file);
      
      await axios.post('http://localhost:5000/api/materials', formData, { headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'multipart/form-data' } });"""
    mat_content = mat_content.replace(axios_old, axios_new)
    
    ui_old = """<textarea required value={description} onChange={e=>setDescription(e.target.value)} placeholder="Description..." className="w-full p-3 border border-slate-200 rounded-xl"></textarea>"""
    ui_new = """<textarea required value={description} onChange={e=>setDescription(e.target.value)} placeholder="Description..." className="w-full p-3 border border-slate-200 rounded-xl"></textarea>
              <input type="file" required accept=".pdf" onChange={e => setFile(e.target.files?.[0] || null)} className="w-full p-3 border border-slate-200 rounded-xl" />"""
    mat_content = mat_content.replace(ui_old, ui_new)
    
    dl_old = """<button className="text-indigo-600 font-bold text-sm flex items-center gap-1 group-hover:text-indigo-700"><Download className="w-4 h-4" /> Download</button>"""
    dl_new = """<a href={`http://localhost:5000${mat.file_url}`} target="_blank" className="text-indigo-600 font-bold text-sm flex items-center gap-1 group-hover:text-indigo-700"><Download className="w-4 h-4" /> View/Download</a>"""
    mat_content = mat_content.replace(dl_old, dl_new)
    
    with open(mat_path, "w", encoding="utf-8") as f: f.write(mat_content)

print("Multer implementation complete.")
