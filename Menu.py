class DadosPaciente:
    def __init__(self, nome, cpf, email, logradouro, data_nascimento, idade):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.logradouro = logradouro
        self.data_nascimento = data_nascimento
        self.idade = idade

pacientes = []

def cadastrar_paciente(nome, cpf, email, logradouro, data_nascimento, idade):
    paciente = DadosPaciente(nome, cpf, email, logradouro, data_nascimento, idade)
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

def fazer_login(email):
    for paciente in pacientes:
        if paciente.email == email:
            paciente_logado = paciente
            print("Login realizado com sucesso!")
            return paciente_logado
    print("Paciente não encontrado. Verifique o email e tente novamente.")
    return None

if __name__ == "__main__":
    escolha = 0

    while escolha != 4:
        print("Menu:")
        print("1. Cadastrar Paciente")
        print("2. Fazer Login")
        print("3. Exibir Dados do Paciente Logado")
        print("4. Sair")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            print("Digite o nome do paciente: ")
            nome_cadastro = input()
            print("Digite o cpf do paciente: ")
            cpf_cadastro = input()
            print("Digite o email do paciente: ")
            email_cadastro = input()
            print("Digite o endereço do paciente: ")
            logradouro_cadastro = input()
            print("Digite a Data de nascimento do paciente: ")
            data_cadastro = input()
            print("Digite a idade do paciente: ")
            idade_cadastro = int(input())

            cadastrar_paciente(nome_cadastro, cpf_cadastro, email_cadastro, logradouro_cadastro, data_cadastro, idade_cadastro)

        elif escolha == 2:
            print("Email do Paciente para login: ")
            email_login = input()
            paciente_logado = fazer_login(email_login)

        elif escolha == 3:
            if paciente_logado is not None:
                print("Dados do paciente logado: ")
                print(f"Nome: {paciente_logado.nome}, CPF: {paciente_logado.cpf}, Email: {paciente_logado.email}, Endereço: {paciente_logado.logradouro}, Data de Nascimento: {paciente_logado.data_nascimento}, Idade: {paciente_logado.idade}")
            else:
                print("Nenhum paciente logado, faça login.")

        elif escolha == 4:
            print("Saindo do programa.")

        else:
            print("Opção inválida. Tente novamente.")
