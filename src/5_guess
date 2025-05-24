#  _______________________
#  Import LIBRARIES
import random
import flet as ft
from flet import Page, app, Text, TextField, Column, ElevatedButton
#  Import FILES
#  https://www.youtube.com/watch?v=S64XGQiQp68
#  https://www.youtube.com/watch?v=DHUl_KncLdU
#  https://www.youtube.com/watch?v=xr7vDSFXjW0
#  https://www.youtube.com/watch?v=529LYDgRTgQ

# _________________ @ 1:20:00


def generate_number() -> int:
    return random.randint(a=1, b=100)


def main(page: Page) -> None:
    page.title = "Guess a number!"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    number_to_guess: int = generate_number()
    print(number_to_guess)
    text: Text = Text(value="Enter a Number (1-100) : ")
    input_field: TextField = TextField(
        label="Number:",
        autofocus=True,
        width=80,
    )
    guess_btn: ElevatedButton = ElevatedButton(
        text="Check your guess",
        on_click=lambda e: check_guess(
            input_field=input_field, result_text=result_text
        ),
    )
    result_text: Text = ft.Text(".")

    def check_guess(input_field, result_text) -> None:
        user_guess: int = int(input_field.value)
        if user_guess == number_to_guess:
            result_text.value = f"You guessed correctly!\n The number was {user_guess}"
            print("Inside if")
        elif user_guess < number_to_guess:
            result_text.value = "Your guess is too low"
            guess_btn.text = "New Game"
            guess_btn.on_click = start_new_game
            print("Inside high")
        elif user_guess > number_to_guess:
            result_text.value = "Your guess is too high"
            print("Inside low")
        else:
            result_text.value = f"Sorry, the correct number was {number_to_guess}"
        page.update()

    def start_new_game(e) -> None:
        nonlocal number_to_guess
        number_to_guess = generate_number()
        input_field.value = ""
        guess_btn.text = "Check your guess"
        result_text.value = ""
        guess_btn.on_click = (
            lambda e: check_guess(input_field=input_field, result_text=result_text),
        )
        page.update()

        # guess_btn.on_click = start_new_game

    page.add(
        Column(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            controls=[text, input_field, guess_btn, result_text],
        )
    )


if __name__ == "__main__":
    app(target=main)
