from occurence import Occurence, Occ_Priority, Occ_Type

class Employee():
    def __init__(self, name:str) -> None:
        self.__name = name
        self.__projects = []
        self.__occurences = []
        self.__high_idx = 0
        self.__medi_idx = 0
        self.__low_idx = 0

    def get_name(self) -> str:
        return self.__name

    def join_project(self, project_name:str):
        self.__projects.append(project_name)

    def get_projects(self):
        return self.__projects

    def add_occurence(self, occurence:Occurence):
        idx = -1
        match occurence.get_priority():
            case Occ_Priority.ALTA:
                self.__high_idx += 1
                idx = self.__high_idx
            case Occ_Priority.MEDIA:
                self.__medi_idx += 1
                idx = self.__medi_idx
            case Occ_Priority.BAIXA:
                self.__low_idx += 1
                idx = self.__low_idx

        self.__occurences.insert(idx, occurence)

    def get_occurences(self) -> list[Occurence]:
        return self.__occurences