from enum import Enum


class RequestType(Enum):
    INSTRUMENT = 'I'
    PRODUCT = 'P'


rt = RequestType
t = RequestType.PRODUCT


