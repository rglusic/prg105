"""
    In this programming exercise, you will create a simple trivia game for two players. The program will work like this:

        Starting with player 1, each player gets a turn at answering 5 trivia questions. (There should be a total of
        10 questions.) When a question is displayed, 4 possible answers are also displayed. Only one of the answers is
        correct, and if the player selects the correct answer, he or she earns a point.

        After answers have been selected for all the questions, the program displays the number of points earned by each
        player and declares the player with the highest number of points the winner.
"""

"""
    Creates an array of Question objects, each with a separate questions. Creates two player instances. Shows the player
    the questions, asking for a value between 1 and 4 for their response. Checks to make sure value is correct. Applies
    points if the player guesses correctly. After all of the questions have been exhausted, a winner is declared. Uses
    a for each loop to iterate over each question. 
"""


def main():
    questions = {Question("State capital of New York", ["Albany", "New York", "Rochester", "Syracuse"],
                          "Albany"),
                 Question("State capital of Illinois", ["Chicago", "Naperville", "Springfield", "Peoria"],
                          "Springfield"),
                 Question("State capital of Wyoming", ["Cheyenne", "Casper", "Buffalo", "Rock Springs"],
                          "Cheyenne"),
                 Question("State capital of Alabama", ["Prattville", "Montgomery", "Greenville", "Troy"],
                          "Montgomery"),
                 Question("State capital of Tennessee", ["Nashville", "Clarksville", "Springfield", "Cottontown"],
                          "Nashville"),
                 Question("State capital of Colorado", ["Fort Collins", "Colorado Springs", "Denver", "Pueblo"],
                          "Denver"),
                 Question("State capital of Kansas", ["Topeka", "Maple Hill", "Perry", "Eskridge"],
                          "Topeka"),
                 Question("State capital of Arkansas", ["Jessieville", "Little Rock", "Redfield", "England"],
                          "Little Rock"),
                 Question("State capital of Florida", ["Tampa", "Orlando", "Miami", "Tallahassee"],
                          "Tallahassee"),
                 Question("State capital of Louisiana", ["New Orleans", "Lafayette", "Lake Charles", "Baton Rouge"],
                          "Baton Rouge")
                 }
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    switch_players = len(questions)/2
    index = 0
    cur_player = player1

    print("---- State Capital Game ----")
    for quest in questions:
        if index == switch_players:
            cur_player = player2

        print(cur_player.get_title() + ": " + quest.get_question())
        print("1) " + quest.get_answers()[0])
        print("2) " + quest.get_answers()[1])
        print("3) " + quest.get_answers()[2])
        print("4) " + quest.get_answers()[3])

        while True:
            try:
                guess = int(input("Please enter your guess (1-4) "))
            except ValueError:
                continue
            if guess in range(1, 5):
                break

        if quest.get_answers()[guess-1] == quest.get_correct_answer():
                cur_player.increment_score()
        index += 1
    print(player1.get_title() + " had a total of " + str(player1.get_score()) + " points and " + player2.get_title() +
          " had a total of " + str(player2.get_score()) + " points.")

    if player1.get_score() > player2.get_score():
        print(player1.get_title() + " wins!")
    elif player1.get_score() == player2.get_score():
        print("It's a tie!")
    else:
        print(player2.get_title() + " wins!")


"""
    Holds a question, 4 answers and the actual answer. Contains getter functions to access them.
"""


class Question:
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct = correct_answer

    def get_answers(self):
        return self.answers

    def get_correct_answer(self):
        return self.correct

    def get_question(self):
        return self.question


"""
    Holds player information such as the title of the player, or the current score. Contains getters to retrieve both.
"""


class Player:
    def __init__(self, title):
        self.score = 0
        self.title = title

    def increment_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def get_title(self):
        return self.title


main()
