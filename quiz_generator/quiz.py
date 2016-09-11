"""
Representation of a quiz
"""

default_quiz_template = """
{{ quiz_name }} (version: {{ quiz_version }})
{{ preamble }}

{% for question in questions %}
    Question #{{ loop.index }}:
    {{ question.question_to_latex }}
{% endfor %}
"""

class Quiz:
    """Represents a Quiz"""

    def __init__(self, questions, quiz_name="", quiz_version="",
                 preamble=None, template=default_quiz_template):
        """
        :questions: A collection of questions that comprises this quiz
        :quiz_name: The name of this quiz
        :quiz_version: The version of the quiz
        :preamble: Text to appear before quiz any questions
        """
        self.questions = questions
        self.quiz_name = quiz_name
        self.quiz_version = quiz_version
        self.preamble = preamble

    def add_question(self, question):
        """Add a question to the Quiz"""
        raise NotImplementedError

    def create_marking_sheet(self):
        """Create a marking sheet for this quiz"""
        raise NotImplementedError

    def quiz_to_latex(self):
        """Output the quiz in a LaTeX format"""
        raise NotImplementedError
