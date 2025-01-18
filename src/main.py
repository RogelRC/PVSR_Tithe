import flet as ft

from interfaces.create_user import CreateUser
from interfaces.header import Header
from interfaces.menu import Menu
from interfaces.show_users import ShowUsers


def main(page: ft.Page):
    page.title = "Iglesia Evangélica Pentecostal Asambleas de Dios Palabras de Vida Sobre la Roca"
    page.bgcolor = ft.Colors.BLACK
    page.window.maximized = True

    # Configurar la localización
    page.locale_configuration = ft.LocaleConfiguration(
        supported_locales=[ft.Locale("es", "ES")],  # Soporta español
        current_locale=ft.Locale("es", "ES")  # Establecer el idioma actual a español
    )

    header = Header()
    create_user = CreateUser(page)
    menu = Menu(toggle_visibility_callback=lambda index: set_visible(index))
    show_users = ShowUsers(page)

    controls=[
        create_user,
        show_users
    ]

    def set_visible(index_visible):
        for i, control in enumerate(controls):
            control.visible = (i == index_visible)

            if control.visible:
                # Si el control tiene un método de actualización, llámalo
                if hasattr(control, "load_data"):
                    control.load_data()

        page.update()

    form = ft.Row(
        controls=controls,
        expand = 4
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

ft.app(target=main)
