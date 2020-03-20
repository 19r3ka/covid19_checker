from collections import namedtuple
from helpers import clear_console

# Named tuples work as immutable dictionnaries
Question = namedtuple("Question", "label prompt answers")

def ask(question):
    """ Administer a question """
    prompt = format_prompt(question)
    answer = None

    while True:
        try:
            answer = int(input(prompt + "> "))
            if answer > 0 and answer <= len(question.answers):
                break
            else:
                raise ValueError("Value out of range.")
        except ValueError:
            input("Réponse invalide. Appuyer sur Entrez pour rééssayer.")
            clear_console()

    return answer - 1


def format_prompt(question):
    """ Format a question """
    prompt = question.prompt + "\n"
    
    for i, a in enumerate(question.answers):
        prompt += "\t{}. {}\n".format(i + 1, a)
    
    return prompt