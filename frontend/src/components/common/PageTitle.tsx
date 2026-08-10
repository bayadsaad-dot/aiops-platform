import { Typography } from "@mui/material";

interface Props {
  title: string;
}

export default function PageTitle({ title }: Props) {
  return (
    <Typography
      variant="h4"
      sx={{
        fontWeight: 700,
        mb: 4
      }}>
      {title}
    </Typography>
  );
}