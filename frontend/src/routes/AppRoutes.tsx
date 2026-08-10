import { Routes, Route } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import Dashboard from "../pages/Dashboard";
import Assets from "../pages/Assets";
import AssetDetails from "../pages/AssetDetails";
import Alerts from "../pages/Alerts";
import Incidents from "../pages/Incidents";
import IncidentDetails from "../pages/IncidentDetails";
import Websites from "../pages/Websites";
import Settings from "../pages/Settings";

export default function AppRoutes() {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route path="/" element={<Dashboard />} />

        <Route path="/assets" element={<Assets />} />
        <Route path="/assets/:id" element={<AssetDetails />} />

        <Route path="/alerts" element={<Alerts />} />

        <Route path="/incidents" element={<Incidents />} />
        <Route
          path="/incidents/:id"
          element={<IncidentDetails />}
        />

        <Route
          path="/websites"
          element={<Websites />}
        />

        <Route
          path="/settings"
          element={<Settings />}
        />
      </Route>
    </Routes>
  );
}