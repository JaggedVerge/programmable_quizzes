"""
Representation of a question.
"""

class Question:
    """Object that stores a question"""
    def __init__(self, question_template, answer_template, inputs=None, answer_generation_function=None):
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
        if answer_generation_function:
            self.answers = answer_generation_function(inputs)

    def question_to_latex(self):
        """Write out a representation of the question to LaTeX"""
        if self.question_inputs:
            return self.question_template.render(self.question_inputs)
        else:
            return self.question_template 

    def answer_to_latex(self):
        """Write out a representation of the answer to LaTeX"""
        if answer_generation_function:
            retrun self.answer_template.render(self.answers)
        else:
            return self.answer_template

