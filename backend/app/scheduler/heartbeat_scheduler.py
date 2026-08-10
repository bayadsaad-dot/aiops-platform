from apscheduler.schedulers.background import BackgroundScheduler

from app.database.session import SessionLocal
from app.services.heartbeat_monitor_service import HeartbeatMonitorService


scheduler = BackgroundScheduler()


def check_heartbeats():
    db = SessionLocal()

    try:
        HeartbeatMonitorService.check_offline_assets(db)
    finally:
        db.close()


def start_scheduler():
    if not scheduler.running:
        scheduler.add_job(
            check_heartbeats,
            "interval",
            seconds=1,
            id="heartbeat_monitor",
            replace_existing=True,
        )

        scheduler.start()
        print("✅ Heartbeat Scheduler started.")