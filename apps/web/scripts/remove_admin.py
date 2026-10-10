import os
import re

frontend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web"
backend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\services\api"

# 1. Update App.tsx
app_path = os.path.join(frontend_dir, "src/App.tsx")
with open(app_path, "r", encoding="utf-8") as f: app_content = f.read()

# Remove import
app_content = re.sub(r"import AdminDashboard from '\./pages/dashboard/AdminDashboard';\n?", "", app_content)
app_content = re.sub(r"import AdminDashboard from '\./pages/AdminDashboard';\n?", "", app_content)

# Fix dashboard route
app_content = app_content.replace("{user?.role === 'admin' && <AdminDashboard />}", "")
app_content = app_content.replace("{user?.role === 'admin' ? <AdminDashboard /> : user?.role === 'student' ? <StudentDashboard /> : <FacultyDashboard />}", "{user?.role === 'student' ? <StudentDashboard /> : <FacultyDashboard />}")

with open(app_path, "w", encoding="utf-8") as f: f.write(app_content)


# 2. Update Login.tsx
login_path = os.path.join(frontend_dir, "src/pages/auth/Login.tsx")
with open(login_path, "r", encoding="utf-8") as f: login_content = f.read()

# Remove type definition for admin
login_content = login_content.replace("'student' | 'faculty' | 'admin' | null", "'student' | 'faculty' | null")

# Remove admin payload logic
login_content = re.sub(
    r"const payload = role === 'admin'\s*\?\s*\{\s*role,\s*email,\s*password\s*\}\s*:\s*\{\s*role,\s*identifier,\s*password\s*\};",
    "const payload = { role, identifier, password };",
    login_content
)

# Remove Admin button
admin_btn_regex = r"<button onClick=\{\(\) => setRole\('admin'\)\}.*?</button>"
login_content = re.sub(admin_btn_regex, "", login_content, flags=re.DOTALL)

# Clean up input labels and types
login_content = login_content.replace("{role === 'admin' && \"Email Address\"}", "")
login_content = login_content.replace("type={role === 'admin' ? \"email\" : \"text\"}", "type=\"text\"")
login_content = login_content.replace("value={role === 'admin' ? email : identifier}", "value={identifier}")
login_content = login_content.replace("onChange={(e) => role === 'admin' ? setEmail(e.target.value) : setIdentifier(e.target.value)}", "onChange={(e) => setIdentifier(e.target.value)}")

with open(login_path, "w", encoding="utf-8") as f: f.write(login_content)


# 3. Update seed.js
seed_path = os.path.join(backend_dir, "seed.js")
with open(seed_path, "r", encoding="utf-8") as f: seed_content = f.read()
seed_content = re.sub(r"// Admin\s*db\.run\(`INSERT INTO users.*?`\);\s*", "", seed_content)
with open(seed_path, "w", encoding="utf-8") as f: f.write(seed_content)

print("Admin removed completely.")
