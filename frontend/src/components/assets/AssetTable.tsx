import VisibilityIcon from "@mui/icons-material/Visibility";
import IconButton from "@mui/material/IconButton";
import { useNavigate } from "react-router-dom";

import {
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from "@mui/material";

import type { Asset } from "../../types/asset";
import StatusChip from "../common/StatusChip";

interface Props {
  assets: Asset[];
}

export default function AssetTable({ assets }: Props) {
  const navigate = useNavigate();

  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Code</TableCell>
            <TableCell>Hostname</TableCell>
            <TableCell>IP Address</TableCell>
            <TableCell>Type</TableCell>
            <TableCell>Status</TableCell>
            <TableCell>Last Seen</TableCell>
            <TableCell align="center">Actions</TableCell>
          </TableRow>
        </TableHead>

        <TableBody>
          {assets.map((asset) => (
            <TableRow
              key={asset.id}
              hover
              sx={{ cursor: "pointer" }}
            >
              <TableCell>{asset.asset_code}</TableCell>
              <TableCell>{asset.hostname}</TableCell>
              <TableCell>{asset.ip_address}</TableCell>
              <TableCell>{asset.asset_type}</TableCell>

              <TableCell>
                <StatusChip status={asset.status} />
              </TableCell>

              <TableCell>
                {asset.last_seen ?? "Never"}
              </TableCell>

              <TableCell align="center">
                <IconButton
                  color="primary"
                  onClick={() => navigate(`/assets/${asset.id}`)}
                >
                  <VisibilityIcon />
                </IconButton>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}