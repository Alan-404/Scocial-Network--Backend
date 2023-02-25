class Response:
    def __init__(self, success: bool, message: str) -> None:
        self.success = success
        self.message = message

    def to_dict(self) -> dict:
        dictionary = dict()
        for param in self.__dict__:
            dictionary[param] = self.__dict__[param]
        return dictionary
    