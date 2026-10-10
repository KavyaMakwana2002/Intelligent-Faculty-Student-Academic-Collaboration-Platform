import os

base_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web"

directories = [
    "src/components",
    "src/components/layout",
    "src/components/ui",
    "src/pages",
    "src/pages/dashboard",
    "src/pages/auth",
    "src/services",
    "src/types",
    "src/lib",
    "src/contexts"
]

for d in directories:
    os.makedirs(os.path.join(base_dir, d), exist_ok=True)

# index.css
index_css = """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  body {
    @apply bg-slate-50 text-slate-900;
  }
}
"""

with open(os.path.join(base_dir, "src/index.css"), "w") as f:
    f.write(index_css)

# tailwind.config.js
tailwind_config = """/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eef2ff',
          100: '#e0e7ff',
          500: '#6366f1',
          600: '#4f46e5',
          700: '#4338ca',
          900: '#312e81',
        },
      }
    },
  },
  plugins: [],
}
"""
with open(os.path.join(base_dir, "tailwind.config.js"), "w") as f:
    f.write(tailwind_config)

# utils.ts
utils_ts = """import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
"""
with open(os.path.join(base_dir, "src/lib/utils.ts"), "w") as f:
    f.write(utils_ts)

# types/index.ts
types_ts = """export type Role = 'student' | 'faculty' | 'admin';

export interface User {
  id: string;
  name: string;
  email: string;
  role: Role;
  avatar?: string;
}
"""
with open(os.path.join(base_dir, "src/types/index.ts"), "w") as f:
    f.write(types_ts)

# App.tsx
app_tsx = """import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import Layout from './components/layout/Layout';
import Landing from './pages/Landing';
import Login from './pages/auth/Login';
import StudentDashboard from './pages/dashboard/StudentDashboard';
import FacultyDashboard from './pages/dashboard/FacultyDashboard';
import AdminDashboard from './pages/dashboard/AdminDashboard';
import Courses from './pages/Courses';
import Assignments from './pages/Assignments';

const ProtectedRoute = ({ children, allowedRoles }: { children: React.ReactNode, allowedRoles?: string[] }) => {
  const { user } = useAuth();
  if (!user) return <Navigate to="/login" replace />;
  if (allowedRoles && !allowedRoles.includes(user.role)) return <Navigate to="/unauthorized" replace />;
  return <>{children}</>;
};

function AppRoutes() {
  const { user } = useAuth();
  
  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/login" element={<Login />} />
      
      <Route element={<Layout />}>
        {/* Dashboards based on role */}
        <Route path="/dashboard" element={
          <ProtectedRoute>
            {user?.role === 'student' && <StudentDashboard />}
            {user?.role === 'faculty' && <FacultyDashboard />}
            {user?.role === 'admin' && <AdminDashboard />}
          </ProtectedRoute>
        } />
        
        <Route path="/courses" element={<ProtectedRoute><Courses /></ProtectedRoute>} />
        <Route path="/assignments" element={<ProtectedRoute><Assignments /></ProtectedRoute>} />
        {/* Add more routes here */}
      </Route>
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
with open(os.path.join(base_dir, "src/App.tsx"), "w") as f:
    f.write(app_tsx)

print("Scaffolding complete.")
