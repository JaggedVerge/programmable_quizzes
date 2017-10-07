[![Build Status](https://travis-ci.org/JaggedVerge/programmable_quizzes.svg?branch=master)](https://travis-ci.org/JaggedVerge/programmable_quizzes)
[![Coverage Status](https://coveralls.io/repos/github/JaggedVerge/programmable_quizzes/badge.svg?branch=master)](https://coveralls.io/github/JaggedVerge/programmable_quizzes?branch=master)

# Programmable quiz generator
This package exists to make it easier to program quizzes and to generate assessment materials.

When creating questions to test someones knowledge you have to find the structure of the question and then you have to create an instance of that question.
What this package provides is the means to programatically address the structural nature of the questions.
This is provided by data structures that represent questions and quizzes along with code that will take the structure you have defined to generate instances of your quizzes and questions along with marking sheets.

## A motivating example
For example if you are trying to make questions to test if someone knows how to multiply things by 3 you have various structures that could test this.
For example you could have questions of the form `3*x = ?` where x is some other number.
For example if we wished to create a question instance `3*5=?` we could do it as follows:

```python
three_times_five_question = Question(
    question_template=jinja2.Template("3 \\times 5 = ?"),
    answer_template=jinja2.Template("15"),
    inputs=None,
    answer_generation_function=None
)
```
As you can see creating a specific instance of the question doesn't benefit much from using these classes.
This will automate some template processing that places the questions into a quiz and a marking sheet but this would otherwise be a fairly straightforward task.

However we can do a lot more when we use the functionality that deals with specifying inputs and answer generation.
This gives us power to completely program the contents of our quiz questions.
Say for example we wanted to generate 5 random questions that use this structure:


```python
inputs = {"x": Variation(random.sample(range(15), 5))}

def multiplication_answer_function(input_values):
    return {"answer": 3 * input_values['x']}

three_times_questions = RangedQuestion(
    question_template=jinja2.Template("3 \\times {{x}} = ?"),
    answer_template=jinja2.Template("{{answer}}"),
    inputs=inputs,
    answer_generation_function=multiplication_answer_function
)
```
Now we are generating *multiple* distinct questions that meet this structure.
The question text is generated along with the answer text that will answer this question.

If a large amount of your work is just dealing with creating instances of questions this package gives you tools to automate that part of the process.
This is especially apparent when creating mathematical quiz material where you are making small changes to the numbers across versions is a tedious task.
This is also especially apparent when creating quizzes that are effectively identical except for minor details.


See the `/examples` directory for more examples of how this library can be used.

## Contributing
Contributions are welcome! Please take a moment to read our contribution guide which can be found in CONTRIBUTING.md
