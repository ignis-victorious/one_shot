#  _______________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, ElevatedButton, Image, FilePicker, Column
#  Import FILES
#  https://www.youtube.com/watch?v=S64XGQiQp68
#  https://www.youtube.com/watch?v=DHUl_KncLdU
#  https://www.youtube.com/watch?v=xr7vDSFXjW0
#  https://www.youtube.com/watch?v=529LYDgRTgQ

# _________________ @ 2:07:08


def main(page: Page) -> None:
    page.title = "Image previewer"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    image_preview: Image = Image()

    def on_file(e) -> None:
        if e.files:
            image_preview.src = e.files[0].path
            page.update()

    file_picker: FilePicker = FilePicker(on_result=on_file)

    page.add(
        Column(
            controls=[
                ElevatedButton(
                    text="Upload Image", on_click=lambda _: file_picker.pick_files()
                ),
                image_preview,
            ],
        ),
        file_picker,
    )

    # page.add()


if __name__ == "__main__":
    app(target=main)
