"""Manages flashcard data operations."""

class FlashcardManager:
    """Handles loading and storing flashcard data."""
    
    def __init__(self):
        self.flashcards = {}
    
    def load_from_file(self, filename: str) -> bool:
        """
        Load flashcards from a text file.
        
        Args:
            filename: Path to the file (with or without .txt extension)
            
        Returns:
            bool: True if successful, False otherwise
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the file format is invalid
        """
        if not filename.endswith(".txt"):
            filename += ".txt"
        
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    raise ValueError("File is empty")
                
                qa_pairs = content.split("\n\n")
                for qa in qa_pairs:
                    lines = qa.split("\n")
                    if len(lines) < 2:
                        raise ValueError(f"Invalid format: {qa[:30]}...")
                    
                    question = lines[0].strip()
                    answer = lines[1].strip()
                    
                    if question and answer:
                        self.flashcards[question] = answer
            
            return True
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}' not found")
        except Exception as e:
            raise ValueError(f"Error loading file: {str(e)}")
    
    def get_flashcards(self) -> dict:
        """Return all flashcards."""
        return self.flashcards.copy()
    
    def count(self) -> int:
        """Return the number of flashcards."""
        return len(self.flashcards)
    
    def reset(self):
        """Clear all flashcards."""
        self.flashcards.clear()
