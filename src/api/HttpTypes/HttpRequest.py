class HttpRequest:
    def __init__(self, headers=None, body=None, query_params=None, path_params=None,
                 url=None, ipv4=None) -> None:
        self.header = headers
        self.body = body
        self.query_params = query_params
        self.path_params = path_params
        self.url = url
        self.ipv4 = ipv4

    def to_dict(self):
        return {
            key: value for key, value in vars(self).items() if value is not None
        }
