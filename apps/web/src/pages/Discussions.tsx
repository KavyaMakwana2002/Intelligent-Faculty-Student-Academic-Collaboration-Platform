import { MessageSquare, ThumbsUp, Reply } from 'lucide-react';

export default function Discussions() {
  return (
    <div className="space-y-6 max-w-5xl mx-auto">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-slate-900 flex items-center gap-3">
          <MessageSquare className="w-8 h-8 text-indigo-600" /> Course Discussions
        </h1>
        <button className="bg-indigo-600 text-white px-5 py-2.5 rounded-xl font-medium hover:bg-indigo-700 transition shadow-md">
          Ask a Question
        </button>
      </div>

      <div className="bg-white rounded-3xl p-6 md:p-8 shadow-sm border border-slate-100">
        <div className="flex gap-4">
           <div className="w-12 h-12 bg-indigo-100 rounded-full flex-shrink-0 flex items-center justify-center text-indigo-600 font-bold">JD</div>
           <div className="flex-1">
              <div className="flex justify-between items-start">
                 <div>
                   <h3 className="font-bold text-slate-900 text-lg">Error when running React app</h3>
                   <p className="text-xs text-slate-500 font-medium">John Doe • CS401 • 3 hours ago</p>
                 </div>
                 <span className="bg-emerald-100 text-emerald-700 text-xs px-2 py-1 rounded font-bold">Resolved</span>
              </div>
              <p className="mt-4 text-slate-600">I am getting a "Vite plugin not found" error when trying to run the app. Any ideas?</p>
              
              <div className="mt-4 flex items-center gap-4 text-sm">
                 <button className="flex items-center gap-1.5 text-slate-500 hover:text-indigo-600 font-medium"><ThumbsUp className="w-4 h-4" /> 4 Likes</button>
                 <button className="flex items-center gap-1.5 text-slate-500 hover:text-indigo-600 font-medium"><Reply className="w-4 h-4" /> 2 Replies</button>
              </div>

              {/* Reply */}
              <div className="mt-6 ml-6 p-4 bg-slate-50 border border-slate-100 rounded-2xl flex gap-4">
                 <div className="w-8 h-8 bg-purple-100 rounded-full flex-shrink-0 flex items-center justify-center text-purple-600 font-bold text-xs">PJ</div>
                 <div>
                    <p className="text-xs text-slate-500 font-medium mb-1">Prof. Johnson • 1 hour ago</p>
                    <p className="text-sm text-slate-700">Make sure you ran <code>npm install</code> before running the dev server.</p>
                 </div>
              </div>
           </div>
        </div>
      </div>
    </div>
  );
}
