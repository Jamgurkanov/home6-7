import webbrowser

import flet as ft

def main(page: ft.Page):
    page.title = "my first deskstop app"


    name_input = ft.TextField(label="Enter your name")
    greeting_text = ft.Text("Welcome to my first deskstop app", color=ft.Colors.WHITE)



    page.add(greeting_text, name_input)






ft.app(target=main)
