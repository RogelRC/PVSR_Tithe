import datetime

import flet as ft

from backend.services import get_zones


class CreateUser(ft.Container):
    def __init__(self, page):
        super().__init__(self)

        # nombre(s), apellidos y sexo
        tb_name = ft.TextField(label="Nombre(s)", expand=3)
        tb_last_name = ft.TextField(label="Apellidos(s)", expand=3)
        dropdown_sex = ft.Dropdown(
            label="Sexo",
            options=[
                ft.dropdown.Option("M"),
                ft.dropdown.Option("F"),
            ],
            expand=1
        )

        full_name_row = ft.Row(
            controls=[
                tb_name,
                tb_last_name,
                dropdown_sex
            ],
            spacing=20
        )

        # tipo de diezmador
        type_dropdown = ft.Dropdown(
            label="Tipo",
            options=[
                ft.dropdown.Option("Miembro"),
                ft.dropdown.Option("Visitante"),
                # ft.dropdown.Option("Anónimo")
            ]
        )

        # fecha de nacimiento
        tb_birth_date = ft.TextField(label="Fecha de nacimiento", read_only=True, expand=True)

        def handle_change(e):
            tb_birth_date.value = e.control.value.strftime('%d-%m-%Y')  # Asigna directamente la cadena formateada
            tb_birth_date.update()

        birth_date_picker = ft.ElevatedButton(
            "Selecciona una fecha",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date=datetime.datetime(year=1900, month=1, day=1),
                    last_date=datetime.datetime.now(),
                    on_change=handle_change,
                )
            ),
        )

        birth_date_row = ft.Row(
            controls=[
                tb_birth_date,
                birth_date_picker
            ],
            spacing = 20
        )

        # Territorio y direccion
        zone_options = [ft.dropdown.Option(zone.name) for zone in get_zones()]
        zone_options.pop(0)

        zone_dropdown = ft.Dropdown(
            label="Territorio",
            options=zone_options,
            expand=1
        )

        tb_address = ft.TextField(label="Dirección", expand=3)

        full_address_row = ft.Row(
            controls=[
                zone_dropdown,
                tb_address
            ],
            spacing=20
        )

        # estado civil y carnet de identidad
        marital_state_dropdown = ft.Dropdown(
            label="Estado civil",
            options=[
                ft.dropdown.Option("Casado(a)"),
                ft.dropdown.Option("Soltero(a)"),
                ft.dropdown.Option("Viudo(a)")
            ],
            expand=1
        )

        tb_dni = ft.TextField(label="Carnet de identidad", expand=3)

        full_legal_row = ft.Row(
            controls=[
                marital_state_dropdown,
                tb_dni
            ],
            spacing=20
        )

        # telefonos
        tb_phone = ft.TextField(label="Teléfono fijo", expand=True)
        tb_cellphone = ft.TextField(label="Teléfono celular", expand=True)

        full_phone_row = ft.Row(
            controls=[
                tb_phone,
                tb_cellphone
            ],
            spacing=20
        )

        # notas
        tb_notes = ft.TextField(label="Notas", multiline=True, expand=True)

        # botones de guardar o cancelar
        save_button = ft.ElevatedButton(
            text="Guardar",
            bgcolor=ft.Colors.GREEN,
            expand=True,
            #on_click=lambda e: save_user_button_accion(input_user_column)
        )

        cancel_button = ft.ElevatedButton(
            text="Cancelar",
            bgcolor=ft.Colors.RED,
            expand=True,
            #on_click=lambda e: reset_controls(input_user_column)
        )

        action_buttons = ft.Row(
            controls=[
                save_button,
                cancel_button
            ],
            spacing=20
        )







        # Contenido
        self.content = ft.Column(
            controls=[
                full_name_row,
                type_dropdown,
                birth_date_row,
                full_address_row,
                full_legal_row,
                full_phone_row,
                tb_notes,
                action_buttons
            ],
            spacing=32,
            expand=True,
        )


        self.expand = 4
        self.border_radius = 20
        self.bgcolor = "#202120"
        self.padding = ft.padding.all(32)