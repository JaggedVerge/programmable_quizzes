"""
Representation of a question with a range of input values
"""
from .question import Question

class RangedQuestion:
    """Helper class for generating questions"""
    def __init__(self, question_template, answer_template,
                 inputs, answer_generation_function=None):
        """
        :question_template: a template for the question
        :answer_template: a template for the answer
        :inputs: a dictionary of substitutions to make in the templates
        :answer_generation_function: a function that takes the variables found in the
                                     question template and returns a dictionary of answer
                                     keys with values for use in the answer_template
        """
        self.question_template = question_template
        self.answer_template = answer_template
        self.question_inputs = inputs
        self.answer_generation_function = answer_generation_function

    def create_question(self):
        """
        Create a specific instance of this Question by choosing a value
        from the inputs
        """
        return Question(
            question_template=self.question_template,
            answer_template=self.answer_template,
            inputs=self.question_inputs,
            answer_generation_function=self.answer_generation_function
        )
