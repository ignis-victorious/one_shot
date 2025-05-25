#  _______________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, Text, ElevatedButton
#  Import FILES
#  https://www.youtube.com/watch?v=S64XGQiQp68
#  https://www.youtube.com/watch?v=DHUl_KncLdU
#  https://www.youtube.com/watch?v=xr7vDSFXjW0
#  https://www.youtube.com/watch?v=529LYDgRTgQ

# _________________ @ 2:00:00


flashcards: list[tuple[str, str]] = [
    ("What is the capital of France?", "Paris"),
    ("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
    ("What is 5 + 7?", "12"),
]


def main(page: Page) -> None:
    page.title = "Flashcards app!"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    current_card_index: int = 0
    show_answer: bool = False

    def next_flashcard(e) -> None:
        nonlocal current_card_index
        current_card_index += 1
        if current_card_index >= len(flashcards):
            current_card_index = 0
        update_flashcard()

    def flip_card(e) -> None:
        nonlocal show_answer
        show_answer = not show_answer
        update_flashcard()

    def update_flashcard() -> None:
        question, answer = flashcards[current_card_index]
        flashcard_label.value = question if not show_answer else answer
        page.update()

    flashcard_label = Text("", size=24)
    flip_button = ElevatedButton(text="Flip", on_click=flip_card)
    next_button = ElevatedButton(text="Next", on_click=next_flashcard)

    page.add(flashcard_label, flip_button, next_button)

    update_flashcard()

    # page.update()

    page.add()


if __name__ == "__main__":
    app(target=main)
