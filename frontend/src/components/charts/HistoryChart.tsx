import {
  Area,
  AreaChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

interface Props {
  data: any[];
  dataKey: string;
  color: string;
  title: string;
}

export default function HistoryChart({
  data,
  dataKey,
  color,
  title,
}: Props) {
  const gradientId = `${dataKey}-gradient`;

  return (
    <ResponsiveContainer width="100%" height={320}>
      <AreaChart
        data={data}
        margin={{
          top: 10,
          right: 20,
          left: 0,
          bottom: 0,
        }}
      >
        <defs>
          <linearGradient
            id={gradientId}
            x1="0"
            y1="0"
            x2="0"
            y2="1"
          >
            <stop
              offset="5%"
              stopColor={color}
              stopOpacity={0.35}
            />
            <stop
              offset="95%"
              stopColor={color}
              stopOpacity={0}
            />
          </linearGradient>
        </defs>

        <CartesianGrid
          stroke="#e5e7eb"
          strokeDasharray="4 4"
        />

        <XAxis
          dataKey="created_at"
          tickFormatter={(value) =>
            new Date(value).toLocaleTimeString([], {
              hour: "2-digit",
              minute: "2-digit",
            })
          }
          axisLine={false}
          tickLine={false}
          tick={{ fontSize: 12 }}
        />

        <YAxis
          axisLine={false}
          tickLine={false}
          tick={{ fontSize: 12 }}
        />

        <Tooltip
          contentStyle={{
            borderRadius: 12,
            border: "1px solid #ddd",
            boxShadow: "0 8px 24px rgba(0,0,0,.15)",
          }}
          labelFormatter={(value) =>
            new Date(value as string).toLocaleString()
          }
          formatter={(value: number) => [
            Number(value).toFixed(2),
            title,
          ]}
        />

        <Area
          type="monotone"
          dataKey={dataKey}
          stroke={color}
          strokeWidth={3}
          fill={`url(#${gradientId})`}
          activeDot={{
            r: 6,
          }}
          animationDuration={900}
        />
      </AreaChart>
    </ResponsiveContainer>
  );
}