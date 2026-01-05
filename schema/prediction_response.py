from pydantic import BaseModel, Field
from typing import Dict

# pydantic model to structure and validate the prediction response
class PredictionResponse(BaseModel):
    predicted_category: str = Field(
        ..., description="The predicted insurance premium category",
        example="high"
    )
    confidence: float = Field(
        ..., description="The confidence score of the prediction ranging from 0 to 1",
        example=0.85
    )
    class_probabilities: Dict[str, float] = Field(
        ..., description="A dictionary mapping each insurance premium category to its predicted probability",
        example={"low": 0.1, "medium": 0.05, "high": 0.85}
    )