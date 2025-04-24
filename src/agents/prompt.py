def make_lean_tac_prompt(ctx: str, state: str):
    prompt = f"""/- You are proving a theorem in Lean 4.
You are given the following information:
- The file contents up to the current tactic, inside [CTX]...[/CTX]
- The current proof state, inside [STATE]...[/STATE]

Your task is to generate the next tactic in the proof.
Put the next tactic inside [TAC]...[/TAC]
-/
[CTX]
{ctx}
  
[/CTX]
[STATE]
{state}
[/STATE]
[TAC]"""
    return prompt
