import { useState } from "react";

import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  TextField,
} from "@mui/material";

import { useCreateWebsite } from "../../hooks/useCreateWebsite";

interface Props {
  open: boolean;
  onClose: () => void;
  refresh: () => void;
}

export default function WebsiteDialog({
  open,
  onClose,
  refresh,
}: Props) {
  const { create, loading } = useCreateWebsite(() => {
    refresh();
    onClose();
  });

  const [name, setName] = useState("");
  const [url, setUrl] = useState("");

  async function handleSave() {
    if (!name.trim() || !url.trim()) {
      return;
    }

    const success = await create({
      name,
      url,
    });

    if (success) {
      setName("");
      setUrl("");
    }
  }

  return (
    <Dialog
      open={open}
      onClose={onClose}
      maxWidth="sm"
      fullWidth
    >
      <DialogTitle>
        Add Website
      </DialogTitle>

      <DialogContent>

        <TextField
          fullWidth
          margin="normal"
          label="Website Name"
          value={name}
          onChange={(e) =>
            setName(e.target.value)
          }
        />

        <TextField
          fullWidth
          margin="normal"
          label="Website URL"
          placeholder="https://example.com"
          value={url}
          onChange={(e) =>
            setUrl(e.target.value)
          }
        />

      </DialogContent>

      <DialogActions>

        <Button
          onClick={onClose}
        >
          Cancel
        </Button>

        <Button
          variant="contained"
          onClick={handleSave}
          disabled={loading}
        >
          Save
        </Button>

      </DialogActions>
    </Dialog>
  );
}