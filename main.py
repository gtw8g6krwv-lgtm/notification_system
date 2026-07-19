from user_session import UserSession


def main():
    print("\nЗдравствуйте!")
    username = input("Пожалуйста, введите ваше имя: ")
    print(f"Добро пожаловать, {username} в систему оповещений!")

    user = UserSession(username, True)
    user.send_notification()


if __name__ == "__main__":
    main()