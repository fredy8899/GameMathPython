from game_math_python.core.game_logic import GameLogic

def main():
    game = GameLogic()
    print("Welcome to GameMathPython!\n")

    while True:
        question = game.generate_question()
        print(f"Solve: {question}")
        user_input = input("Your answer: ")

        try:
            user_answer = int(user_input)
        except ValueError:
            print("Please enter a valid number!")
            continue

        if game.check_answer(user_answer):
            print(f"Correct! Score: {game.score}, Level: {game.level}\n")
        else:
            print(f"Wrong! The correct answer was {game.current_answer}. Score: {game.score}\n")

if __name__ == "__main__":
    main()
