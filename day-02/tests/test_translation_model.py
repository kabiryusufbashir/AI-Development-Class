# Import sys so we can add the project folder to Python's import path.
import sys

# Import Path so we can work with folder paths safely.
from pathlib import Path

# Store the day-02 folder because it contains the app package.
BASE_DIR = Path(__file__).resolve().parents[1]

# Add day-02 to Python's import path so app imports work when this file is run directly.
sys.path.append(str(BASE_DIR))

from app.models.translation_model import(TranslationModel)

def test_translation_model():

    model = TranslationModel()

    result = model.predict("Hello, how are you?")
    
    assert result is not None

