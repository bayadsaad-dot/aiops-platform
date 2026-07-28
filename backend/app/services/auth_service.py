from sqlalchemy.orm import Session

from app.core.security import create_access_token, verify_password
from app.repositories.user_repository import UserRepository


class AuthService:

    @staticmethod
    def login(db: Session, username: str, password: str):
        user = UserRepository.get_by_username(db, username)

        if not user:
            return None

        if not verify_password(password, user.hashed_password):
            return None

        access_token = create_access_token(user.id)

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }