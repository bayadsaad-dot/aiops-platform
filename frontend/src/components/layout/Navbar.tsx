import {
  AppBar,
  Toolbar,
  Typography,
  Box,
  IconButton,
  Avatar,
  Tooltip,
} from "@mui/material";

import NotificationsIcon from "@mui/icons-material/Notifications";
import MonitorHeartIcon from "@mui/icons-material/MonitorHeart";

export default function Navbar() {
  return (
    <AppBar
      position="fixed"
      color="inherit"
      elevation={1}
      sx={{
        zIndex: (theme) => theme.zIndex.drawer + 1,
        bgcolor: "white",
      }}
    >
      <Toolbar>
        {/* Left Side */}
        <Box
          sx={{
            display: "flex",
            alignItems: "center",
            flexGrow: 1,
          }}
        >
          <MonitorHeartIcon
            color="primary"
            sx={{
              mr: 1,
              fontSize: 30,
            }}
          />

          <Typography
            variant="h6"
            fontWeight={700}
          >
            AIOps Platform
          </Typography>
        </Box>

        {/* Right Side */}
        <Tooltip title="Notifications">
          <IconButton>
            <NotificationsIcon />
          </IconButton>
        </Tooltip>

        <Avatar
          sx={{
            ml: 2,
            bgcolor: "primary.main",
          }}
        >
          A
        </Avatar>
      </Toolbar>
    </AppBar>
  );
}