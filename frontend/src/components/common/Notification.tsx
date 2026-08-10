import Snackbar from "@mui/material/Snackbar";
import Alert from "@mui/material/Alert";

interface Props {
  open: boolean;
  message: string;
  severity: "success" | "info" | "warning" | "error";
  onClose: () => void;
}

export default function Notification({
  open,
  message,
  severity,
  onClose,
}: Props) {
  return (
    <Snackbar
      open={open}
      autoHideDuration={5000}
      onClose={onClose}
      anchorOrigin={{
        vertical: "top",
        horizontal: "right",
      }}
    >
      <Alert
        severity={severity}
        onClose={onClose}
        variant="filled"
      >
        {message}
      </Alert>
    </Snackbar>
  );
}