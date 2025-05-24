#  _______________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, Text, ElevatedButton
#  Import FILES
#  https://www.youtube.com/watch?v=S64XGQiQp68
#  https://www.youtube.com/watch?v=xr7vDSFXjW0
#  https://www.youtube.com/watch?v=529LYDgRTgQ

#  _______________________


# _________________ 42.18
def main(page: Page) -> None:
    page.title = "Manny's test"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    counter: Text = Text(value="0", size=50)

    def increase(e) -> None:
        counter.value = str(object=int(counter.value) + 1)
        counter.update()

    def decrease(e) -> None:
        counter.value = str(object=int(counter.value) - 1)
        counter.update()

    btn_inc: ElevatedButton = ElevatedButton(text="+", on_click=increase)
    btn_dec: ElevatedButton = ElevatedButton(text="-", on_click=decrease)

    page.add(btn_inc, counter, btn_dec)

    # _________________ 24.10
    # text: Text = Text(value="Hello World", size=50)
    # page.add(text)

    # page.add(
    #     ft.Container(
    #         content=ft.Row(
    #             controls=[
    #                 Text(value="Left"),
    #                 Text(value="center"),
    #                 Text(value="Right"),
    #             ],
    #             alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    #         ),
    # content=ft.Icon(name=ft.Icons.ACCESS_TIME),
    # content=ft.Icon(name=ft.Icons.HOME),
    # content=ft.ListView(
    #     controls=[
    #         Text(value="I am happy", color="black"),
    #         Text(
    #             value="I am happy",
    #             color="black",
    #             font_family="Arial",
    #         ),
    #         Text(value="We will succed!", size=22),
    #         Text(
    #             value="You're soo cool",
    #             size=18,
    #             weight=ft.FontWeight.BOLD,
    #             font_family="Arial",
    #         ),
    #     ]
    # ),
    # content=Text(value="Hello World", size=24),
    #     bgcolor="#000000",
    #     # bgcolor="#aaaaaa",
    #     # bgcolor="blue",
    #     margin=10,
    #     border_radius=10,
    # ),
    # ft.Tabs(
    #     selected_index=0,
    #     tabs=[
    #         ft.Tab(text="Home", content=Text(value="This is the Home page")),
    #         ft.Tab(text="About", content=Text(value="This is the About page")),
    #         ft.Tab(text="Contact", content=Text(value="This is the Contact page")),
    #     ],
    # ),
    # _________________ Start
    # Text(value="Some text here ...."),
    # Text(
    #     value="___________________________________________________________________________________________________"
    # ),
    # ListView(
    #     controls=[
    #         ft.Text(value="List 1"),
    #         ft.Text(value="List 2"),
    #         ft.Text(value="List 3"),
    #     ]
    # ),
    # )

    # page.add(
    #     Text(value="hello World"),
    #     TextField(label="Username", hint_text="Enter Your Username"),
    #     OutlinedButton(text="Login"),
    #     TextButton("Login"),
    #     Checkbox(label="Subscibed to the new magazine?"),
    #     Switch(label="Dark Mode"),
    #     Dropdown(
    #         label="Branch",
    #         options=[
    #             ft.dropdown.Option(key="CSE"),
    #             ft.dropdown.Option(key="AI-ML"),
    #             ft.dropdown.Option(key="DS"),
    #             ft.dropdown.Option(key="IT"),
    #         ],
    #     ),
    #     ft.Slider(min=0, max=10, divisions=10),
    # )


if __name__ == "__main__":
    app(target=main)
    # app(target=main, view=ft.WEB_BROWSER)
