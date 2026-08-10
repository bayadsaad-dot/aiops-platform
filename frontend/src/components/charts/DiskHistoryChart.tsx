import HistoryChart from "./HistoryChart";

interface Props {
  data: any[];
}

export default function DiskHistoryChart({ data }: Props) {
  return (
    <HistoryChart
      data={data}
      dataKey="disk_usage"
      color="#2e7d32"
      title="Disk Usage"
    />
  );
}