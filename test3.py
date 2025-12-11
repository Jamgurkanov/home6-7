import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value='Hello world')

    greeting_history = []
    favorite_names = []
    history_text = ft.Text(value="История приветствий:")
    favorites_text = ft.Text(value="Любимые имена:")

    def on_button_click(_):
        name = name_input.value.strip()
        timestamp = datetime.now().strftime("%y:%m:%d - %H:%M:%S")

        if name:
            greeting_text.value = f'{timestamp} Hello {name}'
            greeting_text.color = None
            name_input.value = None

            greeting_history.append(name)
            history_text.value = "История приветствий:\n" + '\n'.join(greeting_history)
        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED


        page.update()

    def add_favorite(_):
        name = name_input.value.strip()
        if name and name not in favorite_names:
            favorite_names.append(name)
            favorites_text.value = "Любимые имена:\n" + "\n".join(favorite_names)
            page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)
    button_elevated = ft.ElevatedButton(text='send', on_click=on_button_click)
    favorite_button = ft.ElevatedButton(text='В избранное', on_click=add_favorite)

    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'История приветствий:'
        page.update()

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    def morning(_):
        if greeting_history:
            greeting_text.value = '\n'.join([f"Hello {name}" for name in greeting_history])
        page.update()

    def evening(_):
        if greeting_history:
            greeting_text.value = '\n'.join([f"Hello {name}" for name in greeting_history])
        page.update()

    morning_button = ft.ElevatedButton(text="Morning", on_click=morning)
    evening_button = ft.ElevatedButton(text="Evening", on_click=evening)

    view_greeting_text = ft.Row([greeting_text], alignment=ft.MainAxisAlignment.CENTER)

    page.add(
        view_greeting_text,
        ft.Row([name_input, button_elevated, favorite_button, clear_button]),
        ft.Row([morning_button, evening_button], alignment=ft.MainAxisAlignment.CENTER),
        favorites_text,
        history_text
    )

ft.app(target=main)

