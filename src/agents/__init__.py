from .llmlean import LLMLean
from .qwen7b import Qwen7b
from .llama3 import Llama3
from .prompt import make_lean_tac_prompt


def main() -> None:
    ctx = """import Mathlib.Data.Nat.Prime

theorem test_thm (m n : Nat) (h : m.Coprime n) : m.gcd n = 1 := by
"""
    state = """m n : ℕ
h : Nat.Coprime m n
⊢ Nat.gcd m n = 1
"""
    prompt = make_lean_tac_prompt(ctx, state)

    agent = LLMLean()
    agent2 = Qwen7b()
    agent3 = Llama3()

    print(agent.get_messages(prompt))
    print(agent2.get_messages(prompt))
    print(agent3.get_messages(prompt))
