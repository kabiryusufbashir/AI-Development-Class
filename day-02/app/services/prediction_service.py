from app.models.base_model import BaseModel

class PredictionService:
    def __init__(self, model: BaseModel):
        # The service must receive a concrete model, not BaseModel directly.
        self.model = model

    def predict(self, input_data):
        return self.model.predict(input_data)