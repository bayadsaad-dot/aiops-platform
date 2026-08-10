import Chip from "@mui/material/Chip";

interface Props {
  status: string;
}

export default function WebsiteStatusChip({
  status,
}: Props) {
  switch (status) {
    case "UP":
      return (
        <Chip
          label="UP"
          color="success"
          size="small"
        />
      );

    case "DOWN":
      return (
        <Chip
          label="DOWN"
          color="error"
          size="small"
        />
      );

    default:
      return (
        <Chip
          label="UNKNOWN"
          color="warning"
          size="small"
        />
      );
  }
}