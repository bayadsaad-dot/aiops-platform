from app.enums.alert import AlertSeverity, AlertStatus
from app.models.alert import Alert
from app.repositories.alert_repository import AlertRepository
from app.services.incident_service import IncidentService



class AlertEngine:

    @staticmethod
    def evaluate_metric(db, asset, metric):

        AlertEngine._check_cpu(db, asset, metric)
        AlertEngine._check_memory(db, asset, metric)
        AlertEngine._check_disk(db, asset, metric)

    @staticmethod
    def _check_cpu(db, asset, metric):

        open_alert = AlertRepository.get_open_alert(
            db=db,
            asset_id=asset.id,
            title="High CPU Usage",
        )

        if metric.cpu_usage >= 90:

            if not open_alert:

                alert = AlertRepository.create(
                    db,
                    Alert(
                        asset_id=asset.id,
                        title="High CPU Usage",
                        message=f"CPU usage reached {metric.cpu_usage:.1f}%",
                        severity=AlertSeverity.CRITICAL,
                    ),
                )

                IncidentService.create_from_alert(
                    db=db,
                    alert=alert,
                )

                print("🔥 CPU Alert Created")

        elif open_alert:

            open_alert.status = AlertStatus.RESOLVED
            AlertRepository.update(db, open_alert)

            print("✅ CPU Alert Resolved")

    @staticmethod
    def _check_memory(db, asset, metric):

        open_alert = AlertRepository.get_open_alert(
            db=db,
            asset_id=asset.id,
            title="High Memory Usage",
        )

        if metric.memory_usage >= 90:

            if not open_alert:

                alert = AlertRepository.create(
                    db,
                    Alert(
                        asset_id=asset.id,
                        title="High Memory Usage",
                        message=f"Memory usage reached {metric.memory_usage:.1f}%",
                        severity=AlertSeverity.WARNING,
                    ),
                )

                IncidentService.create_from_alert(
                    db=db,
                    alert=alert,
                )

                print("🔥 Memory Alert Created")


        elif open_alert:

            open_alert.status = AlertStatus.RESOLVED
            AlertRepository.update(db, open_alert)

            print("✅ Memory Alert Resolved")

    @staticmethod
    def _check_disk(db, asset, metric):

        open_alert = AlertRepository.get_open_alert(
            db=db,
            asset_id=asset.id,
            title="Low Disk Space",
        )

        if metric.disk_usage >= 95:

            if not open_alert:

                alert = AlertRepository.create(
                    db,
                    Alert(
                        asset_id=asset.id,
                        title="Low Disk Space",
                        message=f"Disk usage reached {metric.disk_usage:.1f}%",
                        severity=AlertSeverity.CRITICAL,
                    ),
                )

                IncidentService.create_from_alert(
                    db=db,
                    alert=alert,
                )

                print("🔥 Disk Alert Created")

        elif open_alert:

            open_alert.status = AlertStatus.RESOLVED
            AlertRepository.update(db, open_alert)

            print("✅ Disk Alert Resolved")