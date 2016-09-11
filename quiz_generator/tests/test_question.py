"""
Tests for question class
"""
from quiz_generator.question import Question

def test_question_with_no_substitution():
    """Test that a question with no function to substitute values works as expected"""
    simple_question = Question("1+1 = ?", "2")
    assert simple_question.question_to_latex() == "1+1 = ?"
    assert simple_question.answer_to_latex() == "2"

def test_question_with_template():
    """Test that a question with a templated input works as expected"""
    import jinja2
    input_name = { "name": "bob" }
    q_template = jinja2.Template("Hi I'm {{ name }}!")
    a_template = jinja2.Template("This wasn't really a question, so there's no answer")
    question_with_template = Question(
        question_template=q_template,
        answer_template=a_template,
        inputs=input_name
    )
    assert question_with_template.question_to_latex() == "Hi I'm bob!"
    assert question_with_template.answer_to_latex() == "This wasn't really a question, so there's no answer"
