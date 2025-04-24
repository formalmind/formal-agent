from dataclasses import dataclass
from smolagents import LiteLLMModel


@dataclass
class LocalAgent:
    api_base: str = "http://127.0.0.1:11434"
    num_ctx: int = 8192

    def __init__(self, model_id: str):
        self.model = LiteLLMModel(
            model_id=model_id,
            api_base=self.api_base,
            num_ctx=self.num_ctx,
        )
