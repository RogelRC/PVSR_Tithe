import flet as ft
from backend.services import get_zones
from backend.services import create_user
from backend.services import get_zone_code_by_name
from datetime import datetime


class CreateUser(ft.Container):

    def __init__(self, page):
        super().__init__(self)

        # nombre(s), apellidos y sexo
        self.tb_name = ft.TextField(label="Nombre(s)", expand=3)
        self.tb_last_name = ft.TextField(label="Apellidos(s)", expand=3)
        self.dropdown_sex = ft.Dropdown(
            label="Sexo",
            options=[
                ft.dropdown.Option("M"),
                ft.dropdown.Option("F"),
            ],
            expand=1
        )

        full_name_row = ft.Row(
            controls=[
                self.tb_name,
                self.tb_last_name,
                self.dropdown_sex
            ],
            spacing=20
        )

        # tipo de diezmador
        self.type_dropdown = ft.Dropdown(
            label="Tipo",
            options=[
                ft.dropdown.Option("Miembro"),
                ft.dropdown.Option("Visitante"),
                # ft.dropdown.Option("Anónimo")
            ]
        )

        # fecha de nacimiento
        self.tb_birth_date = ft.TextField(label="Fecha de nacimiento", read_only=True, expand=True)

        def handle_change(e):
            self.tb_birth_date.value = e.control.value.strftime('%d-%m-%Y')  # Asigna directamente la cadena formateada
            self.tb_birth_date.update()

        birth_date_picker = ft.ElevatedButton(
            "Selecciona una fecha",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date=datetime(year=1900, month=1, day=1),
                    last_date=datetime.now(),
                    on_change=handle_change,
                )
            ),
        )

        birth_date_row = ft.Row(
            controls=[
                self.tb_birth_date,
                birth_date_picker
            ],
            spacing = 20
        )

        # Territorio y direccion
        zone_options = [ft.dropdown.Option(zone.name) for zone in get_zones()]
        zone_options.pop(0)

        self.zone_dropdown = ft.Dropdown(
            label="Territorio",
            options=zone_options,
            expand=1
        )

        self.tb_address = ft.TextField(label="Dirección", expand=3)

        full_address_row = ft.Row(
            controls=[
                self.zone_dropdown,
                self.tb_address
            ],
            spacing=20
        )

        # estado civil y carnet de identidad
        self.marital_state_dropdown = ft.Dropdown(
            label="Estado civil",
            options=[
                ft.dropdown.Option("Casado(a)"),
                ft.dropdown.Option("Soltero(a)"),
                ft.dropdown.Option("Viudo(a)")
            ],
            expand=1
        )

        self.tb_dni = ft.TextField(label="Carnet de identidad", expand=3)

        full_legal_row = ft.Row(
            controls=[
                self.marital_state_dropdown,
                self.tb_dni
            ],
            spacing=20
        )

        # telefonos
        self.tb_phone = ft.TextField(label="Teléfono fijo", expand=True)
        self.tb_cellphone = ft.TextField(label="Teléfono celular", expand=True)

        full_phone_row = ft.Row(
            controls=[
                self.tb_phone,
                self.tb_cellphone
            ],
            spacing=20
        )

        # notas
        self.tb_notes = ft.TextField(label="Notas", multiline=True, expand=True)

        # botones de guardar o cancelar
        def clean_fields():
            self.tb_name.value = None
            self.tb_last_name.value = None
            self.dropdown_sex.value = None
            self.type_dropdown.value = None
            self.tb_birth_date.value = None
            self.zone_dropdown.value = None
            self.tb_address.value = None
            self.marital_state_dropdown.value = None
            self.tb_dni.value = None
            self.tb_phone.value = None
            self.tb_cellphone.value = None
            self.tb_notes.value = None

            self.page.update()

        def save_user():
            if(
                not self.tb_name.value or
                not self.tb_last_name.value or
                not self.type_dropdown.value or
                not self.zone_dropdown.value
            ):
                def handle_close():
                    page.close(dialog)

                dialog = ft.AlertDialog(
                    modal=True,
                    title=ft.Text("Advertencia"),
                    content=ft.Text("Debes llenar todos los campos obligatorios:\nNombre(s)\nApellidos\nTipo\nTerritorio"),
                    actions=[
                        ft.TextButton("Aceptar", on_click=lambda e: handle_close()),
                    ],
                    actions_alignment=ft.MainAxisAlignment.END
                )

                page.open(
                    dialog
                )
                return

            def reformat_date(date_str):
                # Parse the input date
                date_obj = datetime.strptime(date_str, "%d-%m-%Y")
                # Format and return as 'yyyymmdd'
                return date_obj.strftime("%Y%m%d")

            fixed_birth_date = self.tb_birth_date.value

            if fixed_birth_date:
                fixed_birth_date = reformat_date(fixed_birth_date)

            create_user(
                self.tb_name.value or None,
                self.tb_last_name.value or None,
                self.dropdown_sex.value or None,
                self.type_dropdown.value or None,
                fixed_birth_date or None,
                get_zone_code_by_name(self.zone_dropdown.value) or None,
                self.tb_address.value or None,
                self.marital_state_dropdown.value or None,
                self.tb_dni.value or None,
                self.tb_phone.value or None,
                self.tb_cellphone.value or None,
                self.tb_notes.value or None
            )

            clean_fields()

        save_button = ft.ElevatedButton(
            text="Guardar",
            bgcolor=ft.Colors.GREEN,
            expand=True,
            on_click=lambda e: save_user()
        )

        restart_button = ft.ElevatedButton(
            text="Reiniciar",
            bgcolor=ft.Colors.RED,
            expand=True,
            on_click=lambda e: clean_fields()
        )

        action_buttons = ft.Row(
            controls=[
                save_button,
                restart_button
            ],
            spacing=20
        )

        # Contenido
        self.content = ft.Column(
            controls=[
                full_name_row,
                self.type_dropdown,
                birth_date_row,
                full_address_row,
                full_legal_row,
                full_phone_row,
                self.tb_notes,
                action_buttons
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
        self.zone_dropdown.options = [ft.dropdown.Option(zone.name) for zone in get_zones()]
        self.zone_dropdown.options.pop(0) # Actualiza las opciones del dropdown
        self.zone_dropdown.update()  # Refresca el dropdown en la UI
