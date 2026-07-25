from utils.validators import *

class StrengthService:

    def score(

        self,

        password

    ):

        score = 0

        if len(password) >= 8:
            score += 1

        if has_upper(password):
            score += 1

        if has_lower(password):
            score += 1

        if has_digit(password):
            score += 1

        if has_symbol(password):
            score += 1

        return score

    def level(

        self,

        score

    ):

        if score <= 2:
            return "Weak"

        if score == 3:
            return "Medium"

        return "Strong"
