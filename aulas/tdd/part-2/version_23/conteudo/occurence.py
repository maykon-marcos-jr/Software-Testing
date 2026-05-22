from enum import Enum
"""
    Cada ocorrência tem um funcionário responsável, que precisa trabalhar no mesmo projeto da ocorrência
    Cada funcionário pode trabalhar em vários projetos simultaneamente, e pode ser responsável por várias ocorrências.
    Uma chave identifica unicamente uma ocorrência e um resumo mostra sobre o que trata a ocorrência.
    Cada ocorrência pode estar em dois estados: aberta ou fechada.
    Quando uma ocorrência é criada, ela é atribuída ao seu responsável e permanece no estado aberta enquanto o seu responsável não a termina.
    Quando o responsável termina a ocorrência, ela é fechada.
    O responsável pela ocorrência pode ser modificado somente enquanto a ocorrência está aberta.
    ▪ Existem diferentes tipos de ocorrências: tarefa, bug, refatoração.
    ▪ Cada ocorrência tem diferentes prioridades (alta, média, baixa) e estas prioridades podem ser modificadas somente enquanto a ocorrência está aberta.
    ▪ Cada funcionário pode ser responsável por, no máximo, 10 ocorrências abertas considerando todos os projetos nos quais ele participa
"""

class Occ_Priority(Enum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3

class Occ_Type(Enum):
    TAREFA = 1
    BUG = 2
    REFATORACAO = 3

class Occurence:
    def __init__(
        self,
        key:str,
        name:str,
        project:str,
        leader:str,
        type:Occ_Type,
        priority:Occ_Priority,
        description:str,
    ):
        self.__key = key
        self.__name = name
        self.__project = project
        self.__leader = leader
        self.__type = type
        self.__priority = priority
        self.__description = description
        self.__is_open = True


    def get_key(self) -> str:
        return self.__key


    def get_name(self) -> str:
        return self.__name


    def get_project(self) -> str:
        return self.__project


    def get_leader(self) -> str:
        return self.__leader


    def get_type(self) -> Occ_Type:
        return self.__type


    def get_priority(self) -> Occ_Priority:
        return self.__priority


    def get_description(self) -> str:
        return self.__description


    def is_open(self) -> bool:
        return self.__is_open

    def finish_occurence(self):
        if self.__is_open:
            self.__is_open = False
        else:
            raise Exception(f"Occurence {self.__key} Already Closed")

    def reset_priority(self, new_priority:Occ_Priority):
        if self.__is_open:
            self.__priority = new_priority
        else:
            raise Exception(f"Occurence {self.__key} is Closed")

    def change_leader(self, new_leader:str):
        if self.__is_open:
            self.__leader = new_leader
        else:
            raise Exception(f"Occurence {self.__key} is Closed")