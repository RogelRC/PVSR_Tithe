import flet as ft

from interfaces.create_user import CreateUser
from interfaces.header import Header
from interfaces.menu import Menu


def main(page: ft.Page):
    header = Header()
    create_user = CreateUser(page)
    menu = Menu(toggle_visibility_callback=create_user.toggle_visibility)

    form = ft.Row(
        controls=[
            create_user
        ],
        expand = 4,
    )

    body = ft.Row(
        controls=[
            menu,
            form
        ],
        expand=5
    )

    page.add(
        header,
        body
    )
    page.title = "Iglesia Evangélica Pentecostal Asambleas de Dios Palabras de Vida Sobre la Roca"
    page.bgcolor = ft.Colors.BLACK
    page.window.maximized = True

ft.app(target=main)
