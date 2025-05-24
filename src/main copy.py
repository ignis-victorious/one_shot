#  _______________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, Text, Row
from datetime import datetime
import time
import threading  # We'll use this explicitly for clarity, though Flet often abstracts it.

#  Import FILES
#  https://www.youtube.com/watch?v=S64XGQiQp68
#  https://www.youtube.com/watch?v=xr7vDSFXjW0
#  https://www.youtube.com/watch?v=529LYDgRTgQ

#  _______________________


# _________________ 1:02:20
def main(page: Page) -> None:
    page.title = "Digital clock!"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    time_display: Text = Text(
        value="00:00:00", color=ft.Colors.CYAN_300, size=60, weight=ft.FontWeight.BOLD
    )

    page.add(
        Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                time_display,
            ],
        )
    )

    def update_time_background(e) -> None:
        while True:
            # Get current time
            now: str = datetime.now().strftime(format="%H:%M:%S")

            # Update the value of the Flet Text control
            # This change happens in the background thread.
            time_display.value = now

            # Request Flet to update this specific control on the UI.
            # This is safe to call from a background thread.
            time_display.update()

            print("Inside while")
            # Wait for 1 second before updating again
            time.sleep(1)

    # Start the background thread
    # It's better to start the thread explicitly using 'threading.Thread'
    # and then start it. Flet's run_thread is good for Flet-specific tasks.
    # For a simple background loop, standard threading is perfectly fine.
    # We make it a daemon thread so it exits when the main application exits.
    clock_thread = threading.Thread(target=update_time_background, daemon=True)
    clock_thread.start()

    # Any other controls you want to add initially
    # Remove the second static Text control, it's not needed for the clock functionality
    # page.add(Text(value=f"{time_display.value}")) # This line is removed

    # No need for page.update() here as time_display.update() will handle the rendering
    # once the thread starts.

    # page.run_thread(handler=update_time)  # Old

    # page.add(Text(value=f"{update_time_background.value}"))
    # page.add(Text(value="Hello Mum!", size=55))

    # page.update()


if __name__ == "__main__":
    app(target=main)
