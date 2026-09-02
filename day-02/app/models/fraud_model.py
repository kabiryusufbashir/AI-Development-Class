from app.models.base_model import BaseModel

class FraudDetectionModel(BaseModel):
    def __init__(self, model):
        self.model = model

    def predict(self, prompt: int) -> int:
        # Fraud model uses the original numeric input to calculate a fraud score.
        fraud_score = self.model.predict(prompt)
        return fraud_score