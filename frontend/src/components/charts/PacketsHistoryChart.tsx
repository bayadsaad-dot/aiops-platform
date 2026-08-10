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

export default function PacketsHistoryChart({
  data,
}: Props) {

  const chartData = [...data]
    .reverse()
    .map((m) => ({
      time: new Date(m.created_at).toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
      }),
      sent: m.packets_sent,
      received: m.packets_received,
    }));

  return (
    <Card elevation={3}>
      <CardContent>
        <Typography
          variant="h6"
          fontWeight={700}
          gutterBottom
        >
          Network Packets
        </Typography>

        <ResponsiveContainer
          width="100%"
          height={320}
        >
          <AreaChart data={chartData}>

            <defs>

              <linearGradient
                id="packetsSent"
                x1="0"
                y1="0"
                x2="0"
                y2="1"
              >
                <stop offset="5%" stopColor="#ef6c00" stopOpacity={0.35} />
                <stop offset="95%" stopColor="#ef6c00" stopOpacity={0} />
              </linearGradient>

              <linearGradient
                id="packetsReceived"
                x1="0"
                y1="0"
                x2="0"
                y2="1"
              >
                <stop offset="5%" stopColor="#7b1fa2" stopOpacity={0.35} />
                <stop offset="95%" stopColor="#7b1fa2" stopOpacity={0} />
              </linearGradient>

            </defs>

            <CartesianGrid strokeDasharray="4 4" />

            <XAxis dataKey="time" />

            <YAxis />

            <Tooltip />

            <Area
              type="monotone"
              dataKey="sent"
              stroke="#ef6c00"
              fill="url(#packetsSent)"
              strokeWidth={3}
              name="Packets Sent"
            />

            <Area
              type="monotone"
              dataKey="received"
              stroke="#7b1fa2"
              fill="url(#packetsReceived)"
              strokeWidth={3}
              name="Packets Received"
            />

          </AreaChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
}