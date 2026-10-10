import os

frontend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web"

# 1. AiChatWidget.tsx
f_path = os.path.join(frontend_dir, "src/components/AiChatWidget.tsx")
with open(f_path, "r", encoding="utf-8") as f: content = f.read()
content = content.replace("import { MessageSquare, X, Send, Bot, Sparkles } from 'lucide-react';", "import { X, Send, Bot, Sparkles } from 'lucide-react';")
with open(f_path, "w", encoding="utf-8") as f: f.write(content)

# 2. FacultyDashboard.tsx
f_path = os.path.join(frontend_dir, "src/pages/FacultyDashboard.tsx")
with open(f_path, "r", encoding="utf-8") as f: content = f.read()
content = content.replace("import { Book, Users, FileText, CheckCircle } from 'lucide-react';", "import { Book, Users, FileText } from 'lucide-react';")
with open(f_path, "w", encoding="utf-8") as f: f.write(content)

# 3. Materials.tsx
f_path = os.path.join(frontend_dir, "src/pages/Materials.tsx")
with open(f_path, "r", encoding="utf-8") as f: content = f.read()
content = content.replace("import { FileText, Download, Plus, Search } from 'lucide-react';", "import { FileText, Download, Plus } from 'lucide-react';")
with open(f_path, "w", encoding="utf-8") as f: f.write(content)

# 4. StudentDashboard.tsx
f_path = os.path.join(frontend_dir, "src/pages/StudentDashboard.tsx")
with open(f_path, "r", encoding="utf-8") as f: content = f.read()
content = content.replace("import { Link } from 'react-router-dom';", "")
content = content.replace("user?.name.split(' ')[0]", "user?.name?.split(' ')[0] || 'Student'")
with open(f_path, "w", encoding="utf-8") as f: f.write(content)

print("Fixed TS errors")
