questions = [
  "Who created this?",
  "What is the capital city of Pakistan?",
  "When did Pakistan gain independence (Year)?",
  "What is the national flower of Pakistan?",
]
answers = [
  "Hussain",
  "Islamabad",
  "1947",
  "Jasmine",
];


correctAnswers = 0
index = 0
moneyEarn = 0

for question in questions:
  userAnswer = input(question + ' ')

  if (userAnswer.lower() == answers[index].lower()):
    correctAnswers = correctAnswers + 1
    moneyEarn = moneyEarn + 1000
  
  index = index + 1


print("You earned", str(moneyEarn) + "PKR")
  