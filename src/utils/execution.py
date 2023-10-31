# will be called by main and run the actual code
from utils.questions import Question
from utils.dataHandling import DataHandler
import random

class Quiz:
    # can be thought of as quiz generator

    # shuffles questions
    # handles difficulty of questions
    # keep track of correctly answered questions (and scores)
    # takes in settings from the user (such as difficulty or the amount of questions) (optional)

    # should consider writing one function which handles all the printing for a question
    #  --> makes code more structured because for each question we only have to call one or two functions
    # TODO: insert suffling beween answer options in questionPrinting()


    def __init__(self):
        print("Welcome to GeoGraphY!")
        self.localData = DataHandler()
        self.qGenerator = Question(self.localData)
        self.difficulty, self.nQuestions = self.getSettings()


    def run(self):
        '''
        q1 = self.qGenerator.questionCapitalOfCountry()
        self.questionPrinting(q1)

        q2 = self.qGenerator.questionDiallingCodeOfCountry()
        self.questionPrinting(q2)
        '''

        q3 = self.qGenerator.questionAirportCountryLocation()
        self.questionPrinting(q3)

        return

    def questionPrinting(self, question):
        print("Question:", question["template"])

        answers = question["wrong answers"]
        correct_index = random.randint(0,3)
        answers.insert(correct_index, question["correct answer"])


        for index, answer in enumerate(answers):
            print(f"{index + 1}. {answer}")

        x = input("Please choose the correct option: ")
        if x == str(correct_index + 1):
            print("Correct!", question["return"] + "!")
        else:
            print("Try again!", question["return"] + ".")



    def getSettings(self):
        print("Available Difficulty-Levels for this Quiz:")
        print("1: Easy")
        print("2: Medium")
        print("3: Advanced")
        difficulty = input("How difficult shall the questions be?")
        if difficulty not in ["1", "2", "3"]:
            print("Wrong input for 'difficulty'. The quiz will have the difficulty 'Easy' as default value.")
            difficulty = 1

        nQuestions = input("Please choose the number of questions you want to be asked. The number shall be between 1 and 25.")
        if int(nQuestions) < 1 or int(nQuestions) > 25:
            print("Wrong input for the number of Questions. The quiz will have 10 questions as default value.")
            nQuestions = 10