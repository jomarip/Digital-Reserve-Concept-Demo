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
	
	return {"answer": "More than $" + str(inputs['x']+inputs['y']*inputs['x']) + "."}
		
financial_questions = RangedQuestion(
	
    question_template=jinja2.Template("Suppose you have {{x}} in Savings Account earning {{y}} % interest in a year. After {{z}} years, how much would you have?"),
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
