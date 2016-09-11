"""
Representation of a question.
"""

class Question:
    """Object that stores a question"""
    def __init__(self):
        pass

    def question_to_latex(self):
        """Write out a representation of the question to LaTeX"""
        raise NotImplementedError

    def answer_to_latex(self):
        """Write out a representation of the answer to LaTeX"""
        raise NotImplementedError

