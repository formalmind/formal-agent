from dataclasses import dataclass
from typing import List, Dict, Any
from .agent import LocalAgent


@dataclass
class LLMLean(LocalAgent):
    def __init__(self):
        model_id: str = "wellecks/ntpctx-llama3-8b"
        super().__init__(f"ollama/{model_id}")

    def get_messages(self, prompt: str):
        messages: List[Dict[str, Any]] = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"{prompt}",
                    }
                ],
            },
        ]
        return self.model(messages)
