#  _______________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, Text, TextField
#  Import FILES
#  https://www.youtube.com/watch?v=S64XGQiQp68
#  https://www.youtube.com/watch?v=DHUl_KncLdU
#  https://www.youtube.com/watch?v=xr7vDSFXjW0
#  https://www.youtube.com/watch?v=529LYDgRTgQ

# _________________ @ 1:44:44


def main(page: Page) -> None:
    page.title = "Character counting"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    text_input: TextField = TextField(
        label="Enter Your Text", multiline=True, width=300
    )
    char_count: Text = Text(value="Character Count : 0", size=20)

    def update_char_count(e):
        char_count.value = f"Character Count : {len(text_input.value)}"
        page.update()

    text_input.on_change = update_char_count

    page.add(text_input, char_count)


if __name__ == "__main__":
    app(target=main)
