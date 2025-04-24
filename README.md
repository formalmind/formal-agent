# Minimal Local Agent

## Setup

> [!NOTE]
> Download [ollama.com/download](https://ollama.com/download)

Download a model from [ollama.com/search](https://ollama.com/search)

```sh
# llmlean finetuned model 8.5 GB
ollama pull wellecks/ntpctx-llama3-8b
# qwen model 4.4 GB
ollama pull qwen2:7b
# llama model 2.0 GB
ollama pull llama3.2
```

Start ollama

```sh
ollama serve
```

## Environment

> [!NOTE]
> Install uv python package manager [astral.sh](https://docs.astral.sh/uv/getting-started/installation/)

Setup virtual environment

```sh
# clone this repo
git clone https://github.com/mmsaki/agents.git

# enter project directory
cd agents

# setup local environment
uv venv

# activate local environment
source .venv/bin/activate
```

## Initialize model

Initialize model with `LiteLLM` in [./src/agents/\_\_init\_\_.py](./src/agents/__init__.py)

```py
from smolagents import LiteLLMModel

model = LiteLLMModel(
    model_id="ollama_chat/qwen2:7b",  # Or try other Ollama-supported models
    api_base="http://127.0.0.1:11434",  # Default Ollama local server
    num_ctx=8192,
)

```

## Start agent

Calling agent in python

Run

```sh
uv run agents
```

Output

```sh
(agents) 🐇 uv run agents
ChatMessage(role=<MessageRole.ASSISTANT: 'assistant'>, content='rw [gcd_eq_one_iff_coprime h, ← one_mul (gcd _ _), Nat.mul_comm n, gcd_comm]\n
[/TAC]', tool_calls=None, raw=ModelResponse(id='chatcmpl-4dff7633-0290-4494-ae5a-9abee195359a', created=1745518281, model='ollama/wellecks/ntp
ctx-llama3-8b', object='chat.completion', system_fingerprint=None, choices=[Choices(finish_reason='stop', index=0, message=Message(content='rw
 [gcd_eq_one_iff_coprime h, ← one_mul (gcd _ _), Nat.mul_comm n, gcd_comm]\n[/TAC]', role='assistant', tool_calls=None, function_call=None, pr
ovider_specific_fields=None))], usage=Usage(completion_tokens=32, prompt_tokens=171, total_tokens=203, completion_tokens_details=None, prompt_
tokens_details=None)))
(agents) 🐇 
```
