import { Box, Toolbar } from "@mui/material";

import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

interface Props {
    children: React.ReactNode;
}

export default function MainLayout({ children }: Props) {
    return (
        <Box sx={{ display: "flex" }}>

            <Sidebar />

            <Box sx={{ flexGrow: 1 }}>

                <Navbar />

                <Toolbar />

                <Box sx={{
                    p: 3
                }}>
                    {children}
                </Box>

            </Box>

        </Box>
    );
}