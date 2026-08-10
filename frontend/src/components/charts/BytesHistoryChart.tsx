import {
  Card,
  CardContent,
  Typography,
} from "@mui/material";

import {
  ResponsiveContainer,
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from "recharts";

import type { NetworkMetric } from "../../services/networkMetricService";

interface Props {
  data: NetworkMetric[];
}

export default function BytesHistoryChart({
  data,
}: Props) {

  const chartData = [...data]
    .reverse()
    .map((m) => ({
      time: new Date(m.created_at).toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
      }),
      sent: m.bytes_sent,
      received: m.bytes_received,
    }));

  return (
    <Card elevation={3}>
      <CardContent>
        <Typography
          variant="h6"
          fontWeight={700}
          gutterBottom
        >
          Network Bytes
        </Typography>

        <ResponsiveContainer
          width="100%"
          height={320}
        >
          <AreaChart data={chartData}>

            <defs>

              <linearGradient
                id="bytesSent"
                x1="0"
                y1="0"
                x2="0"
                y2="1"
              >
                <stop offset="5%" stopColor="#1976d2" stopOpacity={0.35} />
                <stop offset="95%" stopColor="#1976d2" stopOpacity={0} />
              </linearGradient>

              <linearGradient
                id="bytesReceived"
                x1="0"
                y1="0"
                x2="0"
                y2="1"
              >
                <stop offset="5%" stopColor="#2e7d32" stopOpacity={0.35} />
                <stop offset="95%" stopColor="#2e7d32" stopOpacity={0} />
              </linearGradient>

            </defs>

            <CartesianGrid
              strokeDasharray="4 4"
            />

            <XAxis
              dataKey="time"
            />

            <YAxis />

            <Tooltip />

            <Area
              type="monotone"
              dataKey="sent"
              stroke="#1976d2"
              fill="url(#bytesSent)"
              strokeWidth={3}
              name="Bytes Sent"
            />

            <Area
              type="monotone"
              dataKey="received"
              stroke="#2e7d32"
              fill="url(#bytesReceived)"
              strokeWidth={3}
              name="Bytes Received"
            />

          </AreaChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
}