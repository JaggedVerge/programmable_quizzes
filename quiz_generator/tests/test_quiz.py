"""
Tests for the Quiz class
"""
from unittest.mock import Mock

from quiz_generator.quiz import Quiz

def test_quiz_creation():
    """Create a Quiz"""
    question1 = Mock()
    example_quiz = Quiz(
        [question1],
        quiz_name="Test quiz",
        quiz_version="Unit test version",
        preamble="Preamble, preamble, more preamble"
    )

    question2 = Mock()
    example_quiz.add_question(question2)

def test_marking_sheet():
    """Test marking sheet correctly made for a Quiz"""
    answer_to_q_1 = "Answer to question1"
    answer_to_q_2 = "Answer to question2"
    question1 = Mock()
    question1.answer_to_latex = answer_to_q_1
    question2 = Mock()
    question2.answer_to_latex = answer_to_q_2

    name = "Mock quiz"
    test_quiz = Quiz(
        questions=[question1, question2],
        quiz_name=name
    )
    marking_sheet = test_quiz.create_marking_sheet()
    assert name in marking_sheet
    assert answer_to_q_1 in marking_sheet
    assert answer_to_q_2 in marking_sheet
