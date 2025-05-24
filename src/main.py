#  _______________________
#  Import LIBRARIES
import flet as ft
<<<<<<< HEAD
from flet import Page, app, View, Text, ElevatedButton, Column, Row
=======
from flet import Page, app, Text, Switch
>>>>>>> 5_theme_switcher
#  Import FILES
#  https://www.youtube.com/watch?v=S64XGQiQp68
#  https://www.youtube.com/watch?v=xr7vDSFXjW0
#  https://www.youtube.com/watch?v=529LYDgRTgQ
# 

#  _______________________  47.18


<<<<<<< HEAD
def main(page: Page) -> None:
    def route_change(e) -> None:
        page.views.clear()
        if page.route == "/":
            page.views.append(
                View(
                    route="/",
                    controls=[
                        Row(
                            controls=[
                                Text(
                                    value="This is the Home Page. Press a butto to navigate:"
                                ),
                                # Text(value="Contact Page"),
                            ]
                        ),
                        Row(
                            controls=[
                                ElevatedButton(
                                    text="Go To About",
                                    on_click=lambda _: page.go("/about"),
                                ),
                                ElevatedButton(
                                    text="Goto Contact",
                                    on_click=lambda _: page.go(route="/contact"),
                                ),
                            ]
                        ),
                        # Text(value="Home"),
                        # ElevatedButton(
                        #     text="Go To About", on_click=lambda _: page.go("/about")
                        # ),
                        # Text(value="Contact Page"),
                        # ElevatedButton(
                        #     text="Goto Contact",
                        #     on_click=lambda _: page.go(route="/contact"),
                        # ),
                    ],
                )
            )
        elif page.route == "/about":
            page.views.append(
                ft.View(
                    route="/about",
                    controls=[
                        Text(value="This is the About Page"),
                        ElevatedButton(
                            text="Back", on_click=lambda _: page.go(route="/")
                        ),
                        ElevatedButton(
                            text="Goto Contact",
                            on_click=lambda _: page.go(route="/contact"),
                        ),
                    ],
                )
            )
        elif page.route == "/contact":
            page.views.append(
                ft.View(
                    route="/contact",
                    controls=[
                        Text(value="This is the Contact Page"),
                        ElevatedButton(
                            text="Goto Home Page", on_click=lambda _: page.go(route="/")
                        ),
                        Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                Text(value="Add here your Email and conctact number")
                            ],
                            spacing=20,
                        ),
                    ],
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go(route=page.route)
=======
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
>>>>>>> 5_theme_switcher


if __name__ == "__main__":
    app(target=main)
<<<<<<< HEAD
    # app(target=main, view=ft.WEB_BROWSER)
=======
>>>>>>> 5_theme_switcher
