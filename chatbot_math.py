from chatterbot import ChatBot

spider = ChatBot("Math", logic_adapters=[
    "chatterbot.logic.MathematicalEvaluation"
])
print("--------------Math Baba------------------")

while True:
    Stranger = input("Type any math equation You want to solve: ")
    print("Spider: ",spider.get_response(Stranger))