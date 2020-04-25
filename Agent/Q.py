

import random


class Q():

    # The Q value-function measures the attractiveness of each state-action pair.
    # Q : {State} x {Action} -> R

    def __init__(self, environment, initialValue=None):
        print("New Q")
        self.name = "Q"

        self.Q = {}
        for state in environment.states():
            for action in environment.possibleActions(state):

                state_str = state
                if not(isinstance(state_str, str)): state_str = str(state_str)

                action_str = state
                if not(isinstance(action_str, str)): action_str = str(action_str)

                stateAction_str = f"{state}{action}"

                if (state in environment.obstacles):
                    self.Q[stateAction_str] = 0
                    continue

                # Unless otherwise specified, Q is uniformely defined in [0, 0.1]
                if (initialValue is None): self.Q[stateAction_str] = random.random() * 0.1
                else: self.Q[stateAction_str] = initialValue


    def setValue(self, state, action, value):
        if not(isinstance(state, str)): state = str(state)
        if not(isinstance(action, str)): action = str(action)
        stateAction = f"{state}{action}"
        self.Q[stateAction] = value


    def stateActions(self):
        return list(self.Q.keys())


    def __call__(self, state, action):
        if not(isinstance(state, str)): state = str(state)
        if not(isinstance(action, str)): action = str(action)

        stateAction = f"{state}{action}"
        assert (stateAction in self.Q.keys()), f"[{self.name}] : Q not defined on state-action pair {stateAction}"

        return self.Q[stateAction]


