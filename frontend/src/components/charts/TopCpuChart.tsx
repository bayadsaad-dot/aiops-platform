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

export default function TopCpuChart({
  data,
}: Props) {

  const chartData = [...data]
    .sort((a, b) => b.cpu_percent - a.cpu_percent)
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
        Top CPU Processes
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
            right: 25,
            left: 30,
            bottom: 10,
          }}
        >
          <CartesianGrid
            strokeDasharray="4 4"
            horizontal={false}
          />

          <XAxis
            type="number"
            domain={[0, "dataMax + 5"]}
            tickFormatter={(v) => `${v.toFixed(1)}%`}
          />

          <YAxis
            type="category"
            dataKey="name"
            width={170}
            tick={{ fontSize: 12 }}
          />

          <Tooltip
            formatter={(value: number) => [
              `${value.toFixed(2)} %`,
              "CPU",
            ]}
          />

          <Bar
            dataKey="cpu_percent"
            radius={[0, 8, 8, 0]}
          >
            {chartData.map((_, index) => (
              <Cell
                key={index}
                fill="#1976d2"
              />
            ))}
          </Bar>

        </BarChart>
      </ResponsiveContainer>
    </Paper>
  );
}