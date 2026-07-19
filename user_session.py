class UserSession:
    def __init__(self, username: str, has_alert_access: bool):
        self._username = username
        self._has_alert_access = has_alert_access

    def send_notification(self):
        if self._has_alert_access:
            print(f"[УВЕДОМЛЕНИЕ] Пользователю {self._username} отправлено уведомление о входе в систему")
        else:
            print(f"[УВЕДОМЛЕНИЕ] Пользователь {self._username} не имеет доступа к оповещениям")