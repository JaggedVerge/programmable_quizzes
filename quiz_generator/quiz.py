"""
Representation of a quiz
"""

class Quiz:
    """Represents a Quiz"""

    def __init__(self, questions, preamble=None):
        """
        :questions: A collection of questions that comprises this quiz
        :preamble: Text to appear before quiz any questions.
        """
        self.questions = questions

    def add_question(self, question):
        """Add a question to the Quiz"""
        raise NotImplementedError

    def create_marking_sheet(self):
        """Create a marking sheet for this quiz"""
        raise NotImplementedError

    def quiz_to_latex(self);
        """Output the quiz in a LaTeX format"""
        raise NotImplementedError
