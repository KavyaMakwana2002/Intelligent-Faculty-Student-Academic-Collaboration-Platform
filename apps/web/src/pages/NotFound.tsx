import { Link } from 'react-router-dom';

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-slate-50 text-center px-4">
      <h1 className="text-9xl font-black text-slate-200 mb-4">404</h1>
      <h2 className="text-3xl font-bold text-slate-800 mb-6">Page Not Found</h2>
      <p className="text-slate-500 mb-8 max-w-md">The page you are looking for doesn't exist or has been moved.</p>
      <Link to="/" className="bg-indigo-600 text-white px-8 py-3 rounded-xl font-bold hover:bg-indigo-700 transition shadow-md">
        Go Back Home
      </Link>
    </div>
  );
}
