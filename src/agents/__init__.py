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
