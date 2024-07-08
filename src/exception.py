class CustomException(Exception):
    def __init__(self, message, error):
        super().__init__(message)
        self.error = error

    def __str__(self):
        return f"{self.message}: {self.error}"