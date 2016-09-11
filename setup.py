from setuptools import setup
import os

setup(name='randomized_quiz_generator',
      version='0.1.0',
      description='Generates randomized quizzes from templates along with generated marking sheets',
      url='https://github.com/shuttle1987/latex_quiz_generator',
      packages=['quiz_generator'],
      classifiers = [
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Education',
          'Programming Language :: Python',
      ],
      keywords='',
      install_requires=['jinja2'],
)

