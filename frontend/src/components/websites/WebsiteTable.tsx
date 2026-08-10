import DeleteIcon from "@mui/icons-material/Delete";
import IconButton from "@mui/material/IconButton";
import {
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from "@mui/material";

import type { Website } from "../../types/website";
import WebsiteStatusChip from "./WebsiteStatusChip";
import { deleteWebsite } from "../../services/websiteService";

interface Props {
  websites: Website[];
  refresh: () => void;
}

export default function WebsiteTable({
  websites,
  refresh,
}: Props) {
  async function handleDelete(id: string) {
    if (!window.confirm("Delete this website?")) {
      return;
    }

    try {
      await deleteWebsite(id);
      refresh();
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <TableContainer component={Paper}>
      <Table>

        <TableHead>
          <TableRow>
            <TableCell>Name</TableCell>
            <TableCell>URL</TableCell>
            <TableCell>Status</TableCell>
            <TableCell>Status Code</TableCell>
            <TableCell>Response Time</TableCell>
            <TableCell>SSL Expiry</TableCell>
            <TableCell>Last Check</TableCell>
            <TableCell align="center">
              Actions
            </TableCell>
          </TableRow>
        </TableHead>

        <TableBody>

          {websites.map((website) => (
            <TableRow key={website.id} hover>

              <TableCell>
                {website.name}
              </TableCell>

              <TableCell>
                {website.url}
              </TableCell>

              <TableCell>
                <WebsiteStatusChip
                  status={website.status}
                />
              </TableCell>

              <TableCell>
                {website.status_code ?? "-"}
              </TableCell>

              <TableCell>
                {website.response_time != null
                  ? `${website.response_time} ms`
                  : "-"}
              </TableCell>

              <TableCell>
                {website.ssl_expiry ?? "-"}
              </TableCell>

              <TableCell>
                {website.last_check ?? "-"}
              </TableCell>

              <TableCell align="center">
                <IconButton
                  color="error"
                  onClick={() =>
                    handleDelete(website.id)
                  }
                >
                  <DeleteIcon />
                </IconButton>
              </TableCell>

            </TableRow>
          ))}

        </TableBody>

      </Table>
    </TableContainer>
  );
}