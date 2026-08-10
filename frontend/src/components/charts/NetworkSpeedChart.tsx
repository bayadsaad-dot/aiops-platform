import HistoryChart from "./HistoryChart";

interface Props {
  data: any[];
}

export default function NetworkSpeedChart({ data }: Props) {

    return (
    <HistoryChart
      data={data}
      dataKey="download_speed"
      color="#1976d2"
      title="Download Speed"
    />
  );
  
}