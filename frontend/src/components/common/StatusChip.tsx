import Chip from "@mui/material/Chip";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import CancelIcon from "@mui/icons-material/Cancel";
import WarningIcon from "@mui/icons-material/Warning";

interface StatusChipProps {
  status: string;
}

export default function StatusChip({ status }: StatusChipProps) {
  const value = status.toLowerCase();

  switch (value) {
    case "online":
      return (
        <Chip
          icon={<CheckCircleIcon />}
          label="Online"
          color="success"
          variant="filled"
          size="small"
        />
      );

    case "offline":
      return (
        <Chip
          icon={<CancelIcon />}
          label="Offline"
          color="error"
          variant="filled"
          size="small"
        />
      );

    default:
      return (
        <Chip
          icon={<WarningIcon />}
          label={status}
          color="warning"
          variant="filled"
          size="small"
        />
      );
  }
}