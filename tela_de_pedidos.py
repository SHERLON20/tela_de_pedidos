import flet as ft
from delete_pg import consulta_bd
from conexao_pg import conn
from time import sleep
def main(page:ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM todos_pedidos")
    result = cursor.fetchall()
    def mudar_foto(e):
        if e.control.content.src=='nao.jpeg':
            e.control.content.src = 'verificado.jpeg'
        else:
            e.control.content.src = 'nao.jpeg'
        e.control.update()
    
    def atualiza(e):
        while e.control.value == True:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM todos_pedidos")
            resultado = cursor.fetchall()
            parte_pedidos.content.controls=[
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Container(
                            data=l[1],
                            content=ft.Text(value=l[0],color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,size=20),
                            bgcolor=ft.colors.with_opacity(color=ft.colors.WHITE,opacity=1.0),
                            shadow=ft.BoxShadow(blur_radius=5,color=ft.colors.BLACK),
                            padding=ft.padding.only(left=15,right=15,bottom=5,top=5),
                            border_radius=ft.border_radius.all(10),
                            col={'xs':10}
                                ),
                        ft.Column(
                            col={'xs':2},
                            controls=[
                                ft.Container(
                            content=ft.Image(
                                src='deleta.png'
                            ),width=50,height=50,on_click=deleta
                        ),
                                ft.Container(
                                    border_radius=ft.border_radius.all(30),
                                    bgcolor=ft.colors.BLACK,
                            content=ft.Image(
                                src='nao.jpeg'
                            ),width=50,height=50,on_click=mudar_foto
                        )
                            ]
                        )
                    ]
            ) for l in resultado
            ]
            parte_pedidos.update()
            sleep(5)
            conn.commit()
    
    def deleta(e):
        valor = e.control.parent.parent.controls[0].data
        for p in parte_pedidos.content.controls:
            if p.controls[0].data == e.control.parent.parent.controls[0].data:
                parte_pedidos.content.controls.remove(p)
        consulta_bd(sql='DELETE FROM todos_pedidos WHERE id = %s ',valores=(valor,))
        
        parte_pedidos.update()
        print(valor)
    tela=ft.Column(
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text(
                value='tela de pedidos',
                color=ft.colors.WHITE,
                size=30,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                ),
            ft.ListTile(
                title=ft.Text(
                    value='atualizar automatico',
                    weight=ft.FontWeight.BOLD
                    ),
                trailing=ft.Switch(active_color=ft.colors.RED,adaptive=True,on_change=atualiza)
            ),
          parte_pedidos :=  ft.Container(
              expand=True,
        padding=ft.padding.all(30),
        content=ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            expand=True,
            auto_scroll=True,
            controls=[
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Container(
                            data=item[1],
                            content=ft.Text(value=item[0],color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,size=20),
                            bgcolor=ft.colors.with_opacity(color=ft.colors.WHITE,opacity=1.0),
                            shadow=ft.BoxShadow(blur_radius=5,color=ft.colors.BLACK),
                            padding=ft.padding.only(left=15,right=15,bottom=5,top=5),
                            border_radius=ft.border_radius.all(10),
                            col={'xs':10}
                                ),
                       ft.Column(
                            col={'xs':2},
                            controls=[
                                ft.Container(
                            content=ft.Image(
                                src='deleta.png'
                            ),width=50,height=50,on_click=deleta
                        ),
                                ft.Container(
                                    border_radius=ft.border_radius.all(30),
                                    bgcolor=ft.colors.BLACK,
                            content=ft.Image(
                                src='nao.jpeg'
                            ),width=50,height=50,on_click=mudar_foto
                        )
                            ]
                        )
                    ]
            ) for item in result
            ]
        )
    )
        ]
    )
    
    page.add(tela)
ft.app(target=main,assets_dir='assets')