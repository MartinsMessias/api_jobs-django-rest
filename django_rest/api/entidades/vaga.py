class Vaga():
    def __init__(self, titulo, descricao, salario, local, quantidade, contato, tipo_contratacao, tecnologias):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__salario = salario
        self.__local = local
        self.__quantidade = quantidade
        self.__contato = contato
        self.__tipo_contratacao = tipo_contratacao
        self.__tecnologias = tecnologias

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, local):
        self.__local = local

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def tipo_contratacao(self):
        return self.__tipo_contratacao

    @tipo_contratacao.setter
    def tipo_contratacao(self, tipo_contratacao):
        self.__tipo_contratacao = tipo_contratacao

    @property
    def tecnologias(self):
        return self.__tecnologias

    @tecnologias.setter
    def tecnologias(self, tecnologias):
        self.__tecnologias = tecnologias