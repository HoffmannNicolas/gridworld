

import random


class Policy():

    # A policy is used to select an action in a given state.
    # Policy : {State} -> {Action}
    # To be compatible with stochasticity : The output of a Policy is a [list] of [action_i, actionProbability_i, action_i+1, actionProbability_i+1,...]
    # A deterministic policy will return [action, 1]

    def __init__(self, environment):
        print("New Policy")
        self.name = "Policy"

        self.policy = {}
        for state in environment.states():
            if not(isinstance(state, str)): state = str(state)
            self.policy[state] = None


    def setValue(self, state, value):
        if not(isinstance(state, str)): state = str(state)
        self.policy[state] = value


    def states(self):
        return list(self.policy.keys())


    def __call__(self, state):
        if not(isinstance(state, str)): state = str(state)
        
        assert (state in self.policy.keys()), f"[{self.name}] : Policy not defined on state {state}"

        return self.policy[state]


