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

import { useAssets } from "../../hooks/useAssets";

export default function RecentAssetsTable() {
  const { assets, loading } = useAssets();

  return (
    <Card sx={{ mt: 3 }}>
      <CardContent>
        <Typography variant="h6" gutterBottom>
          Recent Assets
        </Typography>

        {loading ? (
          <Typography>Loading...</Typography>
        ) : (
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell>Hostname</TableCell>
                <TableCell>IP Address</TableCell>
                <TableCell>Type</TableCell>
                <TableCell>Status</TableCell>
              </TableRow>
            </TableHead>

            <TableBody>
              {assets.map((asset) => (
                <TableRow key={asset.id} hover>
                  <TableCell>{asset.hostname}</TableCell>

                  <TableCell>{asset.ip_address}</TableCell>

                  <TableCell>{asset.asset_type}</TableCell>

                  <TableCell>
                    <Chip
                      label={asset.status}
                      color={
                        asset.status === "Online"
                          ? "success"
                          : asset.status === "Offline"
                          ? "error"
                          : "warning"
                      }
                      size="small"
                    />
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