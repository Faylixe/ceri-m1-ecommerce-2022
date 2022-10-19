import React from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";
import SearchAppBar from './components/searchAppBar';
import HomePage from './pages/homePage';

function App() {
  return (
    <>
      <SearchAppBar />
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
