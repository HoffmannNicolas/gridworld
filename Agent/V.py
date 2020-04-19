

import random


class V():

    # The V value-function measures the attractiveness of each state.
    # V : {State} -> R

    def __init__(self, environment, initialValue=None):
        print("New V")
        self.name = "V"

        self.V = {}
        for state in environment.states():

            state_str = state
            if not(isinstance(state_str, str)): state_str = str(state_str)

            if (state in environment.obstacles):
                self.V[state_str] = 0
                continue

            # Unless otherwise specified, V is uniformely defined in [0, 0.1]
            if (initialValue is None): self.V[state_str] = random.random() * 0.1
            else: self.V[state_str] = initialValue


    def setValue(self, state, value):
        if not(isinstance(state, str)): state = str(state)
        self.V[state] = value


    def states(self):
        return list(self.V.keys())


    def __call__(self, state):
        if not(isinstance(state, str)): state = str(state)
        
        assert (state in self.V.keys()), f"[{self.name}] : V not defined on state {state}"

        return self.V[state]


