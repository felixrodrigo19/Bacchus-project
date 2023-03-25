from bacchus.ext.db.models import User


class AuthService:
    @staticmethod
    def verify_login(user):
        db_result = User.query.filter_by(email=user.get("username")).first()
        if db_result is not None:
            if user.get("username") == db_result.email and user.get("password") == db_result.passwd:
                return True
        return False
