import HistoryChart from "./HistoryChart";

interface Props {
  data: any[];
}

export default function CpuHistoryChart({ data }: Props) {
  return (
    <HistoryChart
      data={data}
      dataKey="cpu_usage"
      color="#1976d2"
      title="CPU Usage"
    />
  );
}