import time


class NetworkSpeedCalculator:

    def __init__(self):
        self.previous = {}
        self.previous_time = {}

    def calculate(self, interface_name, bytes_sent, bytes_received):

        now = time.time()

        upload = 0.0
        download = 0.0

        if interface_name in self.previous:

            elapsed = (
                now -
                self.previous_time[interface_name]
            )

            if elapsed > 0:

                previous = self.previous[interface_name]

                upload = (
                    bytes_sent - previous["sent"]
                ) / elapsed

                download = (
                    bytes_received - previous["received"]
                ) / elapsed

        self.previous[interface_name] = {
            "sent": bytes_sent,
            "received": bytes_received,
        }

        self.previous_time[interface_name] = now

        return (
            round(upload / 1024 / 1024, 2),
            round(download / 1024 / 1024, 2),
        )