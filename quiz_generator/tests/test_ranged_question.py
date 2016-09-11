"""
Tests for ranged questions
"""
from unittest.mock import Mock

from quiz_generator.ranged_question import RangedQuestion
from quiz_generator.question import Question

def test_question_generation():
    """Test that a specific question can be generated from the RangedQuestion"""
    # The specific case where the question inputs are not iterable or form a
    # collection in any way should only ever produce one Question
    r_question = RangedQuestion(
        question_template="mock_question_template",
        answer_template="mock_answer_template",
        inputs=None,
    )

    generated_question = r_question.create_question()
    assert isinstance(generated_question, Question)
