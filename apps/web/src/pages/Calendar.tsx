
export default function Calendar() {
  return (
    <div className="max-w-4xl mx-auto space-y-6 animate-fade-in-up pb-10">
      <h1 className="text-3xl font-extrabold text-slate-900 mb-8">Academic Calendar</h1>
      <div className="bg-white rounded-3xl shadow-sm border border-slate-100 p-8">
         <div className="grid grid-cols-7 gap-4 mb-4 text-center font-bold text-slate-500 text-sm">
            <div>Mon</div><div>Tue</div><div>Wed</div><div>Thu</div><div>Fri</div><div>Sat</div><div>Sun</div>
         </div>
         <div className="grid grid-cols-7 gap-4">
            {Array.from({length: 30}).map((_, i) => (
               <div key={i} className={`h-24 rounded-2xl border ${i===15 ? 'bg-indigo-50 border-indigo-200' : 'border-slate-100'} p-2 hover:border-indigo-300 transition-colors relative group`}>
                  <span className={`font-bold ${i===15 ? 'text-indigo-600' : 'text-slate-700'}`}>{i+1}</span>
                  {i===15 && <div className="mt-2 text-[10px] font-bold bg-indigo-600 text-white p-1 rounded-md leading-tight">Hackathon Submission</div>}
                  {i===18 && <div className="mt-2 text-[10px] font-bold bg-rose-500 text-white p-1 rounded-md leading-tight">Assignment Due</div>}
               </div>
            ))}
         </div>
      </div>
    </div>
  );
}
