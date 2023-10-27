# will be called by main and run the actual code
from utils.questions import Question
from utils.dataHandling import DataHandler

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


    def run(self):
        q1 = self.qGenerator.questionCapitalOfCountry()
        self.questionPrinting(q1)

        return

    def questionPrinting(self, question):
        print("Question:", question["template"])

        print("1. {correct}".format(correct=question["correct answer"]))
        x = input("Please choose the correct option: ")
        if x == "1":
            print("Correct!", question["return"] + "!")
        else:
            print("Try again!", question["return"] + ".")