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
                self.__medi_idx += 1
                self.__low_idx += 1
                idx = self.__high_idx
            case Occ_Priority.MEDIA:
                self.__medi_idx += 1
                self.__low_idx += 1
                idx = self.__medi_idx
            case Occ_Priority.BAIXA:
                self.__low_idx += 1
                idx = self.__low_idx

        self.__occurences.insert(idx, occurence)

    def leave_occurence(self, occ_key:str, new_leader:str):
        occ_idx = None
        for i, occ in enumerate(self.__occurences):
            if occ_key == occ.get_key():
                occ_idx = i
                break
        if occ_idx is None:
            raise Exception(f"Occurence {occ_key} Not Found")
        occ = self.__occurences.pop(occ_idx)
        occ.change_leader(new_leader)

    def get_occurences(self) -> list[Occurence]:
        return self.__occurences

    def finish_occurence(self, occ_key:str):
        occ_idx = None
        for i, occ in enumerate(self.__occurences):
            if occ_key == occ.get_key():
                occ_idx = i
                break
        if occ_idx is None:
            raise Exception(f"Occurence {occ_key} Not Found")

        self.__occurences[occ_idx].finish_occurence()

    def reset_priority(self, occ_key:str, new_priority:Occ_Priority):
        occ_idx = None
        for i, occ in enumerate(self.__occurences):
            if occ_key == occ.get_key():
                occ_idx = i
                break
        if occ_idx is None:
            raise Exception(f"Occurence {occ_key} Not Found")

        self.__occurences[occ_idx].reset_priority(new_priority)