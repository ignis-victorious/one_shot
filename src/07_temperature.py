#  _______________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app, Text, TextField, Dropdown, ElevatedButton
#  Import FILES
#  https://www.youtube.com/watch?v=S64XGQiQp68
#  https://www.youtube.com/watch?v=DHUl_KncLdU
#  https://www.youtube.com/watch?v=xr7vDSFXjW0
#  https://www.youtube.com/watch?v=529LYDgRTgQ

# _________________ @ 1:44:44


def main(page: Page) -> None:
    page.title = "Temperature converter"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    temp_input = TextField(label="Enter Temperature", autofocus=True)
    unit_selector = Dropdown(
        label="Select Unit",
        options=[
            ft.dropdown.Option(key="Celcius"),
            ft.dropdown.Option(key="Fahrenheit"),
            ft.dropdown.Option(key="Kelvin"),
        ],
    )

    result_text = Text(value="Converted Value : ", size=20)
    output_value = Text(value="", size=20)

    def convert_temperature(e) -> None:
        print("Inside convert_temperature")
        temp: float = float(temp_input.value)
        unit: str | None = unit_selector.value
        print(temp, " ", unit)
        if unit == "Celcius":
            fahrenheit: float = (temp * 9 / 5) + 32
            kelvin: float = temp + 273.15
            result_text.value = (
                f"Fahrenheit : {fahrenheit:.2f}ºF\nKelvin : {kelvin:.2f}K"
            )
            print(f"Cel - Fahrenheit : {fahrenheit:.2f}ºF   Kelvin : {kelvin:.2f}K")
        elif unit == "Fahrenheit":
            celcius: float = (temp - 32) * 5 / 9
            kelvin: float = celcius + 273.15
            result_text.value = f"Celcius: {celcius:.2f}°C\nKelvin : {kelvin:.2f}K"
            print(f"Far - Celcius: {celcius:.2f}°C   Kelvin : {kelvin:.2f}K")
        elif unit == "Kelvin":
            celcius: float = temp - 273.15
            fahrenheit: float = (temp - 273.15) * 5 / 9 + 32
            result_text.value = (
                f"Fahrenheit: {fahrenheit: 2f}°F\nCelcius : {celcius: 2f}°C"
            )
            print(f"Kel - Fahrenheit: {fahrenheit: 2f}°F   Celcius : {celcius: 2f}°C")

        output_value.value = "Converted SuccessFully"

        page.update()

    convert_btn = ElevatedButton(text="Convert", on_click=convert_temperature)

    page.add(temp_input, unit_selector, convert_btn, result_text, output_value)


if __name__ == "__main__":
    app(target=main)
