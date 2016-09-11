"""
Tests for ranged questions
"""
from unittest.mock import Mock

from quiz_generator.ranged_question import RangedQuestion
from quiz_generator.question import Question

def test_question_generation_no_inputs():
    """Test that a specific question can be generated from the RangedQuestion"""
    # The specific case where the question inputs are not iterable or form a
    # collection in any way should only ever produce one Question
    r_question = RangedQuestion(
        question_template="mock_question_template",
        answer_template="mock_answer_template",
        inputs=None,
    )

    generated_question = r_question.create_specific_question()
    assert isinstance(generated_question, Question)

def test_question_generation():
    """Test that a specific question can be generated from the RangedQuestion"""
    import jinja2
    inputs = {"x": [1, 2]}
    def answer_function(input_values):
        """
        Simple function that squares a number. The input
        values dictionary stores this under the key for 'x'
        Note the return value is a dictionary because this is required for rendering
        the answer.
        """
        ans = input_values['x']^2
        return {"answer": ans}

    q_template = jinja2.Template("What is {{x}}^2 ?")
    a_template = jinja2.Template("{{answer}}")
    question_with_function_over_range = RangedQuestion(
        question_template=q_template,
        answer_template=a_template,
        inputs=inputs,
        answer_generation_function=answer_function
    )

    generated_question = question_with_function_over_range.create_specific_question()
    assert generated_question.question_to_latex() in ("What is 1^2 ?", "What is 2^2 ?")
    assert generated_question.answer_to_latex() in ("1", "4")
