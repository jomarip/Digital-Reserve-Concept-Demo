"""
Financial quiz containing elementary multiplication exercies.
"""

import random
from random import randint
import math

import jinja2

from quiz_generator.ranged_question import RangedQuestion
from quiz_generator.input_variation import Variation
from quiz_generator.quiz import Quiz

# Financial Literacy Questions


inputs = {"x": randint(1,12),"y": randint(1,12),"z": randint(1,5)}  #random.sample(range(X),Y) creates a list of Y randomly selected values from a list of 0-X



def multiplication_answer_function(inputs):
	if inputs['x']==inputs['y']:
		return {"answer": "same"}
	elif inputs['x']>inputs['y']:
		return {"answer": "more"}
	else:
		return {"answer": "less"}
		
financial_questions = RangedQuestion(

    question_template=jinja2.Template("Imagine that the interest rate on a savings account is {{x}} percent a year and inflation is {{y}} percent a year. After {{z}} year(s), would the money in the account buy more than it does today, exactly the same or less than today?"),
    answer_template=jinja2.Template("{{answer}}"),
    inputs= inputs,
    answer_generation_function=multiplication_answer_function
)

quiz_version1 = Quiz(
    questions=financial_questions.create_all_questions(),
    quiz_name="Financial Comprehension Quiz",
    quiz_version="1",
    preamble="Questions to improve financial educational and literacy. ",
)

print(quiz_version1.render())
print(quiz_version1.create_marking_sheet())
