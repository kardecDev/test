class Pessoa:
    def __init__(self, nome: str, idade: int, email: str):
        self.nome = nome
        self.idade = idade
        self.email = email

    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

    def fazer_aniversario(self):
        self.idade += 1
        print(f"Feliz aniversário, {self.nome}! Agora você tem {self.idade} anos.")

    def __repr__(self) -> str:
        return f"Pessoa(nome='{self.nome}', idade={self.idade}, email='{self.email}')"