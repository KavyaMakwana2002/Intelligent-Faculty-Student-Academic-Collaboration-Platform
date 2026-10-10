import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import Layout from './components/layout/Layout';
import Landing from './pages/Landing';
import Login from './pages/auth/Login';
import StudentDashboard from './pages/dashboard/StudentDashboard';
import FacultyDashboard from './pages/dashboard/FacultyDashboard';
import AdminDashboard from './pages/dashboard/AdminDashboard';

// Placeholder Pages
const Placeholder = ({ title }: { title: string }) => (
  <div className="bg-white p-8 rounded-xl shadow-sm border border-slate-100 h-full flex flex-col items-center justify-center">
    <h1 className="text-2xl font-bold text-slate-800 mb-2">{title}</h1>
    <p className="text-slate-500">This page is under construction for the demo.</p>
  </div>
);

const Courses = () => <Placeholder title="Courses" />;
const Assignments = () => <Placeholder title="Assignments" />;
const Materials = () => <Placeholder title="Study Materials" />;
const Announcements = () => <Placeholder title="Announcements" />;
const Discussions = () => <Placeholder title="Discussions" />;
const Calendar = () => <Placeholder title="Academic Calendar" />;
const Analytics = () => <Placeholder title="Analytics" />;
const Notifications = () => <Placeholder title="Notifications" />;
const Profile = () => <Placeholder title="Profile" />;
const Settings = () => <Placeholder title="Settings" />;
const NotFound = () => <Placeholder title="404 - Not Found" />;

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
      <Route path="/register" element={<Login />} />
      
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
        <Route path="/materials" element={<ProtectedRoute><Materials /></ProtectedRoute>} />
        <Route path="/announcements" element={<ProtectedRoute><Announcements /></ProtectedRoute>} />
        <Route path="/discussions" element={<ProtectedRoute><Discussions /></ProtectedRoute>} />
        <Route path="/calendar" element={<ProtectedRoute><Calendar /></ProtectedRoute>} />
        <Route path="/analytics" element={<ProtectedRoute><Analytics /></ProtectedRoute>} />
        <Route path="/notifications" element={<ProtectedRoute><Notifications /></ProtectedRoute>} />
        <Route path="/profile" element={<ProtectedRoute><Profile /></ProtectedRoute>} />
        <Route path="/settings" element={<ProtectedRoute><Settings /></ProtectedRoute>} />
        <Route path="*" element={<NotFound />} />
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
