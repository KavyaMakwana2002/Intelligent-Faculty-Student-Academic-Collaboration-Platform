import { useState, useEffect } from 'react';
import { Settings as SettingsIcon, Moon, Sun, Monitor, Shield, Bell, Key, Globe } from 'lucide-react';


export default function Settings() {
  // Theme state
  const [theme, setTheme] = useState(localStorage.getItem('theme') || 'light');

  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    localStorage.setItem('theme', theme);
  }, [theme]);

  const toggleTheme = (newTheme: string) => {
    setTheme(newTheme);
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-10 animate-fade-in-up">
      <div className="flex items-center gap-4 mb-8">
        <div className="w-14 h-14 bg-indigo-50 text-indigo-600 rounded-2xl flex items-center justify-center shadow-sm border border-indigo-100">
          <SettingsIcon className="w-7 h-7" />
        </div>
        <div>
          <h1 className="text-3xl font-extrabold text-slate-900">Account Settings</h1>
          <p className="text-slate-500 font-medium">Manage your preferences and configurations</p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="md:col-span-1 space-y-2">
          <button className="w-full flex items-center gap-3 p-3 bg-indigo-50 text-indigo-700 rounded-xl font-bold transition">
            <Monitor className="w-5 h-5" /> Appearance
          </button>
          <button className="w-full flex items-center gap-3 p-3 text-slate-600 hover:bg-slate-50 rounded-xl font-medium transition">
            <Bell className="w-5 h-5" /> Notifications
          </button>
          <button className="w-full flex items-center gap-3 p-3 text-slate-600 hover:bg-slate-50 rounded-xl font-medium transition">
            <Key className="w-5 h-5" /> Security
          </button>
          <button className="w-full flex items-center gap-3 p-3 text-slate-600 hover:bg-slate-50 rounded-xl font-medium transition">
            <Globe className="w-5 h-5" /> Language
          </button>
        </div>

        <div className="md:col-span-2 space-y-6">
          <div className="bg-white rounded-3xl p-8 border border-slate-100 shadow-sm">
            <h2 className="text-xl font-bold text-slate-900 mb-6 flex items-center gap-2">
              <Sun className="w-5 h-5 text-amber-500" /> Theme & Appearance
            </h2>
            
            <p className="text-slate-500 mb-6">Choose how the application looks to you. Dark mode is easier on the eyes in low light.</p>
            
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div 
                onClick={() => toggleTheme('light')}
                className={`cursor-pointer border-2 rounded-2xl p-6 flex flex-col items-center justify-center transition-all ${theme === 'light' ? 'border-indigo-500 bg-indigo-50/50' : 'border-slate-200 hover:border-indigo-300'}`}
              >
                <div className="w-16 h-16 bg-white rounded-full flex items-center justify-center shadow-md mb-4">
                  <Sun className="w-8 h-8 text-amber-500" />
                </div>
                <h3 className="font-bold text-slate-900">Light Mode</h3>
                <p className="text-sm text-slate-500 text-center mt-1">Bright and clear for daytime use</p>
              </div>
              
              <div 
                onClick={() => toggleTheme('dark')}
                className={`cursor-pointer border-2 rounded-2xl p-6 flex flex-col items-center justify-center transition-all ${theme === 'dark' ? 'border-indigo-500 bg-indigo-50/50' : 'border-slate-200 hover:border-indigo-300'}`}
              >
                <div className="w-16 h-16 bg-slate-900 rounded-full flex items-center justify-center shadow-md mb-4">
                  <Moon className="w-8 h-8 text-blue-300" />
                </div>
                <h3 className="font-bold text-slate-900">Dark Mode</h3>
                <p className="text-sm text-slate-500 text-center mt-1">Dark backgrounds for low light</p>
              </div>
            </div>
          </div>
          
          <div className="bg-white rounded-3xl p-8 border border-slate-100 shadow-sm">
             <h2 className="text-xl font-bold text-slate-900 mb-4 flex items-center gap-2">
              <Shield className="w-5 h-5 text-emerald-500" /> Account Security
            </h2>
            <div className="flex justify-between items-center py-4 border-b border-slate-100">
               <div>
                 <p className="font-bold text-slate-700">Two-Factor Authentication</p>
                 <p className="text-sm text-slate-500">Add an extra layer of security</p>
               </div>
               <button className="bg-slate-100 hover:bg-slate-200 text-slate-700 px-4 py-2 rounded-lg font-medium transition">Enable</button>
            </div>
            <div className="flex justify-between items-center py-4">
               <div>
                 <p className="font-bold text-slate-700">Change Password</p>
                 <p className="text-sm text-slate-500">Update your account password</p>
               </div>
               <button className="bg-slate-100 hover:bg-slate-200 text-slate-700 px-4 py-2 rounded-lg font-medium transition">Update</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
