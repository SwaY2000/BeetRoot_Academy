class Validate:

    def __init__(self, mail):
        """Check mail: lenght, entry duplicate "@" and double "." """
        if len(mail) > 64:
            raise ValueError("E-mail is not validate")
        print(f"{mail} is validate")
        Validate.__check(mail)
        Validate.__domen(mail)

    @staticmethod
    def __domen(mail):
        """Check domen: lenght, entry duplicate "@" and double "." """
        if str.count(mail, "@") == 1:
            mail_name, mail_domen = str.split(mail, "@")
            if len(mail_domen) > 3 and mail_domen[0] != ".":
                pass
            else:
                raise ValueError("E-mail is not validate")
        else:
            raise ValueError("E-mail is not validate")
        return mail_name

    @staticmethod
    def __check(var):
        """Check entry in list NOT_VALIDATE"""
        NOT_VALIDATE = ["!", "#", "$", "%", "&", "'", "*", "+", "-", "/", "=", "?", "^", "`", "{", "|", "}", "~", "..", ","]
        for check in var:
            if check in NOT_VALIDATE:
                raise ValueError("E-mail is not validate")
        if str.count(var, "..") == 0:
            pass
        else:
            raise ValueError("E-mail is not validate")


print(Validate("dan.frais2000@gmail.com.ua"))