#  _______________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, Text, TextField, ElevatedButton
#  Import FILES
#  https://www.youtube.com/watch?v=S64XGQiQp68
#  https://www.youtube.com/watch?v=DHUl_KncLdU
#  https://www.youtube.com/watch?v=xr7vDSFXjW0
#  https://www.youtube.com/watch?v=529LYDgRTgQ

# _________________ @ 2:31:20


def main(page: Page) -> None:
    page.title = "Login page"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 30
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    username = TextField(label="Username", autofocus=True)
    password = TextField(label="Password", password=True, can_reveal_password=True)
    message: Text = Text()

    VALID_USERNAME = "admin"
    VALID_PASSWORD = "1234"

    def login_clicked(e):
        if username.value == VALID_USERNAME and password.value == VALID_PASSWORD:
            message.value = "Login Successful!"
            message.color = "green"
        else:
            message.value = "Invalid username or password"
            message.color = "red"
        page.update()

    login_btn = ElevatedButton("Login", on_click=login_clicked)

    page.add(username, password, login_btn, message)


if __name__ == "__main__":
    app(target=main)
