import flet as ft #①部分

def main(page: ft.Page): #②部分
    page.title = "BB777"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    shopNameTitle = ft.Text(value="店名", size=50)
    page.add(
        ft.Row(
            [
                ft.Dropdown(
                    label="SHOP",
                    hint_text="SUPER-CONCORDE 市野",
                    options=[
                        ft.dropdown.Option("SUPER-CONCORDE 市野"),
                        ft.dropdown.Option("Green"),
                        ft.dropdown.Option("Blue"),
                    ],
                    autofocus=True,
                )
            ],
        )
    )

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100) #③

    def minus_click(e): #③部分
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e): #③部分
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    ) #④部分

ft.app(target=main) #②部分