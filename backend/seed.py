from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.models.role import Role
from app.models.user import User
from app.core.security import hash_password


ROLES = [
    ("Super Admin", "Full system access"),
    ("IT Admin", "Infrastructure management"),
    ("SOC Analyst", "Security monitoring"),
    ("Viewer", "Read-only access"),
]


def seed():
    db: Session = SessionLocal()

    try:
        # Create roles
        for name, description in ROLES:
            role = db.query(Role).filter(Role.name == name).first()

            if not role:
                role = Role(
                    name=name,
                    description=description,
                )
                db.add(role)

        db.commit()

        # Get Super Admin role
        super_admin = (
            db.query(Role)
            .filter(Role.name == "Super Admin")
            .first()
        )

        # Create admin user
        admin = (
            db.query(User)
            .filter(User.username == "admin")
            .first()
        )

        if not admin:
            admin = User(
                username="admin",
                email="admin@aiops.local",
                hashed_password=hash_password("Admin@123"),
                role_id=super_admin.id,
            )

            db.add(admin)
            db.commit()

        print("✅ Database seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed()