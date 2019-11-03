from uuid import uuid4
import re


def vuid():
    return str(uuid4().hex)


def validate(vuid):
    val = re.compile('[0-9a-f]{8}[0-9a-f]{4}4[0-9a-f]{3}[89ab][0-9a-f]{3}[0-9a-f]{12}', re.I)
    return bool(val.match(vuid))
