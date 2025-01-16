import datetime
import flet as ft
from services import *
import re


def main(page: ft.Page):
    header = ft.Container(
        content=ft.Text("Bienvenido al sistema de administración de diezmos", size=20, color=ft.Colors.WHITE),
        alignment=ft.alignment.center,
        height=50,  # Altura fija del encabezado
        border_radius=20,
        bgcolor="#202120"
    )

    tb_name = ft.TextField(label="Nombre(s)", expand=2)
    tb_last_name = ft.TextField(label="Apellidos", expand=2)
    sex_dropdown = ft.Dropdown(
        label="Sexo",
        expand=1,
        options=[
            ft.dropdown.Option("M"),
            ft.dropdown.Option("F"),
        ]
    )

    full_name_row = ft.Row(
        controls = [
            tb_name,
            tb_last_name,
            sex_dropdown
        ]
    )

    type_dropdown = ft.Dropdown(
        label="Tipo",
        options=[
            ft.dropdown.Option("Miembro"),
            ft.dropdown.Option("Visitante"),
            #ft.dropdown.Option("Anónimo")
        ]
    )

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
        controls = [
            tb_birth_date,
            birth_date_picker
        ]
    )

    zone_options = [ft.dropdown.Option(zone.name) for zone in get_zones()]
    zone_options.pop(0)

    zone_dropdown = ft.Dropdown(
        label="Territorio",
        options=zone_options
    )

    tb_address = ft.TextField(label="Dirección")

    marital_state_dropdown = ft.Dropdown(
        label="Estado civil",
        options=[
            ft.dropdown.Option("Casado(a)"),
            ft.dropdown.Option("Soltero(a)"),
            ft.dropdown.Option("Viudo(a)")
        ]
    )

    tb_dni = ft.TextField(label="Carnet de identidad")

    tb_phone = ft.TextField(label="Teléfono fijo")

    tb_cellphone = ft.TextField(label="Teléfono celular")

    tb_notes = ft.TextField(label="Notas", multiline=True, expand=True)

    def reset_controls(container):
        for control in container.controls:
            if isinstance(control, ft.TextField):
                control.value = ""  # Limpia el valor del TextField
            elif isinstance(control, ft.Dropdown):
                control.value = None  # Restablece el Dropdown a su estado inicial
            elif isinstance(control, (ft.Row, ft.Column)):  # Verifica contenedores anidados
                reset_controls(control)  # Llama a la función recursivamente
            # Agrega otras condiciones según el tipo de control
            control.update()  # Actualiza cada control para reflejar los cambios

    def save_user_button_accion(container):
        name = tb_name.value or None
        last_name = tb_last_name.value or None
        sex = sex_dropdown.value or None
        type = type_dropdown.value or None

        formatted_date = tb_birth_date.value.split('-')[::-1]
        formatted_date = ''.join(formatted_date)
        birth_date = re.sub('-', "", formatted_date) or None

        zone_code = get_zone_code_by_name(zone_dropdown.value)

        if((type == "Miembro" and name is None and last_name is None and type is None and zone_code is None)
        or(type == "Visitante" and name is None and last_name is None and type is None)):
            # Crear un diálogo de advertencia
            def handle_close(e):
                page.close(dlg_modal)
            dlg_modal = ft.AlertDialog(
                modal=True,
                title=ft.Text("Advertencia"),
                content=ft.Text("Llena los campos obligatorios"),
                actions=[
                    ft.TextButton("Aceptar", on_click=handle_close),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            page.open(dlg_modal)
            return

        address = tb_address.value or None
        marital_state = marital_state_dropdown.value or None
        dni = tb_dni.value or None
        phone = tb_phone.value or None
        cellphone = tb_cellphone.value or None
        notes = tb_notes.value or None

        create_user(name, last_name, sex, type, zone_code, birth_date, address, marital_state, dni, phone, cellphone,
                    notes)

        reset_controls(container)

    save_button = ft.ElevatedButton(
        text="Guardar",
        bgcolor=ft.Colors.GREEN,
        expand=True,
        on_click=lambda e: save_user_button_accion(input_user_column)
    )

    cancel_button = ft.ElevatedButton(
        text="Cancelar",
        bgcolor=ft.Colors.RED,
        expand=True,
        on_click=lambda e: reset_controls(input_user_column)
    )

    action_buttons = ft.Row(
        controls=[
            save_button,
            cancel_button
        ],
        spacing=20
    )

    input_user = [
        full_name_row,
        type_dropdown,
        birth_date_row,
        zone_dropdown,
        tb_address,
        marital_state_dropdown,
        tb_dni,
        tb_phone,
        tb_cellphone,
        tb_notes,
        action_buttons
    ]

    input_user_column = ft.Column(
        visible=False,
        controls=input_user,
        expand=True
    )

    def visibility_toggle(obj):
        obj.visible = not obj.visible
        obj.update()

    body = ft.Container(
        input_user_column,
        alignment=ft.alignment.center,
        expand=True,  # Ocupa el espacio restante
        border_radius=20,
        bgcolor="#202120",
        padding=20
    )

    blue_border = ft.ButtonStyle(
        side=ft.BorderSide(color=ft.Colors.BLUE, width=1),
        bgcolor="#202120",
        text_style=ft.TextStyle(
            size=18  # Color del texto blanco
        )
    )

    green_border = ft.ButtonStyle(
        side=ft.BorderSide(color=ft.Colors.GREEN, width=1),
        bgcolor="#202120",
        text_style=ft.TextStyle(
            size=18
        )
    )

    get_users_button = ft.Button(text="Mostrar usuarios", width=200, height=50, style=blue_border)
    add_user_button = ft.Button(text="Añadir usuario", width=200, height=50, style=blue_border,
                                on_click=lambda e: visibility_toggle(input_user_column))

    get_tethe_button = ft.Button(text="Mostrar diezmos", width=200, height=50, style=green_border)
    add_tethe_button = ft.Button(text="Añadir diezmo", width=200, height=50, style=green_border)

    menu = [
        get_users_button,
        add_user_button,
        get_tethe_button,
        add_tethe_button
    ]

    menu_container = ft.Container(
        ft.Column(
            controls=menu,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=32
        ),
        border_radius=20,
        bgcolor="#202120"
    )

    main_content = ft.Column(
        controls=[header, body],
        expand=4  # 4/5 del espacio total
    )

    layout = ft.Row(
        controls=[
            ft.Container(menu_container, expand=1),  # Menú 1/5
            main_content  # Contenido principal 4/5
        ],
        expand=True  # Expandir para ocupar toda la pantalla
    )

    page.title = "Iglesia Evangélica Pentecostal Asambleas de Dios Palabras de Vida Sobre la Roca"
    page.bgcolor = ft.Colors.BLACK  # Color de fondo de la página
    page.window.maximized = True

    page.add(layout)

# Ejecutar la aplicación Flet
ft.app(target=main)
