import { useAuth } from '../context/AuthContext';
import { Calendar, FileText, User as UserIcon, LogOut, Clock, Activity } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export default function PatientDashboard() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className="max-w-7xl mx-auto space-y-6">
      
      {/* Header */}
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 bg-white/80 p-6 rounded-2xl border border-emerald-100 shadow-sm backdrop-blur-md">
        <div>
          <h1 className="text-2xl font-bold text-emerald-900">Welcome, {user?.name || 'Patient'}</h1>
          <p className="text-slate-500 mt-1">Patient ID: {user?.id || 'P-XXX'}</p>
        </div>
        <button 
          onClick={handleLogout}
          className="flex items-center gap-2 px-4 py-2 bg-red-50 text-red-600 rounded-lg hover:bg-red-100 transition-colors border border-red-100"
        >
          <LogOut className="w-4 h-4" />
          <span className="font-medium">Logout</span>
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        {/* Profile Card */}
        <div className="glass-card p-6 flex flex-col items-center text-center">
          <div className="w-20 h-20 bg-emerald-100 rounded-full flex items-center justify-center mb-4">
            <UserIcon className="w-10 h-10 text-emerald-600" />
          </div>
          <h2 className="text-xl font-bold text-slate-800">{user?.name}</h2>
          <p className="text-slate-500 mb-6">{user?.email}</p>
          <div className="w-full space-y-3 text-sm text-left">
            <div className="flex justify-between border-b border-emerald-50 pb-2">
              <span className="text-slate-500">Phone</span>
              <span className="font-medium text-slate-800">+1 234 567 8900</span>
            </div>
            <div className="flex justify-between border-b border-emerald-50 pb-2">
              <span className="text-slate-500">DOB</span>
              <span className="font-medium text-slate-800">May 12, 1985</span>
            </div>
            <div className="flex justify-between pt-2">
              <span className="text-slate-500">Address</span>
              <span className="font-medium text-slate-800 text-right">123 Wellness Way,<br/>Health City</span>
            </div>
          </div>
          <button className="mt-6 w-full py-2.5 bg-emerald-50 text-emerald-700 font-semibold rounded-xl hover:bg-emerald-100 transition-colors border border-emerald-200">
            Edit Profile
          </button>
        </div>

        {/* Content Column */}
        <div className="md:col-span-2 space-y-6">
          
          {/* Recent Appointments */}
          <div className="glass-card p-6">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-bold text-slate-800 flex items-center gap-2">
                <Calendar className="w-5 h-5 text-emerald-600" />
                Upcoming Appointments
              </h3>
              <button className="text-sm font-medium text-emerald-600 hover:text-emerald-700">View All</button>
            </div>
            <div className="space-y-4">
              <div className="p-4 bg-emerald-50/60 border border-emerald-100 rounded-xl flex items-center justify-between hover:border-emerald-300 transition-colors">
                <div className="flex items-start gap-4">
                  <div className="p-3 bg-white text-emerald-600 rounded-lg border border-emerald-100">
                    <Clock className="w-6 h-6" />
                  </div>
                  <div>
                    <h4 className="font-medium text-slate-800">General Checkup</h4>
                    <p className="text-sm text-slate-500">Dr. Sarah Jenkins</p>
                  </div>
                </div>
                <div className="text-right">
                  <p className="font-medium text-slate-800">Tomorrow</p>
                  <p className="text-sm text-emerald-600 font-medium">10:00 AM</p>
                </div>
              </div>
            </div>
          </div>

          {/* Medical Reports */}
          <div className="glass-card p-6">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-bold text-slate-800 flex items-center gap-2">
                <FileText className="w-5 h-5 text-emerald-600" />
                Recent Reports
              </h3>
              <button className="text-sm font-medium text-emerald-600 hover:text-emerald-700">View All</button>
            </div>
            <div className="space-y-3">
              <div className="flex items-center justify-between p-3 bg-white/60 border border-emerald-100/60 rounded-lg">
                <div className="flex items-center gap-3">
                  <Activity className="w-5 h-5 text-slate-400" />
                  <span className="font-medium text-slate-700">Blood Test Results</span>
                </div>
                <button className="px-3 py-1 text-sm font-medium text-emerald-600 bg-emerald-50 rounded-md hover:bg-emerald-100 border border-emerald-100">
                  View
                </button>
              </div>
              <div className="flex items-center justify-between p-3 bg-white/60 border border-emerald-100/60 rounded-lg">
                <div className="flex items-center gap-3">
                  <FileText className="w-5 h-5 text-slate-400" />
                  <span className="font-medium text-slate-700">X-Ray Scans</span>
                </div>
                <button className="px-3 py-1 text-sm font-medium text-emerald-600 bg-emerald-50 rounded-md hover:bg-emerald-100 border border-emerald-100">
                  View
                </button>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
}
