from dataclasses import dataclass
from typing import List, Dict, Any
from .agent import LocalAgent


@dataclass
class Llama3(LocalAgent):
    def __init__(self):
        model_id: str = "llama3.2"
        super().__init__(f"ollama_chat/{model_id}")

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
