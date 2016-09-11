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
