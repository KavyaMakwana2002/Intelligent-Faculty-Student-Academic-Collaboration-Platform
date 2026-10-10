import { useState, useRef, useEffect } from 'react';
import { X, Send, Bot, Sparkles } from 'lucide-react';
import axios from 'axios';

export default function AiChatWidget() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<{sender: 'user'|'ai', text: string}[]>([{sender: 'ai', text: 'Hi! I am EduConnect AI. How can I help with your semester today?'}]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const endRef = useRef<HTMLDivElement>(null);

  useEffect(() => { endRef.current?.scrollIntoView({ behavior: 'smooth' }); }, [messages]);

  const handleSend = async () => {
    if(!input.trim()) return;
    setMessages(prev => [...prev, {sender: 'user', text: input}]);
    setInput('');
    setLoading(true);
    
    try {
       const res = await axios.post(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/ai-chat`, { message: input });
       setMessages(prev => [...prev, {sender: 'ai', text: res.data.reply}]);
    } catch(err) {
       setMessages(prev => [...prev, {sender: 'ai', text: 'Oops! AI Service is currently offline.'}]);
    } finally { setLoading(false); }
  };

  return (
    <>
      {/* FAB */}
      <button onClick={() => setIsOpen(true)} className={`fixed bottom-8 right-8 w-16 h-16 bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded-full shadow-2xl flex items-center justify-center hover:scale-110 transition-all z-50 ${isOpen ? 'scale-0 opacity-0' : 'scale-100 opacity-100'}`}>
        <Sparkles className="w-8 h-8" />
      </button>

      {/* Chat Window */}
      <div className={`fixed bottom-8 right-8 w-96 h-[32rem] bg-white rounded-3xl shadow-2xl border border-slate-100 flex flex-col z-50 transition-all duration-300 origin-bottom-right ${isOpen ? 'scale-100 opacity-100' : 'scale-0 opacity-0 pointer-events-none'}`}>
         {/* Header */}
         <div className="bg-gradient-to-r from-indigo-600 to-purple-600 p-4 rounded-t-3xl flex justify-between items-center text-white">
            <div className="flex items-center gap-3">
               <div className="w-10 h-10 bg-white/20 rounded-full flex items-center justify-center backdrop-blur-sm"><Bot className="w-6 h-6" /></div>
               <div><h3 className="font-bold leading-tight">EduConnect AI</h3><p className="text-xs text-indigo-100"><div className="w-2 h-2 bg-emerald-400 rounded-full inline-block mr-1"></div>Online</p></div>
            </div>
            <button onClick={() => setIsOpen(false)} className="p-2 hover:bg-white/20 rounded-full transition"><X className="w-5 h-5" /></button>
         </div>
         
         {/* Messages */}
         <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-slate-50">
            {messages.map((m, i) => (
               <div key={i} className={`flex ${m.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
                  <div className={`max-w-[80%] p-3 rounded-2xl text-sm ${m.sender === 'user' ? 'bg-indigo-600 text-white rounded-br-sm' : 'bg-white text-slate-700 border border-slate-100 rounded-bl-sm shadow-sm'}`}>
                     {m.text}
                  </div>
               </div>
            ))}
            {loading && <div className="flex justify-start"><div className="bg-white p-3 rounded-2xl rounded-bl-sm border border-slate-100 shadow-sm text-slate-400 text-xs flex gap-1"><span className="animate-bounce">•</span><span className="animate-bounce delay-75">•</span><span className="animate-bounce delay-150">•</span></div></div>}
            <div ref={endRef}></div>
         </div>
         
         {/* Input */}
         <div className="p-4 bg-white border-t border-slate-100 rounded-b-3xl flex gap-2">
            <input value={input} onChange={e=>setInput(e.target.value)} onKeyDown={e=>e.key==='Enter' && handleSend()} type="text" placeholder="Ask AI a doubt..." className="flex-1 bg-slate-50 border border-slate-200 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm" />
            <button onClick={handleSend} disabled={loading} className="w-10 h-10 bg-indigo-600 text-white rounded-xl flex items-center justify-center hover:bg-indigo-700 transition disabled:opacity-50"><Send className="w-4 h-4" /></button>
         </div>
      </div>
    </>
  );
}
