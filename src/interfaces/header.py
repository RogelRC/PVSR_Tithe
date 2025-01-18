import flet as ft

class Header(ft.Container):
    def __init__(self):
        super().__init__(
            content=ft.Text(
                "Bienvenido al sistema de administración de diezmos",
                size=20,
                color=ft.Colors.WHITE
            ),
            alignment=ft.alignment.center,
            height=50,  # Altura fija del encabezado
            border_radius=20,
            bgcolor="#202120"
        )
