import { Box } from "@mui/material";
import { Outlet } from "react-router-dom";

import Sidebar from "../components/layout/Sidebar";
import Navbar from "../components/layout/Navbar";

export default function MainLayout() {
  return (
    <Box sx={{ display: "flex" }}>
      <Sidebar />

      <Box sx={{ flexGrow: 1 }}>
        <Navbar />

        <Box
          component="main"
          sx={{
            p: 3,
            mt: 8,
          }}
        >
          <Outlet />
        </Box>
      </Box>
    </Box>
  );
}