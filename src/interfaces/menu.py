import flet as ft

class Menu(ft.Container):
    def __init__(self, toggle_visibility_callback):
        super().__init__(self)

        self.toggle_visibility_callback = toggle_visibility_callback

        blue_border = ft.ButtonStyle(
            side=ft.BorderSide(color=ft.Colors.BLUE, width=1),
            bgcolor="#202120",
            text_style=ft.TextStyle(size=18)
        )

        green_border = ft.ButtonStyle(
            side=ft.BorderSide(color=ft.Colors.GREEN, width=1),
            bgcolor="#202120",
            text_style=ft.TextStyle(size=18)
        )

        get_users_button = ft.Button(
            text="Mostrar usuarios",
            expand=3,
            height=50,
            style=blue_border,
            on_click=lambda e: self.toggle_visibility_callback(1)
        )
        add_user_button = ft.IconButton(
            icon=ft.Icons.ADD_CIRCLE,
            icon_color="blue",
            icon_size=50,
            tooltip="Añadir miembro",
            on_click=lambda e: self.toggle_visibility_callback(0)
        )
        users_row = ft.Row(
            controls=[
                get_users_button,
                add_user_button
            ],
            expand_loose=True
        )

        get_tithe_button = ft.Button(text="Mostrar diezmos", expand=3, height=50, style=green_border)
        add_tithe_button = ft.IconButton(
            icon=ft.Icons.ADD_CIRCLE,
            icon_color="green",
            icon_size=50,
            tooltip="Registrar diezmo",
        )
        tithe_row = ft.Row(
            controls=[
                get_tithe_button,
                add_tithe_button
            ],
            expand_loose=True
        )

        self.content = ft.Column(
            controls=[
                users_row, tithe_row
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=32,
        )

        self.border_radius = 20
        self.bgcolor = "#202120"
        self.expand = 1
        self.padding = ft.padding.all(20)