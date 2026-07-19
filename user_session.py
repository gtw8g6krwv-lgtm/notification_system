class UserSession:
    def __init__(self, username: str, has_alert_access: bool):
        self._username = username
        self._has_alert_access = has_alert_access