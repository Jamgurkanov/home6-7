import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text(value='Hello world')
    greeting_history = []
    history_text = ft.Text(value="История приветствий:")

    def on_button_click(_):
        name = name_input.value.strip()
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        if name:
            greeting_text.value = f'{timestamp} — Hello, {name}!'
            greeting_text.color = None
            name_input.value = ""

            greeting_history.append(f"{timestamp} — {name}")
            history_text.value = "История приветствий:\n" + '\n'.join(greeting_history)
        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED

        page.update()

    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'История приветствий:'
        page.update()

    def delete_last(_):
        if greeting_history:
            greeting_history.pop()
            history_text.value = "История приветствий:\n" + '\n'.join(greeting_history)
        else:
            history_text.value = "История пуста!"
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)
    send_button = ft.ElevatedButton(text='SEND', on_click=on_button_click)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    delete_last_button = ft.IconButton(icon=ft.Icons.REMOVE, tooltip="Удалить последнее", on_click=delete_last)

    page.add(
        ft.Row([greeting_text], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([name_input, send_button, clear_button, delete_last_button]),
        history_text
    )

ft.app(target=main)
