class StringUtils:

    @staticmethod
    def has_upper(text):

        return any(c.isupper() for c in text)

    @staticmethod
    def has_lower(text):

        return any(c.islower() for c in text)

    @staticmethod
    def has_digits(text):

        return any(c.isdigit() for c in text)

    @staticmethod
    def has_symbols(text):

        return any(

            not c.isalnum()

            for c in text

        )
