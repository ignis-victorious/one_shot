#  _______________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, ElevatedButton, Column, Row, Colors, Container
#  Import FILES
#  https://www.youtube.com/watch?v=S64XGQiQp68
#  https://www.youtube.com/watch?v=DHUl_KncLdU
#  https://www.youtube.com/watch?v=xr7vDSFXjW0
#  https://www.youtube.com/watch?v=529LYDgRTgQ

# _________________ @ 2:12:58


def main(page: Page) -> None:
    page.title = "An app to draw"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    rows, cols = 30, 30
    # rows, cols = 20, 20
    cell_size: int = 15
    # cell_size: int = 25
    selected_color: Colors = Colors.BLACK
    grid: list = []

    def paint_cell(e) -> None:
        print("inside Paint")
        e.control.bgcolor = selected_color
        e.control.update()

    for _ in range(rows):
        row: list = []
        for _ in range(cols):
            cell: Container = Container(
                width=cell_size,
                height=cell_size,
                bgcolor=Colors.WHITE,
                border=ft.border.all(width=0.5, color=Colors.GREY),
                on_click=paint_cell,
            )
            row.append(cell)
        grid.append(row)

    grid_ui: Column = Column(
        controls=[Row(controls=row, spacing=0) for row in grid],
        spacing=0,
    )

    def clear_canvas(e) -> None:
        print("inside clear")
        for row in grid:
            print("inside row")
            for cell in row:
                print("inside cell")
                cell.bcolor = Colors.RED

        print("Ready to update")
        page.update()

    page.add(grid_ui, ElevatedButton(text="Clear", on_click=clear_canvas))

    page.add()


if __name__ == "__main__":
    app(target=main)
