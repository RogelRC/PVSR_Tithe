import flet as ft

from backend.services import get_users_with_zone
from flet.core import alignment


class ShowUsers(ft.Container):

    def __init__(self, page):
        super().__init__(self)

        users = get_users_with_zone()

        table = ft.DataTable(
            columns=[
                ft.DataColumn(
                    ft.Text("ID"),
                    numeric=True
                ),
                ft.DataColumn(
                    ft.Text("Nombre(s)")
                ),
                ft.DataColumn(
                    ft.Text("Apellidos")
                ),
                ft.DataColumn(
                    ft.Text("Tipo")
                ),
                ft.DataColumn(
                    ft.Text("Territorio")
                ),
                ft.DataColumn(
                    ft.Text("Opciones")
                ),
            ],
            rows = [
                ft.DataRow([
                    ft.DataCell(ft.Text(user['id'])),
                    ft.DataCell(ft.Text(user['name'])),
                    ft.DataCell(ft.Text(user['last_name'])),
                    ft.DataCell(ft.Text(user['type'])),
                    ft.DataCell(ft.Text(user['zone_name'])),
                    ft.DataCell(
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.TEXT_SNIPPET_SHARP,
                                    icon_color="white",
                                    icon_size=25,
                                    tooltip="Ver detalles",
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.EDIT_NOTE_ROUNDED,
                                    icon_color="yellow",
                                    icon_size=25,
                                    tooltip="Editar",
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.DELETE,
                                    icon_color="red",
                                    icon_size=25,
                                    tooltip="Eliminar",
                                )
                            ]
                        )
                    )
                ])for user in users
            ],
            expand=True,
        )

        # Contenido
        self.content = ft.Column(
            controls=[
                table
            ],
            spacing=32,
            expand=True
        )

        self.expand = True
        self.border_radius = 20
        self.bgcolor = "#202120"
        self.padding = ft.padding.all(32)
        self.visible = True