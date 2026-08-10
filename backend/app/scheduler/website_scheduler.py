from apscheduler.schedulers.background import BackgroundScheduler

from app.database.session import SessionLocal
from app.services.website_service import WebsiteService

scheduler = BackgroundScheduler()


def check_websites():
    db = SessionLocal()

    try:
        WebsiteService.check_all_websites(db)

    finally:
        db.close()


def start_website_scheduler():

    if scheduler.running:
        return

    scheduler.add_job(
        check_websites,
        "interval",
        seconds=60,
        id="website_monitor",
        replace_existing=True,
    )

    scheduler.start()

    print("✅ Website Scheduler started.")