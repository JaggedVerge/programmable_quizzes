"""
Tests for question class
"""
from quiz_generator.question import Question

def test_question_with_no_substitution():
    """Test that a question with no function to substitute values works as expected"""
    simple_question = Question("1+1 = ?", "2")
    assert simple_question.question_to_latex() == "1+1 = ?"
    assert simple_question.answer_to_latex() == "2"
