class Token:
    def __init__(self):
        self.kind = "number"
        self.value = 0
        self.spec_chars = ['+', '-', '*', '/', '(', ')', ';', 'q']

    def get_token(self):
        self.token = input("Expression : ")
        if self.token.isdigit():
            self.kind = "number"
            self.value = self.token
            return self
        elif self.token in self.spec_chars:
            self.kind = self.token
            self.value = None
            return self
        else:
            return None

    def calculate(self):
        if self.kind is None:
            