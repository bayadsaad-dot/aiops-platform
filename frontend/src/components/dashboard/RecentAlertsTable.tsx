import {
  Card,
  CardContent,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  Chip,
} from "@mui/material";

import { useAlerts } from "../../hooks/useAlerts";

export default function RecentAlertsTable() {
  const { alerts, loading } = useAlerts();

  return (
    <Card sx={{ mt: 3 }}>
      <CardContent>
        <Typography
          variant="h6"
          gutterBottom
        >
          Recent Alerts
        </Typography>

        {loading ? (
          <Typography>Loading...</Typography>
        ) : (
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell>Severity</TableCell>
                <TableCell>Title</TableCell>
                <TableCell>Status</TableCell>
                <TableCell>Created</TableCell>
              </TableRow>
            </TableHead>

            <TableBody>
              {alerts.map((alert) => (
                <TableRow key={alert.id}>
                  <TableCell>
                    <Chip
                      label={alert.severity}
                      color={
                        alert.severity === "CRITICAL"
                          ? "error"
                          : alert.severity === "WARNING"
                          ? "warning"
                          : "info"
                      }
                      size="small"
                    />
                  </TableCell>

                  <TableCell>{alert.title}</TableCell>

                  <TableCell>{alert.status}</TableCell>

                  <TableCell>
                    {new Date(alert.created_at).toLocaleString()}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        )}
      </CardContent>
    </Card>
  );
}