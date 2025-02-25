print("***********************\nWelcome to my quiz game\n***********************\n")
question_bank=[
    {"question":"Which is the highest waterfalls of the world?","answer":"B"},
    {"question":"Which country is the richest(according to gdp per capita)?","answer":"D"},
    {"question":"Which desert is the driest of all?","answer":"C"},
    {"question":"Which country has no river?","answer":"A"},
    {"question":"World's second largest fort is situated in India.Do you know?","answer":"C"},
    {"question":"Kohinoor was found in which state?","answer":"B"},
    {"question":"Which is the largest island of the world?","answer":"A"},
    {"question":"Most populated city in the world","answer":"D"},
    {"question":"Santa-Clauss lives in which country?","answer":"C"},
    {"question":"Who is the richest emperor of all time?","answer":"D"}
]
options=[
         ["A) Niagra","B) Salto-Angel","C) Iguazu","D) Victoria"],
         ["A) Saudi Arabia","B) San Marino","C) Switzerland","D) Luxemberg"],
         ["A) Thor","B) Sahara","C) Atacama","D)Kalahari"],
         ["A) Saudi Arabia","B) Indonesia","C) Sweden","D) Sudan"],
         ["A) Red Fort","B) Agra Fort","C) Kumbhalgarh Fort","D) Gwalior Fort"],
         ["A) Karnataka","B) Andhra Pradesh","C) Assam","D) Jharkhand"],
         ["A) Greenland","B) Sundarban","C) New Guinea","D) Madagascar"],
         ["A) Shanghai","B) Mumbai","C) New York","D) Tokyo"],
         ["A) Iceland","B) Greenland","C) Finland","D) Norway"],
         ["A) Alexander","B) Chengiz Khan","C) Nepoleon","D) Mansa Musa"]
]
score=0
for question_num in range(len(question_bank)):
    print(question_bank[question_num]["question"])
    for option in options[question_num]:
        print(option)
    guess = input("\nEnter your answer (A/B/C/D): ").upper()
    correct = (guess == question_bank[question_num]["answer"])
    if correct:
        print("Correct answer")
        score += 1
    else:
        print("Incorrect answer")
        print(f"The correct answer is {question_bank[question_num]['answer']}")
    print(f"Your current score is {score}/{question_num + 1}\n")

print(f"\nYou have answered {score} questions correctly out of {len(question_bank)}")
print(f"Your final score is: {(score / len(question_bank)) * 100}%")