class Question:
    def __init__(self, text, answer, category):
        self.text = text
        self.answer = answer
        self.category = category

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

questions = [
    Question("What is 2 + 2?", "4", "Math"),
    Question("Capital of France?", "Paris", "Geography"),
    Question("Color of the sky?", "Blue", "General"),
    Question("The title of Goat of all time in football?", "pele", "Sports"),
]

name1 = input("Enter name for Player 1: ")
name2 = input("Enter name for Player 2: ")

player1 = Player(name1)
player2 = Player(name2)

for question in questions:
    for player in [player1, player2]:
        print(f"\n{player.name}, Category: {question.category}")
        print("Question:", question.text)
        answer = input("Your answer: ")
        if answer.lower() == question.answer.lower():
            print("Correct!")
            player.score += 1
        else:
            print("Wrong. Correct answer is:", question.answer)

print("\n--- Leaderboard ---")
players = [player1, player2]
players.sort(key=lambda p: p.score, reverse=True)

for i, p in enumerate(players):
    print(f"{i + 1}. {p.name} - {p.score} points")
