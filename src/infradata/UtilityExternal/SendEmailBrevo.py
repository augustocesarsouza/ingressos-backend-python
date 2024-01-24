from src.infradata.UtilityExternal.Interface.ISendEmailBrevo import ISendEmailBrevo
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from src.infradata.Config.JwtConfigFile import jwt_config
from src.application.Services.ResponseWrapper import ResponseWrapper


class SendEmailBrevo(ISendEmailBrevo):

    def send_email(cls, user: dict[str, any], url: str) -> ResponseWrapper:
        key_brevo = jwt_config["API-KEY-BREVO"]
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = str(key_brevo)

        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
            sib_api_v3_sdk.ApiClient(configuration))
        subject = "Seu token de confirmação"
        html_content = f"<h1>Clique no token disponivel: {url}</h1>"
        sender = {"name": "augusto",
                  "email": "augustocesarsantana90@gmail.com"}
        to = [{"email": f"{user['email']}", "name": f"{user['name']}"}]
        cc = [{"email": "example2@example2.com", "name": "Janice Doe"}]
        bcc = [{"name": "John Doe", "email": "example@example.com"}]
        reply_to = {"email": "replyto@domain.com", "name": "John Doe"}
        headers = {"Some-Custom-Name": "unique-id-1234"}
        params = {"parameter": "My param value", "subject": "New Subject"}
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=to, bcc=None, cc=None, reply_to=None, headers=headers, html_content=html_content, sender=sender, subject=subject)

        try:
            api_instance.send_transac_email(send_smtp_email)
            return ResponseWrapper.ok("tudo certo")
        except ApiException as e:
            return ResponseWrapper.fail(f"errro ao enviar {e}")

    def send_code(cls, user: dict[str, any], code_randon: int) -> ResponseWrapper:
        key_brevo = jwt_config["API-KEY-BREVO"]
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = str(key_brevo)

        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
            sib_api_v3_sdk.ApiClient(configuration))
        subject = "SEU NUMERO ALEATORIO DE CONFIRMAÇÃO"
        html_content = f"Seu numero de Confirmação: {str(code_randon)}"
        sender = {"name": "augusto",
                  "email": "augustocesarsantana90@gmail.com"}
        to = [{"email": f"{user['email']}", "name": f"{user['name']}"}]
        cc = [{"email": "example2@example2.com", "name": "Janice Doe"}]
        bcc = [{"name": "John Doe", "email": "example@example.com"}]
        reply_to = {"email": "replyto@domain.com", "name": "John Doe"}
        headers = {"Some-Custom-Name": "unique-id-1234"}
        params = {"parameter": "My param value", "subject": "New Subject"}
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=to, bcc=None, cc=None, reply_to=None, headers=headers, html_content=html_content, sender=sender, subject=subject)

        try:
            api_instance.send_transac_email(send_smtp_email)
            return ResponseWrapper.ok("tudo certo")
        except ApiException as e:
            return ResponseWrapper.fail(f"errro ao enviar {e}")
