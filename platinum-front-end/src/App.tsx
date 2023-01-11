import React, { createContext, ReactNode, useEffect, useState } from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";
import SearchAppBar from './components/searchAppBar';
import HomePage from './pages/homePage';
import ProductPage from './pages/productPage';
import SigninPage from './pages/signinPage';

interface AppContextType {
  user: {},
  isConnected: boolean,
  setUser: (s: {}) => void
  setIsConnected: (s: boolean) => void
}

export const AppContext = createContext<AppContextType | null>(null)

const AppContextProvider = ({ children }: any) => {

  console.log(localStorage.getItem('user') || "{}")
  const userInitialState = JSON.parse(localStorage.getItem('user') || "{}") || {};

  const [user, setUser] = useState(userInitialState);

  //const [user, setUser] = useState<{}>({})
  const [isConnected, setIsConnected] = useState(false)

  useEffect(() => {
    localStorage.setItem("user", JSON.stringify(user));
  }, [user]);

  const values = {
    user, setUser, isConnected, setIsConnected
  };

  return (
    <AppContext.Provider value={values}>
      {children}
    </AppContext.Provider>
  );
};


function App() {

  return (
    <AppContextProvider >
      <Router>
        <SearchAppBar />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="product" element={<ProductPage />} />
          <Route path="signin" element={<SigninPage />} />
        </Routes>
      </Router>
    </AppContextProvider>
  );
}

export default App;
