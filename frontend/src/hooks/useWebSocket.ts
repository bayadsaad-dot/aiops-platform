import { useEffect } from "react";

export function useWebSocket(
    onMessage: (data: any) => void,
) {
    useEffect(() => {

        const socket = new WebSocket(
            "ws://127.0.0.1:8000/ws",
        );

        socket.onopen = () => {
            console.log("✅ WebSocket Connected");
        };

        socket.onmessage = (event) => {
            console.log("📩 Message:", event.data);

            const data = JSON.parse(event.data);

            onMessage(data);
        };

        socket.onerror = (event) => {
            console.error("🔥 WebSocket Error:", event);
        };

        socket.onclose = (event) => {
            console.log(
                "❌ WebSocket Closed",
                event.code,
                event.reason,
            );
        };

        return () => {
            socket.close();
        };

    }, [onMessage]);
}