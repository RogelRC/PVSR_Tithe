import flet as ft
from backend.services import get_users_with_zone, \
    delete_user  # Asegúrate de importar el servicio y las funciones necesarias


class ShowUsers(ft.Container):
    def __init__(self, page):
        super().__init__(self)

        # Crear la tabla vacía
        self.data_table = ft.DataTable(
            expand=True,
            border_radius=10,
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.Colors.BLACK12,
            heading_row_height=50,
            data_row_color={ft.ControlState.HOVERED: "0x30FF0000"},
            divider_thickness=1,
            column_spacing=15,
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Nombre(s)")),
                ft.DataColumn(ft.Text("Apellidos")),
                ft.DataColumn(ft.Text("Territorio")),
                ft.DataColumn(ft.Text("Acciones")),  # Columna para los iconos
            ],
            rows=[]
        )

        # Contenedor principal
        self.content = ft.Column(
            controls=[
                self.data_table,
            ],
            spacing=32,
            expand=True,
        )

        self.expand = True
        self.border_radius = 20
        self.bgcolor = "#202120"
        self.padding = ft.padding.all(32)
        self.visible = False

    def load_data(self):
        """
        Carga los datos de los usuarios con información de la zona
        y los agrega a la tabla.
        """
        # Obtener datos del servicio
        users_with_zones = get_users_with_zone()

        # Limpiar filas existentes
        self.data_table.rows.clear()

        # Agregar nuevas filas
        for user in users_with_zones:
            self.data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(user["id"]))),
                        ft.DataCell(ft.Text(user["name"])),
                        ft.DataCell(ft.Text(user["last_name"])),
                        ft.DataCell(ft.Text(user["zone_name"])),
                        ft.DataCell(  # Celda para los iconos de acción
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.VISIBILITY,
                                        tooltip="Ver detalles",
                                        on_click=lambda e, user_id=user["id"]: self.show_user_details(user_id),
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.EDIT,
                                        tooltip="Editar usuario",
                                        on_click=lambda e, user_id=user["id"]: self.edit_user(user_id),
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.DELETE,
                                        tooltip="Eliminar usuario",
                                        icon_color="red",
                                        on_click=lambda e, user_id=user["id"]: self.delete_user(user_id),
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            )

        # Actualizar la vista
        self.update()

    def show_user_details(self, user_id):
        print(f"Mostrar detalles del usuario {user_id}")
        # Aquí puedes implementar la lógica para mostrar detalles del usuario

    def edit_user(self, user_id):
        print(f"Editar usuario {user_id}")
        # Aquí puedes implementar la lógica para editar al usuario

    def delete_user(self, user_id):
        print(f"Eliminar usuario {user_id}")
        # Confirmación y eliminación del usuario
        def handle_close():
            page.close(confirmation)

        confirmation = ft.AlertDialog(
            title=ft.Text("Confirmar eliminación"),
            content=ft.Text("¿Estás seguro de que deseas eliminar este usuario?"),
            actions=[
                ft.TextButton(
                    "Cancelar", on_click=lambda _: handle_close()
                ),
                ft.TextButton(
                    "Eliminar",
                    on_click=lambda _: (
                        delete_user(user_id),  # Llamar al servicio para eliminar
                        self.load_data(),  # Recargar datos
                        handle_close()
                    ),
                ),
            ],
        )

        self.content.controls.append(confirmation)
        self.update()
