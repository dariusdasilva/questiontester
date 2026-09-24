"""Quiz logic and scoring operations."""

from typing import Tuple, Dict
import random


class QuizSession:
    """Manages a quiz session with scoring."""
    
    def __init__(self, flashcards: Dict[str, str]):
        """
        Initialize a quiz session.
        
        Args:
            flashcards: Dictionary of {question: answer}
        """
        self.flashcards = flashcards
        self.score = 0
        self.total = len(flashcards)
        self.wrong_questions = {}
    
    def check_answer(self, question: str, answer: str) -> bool:
        """
        Check if the answer is correct (case-insensitive).
        
        Args:
            question: The question
            answer: The user's answer
            
        Returns:
            bool: True if correct, False otherwise
        """
        correct_answer = self.flashcards.get(question, "")
        is_correct = answer.lower().strip() == correct_answer.lower().strip()
        
        if is_correct:
            self.score += 1
        else:
            self.wrong_questions[question] = correct_answer
        
        return is_correct

    def shuffle_questions(self):
        """Shuffle the order of questions."""
        questions_list = list(self.flashcards.items())
        random.shuffle(questions_list)
        self.flashcards = dict(questions_list)
    
    def get_score(self) -> Tuple[int, int]:
        """Return (score, total)."""
        return self.score, self.total
    
    def get_wrong_questions(self) -> Dict[str, str]:
        """Return dictionary of wrong questions."""
        return self.wrong_questions.copy()
    
    def reset(self):
        """Reset the session."""
        self.score = 0
        self.wrong_questions.clear()
    
    def get_percentage(self) -> float:
        """Calculate and return percentage score."""
        if self.total == 0:
            return 0.0
        return (self.score / self.total) * 100
