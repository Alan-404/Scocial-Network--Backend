class Response:
    def __init__(self, success: bool, message: str) -> None:
        self.success = success
        self.message = message
        """ self.name = name
        self.dictionary = dictionary """

    def to_dict(self) -> dict:
        dictionary = dict()
        for param in self.__dict__.keys():
            dictionary[param] = self.__dict__[param]
        return dictionary

class APIResponse:
    def __init__(self, success: bool = False, message: str = '', object: str = None, data: dict = None) -> None:
        self.success = success
        self.message = message
        self.object = object
        self.data = data

    def to_json(self) -> dict:
        if self.object is not None:
            return {
                'success': self.success,
                'message': self.message,
                self.object: self.data
            }
        else:
            return {
                'success': self.success,
                'message': self.message
            }