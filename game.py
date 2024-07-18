import random
import json

def load_questions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [Question(q['question'], q['answers'], q['correct_answer']) 
                for q in json.load(file)['questions']]

def get_players():
    count = int(input("Number of players: "))
    return [Player(input(f"Player {i+1} name: ")) for i in range(count)]

def ask_question(player, question):
    print(f"\n{player.name}, your question is: {question.text}")
    options = list(question.options.items())
    random.shuffle(options)
    for i, (key, value) in enumerate(options, 1):
        print(f"{i}. {value}")
    while True:
        try:
            answer = int(input("Your answer (number): "))
            if 1 <= answer <= len(options):
                break
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")
    return options[answer - 1][1] == question.correct

def play_game(questions, players):
    random.shuffle(questions)
    for question in questions:
        for player in players:
            if ask_question(player, question):
                player.score += 1
                print("Correct!")
            else:
                print(f"Wrong. The correct answer was: {question.correct}")

def main():
    questions = load_questions("trivia_questions.json")
    players = get_players()
    play_game(questions, players)
    winner = max(players, key=lambda p: p.score)
    print(f"\nWinner: {winner.name} with {winner.score} points!")

if __name__ == "__main__":
    main()
