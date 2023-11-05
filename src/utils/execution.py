# will be called by main and run the actual code
import time

from utils.questions import Question
from utils.dataHandling import DataHandler
import random

class Quiz:
    # can be thought of as quiz generator

    # shuffles questions
    # handles difficulty of questions
    # keep track of correctly answered questions (and scores) (optional)
    # takes in settings from the user (such as difficulty or the amount of questions)

    # TODO: take setting inputs as parameters to adjust the quiz


    def __init__(self):
        print("Welcome to GeoGraphY!")
        self.localData = DataHandler()
        self.qGenerator = Question(self.localData)
        self.difficulty, self.nQuestions = self.getSettings()


    def run(self):

        questions = {"1": ["questionCapitalOfCountry",
                           "questionLeaderNameEasy",
                           "questionNationalAnthem"], # currency, population

                     "2": ["questionCapitalOfCountry",
                           "questionLeaderName",
                           "questionNationalAnthem",
                           "questionAirportCountryLocation"], # easy + location of building/company

                     "3": ["questionCapitalOfCountry",
                           "questionLeaderName",
                           "questionNationalAnthem",
                           "questionAirportCountryLocation",
                           "questionDiallingCodeOfCountry",
                           "questionPersonBorn"] # easy + medium + mouth of river location
                     }

        question_sampling = random.choices(questions[self.difficulty], k=int(self.nQuestions))
        quiz = [getattr(self.qGenerator, question) for question in question_sampling]

        for question in quiz:
            self.questionPrinting(question())
            time.sleep(1)

        #q6 = self.qGenerator.questionLeaderName()
        #self.questionPrinting(q6)

        return

    def questionPrinting(self, question):
        print("")
        print("Question:", question["template"])

        answers = question["wrong answers"]
        correct_index = random.randint(0,3)
        answers.insert(correct_index, question["correct answer"])

        for index, answer in enumerate(answers):
            print(f"{index + 1}. {answer}")

        x = input("Please select your answer: ")
        if x == str(correct_index + 1):
            print("Correct!", question["return"] + "!")
        else:
            print("Incorrect. Better luck next time!", question["return"] + ".")



    def getSettings(self):
        print("Available difficulty levels for this quiz:")
        print("1: Easy")
        print("2: Medium")
        print("3: Advanced")
        difficulty = input("How difficult should the questions be? Please choose a number from 1 to 3: ")
        if difficulty not in ["1", "2", "3"]:
            print("Invalid input for 'difficulty'. The quiz will default to difficulty 'Easy'.")
            difficulty = "1"
        elif difficulty == "1":
            print("The quiz will have the difficulty 'Easy'.")
        elif difficulty == "2":
            print("The quiz will have the difficulty 'Medium'.")
        else:
            print("The quiz will have the difficulty 'Advanced'.")

        nQuestions = input("Please choose the number of questions you want to be asked. Please choose a number from 1 to 25: ")
        if int(nQuestions) < 1 or int(nQuestions) > 25:
            print("Invalid input for the number of questions. The quiz will default to 10 questions.")
            nQuestions = 10
        else:
            print(f"Perfect! You will be asked {nQuestions} in the following quiz.")

        print("Good luck! :)")

        return difficulty, nQuestions