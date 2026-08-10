import { useState } from "react";

import {
  Box,
  Button,
  Container,
  Typography,
} from "@mui/material";

import AddIcon from "@mui/icons-material/Add";

import { useWebsites } from "../hooks/useWebsites";
import WebsiteTable from "../components/websites/WebsiteTable";
import WebsiteDialog from "../components/websites/WebsiteDialog";

export default function Websites() {
  const {
    websites,
    loading,
    error,
    refresh,
  } = useWebsites();

  const [open, setOpen] = useState(false);

  if (loading) {
    return (
      <Container sx={{ mt: 3 }}>
        Loading...
      </Container>
    );
  }

  if (error) {
    return (
      <Container sx={{ mt: 3 }}>
        {error}
      </Container>
    );
  }

  return (
    <Container maxWidth="xl" sx={{ mt: 3 }}>

      <Box
        display="flex"
        justifyContent="center"
        alignItems="center"
        mb={3}
      >
        <Typography variant="h4">
          Website Monitoring
        </Typography>

        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={() => setOpen(true)}
        >
          Add Website
        </Button>
      </Box>

      <WebsiteTable
        websites={websites}
        refresh={refresh}
      />

      <WebsiteDialog
        open={open}
        onClose={() => setOpen(false)}
        refresh={refresh}
      />

    </Container>
  );
}