from app.models.base_model import BaseModel

class SentimentAnalysisModel(BaseModel):
    def __init__(self, model):
        self.model = model

    def predict(self, prompt: str) -> str:
        # Sentiment analysis model uses the original text input to calculate a sentiment score.
        sentiment_score = self.model.predict(prompt)
        return sentiment_score
