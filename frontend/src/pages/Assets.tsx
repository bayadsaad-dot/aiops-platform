import { useState } from "react";

import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import TextField from "@mui/material/TextField";

import AssetTable from "../components/assets/AssetTable";
import { useAssets } from "../hooks/useAssets";

export default function Assets() {
  const { assets, loading, error } = useAssets();

  const [search, setSearch] = useState("");

  if (loading) {
    return <Container sx={{ mt: 3 }}>Loading...</Container>;
  }

  if (error) {
    return <Container sx={{ mt: 3 }}>{error}</Container>;
  }

  const filteredAssets = assets.filter((asset) => {
    const query = search.toLowerCase();

    return (
      asset.hostname.toLowerCase().includes(query) ||
      asset.asset_code.toLowerCase().includes(query) ||
      asset.ip_address.toLowerCase().includes(query)
    );
  });

  return (
    <Container maxWidth="xl" sx={{ mt: 3 }}>
      <Typography variant="h4" sx={{
        mb: 3
      }}>
        Assets
      </Typography>

      <TextField
        fullWidth
        label="Search by Hostname, Asset Code or IP..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        sx={{ mb: 3 }}
      />

      <AssetTable assets={filteredAssets} />
    </Container>
  );
}