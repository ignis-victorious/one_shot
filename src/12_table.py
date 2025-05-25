#  _______________________
#  Import LIBRARIES
import re
import flet as ft
from flet import Page, app, Text, TextField
#  Import FILES
#  https://www.youtube.com/watch?v=S64XGQiQp68
#  https://www.youtube.com/watch?v=DHUl_KncLdU
#  https://www.youtube.com/watch?v=xr7vDSFXjW0
#  https://www.youtube.com/watch?v=529LYDgRTgQ

# _________________ @ 2:12:58


def main(page: Page) -> None:
    page.title = "Password strength checker"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    result_text: Text = Text(value="", size=20, weight=ft.FontWeight.BOLD)

    def check_password_strength(e) -> None:
        password: str = str(e.control.value)
        strength: int = 0

        if len(password) >= 8:
            strength += 1
        if re.search(pattern=r"[A-Z]", string=password):
            strength += 1
        if re.search(pattern=r"[a-z]", string=password):
            strength += 1
        if re.search(pattern=r"\d", string=password):
            strength += 1
        if re.search(pattern=r"[!@#$%^&*]", string=password):
            strength += 1

        print(f"Strength: {strength}")

        if strength <= 2:
            result_text.value = "Weak 😟"
            result_text.color = "red"
        elif strength == 3 or strength == 4:
            result_text.value = "Midium 🤨"
            result_text.color = "yellow"
        else:
            result_text.value = "Strong 💪"
            result_text.color = "green"
        page.update()

    password_input: TextField = TextField(
        label="Enter Password",
        password=True,
        can_reveal_password=True,
        on_change=check_password_strength,
        width=300,
    )

    page.add(password_input, result_text)


if __name__ == "__main__":
    app(target=main)
