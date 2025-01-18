import flet as ft
from interfaces.header import Header
from interfaces.menu import Menu
from interfaces.create_user import CreateUser

def main(page: ft.Page):
    header = Header()
    menu = Menu()
    create_user = CreateUser(page)

    body = ft.Row(
        controls=[
            menu,
            create_user
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
