"""
Representation of a question.
"""

class Question:
    """Object that stores a question"""
    def __init__(self, question_template, answer_template, answer_generation_function=None):
        """
        :question_template: a template for the question
        :answer_template: a tempalte for the answer
        :answer_generation_function: a function that takes the variables found in the
                                     question template and generates a dictionary of answer
                                     keys with values for use in the answer_template
        """
        self.question_template = question_template
        self.answer_template = answer_template

    def question_to_latex(self):
        """Write out a representation of the question to LaTeX"""
        raise NotImplementedError

    def answer_to_latex(self):
        """Write out a representation of the answer to LaTeX"""
        raise NotImplementedError

