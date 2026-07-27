class DFA:
    def __init__(self, states, alphabet, transition_table, start_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_table = transition_table
        self.start_state = start_state
        self.final_states = final_states
    def simulate(self, input_string):
        current_state = self.start_state
        path = [current_state]  # track transition path
        for symbol in input_string:
            if symbol not in self.alphabet:
                return f"Invalid symbol '{symbol}' found!"
            current_state = self.transition_table.get((current_state, symbol))
            if current_state is None:
                return "Rejected (No transition)"
            path.append(current_state)
        path_str = " → ".join(path)
        if current_state in self.final_states:
            return f"Transition Path:\n{path_str}\nAccepted"
        else:
            return f"Transition Path:\n{path_str}\nRejected"
states = {"q0", "q1", "q2"}
alphabet = {"a", "b"}
transition_table = {
    ("q0", "a"): "q1",
    ("q0", "b"): "q0",
    ("q1", "a"): "q1",
    ("q1", "b"): "q2",
    ("q2", "a"): "q1",
    ("q2", "b"): "q0",
}
start_state = "q0"
final_states = {"q2"}
dfa = DFA(states, alphabet, transition_table, start_state, final_states)
inputs = ["abaab", "ab", "aab", "baba", "aaabb"]
for s in inputs:
    print(f"Input: {s}")
    print(dfa.simulate(s))
    print("-" * 40)