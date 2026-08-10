import { useCallback } from "react";
import Container from "@mui/material/Container";

import Notification from "../components/common/Notification";
import { useNotifications } from "../hooks/useNotifications";

import { useDashboard } from "../hooks/useDashboard";
import SummaryCards from "../components/dashboard/SummaryCards";
import ResourceUsageCards from "../components/dashboard/ResourceUsageCards";
import RecentAlertsTable from "../components/dashboard/RecentAlertsTable";
import RecentAssetsTable from "../components/dashboard/RecentAssetsTable";

import NetworkSpeedChart from "../components/charts/NetworkSpeedChart";
import BytesHistoryChart from "../components/charts/BytesHistoryChart";
import PacketsHistoryChart from "../components/charts/PacketsHistoryChart";

import { useNetworkMetrics } from "../hooks/useNetworkMetrics";
import { useWebSocket } from "../hooks/useWebSocket";

export default function Dashboard() {
    const {
        dashboard,
        loading,
        error,
        refresh,
    } = useDashboard();

    const {
        open,
        message,
        severity,
        notify,
        close,
    } = useNotifications();

    const handleMessage = useCallback(
        (data: any) => {
            console.log("📩 WebSocket:", data);

            switch (data.type) {
                case "alert_created":
                    notify(
                        `🚨 ${data.asset} is offline`,
                        "error"
                    );
                    refresh();
                    break;

                case "alert_resolved":
                    notify(
                        `✅ ${data.asset} is back online`,
                        "success"
                    );
                    refresh();
                    break;

                case "dashboard_updated":
                    refresh();
                    break;

                default:
                    console.log("Unknown message:", data);
                    break;
            }
        },
        [notify, refresh]
    );

    useWebSocket(handleMessage);

    const { metrics: networkMetrics } = useNetworkMetrics();

    if (loading) {
        return (
            <Container sx={{ mt: 3 }}>
                Loading...
            </Container>
        );
    }

    if (error) {
        return (
            <Container sx={{ mt: 3 }}>
                {error}
            </Container>
        );
    }

    if (!dashboard) {
        return (
            <Container sx={{ mt: 3 }}>
                No data available.
            </Container>
        );
    }

    return (
        <Container maxWidth="xl" sx={{ mt: 3 }}>

            <SummaryCards dashboard={dashboard} />

            <ResourceUsageCards dashboard={dashboard} />

            <RecentAlertsTable />

            <RecentAssetsTable />

            <NetworkSpeedChart data={networkMetrics} />

            <BytesHistoryChart data={networkMetrics} />

            <PacketsHistoryChart data={networkMetrics} />

            <Notification
                open={open}
                message={message}
                severity={severity}
                onClose={close}
            />

        </Container>
    );
}