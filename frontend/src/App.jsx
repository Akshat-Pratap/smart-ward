import { Routes, Route, useLocation } from 'react-router-dom';
import Navbar from './components/Navbar';
import Dashboard from './pages/Dashboard';
import Patients from './pages/Patients';
import Resources from './pages/Resources';
import Alerts from './pages/Alerts';
import Login from './pages/Login';
import PatientDashboard from './pages/PatientDashboard';
import ProtectedRoute from './components/ProtectedRoute';

function MainLayout({ children }) {
  return (
    <>
      <Navbar />
      <main className="lg:ml-[260px] pt-20 lg:pt-6 px-4 sm:px-6 lg:px-8 pb-12 max-w-[1400px]">
        {children}
      </main>
    </>
  );
}

export default function App() {
  const location = useLocation();
  const isLoginPage = location.pathname === '/login';

  return (
    <div className="min-h-screen">
      {isLoginPage ? (
        <Routes>
          <Route path="/login" element={<Login />} />
        </Routes>
      ) : (
        <Routes>
          <Route path="/login" element={<Login />} />
          
          <Route 
            path="/patient/*" 
            element={
              <ProtectedRoute allowedRoles={['Patient']}>
                {/* Patient dashboard layout doesn't need the admin sidebar, or maybe it does? If they have a separate UI, we won't wrap it in MainLayout. */}
                <div className="p-4 sm:p-8 pt-10">
                  <Routes>
                    <Route path="/" element={<PatientDashboard />} />
                  </Routes>
                </div>
              </ProtectedRoute>
            } 
          />

          <Route 
            path="/*" 
            element={
              <ProtectedRoute allowedRoles={['Admin']}>
                <MainLayout>
                  <Routes>
                    <Route path="/" element={<Dashboard />} />
                    <Route path="/patients" element={<Patients />} />
                    <Route path="/resources" element={<Resources />} />
                    <Route path="/alerts" element={<Alerts />} />
                  </Routes>
                </MainLayout>
              </ProtectedRoute>
            } 
          />
        </Routes>
      )}
    </div>
  );
}
