class ResponseWrapper:
    def __init__(self, is_success, data) -> None:
        self.IsSuccess = is_success
        self.Data = data

    @classmethod
    def fail(cls, message):
        return ResponseWrapper(False, {"message": message})

    @classmethod
    def ok(cls, data):
        return ResponseWrapper(True, data)
