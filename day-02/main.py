# Import sys so we can add the project folder to Python's import path.
import sys

# Import Path so we can work with folder paths safely.
from pathlib import Path

# Store the day-02 folder because it contains the app package.
BASE_DIR = Path(__file__).resolve().parents[1]

# Add day-02 to Python's import path so app imports work when this file is run directly.
sys.path.append(str(BASE_DIR))

# Import the application settings from config.py.
from app.config import settings

# Import the fraud detection model class.
from app.models.fraud_model import FraudDetectionModel

# Import the translation model class.
from app.models.translation_model import TranslationModel

# Import the translation model class.
from app.models.sentiment_analysis_model import SentimentAnalysisModel

# Import the prediction service that runs the selected model.
from app.services.prediction_service import PredictionService

# Import the shared logger for logging application events.
from app.utils.logger import logger


# Create a mock translation engine for the exercise.
class SimpleTranslationEngine:
    # Define the predict method expected by TranslationModel.
    def predict(self, prompt: str) -> str:
        # Return a fake translation because the exercise is about architecture, not real AI.
        return "..."


# Create a mock fraud detection engine for the exercise.
class SimpleFraudEngine:
    # Define the predict method expected by FraudDetectionModel.
    def predict(self, amount: int) -> str:
        # Return a fake fraud result based on the amount entered by the user.
        return "Fraud Risk: High" if amount >= 1000 else "Fraud Risk: Low"


# Create a mock sentiment analysis engine for the exercise.
class SimpleSentimentEngine:
    # Define the predict method expected by SentimentAnalysisModel.
    def predict(self, prompt: str) -> str:
        # Return a fake sentiment score based on the input text.
        return "Positive" if "good" in prompt.lower() else "Negative"
        return "Fraud Risk: High" if amount >= 1000 else "Fraud Risk: Low"

# Define a function to print the application title and configuration.
def show_header():
    # Print the top border for the title.
    print("=========================")
    # Print the application title.
    print("      AI MODEL MANAGER")
    # Print the bottom border for the title.
    print("=========================")
    # Print a blank line to make the output easier to read.
    print()
    # Print the application name from the settings object.
    print(f"Application: {settings.app_name}")
    # Print the environment from the settings object.
    print(f"Environment: {settings.environment}")
    # Print a blank line before showing the model list.
    print()


# Define a function that asks the user which model to use.
def select_model():
    # Print the model section heading.
    print("Available Models")
    # Print option 1 for the translation model.
    print("1. Translation Model")
    # Print option 2 for the fraud detection model.
    print("2. Fraud Detection Model")
    # Print option 3 for the sentiment analysis model.
    print("3. Sentiment Analysis Model")
    # Print a blank line before asking for input.
    print()
    # Ask the user to select one model.
    choice = input("Select Model: ")

    # Check if the user selected the translation model.
    if choice == "1":
        # Log that the translation model is being loaded.
        logger.info("Loading Translation Model")
        # Create the translation model and give it the mock translation engine.
        model = TranslationModel(SimpleTranslationEngine())
        # Return both the model object and the display name.
        return model, "English-Hausa Translator"

    # Check if the user selected the fraud detection model.
    if choice == "2":
        # Log that the fraud detection model is being loaded.
        logger.info("Loading Fraud Detection Model")
        # Create the fraud model and give it the mock fraud engine.
        model = FraudDetectionModel(SimpleFraudEngine())
        # Return both the model object and the display name.
        return model, "Fraud Detection Model"

    # Check if the user selected the sentiment analysis model.
    if choice == "3":
        # Log that the sentiment analysis model is being loaded.
        logger.info("Loading Sentiment Analysis Model")
        # Create the sentiment analysis model and give it the mock sentiment engine.
        model = SentimentAnalysisModel(SimpleSentimentEngine())
        # Return both the model object and the display name.
        return model, "Sentiment Analysis Model"

    # Stop the program with a clear message if the user enters a wrong option.
    raise ValueError("Invalid model selected. Please select 1, 2, or 3.")


# Define a function that validates user input before prediction.
def validate_input(model, user_input):
    # Check if the selected model is the fraud detection model.
    if isinstance(model, FraudDetectionModel):
        # Make sure the fraud model receives a number.
        if not user_input.isdigit():
            # Stop the program if the fraud input is not numeric.
            raise ValueError("Fraud Detection Model needs a numeric amount.")
        # Convert the numeric text input into an integer.
        return int(user_input)

    # Return normal text input for the translation model.
    return user_input


# Define the main function that controls the whole application flow.
def main():
    # Log that the application has started.
    logger.info("Application started")
    # Print the application heading and configuration.
    show_header()
    # Ask the user to choose a model and receive the model name.
    model, model_name = select_model()
    # Log that the selected model loaded successfully.
    logger.info("Model loaded successfully")
    # Inject the selected model into the prediction service.
    service = PredictionService(model)
    # Print a blank line before asking for the prediction input.
    print()
    # Ask the user for the input that should be predicted.
    user_input = input("Input: ")
    # Print a blank line before the processing message.
    print()
    # Tell the user the prediction is being processed.
    print("Processing...")
    # Print a blank line before the final result block.
    print()
    # Validate and prepare the input for the selected model.
    valid_input = validate_input(model, user_input)
    # Run prediction through the prediction service.
    prediction = service.predict(valid_input)
    # Log that prediction completed successfully.
    logger.info("Prediction completed successfully")
    # Print the selected model name.
    print(f"Model: {model_name}")
    # Print the prediction output.
    print(f"Prediction: {prediction}")
    # Print a blank line before the success message.
    print()
    # Print the final success message so the program feels complete.
    print("Execution successful.")


# Make sure main runs only when this file is executed directly.
if __name__ == "__main__":
    # Try to run the application normally.
    try:
        # Start the application.
        main()
    # Catch any error that happens while the app is running.
    except Exception as error:
        # Log the error for debugging.
        logger.error("Application failed: %s", error)
        # Print a friendly error message for the user.
        print(f"Error: {error}")