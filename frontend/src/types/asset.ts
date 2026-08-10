export interface Asset {
  id: string;
  asset_code: string;
  hostname: string;
  ip_address: string;
  asset_type: string;
  status: string;
  last_seen: string | null;
}