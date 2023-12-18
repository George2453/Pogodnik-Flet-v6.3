import flet as ft
import requests

def get_weather(city):
    api_key = "cef30b9ce8a29e66ffa882b58826229c" # api
    base_url = "http://api.openweathermap.org/data/2.5/weather" # источник
    params = {
        "q": city,
        "appid": api_key,
        "lang": "ru",
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if weather_data["cod"] == 200:
        temperature = weather_data["main"]["temp"]
        wind_speed = weather_data["wind"]["speed"]
        description = weather_data["weather"][0]["description"]

        return temperature, wind_speed, description
    else:
        return None

def update_weather(city, page):
    weather_info = get_weather(city)
    if weather_info:
        temperature, wind_speed, description = weather_info
        weather_text = f' B городе "{city}" сейчас: \n {temperature}° градусов, {description} \n Cкopocть ветра {wind_speed} м/c'
        page.add(ft.Text(weather_text))
    else:
        page.add(ft.Text("Ошибка! Город не найден."))

def main(page: ft.Page):
    page.window_width = 550        # ширина окна
    page.window_height = 500       # высота окна
    page.window_resizable = False  # неизменяемый размер
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.BLUE_400), # Тема
    )
    def click_drop():
        pass
    def change_theme(e):
        page.theme_mode = 'dark' if page.theme_mode == 'light' else 'light' # кнопка темы
        page.update()
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click = change_theme)
            ],
            alignment=ft.MainAxisAlignment.START
        )
    )
    page.add(
        ft.Text(
            spans=[
                ft.TextSpan(
                    "      Погодник v6.4                 ",
                    ft.TextStyle(
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        foreground=ft.Paint(
                            gradient=ft.PaintLinearGradient(
                                (0, 10), (149, 170), [ft.colors.PURPLE, ft.colors.BLUE],
                            )
                        ),
                    ),
                ),
            ],
      )
    )
     # В будущем
   # page.add(ft.Row([ft.ElevatedButton("Город 1", on_click=click_drop), ft.ElevatedButton("Город 2", on_click=click_drop)]))
    def add_clicked(e):
        city = new_task.value
        update_weather(city, page)
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Название города", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Узнать", on_click=add_clicked)], alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main)
