from repository.password_repository import PasswordRepository
from services.password_service import PasswordService
from services.report_service import ReportService
from exporters.text_exporter import TextExporter

from config import REPORT_FILE

password = PasswordRepository().load()

result = PasswordService().analyze(

    password

)

ReportService().print(

    result

)

TextExporter().export(

    result,

    REPORT_FILE

)
