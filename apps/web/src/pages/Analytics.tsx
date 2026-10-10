import { BarChart2 } from 'lucide-react';

export default function Analytics() {
  return (
    <div className="flex flex-col items-center justify-center h-[70vh] text-center animate-fade-in-up">
      <div className="w-24 h-24 bg-indigo-50 text-indigo-600 rounded-3xl flex items-center justify-center mb-6 shadow-sm border border-indigo-100 transform rotate-3">
        <BarChart2 className="w-12 h-12" />
      </div>
      <h1 className="text-3xl font-extrabold text-slate-900 mb-4">Platform Analytics</h1>
      <p className="text-slate-500 max-w-md text-lg">This section is currently under construction for Phase 2 of the hackathon.</p>
    </div>
  );
}
