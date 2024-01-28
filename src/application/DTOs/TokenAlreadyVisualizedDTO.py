class TokenAlreadyVisualizedDTO:
    def __init__(self, TokenAlreadyVisualized: bool, ErroMessage: str) -> None:
        self.TokenAlreadyVisualized = TokenAlreadyVisualized
        self.ErroMessage = ErroMessage

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }
