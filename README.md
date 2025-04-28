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
git clone https://github.com/formalmind/formal-agent.git

# enter project directory
cd agents

# setup local environment
uv venv

# activate local environment
source .venv/bin/activate
```

## Initialize model

Initialize `LLMLean` model in [./src/agents/\_\_init\_\_.py](./src/agents/__init__.py)

```py
from smolagents import CodeAgent
from .llmlean import LLMLean
from .prompt import make_lean_tac_prompt
from phoenix.otel import register
from openinference.instrumentation.smolagents import SmolagentsInstrumentor

register()
SmolagentsInstrumentor().instrument()


def main() -> None:
    llmlean = LLMLean()

    lean4_agent = CodeAgent(
        tools=[],
        model=llmlean.model,
        name="lean4_agent",
        description="Generetes Lean 4 tactics for you.",
    )

    ctx = """import Mathlib.Data.Nat.Prime

theorem test_thm (m n : Nat) (h : m.Coprime n) : m.gcd n = 1 := by
"""
    state = """m n : ℕ
h : Nat.Coprime m n
⊢ Nat.gcd m n = 1
"""

    prompt = make_lean_tac_prompt(ctx, state)
    print(lean4_agent.run(prompt))
```

## Start agent

Run

```sh
uv run agents
```

## Debbging Model

Run the phoenix server from your environment

```py
uv run python -m phoenix.server.main serve
```

Go to [`http://localhost:6006`](http://localhost:6006) to agent traces
