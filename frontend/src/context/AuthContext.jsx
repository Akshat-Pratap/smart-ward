import { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check local storage for mocked session on mount
    const storedUser = localStorage.getItem('mockUser');
    if (storedUser) {
      setUser(JSON.parse(storedUser));
    }
    setLoading(false);
  }, []);

  const login = (email, password, role) => {
    // Mock user login
    const mockUser = {
      id: role === 'Admin' ? 'A-101' : 'P-505',
      name: role === 'Admin' ? 'Dr. Admin' : 'John Doe',
      email,
      role, // 'Admin' or 'Patient'
    };
    setUser(mockUser);
    localStorage.setItem('mockUser', JSON.stringify(mockUser));
    return true;
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem('mockUser');
  };

  return (
    <AuthContext.Provider value={{ user, login, logout, loading }}>
      {!loading && children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
