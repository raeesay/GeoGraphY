# will be called by main and run the actual code
from utils.questions import Question
from utils.dataHandling import DataHandler

class Executer:
    # can be thought of as quiz generator

    # shuffles questions
    # handles difficulty of questions
    # keep track of correctly answered questions (and scores)
    # takes in settings from the user (such as difficulty or the amount of questions) (optional)

    # should consider writing one function which handles all the printing for a question
    #  --> makes code more structured because for each question we only have to call one or two functions


    def __init__(self):
        print("Welcome to GeoGraphY!")
        self.localData = DataHandler()
        self.qGenerator = Question(self.localData)


    def runQuiz(self):
        q1 = self.qGenerator.questionCapitalOfCountry()


        print("Question:", q1["template"])

        print("1. {correct}".format(correct=q1["correct answer"]))

        x = input("Please choose the correct option: ")

        if x == "1":
            print(f"Correct!", q1["return"], "!")
        else:
            print(f"Try again!", q1["return"], ".")
        return self