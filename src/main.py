#  _______________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, Text, TextField, FilePicker, SnackBar, Row, ElevatedButton, Icons
#  Import FILES
#  https://www.youtube.com/watch?v=S64XGQiQp68
#  https://www.youtube.com/watch?v=DHUl_KncLdU
#  https://www.youtube.com/watch?v=xr7vDSFXjW0
#  https://www.youtube.com/watch?v=529LYDgRTgQ

# _________________ @ 2:31:20


def main(page: Page) -> None:
    page.title = "Simple text editor"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 30
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 800
    page.window.height = 600
    page.scroll = ft.ScrollMode.AUTO

    text_area = TextField(
        multiline=True, min_lines=20, expand=True,
        hint_text="Type Your Notes Here..."
    )
    
    file_picker_open = FilePicker ()
    file_picker_save_as = FilePicker()

    current_file_path: dict = {"path":None}

    def open_file_result(e: ft.FilePickerResultEvent) -> None:
        if e.files:
            file_path = e.files[0].path 
            try:
                with open(file_path, mode="r", encoding="utf-8") as f:
                    text_area. value = f.read ()
                    current_file_path["path"] = file_path
                    page.snack_bar = SnackBar(content=Text(value=f"Opened : {file_path}"))
                    page.snack_bar.open = True
                    page.update()
            except Exception as err:
                page.snack_bar = SnackBar(Text(value=f"Error : {err}", color="red"))
                page.snack_bar.open = True
                page.update()


    def save_as_result(e: ft.FilePickerResultEvent) -> None:
        if e.path: 
            try:
                with open(e.path, mode="w", encoding="utf-8") as f:
                    f.write(text_area.value)
                    current_file_path["path"] = e. path
                    # page.snack_bar === page.overlay.append(page.snack_bar)
                    page.snack_bar= SnackBar(content=Text(value="Saved As : {e.path}"))
                    page.snack_bar.open = True
                    page.update()
            except Exception as err:
                page.snack_bar = SnackBar (ft. Text(f"Error : {err}", color="red"))
                page.snack_bar.open = True
                page.update()

    def save_clicked(e) -> None:
        if current_file_path["path"]:
            try:
                with open(current_file_path["path"], mode="w", encoding=utf-8) as f:
                f.write (text_area. value)
                page.snack_bar = SnackBar(content=ft. Text(value=f"Saved As: {e.path}"))
                page.snack_bar.open = True
                page.update()
            except Exception as err:
                page.snack_bar = ft.SnackBar(content=Text(value=f"Error : {err}", color="red"))
                page.snack_bar.open = True
                page.update()
        else:
            file_picker_save_as.save_file(file_type="text")

    file_picker_open.on_result = open_file_result
    file_picker_save_as = save_as_result
    
    page.overlay.append(file_picker_open) 
    page.overlay.append(file_picker_save_as)
    
    page.add(
        text_area, 
        Row(controls=[
            ElevatedButton (text="Open", icon=Icons.FOLDER_OPEN,on_click=lambda e: file_picker_open.pick_files(allow_multiple=False)),
            ElevatedButton (text="Save", icon=Icons.SAVE, on_click=save_clicked),
            ElevatedButton (text="Save As", icon=Icons.SAVE_AS, on_click=lambda e: file_picker_save_as.save_file(file_type="text"))
        ], spacing=20)
    )






if __name__ == "__main__":
    app(target=main)
