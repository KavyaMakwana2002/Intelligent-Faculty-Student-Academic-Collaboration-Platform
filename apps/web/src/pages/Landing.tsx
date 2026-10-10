import { ArrowRight, Bot, BookOpen, Sparkles, ShieldCheck } from 'lucide-react';
import { Link } from 'react-router-dom';

export default function Landing() {
  return (
    <div className="min-h-screen bg-[#0f172a] text-white overflow-hidden relative">
      {/* Animated Background Gradients */}
      <div className="absolute top-[-20%] left-[-10%] w-[50%] h-[50%] bg-indigo-600/30 blur-[120px] rounded-full animate-pulse-slow pointer-events-none"></div>
      <div className="absolute bottom-[-20%] right-[-10%] w-[50%] h-[50%] bg-purple-600/30 blur-[120px] rounded-full animate-pulse-slow pointer-events-none" style={{animationDelay: '2s'}}></div>

      {/* Navbar */}
      <nav className="relative z-10 flex justify-between items-center p-8 max-w-7xl mx-auto">
        <div className="flex items-center gap-3">
           <div className="w-12 h-12 bg-gradient-to-br from-indigo-500 to-purple-500 rounded-xl flex items-center justify-center shadow-lg shadow-indigo-500/30">
              <BookOpen className="w-6 h-6 text-white" />
           </div>
           <span className="text-2xl font-black tracking-tight">EduConnect <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-purple-400">AI</span></span>
        </div>
        <div className="flex gap-4">
          <Link to="/login" className="px-6 py-2.5 font-bold text-slate-300 hover:text-white transition">Sign In</Link>
          <Link to="/register" className="bg-white text-slate-900 px-6 py-2.5 rounded-full font-bold hover:scale-105 transition-transform shadow-xl">Get Started</Link>
        </div>
      </nav>

      {/* Hero Section */}
      <main className="relative z-10 flex flex-col items-center text-center px-4 pt-20 pb-32 max-w-5xl mx-auto animate-fade-in-up">
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-300 font-bold text-sm mb-8">
           <Sparkles className="w-4 h-4" /> Ganpat University Hackathon 2026 (PS-04)
        </div>
        
        <h1 className="text-6xl md:text-8xl font-black tracking-tighter mb-8 leading-[1.1]">
          The Future of <br/>
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-purple-400 to-pink-400">Academic Collaboration</span>
        </h1>
        
        <p className="text-xl text-slate-400 mb-12 max-w-2xl font-medium leading-relaxed">
          An intelligent platform uniting faculty and students with smart assignments, AI doubt-solving, explainable risk indicators, and secure workflows.
        </p>
        
        <div className="flex flex-col sm:flex-row gap-4">
          <Link to="/register" className="bg-gradient-to-r from-indigo-600 to-purple-600 px-8 py-4 rounded-full font-bold text-lg hover:scale-105 transition-transform shadow-lg shadow-indigo-500/25 flex items-center justify-center gap-2">
            Explore Platform <ArrowRight className="w-5 h-5" />
          </Link>
        </div>

        {/* Glassmorphism Feature Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-24 text-left w-full">
           <div className="glass-dark p-8 rounded-3xl relative overflow-hidden group">
              <div className="absolute top-0 right-0 w-32 h-32 bg-indigo-500/10 rounded-full blur-2xl group-hover:bg-indigo-500/20 transition-all"></div>
              <Bot className="w-10 h-10 text-indigo-400 mb-6" />
              <h3 className="text-xl font-bold mb-2">AI Study Assistant</h3>
              <p className="text-slate-400">Context-aware AI helping students resolve doubts instantly based on course materials.</p>
           </div>
           <div className="glass-dark p-8 rounded-3xl relative overflow-hidden group">
              <div className="absolute top-0 right-0 w-32 h-32 bg-purple-500/10 rounded-full blur-2xl group-hover:bg-purple-500/20 transition-all"></div>
              <ShieldCheck className="w-10 h-10 text-purple-400 mb-6" />
              <h3 className="text-xl font-bold mb-2">Secure Submissions</h3>
              <p className="text-slate-400">Role-based access control ensuring students only see what belongs to their semester.</p>
           </div>
           <div className="glass-dark p-8 rounded-3xl relative overflow-hidden group">
              <div className="absolute top-0 right-0 w-32 h-32 bg-pink-500/10 rounded-full blur-2xl group-hover:bg-pink-500/20 transition-all"></div>
              <BookOpen className="w-10 h-10 text-pink-400 mb-6" />
              <h3 className="text-xl font-bold mb-2">Risk Indicators</h3>
              <p className="text-slate-400">Predictive analytics warning students of overdue tasks before they fail.</p>
           </div>
        </div>
      </main>
    </div>
  );
}
