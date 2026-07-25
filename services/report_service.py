class ReportService:

    def print(

        self,

        result

    ):

        print()

        print("Password Report\n")

        print(

            f"Password: {result.password}"

        )

        print(

            f"Strength: {result.level}"

        )

        print(

            f"Score: {result.score}/5"

        )

        print(

            f"Entropy: {result.entropy} bits"

        )

        print(

            f"Dictionary Password: {result.dictionary_match}"

        )
