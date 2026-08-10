import {
  Card,
  CardContent,
  Typography,
  Box,
} from "@mui/material";

import TrendingUpIcon from "@mui/icons-material/TrendingUp";

interface Props {
  title: string;
  value: string | number;
  icon?: React.ReactNode;
}

export default function MetricCard({
  title,
  value,
  icon,
}: Props) {
  return (
    <Card
      elevation={2}
      sx={{
        borderRadius: 3,
        transition: ".3s",

        "&:hover": {
          transform: "translateY(-5px)",
          boxShadow: 8,
        },
      }}
    >
      <CardContent>
        <Box
          sx={{
             display:"flex",
             justifyContent: "center",
             alignItems: "center",
             mb: 2,
           }}  
         
        >
          <Typography
            color="text.secondary"
            fontWeight={600}
          >
            {title}
          </Typography>

          {icon ?? (
            <TrendingUpIcon
              color="primary"
            />
          )}
        </Box>

        <Typography
          variant="h4"
          fontWeight={700}
        >
          {value}
        </Typography>
      </CardContent>
    </Card>
  );
}