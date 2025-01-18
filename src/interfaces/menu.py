import flet as ft

class Menu(ft.Container):
    def __init__(self):
        super().__init__(self)

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

        get_users_button = ft.Button(text="Mostrar usuarios", expand_loose=True, height=50, style=blue_border)
        add_user_button = ft.Button(text="Añadir usuario", expand_loose=True, height=50, style=blue_border)
        get_tethe_button = ft.Button(text="Mostrar diezmos", expand_loose=True, height=50, style=green_border)
        add_tethe_button = ft.Button(text="Añadir diezmo", expand_loose=True, height=50, style=green_border)

        self.content = ft.Column(
            controls=[
                get_users_button, add_user_button, get_tethe_button, add_tethe_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=32,
        )

        self.border_radius = 20
        self.bgcolor = "#202120"
        self.expand = 1
        self.padding = ft.padding.all(20)