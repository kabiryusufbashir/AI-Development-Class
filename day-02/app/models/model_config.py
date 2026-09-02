from dataclasses import dataclass

@dataclass
class ModelConfig:
    name: str
    version: str
    temperature: float = 0.2
    max_tokens: int = 500

translation_model = ModelConfig(
    name = "Translation Model",
    version = "1.0"
)

fraud_detection_model = ModelConfig(
    name = "Fraud Detection Model",
    version = "1.0"
)

print(translation_model)
print(fraud_detection_model)
