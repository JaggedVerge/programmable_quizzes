"""
This is an example of generating a question with no function
"""
from quiz_generator import question

simple_question = question.Question(
    question_template = "What is 1+1 equal to?",
    answer_template = "2"
)

output = """Question:
{}
Answer:
{}
""".format(simple_question.question_to_latex, simple_question.answer_to_latex)
