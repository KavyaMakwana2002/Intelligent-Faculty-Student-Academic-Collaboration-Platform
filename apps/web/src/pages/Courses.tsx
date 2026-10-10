import { Book, Users, Star, ChevronRight } from 'lucide-react';

export default function Courses() {
  const courses = [
    { id: 1, name: "Advanced Web Development", code: "CS401", students: 120, rating: 4.8, color: "from-blue-500 to-indigo-600" },
    { id: 2, name: "Database Management Systems", code: "CS302", students: 85, rating: 4.6, color: "from-emerald-500 to-teal-600" },
    { id: 3, name: "Artificial Intelligence", code: "CS505", students: 150, rating: 4.9, color: "from-purple-500 to-pink-600" },
    { id: 4, name: "Data Structures", code: "CS201", students: 210, rating: 4.5, color: "from-amber-500 to-orange-600" },
  ];

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-slate-900">My Courses</h1>
        <button className="bg-indigo-600 text-white px-5 py-2 rounded-xl font-medium hover:bg-indigo-700 transition shadow-md">Browse Catalog</button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
        {courses.map(course => (
          <div key={course.id} className="bg-white rounded-3xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 overflow-hidden group hover:-translate-y-1">
            <div className={`h-32 bg-gradient-to-r ${course.color} p-6 flex flex-col justify-between relative overflow-hidden`}>
               <div className="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full translate-x-8 -translate-y-8 blur-2xl"></div>
               <span className="bg-white/20 text-white text-xs font-bold px-3 py-1 rounded-full w-fit backdrop-blur-sm">{course.code}</span>
            </div>
            <div className="p-6 relative">
              <div className="w-12 h-12 bg-white rounded-2xl shadow-md absolute -top-6 flex items-center justify-center text-indigo-600">
                <Book className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold text-slate-900 mt-4 mb-2 group-hover:text-indigo-600 transition-colors">{course.name}</h3>
              
              <div className="flex items-center gap-4 text-sm text-slate-500 mt-4">
                <div className="flex items-center gap-1"><Users className="w-4 h-4" /> {course.students}</div>
                <div className="flex items-center gap-1 text-amber-500"><Star className="w-4 h-4 fill-current" /> {course.rating}</div>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-100 flex justify-between items-center">
                 <div className="w-full bg-slate-100 rounded-full h-2 mr-4">
                    <div className="bg-indigo-500 h-2 rounded-full" style={{width: '65%'}}></div>
                 </div>
                 <button className="p-2 text-indigo-600 hover:bg-indigo-50 rounded-full transition"><ChevronRight className="w-5 h-5" /></button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
