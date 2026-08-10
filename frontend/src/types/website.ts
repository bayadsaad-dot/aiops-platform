export interface Website {
  id: string;
  name: string;
  url: string;
  status: string;
  status_code: number | null;
  response_time: number | null;
  ssl_expiry: string | null;
  last_check: string | null;
  created_at: string;
  updated_at: string;
}

export interface WebsiteCreate {
  name: string;
  url: string;
}