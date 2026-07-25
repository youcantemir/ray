from data.common_passwords import COMMON_PASSWORDS

class DictionaryService:

    def contains(

        self,

        password

    ):

        return password.lower() in COMMON_PASSWORDS
