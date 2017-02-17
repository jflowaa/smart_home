import re


class Validator:

    @staticmethod
    def validate_tag(tag):
        if re.match(r"^[A-z0-9][A-z0-9_\-\s]{1,24}$", tag):
            return ""
        else:
            return "Not a valid tag. A-z, 0-9, (_), (-) and space characters only.\
             1 to 25 characters.\
             Must start with A-z or 0-9."

    @staticmethod
    def validate_ip(ip):
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
            return ""
        else:
            return "Not a valid IP"

    @staticmethod
    def validate_port(port):
        if re.match(r"^\d{1,5}$", port):
            return ""
        else:
            return "Not a valid port"
