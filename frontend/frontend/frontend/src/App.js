import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from "./components/LoginPage";
import Dashboard from "./components/Dashboard";
import XMLManager from "./components/XMLManager";
import PricingManager from "./components/PricingManager";
import MarketplaceManager from "./components/MarketplaceManager";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<LoginPage />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/xml-sources" element={<XMLManager />} />
          <Route path="/pricing" element={<PricingManager />} />
          <Route path="/marketplaces" element={<MarketplaceManager />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
