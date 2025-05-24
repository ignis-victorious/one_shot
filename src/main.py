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
    page.title = "Manny's Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    counter: Text = Text(value="0", size=50)
    status: Text = Text(value="", size=50)  # This will display the actual status string
    text: Text = Text(value="Please press +/-", size=30)

    def increase(e) -> None:
        counter.value = str(object=int(counter.value) + 1)
        status.value = str(object="You added one")
        # Update the 'text' control's value based on the current status
        text.value = f"Current action: {status.value}. Total: {counter.value}"
        counter.update()
        status.update()
        text.update()

    def decrease(e) -> None:
        counter.value = str(object=int(counter.value) - 1)
        status.value = str(object="You removed one")
        # Update the 'text' control's value based on the current status
        text.value = f"Current action: {status.value}. Total: {counter.value}"
        counter.update()
        status.update()
        text.update()

    btn_inc: ElevatedButton = ElevatedButton(text="+", on_click=increase)
    btn_dec: ElevatedButton = ElevatedButton(text="-", on_click=decrease)

    page.add(
        ft.Column(  # Group controls in a Column for better layout control
            controls=[
                btn_inc,
                counter,
                btn_dec,
                status,
                text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center items within the column
            spacing=20,
        )
    )

    page.update()


if __name__ == "__main__":
    app(target=main)

    # def main(page: Page) -> None:
    #     page.title = "Manny's Counter"
    #     page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #     counter: Text = Text(value="0", size=50)
    #     status: Text = Text(value="", size=50)  # This will display the actual status string
    #     text: Text = Text(
    #         value="Current action: None", size=30
    #     )  # This will describe the action

    # def increase(e) -> None:
    #     new_count: int = int(counter.value) + 1
    #     counter.value = str(object=new_count)
    #     status_message: str = "You added one"
    #     status.value = status_message
    #     # Update the 'text' control's value based on the current status
    #     text.value = f"Current action: {status_message}. Total: {new_count}"

    # Update all controls whose values have changed
    # counter.update()
    # status.update()
    # text.update()  # <--- THIS IS THE KEY! Update the 'text' control

    # def decrease(e) -> None:
    #     new_count: int = int(counter.value) - 1
    #     counter.value = str(object=new_count)
    #     status_message: str = "You removed one"
    #     status.value = status_message
    #     # Update the 'text' control's value based on the current status
    #     text.value = f"Current action: {status_message}. Total: {new_count}"

    #     # Update all controls whose values have changed
    #     counter.update()
    #     status.update()
    #     text.update()  # <--- THIS IS THE KEY! Update the 'text' control

    # btn_inc: ElevatedButton = ElevatedButton(text="+", on_click=increase)
    # btn_dec: ElevatedButton = ElevatedButton(text="-", on_click=decrease)

    # page.add(
    #     ft.Column(  # Group controls in a Column for better layout control
    #         controls=[
    #             btn_inc,
    #             counter,
    #             # btn_dec,
    #             status,  # Display the specific action message
    #             text,  # Display the combined descriptive text
    #         ],
    #         horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center items within the column
    #         spacing=20,  # Add some space between controls
    #     )
    # )
    # # Important: Call page.update() after adding all controls to ensure they are rendered initially
    # page.update()


# if __name__ == "__main__":
#     app(target=main)
# def main(page: Page) -> None:
#     page.title = "Manny's test"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

#     counter: Text = Text(value="0", size=50)
#     status: Text = Text(value="", size=50)
#     text: Text = Text(value="Current action: None", size=30)

#     def increase(e) -> None:
#         counter.value = str(object=int(counter.value) + 1)
#         status.value = "You added one"
#         text.value = f"Current action: {status.value}. Total: {counter.value}"
#         counter.update()
#         status.update()
#         text.update()

#     def decrease(e) -> None:
#         counter.value = str(object=int(counter.value) - 1)
#         status.value = "You removed one"
#         text.value = f"Current action: {status.value}. Total: {counter.value}"
#         counter.update()
#         status.update()

#     btn_inc: ElevatedButton = ElevatedButton(text="+", on_click=increase)
#     btn_dec: ElevatedButton = ElevatedButton(text="-", on_click=decrease)

#     page.add(btn_inc, counter, btn_dec, text)


# if __name__ == "__main__":
#     app(target=main)
# app(target=main, view=ft.WEB_BROWSER)
