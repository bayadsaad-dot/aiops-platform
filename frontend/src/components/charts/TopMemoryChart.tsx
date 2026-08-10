import {
  Paper,
  Typography,
} from "@mui/material";

import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Cell,
} from "recharts";

interface Props {
  data: any[];
}

export default function TopMemoryChart({
  data,
}: Props) {

  const chartData = [...data]
    .sort((a, b) => b.memory_percent - a.memory_percent)
    .slice(0, 10);

  return (
    <Paper
      elevation={3}
      sx={{
        p: 3,
        borderRadius: 3,
      }}
    >
      <Typography
        variant="h6"
        fontWeight={700}
        mb={2}
      >
        Top Memory Processes
      </Typography>

      <ResponsiveContainer
        width="100%"
        height={360}
      >
        <BarChart
          data={chartData}
          layout="vertical"
          margin={{
            top: 10,
            right: 20,
            left: 40,
            bottom: 10,
          }}
        >
          <CartesianGrid
            strokeDasharray="4 4"
            horizontal={false}
          />

          <XAxis
            type="number"
            domain={[0, "dataMax + 1"]}
            tickFormatter={(v) => `${v}%`}
          />

          <YAxis
            type="category"
            dataKey="name"
            width={180}
            tick={{ fontSize: 12 }}
          />

          <Tooltip
            formatter={(value: number) => [
              `${value.toFixed(2)} %`,
              "Memory",
            ]}
          />

          <Bar
            dataKey="memory_percent"
            radius={[0, 8, 8, 0]}
          >
            {chartData.map((_, index) => (
              <Cell
                key={index}
                fill="#9c27b0"
              />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </Paper>
  );
}