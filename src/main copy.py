#  _______________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, Text, Switch
#  Import FILES
#  https://www.youtube.com/watch?v=S64XGQiQp68
#  https://www.youtube.com/watch?v=xr7vDSFXjW0
#  https://www.youtube.com/watch?v=529LYDgRTgQ

#  _______________________


# _________________ 54.00
def main(page: Page) -> None:
    page.title = "Theme Switcher App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def theme_switcher(e) -> None:
        if e.control.value:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        text.value = f"Current Theme : {page.theme_mode.value}"

        page.update()

    btn: Switch = Switch(label="Dark Mode", on_change=theme_switcher)
    text: Text = Text(value=f"Current Theme : {page.theme_mode.value}", size=35)
    page.add(text, btn)

    # page.update()


if __name__ == "__main__":
    app(target=main)
