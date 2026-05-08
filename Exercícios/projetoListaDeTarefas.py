class Tarefa:
    def __init__(self):
        self.proximo_id = 1
        self.lista_de_tarefas = []

    def cadastrar_tarefa(self):
        nome = input("Digite o nome da tarefa que deseja cadastrar: ")
        categoria = input("Digite a categoria da tarefa: ")
        prioridade = input("Digite a prioridade da tarefa: ")
        status = input("Digite o status da tarefa: ")

        nova_tarefa = {
            "id": self.proximo_id,
            "nome": nome,
            "categoria": categoria,
            "prioridade": prioridade,
            "status": status
        }
        self.lista_de_tarefas.append(nova_tarefa)
        self.proximo_id += 1
        print("Tarefa cadastrada com sucesso!!!")

    def ver_tarefas(self, lista=None):
        exibir_tarefas = lista if lista is not None else self.lista_de_tarefas
        if not exibir_tarefas:
            print("\nTarefa não encontrada. Tente novamente.")
            return 

        for tarefa in exibir_tarefas:
            print(f"\nID: {tarefa['id']} | Nome: {tarefa['nome']} | Categoria: {tarefa['categoria']} | Prioridade: {tarefa['prioridade']} | Status: {tarefa['status']}")

    def mudar_status(self):
        id_busca = int(input("Digite o ID da tarefa que deseja alterar: "))
        encontrada = False
        for tarefa in self.lista_de_tarefas:
            if tarefa['id'] == id_busca:
                novo_status = input("Digite o status novo: ")
                tarefa['status'] = novo_status
                print("Status atualizado com sucesso!!!")
                encontrada = True
                break
        if not encontrada:
            print("ID não encontrado. Tente novamente.")

    def filtrar_prioridade(self):
        prio = input("Digite a prioridade que será filtrada: ")
        filtradas = [t for t in self.lista_de_tarefas if t['prioridade'].lower() == prio.lower()]
        self.ver_tarefas(filtradas)

def executar_sistema():
    sistema = Tarefa()
    while True:
        print("\n--- MENU DE TAREFAS ---")
        print("1. Cadastrar Nova Tarefa")
        print("2. Ver Todas as Tarefas")
        print("3. Mudar Status de Tarefa")
        print("4. Filtrar por Prioridade")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sistema.cadastrar_tarefa()
        elif opcao == "2":
            sistema.ver_tarefas()
        elif opcao == "3":
            sistema.mudar_status()
        elif opcao == "4":
            sistema.filtrar_prioridade()
        elif opcao == "5":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Digite uma opção válida.")

if __name__ == "__main__":
    executar_sistema()