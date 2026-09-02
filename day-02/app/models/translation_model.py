from base_model import BaseModel

class TranslationModel(BaseModel):
    def __init__(self, model):
        self.model = model

    def predict(self, prompt: int) -> int:
        # Translation model converts the input into text before making a prediction.
        text_prompt = str(prompt)
        translated_text = self.model.predict(text_prompt)
        return translated_text
