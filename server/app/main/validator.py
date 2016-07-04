import re


class Validator():

    def validate_tag(self, tag):
        if re.match(r"^[A-z0-9_\-\s]{1,25}$", tag):
            return ""
        else:
            return "Not a valid tag. A-z, 0-9, (_), and (-) characters only. 1 to 25 characters"

    def validate_ip(self, ip):
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
            return ""
        else:
            return "Not a valid IP"

    def validate_port(self, port):
        if re.match(r"^\d{1,5}$", port):
            return ""
        else:
            return "Not a valid port"
