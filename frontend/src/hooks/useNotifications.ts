import { useState, useCallback } from "react";

export function useNotifications() {
  const [open, setOpen] = useState(false);
  const [message, setMessage] = useState("");
  const [severity, setSeverity] = useState<
    "success" | "info" | "warning" | "error"
  >("info");

  const notify = useCallback(
    (
      msg: string,
      type: "success" | "info" | "warning" | "error"
    ) => {
      setMessage(msg);
      setSeverity(type);
      setOpen(true);
    },
    []
  );

  const close = () => setOpen(false);

  return {
    open,
    message,
    severity,
    notify,
    close,
  };
}