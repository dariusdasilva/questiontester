"""CLI flashcard quiz application."""

from flashcard_manager import FlashcardManager
from quiz_manager import QuizSession


def run_quiz():
    """Main CLI quiz application."""
    
    # Load flashcards
    manager = FlashcardManager()
    
    try:
        filename = input("What would you like to revise?: ").strip()
        manager.load_from_file(filename)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    if manager.count() == 0:
        print("No flashcards found!")
        return
    
    print(f"\nLet's begin. ({manager.count()} questions)\n")
    
    # Run initial quiz
    session = QuizSession(manager.get_flashcards())
    session.shuffle_questions()
    _start_quiz(session)
    
    # Loop for reviewing wrong questions
    while session.wrong_questions:
        response = input("Review incorrect answers? (y/n): ").lower().strip()
        
        if response == "y":
            wrong_qs = session.get_wrong_questions()
            session.reset()
            session.flashcards = wrong_qs
            session.shuffle_questions()
            _start_quiz(session)
        elif response == "n":
            print("Better luck next time!")
            break
        else:
            print("Please enter 'y' or 'n'.")
    
    if not session.wrong_questions:
        print("Congratulations! You have mastered the material!")


def _start_quiz(session: QuizSession):
    """
    Conduct a quiz session with user interaction.
    
    Args:
        session: The QuizSession instance
    """
    for question, answer in session.flashcards.items():
        response = input(f"{question}: ").strip()
        
        if session.check_answer(question, response):
            print("✓ Correct!\n")
        else:
            print(f"✗ Incorrect.\nThe correct answer is: {answer}\n")
    
    score, total = session.get_score()
    percentage = session.get_percentage()
    print(f"You scored {score}/{total} ({percentage:.1f}%)\n")


if __name__ == "__main__":
    run_quiz()
