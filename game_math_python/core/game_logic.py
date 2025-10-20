import random

class GameLogic:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.current_question = None
        self.current_answer = None

    def generate_question(self):
        """Genera una multiplicación aleatoria y guarda la respuesta"""
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        self.current_question = f"{a} x {b}"
        self.current_answer = a * b
        return self.current_question

    def check_answer(self, answer):
        """Verifica si la respuesta ingresada es correcta"""
        if answer == self.current_answer:
            self.score += 1
            self.level = 1 + self.score // 5  # sube nivel cada 5 aciertos
            return True
        return False
