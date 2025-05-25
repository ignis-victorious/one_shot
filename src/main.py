#  _______________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, Text, TextField, Column, ElevatedButton
#  Import FILES
#  https://www.youtube.com/watch?v=S64XGQiQp68
#  https://www.youtube.com/watch?v=DHUl_KncLdU
#  https://www.youtube.com/watch?v=xr7vDSFXjW0
#  https://www.youtube.com/watch?v=529LYDgRTgQ

# _________________ @ 2:31:20


def main(page: Page) -> None:
    page.title = "Multiplication-table Generator"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 30
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    tmp: Text = Text()

    number_input: TextField = TextField(
        label="Enter a Number", width=200, keyboard_type=ft.KeyboardType.NUMBER
    )

    result: Column = Column(controls=[])

    def clear_page() -> None:
        page.controls.clear()

    def generate_table(e) -> None:
        print("inside generate_table")
        if number_input.value.isdigit():
            num = int(number_input.value)
            print(f"num: {num}")
            for i in range(1, 11):
                print(f"i: {i} ")
                line = f" {num} X {i} = {num * i}"
                result.controls.append(Text(value=line, size=18))
            result.controls.append(
                ElevatedButton(text="Press to clear", on_click=clear_page)
            )
        else:
            result.controls.append(Text(value="Please Enter A Valid Number"))
        page.update()

    generate_btn = ElevatedButton(
        text="Press to generate the table", on_click=generate_table
    )

    page.add(number_input, generate_btn, result)


if __name__ == "__main__":
    app(target=main)
