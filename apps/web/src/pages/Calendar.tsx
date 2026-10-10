
export default function Calendar() {
  return (
    <div className="max-w-5xl mx-auto space-y-6 animate-fade-in-up pb-10">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-900">Academic Calendar</h1>
          <p className="text-slate-500 font-medium mt-1">BCA Academic Calendar 2026-2027</p>
        </div>
        <a href="/Academic_Calendar.pdf" download className="bg-indigo-600 text-white px-5 py-2.5 rounded-xl font-bold hover:bg-indigo-700 transition shadow-sm">
          Download PDF
        </a>
      </div>
      
      <div className="bg-white rounded-3xl shadow-sm border border-slate-100 p-2 overflow-hidden h-[800px]">
         <object 
            data="/Academic_Calendar.pdf" 
            type="application/pdf" 
            width="100%" 
            height="100%"
            className="rounded-2xl"
         >
            <div className="flex flex-col items-center justify-center h-full text-slate-500">
               <p className="mb-4 font-bold text-lg">Your browser doesn't support PDF viewing.</p>
               <a href="/Academic_Calendar.pdf" target="_blank" className="text-indigo-600 underline font-semibold">Click here to view the PDF</a>
            </div>
         </object>
      </div>
    </div>
  );
}
