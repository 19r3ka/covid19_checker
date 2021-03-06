from prompts import prompts
from helpers import clear_console
from question import Question, ask
from datetime import datetime

def main():
    clear_console()
    print("Bienvenue sur l'outil d'autodiagnostic du COVID-19")
    print("Disclaimer: Ceci n'est pas un substitut à un avis médical professionnel")
    print("=" * 80)
    input("\nAppuyer sur Entrée pour commencer le test")
    clear_console()

    answers = {}

    for label, prompt in prompts.items():
        answers[label] = ask(Question(prompt=prompt, label=label, answers=("Non", "Oui")))
        clear_console()

    # Returns True if user responds "Yes" to at least one question
    if any(answers.values()):
        print("Il se pourrait que vous représentiez un risque de santé. Mettez-vous en confinement.")
        print("Un agent de santé prendra attache avec vous pour des analyses plus approfondies.")
        input("\nAppuyer sur Entrée pour continuer.")
    else:
        print("Merci d'avoir complèté le test. Vous ne présentez aucun symptôme!")
        print("La prudence reste de mise. Continuez à suivre les consignes sanitaires.\n")

    # Record the completion datetime as UNIX timestamp
    answers["timestamp"] = datetime.timestamp(datetime.now())
    answers["uid"] = "USER PHONE NUMBER"

    print("Informations enrégistrées dans la base de données pour analyse: \n{}".format(answers))

if __name__ == "__main__":
    main()

