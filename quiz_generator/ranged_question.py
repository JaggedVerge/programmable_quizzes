"""
Representation of a question with a range of input values
"""
from .question import Question
from .input_variation import Variation

def extract_input_combination(inputs_mapping):
    """Extract a random input choice from the given dictionary of possible inputs.
    For each key this will chose an element from a Variation otherwise it and will
    choose the value directly.
    Example usage:

    >>> extract_random_input_combination({1: ['a', 'b'], 2: ['c']})
    {1: ['a', 'b'], 2: 'c'}
    >>> extract_random_input_combination({1: Variation(['a', 'b']), 2: ['c']})
    {1: 'b', 2: 'c'}
    >>> extract_random_input_combination({1: 'Example string', 2: ['c']})
    {1: 'not a collection', 2: 'c'}

    """
    results = {}
    for key, value in inputs_mapping.items():
        if isinstance(value, Variation):
            results[key] = next(value.get())
        else:
            results[key] = value
    return results


class RangedQuestion:
    """Helper class for generating questions"""
    def __init__(self, question_template, answer_template,
                 inputs, answer_generation_function=None):
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
        self.answer_generation_function = answer_generation_function

    def create_specific_question(self):
        """
        Create a specific singular instance of this Question by choosing a value
        from the inputs
        """
        # If no inputs then we have only one choice possible which is as follows:
        if self.question_inputs is None:
            return Question(
                question_template=self.question_template,
                answer_template=self.answer_template,
                inputs=None,
                answer_generation_function=self.answer_generation_function
            )

        specific_input = extract_input_combination(self.question_inputs)
        return Question(
            question_template=self.question_template,
            answer_template=self.answer_template,
            inputs=specific_input,
            answer_generation_function=self.answer_generation_function
        )

    def create_all_questions(self):
        """
        Create all possible questions from the input combinations
        """
        raise NotImplementedError
