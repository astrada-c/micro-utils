from enum import Enum

import json

class StatusEnum(Enum):
    FAILED = 'failed'
    SUCCESS = 'success'


class InvalidResponse(Exception):
    """ Raise when the response model is missing params """


class ResponseModel:
    def __init__(self, **kwargs):
        self.status = kwargs.get('status', None)
        self.error = kwargs.get('error', None)
        self.message = kwargs.get('message', None)
        self.data = kwargs.get('data', None)

    def json(self):
        self.validate_params()
        return json.dumps(dict([(k, v) for k, v in self.__dict__.items() if v != None]))

    def validate_params(self):
        if self.status not in [i.value for i in StatusEnum]:
            raise InvalidResponse('Status provided is not valid')
        if not self.status:
            raise InvalidResponse("Invalid or missing status")
        elif (self.error) and (not self.message):
            raise InvalidResponse('Message is missing')
        else:
            pass
        # elif (self.status == StatusEnum.SUCCESS.value) and (not self.data):
        #     raise InvalidResponse('Data field is missing')


if __name__ == '__main__':
    response = ResponseModel()
    response.status = 'failed'
    response.error = True
    response.message = 'something went wong'
    print(response.json())
