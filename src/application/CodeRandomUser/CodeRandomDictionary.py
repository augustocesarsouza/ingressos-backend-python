from typing import Dict


class CodeRandomDictionary:
    def __init__(self) -> None:
        self.DictionaryCode: Dict[str, int] = {}

    def add(self, id_guid: str, value_code: int):
        if id_guid not in self.DictionaryCode:
            self.DictionaryCode[id_guid] = value_code
        else:
            self.DictionaryCode[id_guid] = value_code

        print(self.DictionaryCode)

    def container(self, guid_id: str, value_code: int) -> bool:
        if guid_id in self.DictionaryCode:
            value = self.DictionaryCode[guid_id]
            print(value)
            print(value_code)

            if int(value) == int(value_code):
                print(self.DictionaryCode)
                print("True")
                return True
        print("False")
        return False

    def remove(self, id_guid: str):
        if id_guid in self.DictionaryCode:
            del self.DictionaryCode[id_guid]


code_random_dictionary_instance = CodeRandomDictionary()
