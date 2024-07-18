class Question:
    def __init__(self, text, options, correct):
        self.text = text
        self.options = options
        self.correct = correct

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0