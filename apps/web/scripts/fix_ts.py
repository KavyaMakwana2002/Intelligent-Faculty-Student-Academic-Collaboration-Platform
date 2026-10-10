import os

frontend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web"

# 1. Layout.tsx
f_path = os.path.join(frontend_dir, "src/components/layout/Layout.tsx")
with open(f_path, "r", encoding="utf-8") as f: content = f.read()
content = content.replace("user.name.charAt(0)", "user?.name?.charAt(0) || 'U'")
with open(f_path, "w", encoding="utf-8") as f: f.write(content)

# 2. AuthContext.tsx
f_path = os.path.join(frontend_dir, "src/contexts/AuthContext.tsx")
with open(f_path, "r", encoding="utf-8") as f: content = f.read()
content = content.replace("import { createContext, useContext, useState, ReactNode, useEffect } from 'react';", "import { createContext, useContext, useState, useEffect } from 'react';\nimport type { ReactNode } from 'react';")
with open(f_path, "w", encoding="utf-8") as f: f.write(content)

# 3. Assignments.tsx
f_path = os.path.join(frontend_dir, "src/pages/Assignments.tsx")
with open(f_path, "r", encoding="utf-8") as f: content = f.read()
content = content.replace(", Filter } from 'lucide-react';", " } from 'lucide-react';")
with open(f_path, "w", encoding="utf-8") as f: f.write(content)

# 4. Profile.tsx
f_path = os.path.join(frontend_dir, "src/pages/Profile.tsx")
with open(f_path, "r", encoding="utf-8") as f: content = f.read()
content = content.replace("import { User, Mail, GraduationCap, Phone, ShieldCheck, Briefcase, BookOpen, Clock, Calendar } from 'lucide-react';", "import { User, Mail, GraduationCap, ShieldCheck, Briefcase, BookOpen, Clock, Calendar } from 'lucide-react';")
with open(f_path, "w", encoding="utf-8") as f: f.write(content)

# 5. Settings.tsx
f_path = os.path.join(frontend_dir, "src/pages/Settings.tsx")
with open(f_path, "r", encoding="utf-8") as f: content = f.read()
content = content.replace("  const { user } = useAuth();\n  \n  // Theme state", "  // Theme state")
content = content.replace("import { useAuth } from '../contexts/AuthContext';", "")
with open(f_path, "w", encoding="utf-8") as f: f.write(content)

print("Fixed TS errors")
