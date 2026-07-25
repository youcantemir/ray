from models.result import PasswordResult

from utils.entropy import calculate

from services.dictionary_service import DictionaryService
from services.strength_service import StrengthService

class PasswordService:

    def analyze(

        self,

        password

    ):

        strength = StrengthService()

        score = strength.score(password)

        return PasswordResult(

            password=password,

            score=score,

            level=strength.level(score),

            entropy=calculate(password),

            dictionary_match=DictionaryService().contains(password)

        )
