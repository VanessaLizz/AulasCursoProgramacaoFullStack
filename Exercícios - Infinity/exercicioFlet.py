import flet as ft

def inicio(pagina: ft.Page):
    pagina.title = "Lista de Tarefas"

    def adicionarTarefa(e):
        if entrada_do_usuario.value:
            lista.controls.append(ft.Checkbox(label=entrada_do_usuario.value))
            entrada_do_usuario.value = ""
            pagina.update()

    entrada_do_usuario = ft.TextField(label="Escreva a tarefa que deseja adicionar: ", expand=True, on_submit=adicionarTarefa)
    lista = ft.ListView(expand=True)

    pagina.add(ft.Row([entrada_do_usuario,ft.ElevatedButton("Adicionar Tarefa", on_click=adicionarTarefa)]),lista)

ft.app(target=inicio)