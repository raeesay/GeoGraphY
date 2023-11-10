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


    def __init__(self):
        print("Welcome to GeoGraphY!")
        self.localData = DataHandler()
        self.qGenerator = Question(self.localData)
        self.difficulty, self.nQuestions = self.getSettings()


    def run(self):

        questions = {"1": ["questionCapitalOfCountry",
                           "questionLeaderNameEasy",
                           "questionNationalAnthem",
                           "questionCurrencyInCountry",
                           "questionPopulationEasy"], # currency, population

                     "2": ["questionCapitalOfCountry",
                           "questionLeaderName",
                           "questionNationalAnthem",
                           "questionCurrencyInCountry",
                           "questionPopulation",
                           "questionAirportCountryLocation"], # easy + location of building/company

                     "3": ["questionCapitalOfCountry",
                           "questionLeaderName",
                           "questionNationalAnthem",
                           "questionCurrencyInCountry",
                           "questionPopulation",
                           "questionAirportCountryLocation",
                           "questionDiallingCodeOfCountry",
                           "questionPersonBorn",
                           "questionRiverCountry",
                           "questionBuildingCountry"] # easy + medium + mouth of river location
                     }

        question_sampling = random.choices(questions[self.difficulty], k=int(self.nQuestions))
        quiz = [getattr(self.qGenerator, question) for question in question_sampling]

        correct_count = 0
        wrong_count = 0
        for question in quiz:
            correct_count, wrong_count = self.questionPrinting(question(), correct_count, wrong_count)
            time.sleep(1)

        print("You are done with the quiz.")
        print(f"You had {correct_count} correct answers and {wrong_count} wrong answers."
              f" Therefore you answered {(correct_count / int(self.nQuestions)) * 100}% correctly.")

        return

    def questionPrinting(self, question, correct_answers, wrong_answers):

        answers = question["wrong answers"]
        correct_index = random.randint(0,3)
        answers.insert(correct_index, question["correct answer"])

        print("")
        print("Question:", question["template"])

        for index, answer in enumerate(answers):
            print(f"{index + 1}. {answer}")

        x = input("Please select your answer: ")

        #check if input is correct for answer selection
        while x not in ["1", "2", "3", "4"]:
            print("Wrong input for answer selection. Please try again and choose a number from 1 to 4!")
            print("")
            print("Question:", question["template"])

            for index, answer in enumerate(answers):
                print(f"{index + 1}. {answer}")

            x = input("Please select your answer: ")



        if x == str(correct_index + 1):
            print("Correct!", question["return"] + "!")
            correct_answers += 1
        else:
            print("Incorrect. Better luck next time!", question["return"] + ".")
            wrong_answers += 1

        return correct_answers, wrong_answers


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
        if not nQuestions.isdigit():
            print("Invalid input for the number of questions. The quiz will default to 10 questions.")
            nQuestions = 10
        elif int(nQuestions) < 1 or int(nQuestions) > 25:
            print("Invalid input for the number of questions. The quiz will default to 10 questions.")
            nQuestions = 10
        else:
            print(f"Perfect! You will be asked {nQuestions} in the following quiz.")

        print("Good luck! :)")

        return difficulty, nQuestions