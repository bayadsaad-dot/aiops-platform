import {
  Card,
  CardContent,
  Typography,
  LinearProgress,
  Grid,
} from "@mui/material";

interface Props {
  dashboard: {
    avg_cpu: number;
    avg_memory: number;
    avg_disk: number;
  };
}

function UsageCard({
  title,
  value,
}: {
  title: string;
  value: number;
}) {
  return (
    <Card
      elevation={2}
      sx={{
        borderRadius: 3,
        height: "100%",
      }}
    >
      <CardContent>
        <Typography
          variant="subtitle1"
          gutterBottom
        >
          {title}
        </Typography>

        <Typography
          variant="h5"
          sx={{
            fontWeight: "bold",
            mb: 2
          }}>
          {value.toFixed(1)}%
        </Typography>

        <LinearProgress
          variant="determinate"
          value={value}
          sx={{
            height: 10,
            borderRadius: 5,
          }}
        />
      </CardContent>
    </Card>
  );
}

export default function ResourceUsageCards({
  dashboard,
}: Props) {
  return (
    <Grid
      container
      spacing={3}
      sx={{ mt: 1 }}
    >
      <Grid size={{ xs: 12, md: 4 }}>
        <UsageCard
          title="Average CPU Usage"
          value={dashboard.avg_cpu}
        />
      </Grid>

      <Grid size={{ xs: 12, md: 4 }}>
        <UsageCard
          title="Average Memory Usage"
          value={dashboard.avg_memory}
        />
      </Grid>

      <Grid size={{ xs: 12, md: 4 }}>
        <UsageCard
          title="Average Disk Usage"
          value={dashboard.avg_disk}
        />
      </Grid>
    </Grid>
  );
}