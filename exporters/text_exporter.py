class TextExporter:

    def export(

        self,

        result,

        filename

    ):

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                f"Password: {result.password}\n"

            )

            file.write(

                f"Strength: {result.level}\n"

            )

            file.write(

                f"Entropy: {result.entropy}\n"

            )

            file.write(

                f"Dictionary Match: {result.dictionary_match}\n"

            )
