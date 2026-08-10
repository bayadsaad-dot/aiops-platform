import HistoryChart from "./HistoryChart";

interface Props {
  data: any[];
}

export default function MemoryHistoryChart({ data }: Props) {
  return (
    <HistoryChart
      data={data}
      dataKey="memory_usage"
      color="#9c27b0"
      title="Memory Usage"
    />
  );
}