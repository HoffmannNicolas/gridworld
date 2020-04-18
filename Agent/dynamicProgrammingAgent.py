

import random
import copy

import Agent.Agent as Agent
import Agent.Policy as Policy
import Agent.V as V


class dynamicProgrammingAgent(Agent.Agent):

    def __init__(self, gamma=0.9):
        print("New dynamicProgramming Agent")
        self.name = "dynamicProgrammingAgent"

        self.gamma = gamma

        self.V = None # Value-function of the states
        self.policy = None # PI, policy : {State} -> {Action}
        # Agent is not dedicated to an environment for now : This is done on first episode.


    def onEpisodeStart(self, environment):
        if (self.V == None):
            self.V = V.V(environment)
            self.V.setValue(environment.goalState, 0)
            print(f"[{self.name}] : V set up")

        if (self.policy == None):
            self.policy = Policy.Policy(environment)
            self._computeGreedyPolicy(environment)
            print(f"[{self.name}] : Policy set up")


    def choseAction(self, environment):
        actionDistribution = sorted(self.policy(self.state), key=lambda x : x[1]) # Sort action distribution
        action = actionDistribution[0] # Select most probable action
        action = action[0] # (action, probability) -> action

        print(f"[{self.name}] State {self.state}")
        print(f"[{self.name}] Action {action} chosen !")
        return action


    def onTransition(self, environment):

        print(f"[{self.name}] State {self.state}")

        self._policyEvaluation(environment)
        print(f"[{self.name}] : Policy Evaluation done.")


        """
        def _policyImprovement(environment):
            # Policy Improvement (p.80)
            old_policy = copy.deepcopy(self.policy)
            computeGreedyPolicy(environment)
                oldActionDistribution = old_policy(state).sorted(key=lambda x : x[1]) # Sort all actions considered
                oldAction = oldActionDistribution[0] # Select most probable action
                oldAction = oldAction[0] # (action, probability) -> action

            # TODO : compare new with old policy and stop if needed
        """

        self._computeGreedyPolicy(environment)
        print(f"[{self.name}] : Policy Improvement done.")


    def _policyEvaluation(self, environment):
        # Iterative Policy Evaluation (p.80)
        old_V = copy.deepcopy(self.V)

        for state in environment.states():
            newStateValue = 0

            for actionProbability, action in self.policy(state):
                actionValue = 0

                for nextState, nextStatesProbability, nextReward, _ in environment._transition(state, action): # episodeEnded is discarted
                    transitionValue = nextReward + self.gamma * old_V(nextState)
                    actionValue += transitionValue * nextStatesProbability

                newStateValue += actionValue

            self.V.setValue(state, newStateValue)


    def _computeGreedyPolicy(self, environment):
        for state in environment.states():

            highestReturnAction = None
            highestReturnAction_value = None

            for action in environment.possibleActions(state):
                actionValue = 0

                for nextState, nextStatesProbability, nextReward, _ in environment._transition(state, action): # episodeEnded is discarted
                    transitionValue = nextReward + self.gamma * self.V(nextState)
                    actionValue += transitionValue * nextStatesProbability

                if (highestReturnAction is None):
                    highestReturnAction = action
                    highestReturnAction_value = actionValue
                elif (actionValue > highestReturnAction_value):
                    highestReturnAction = action
                    highestReturnAction_value = actionValue

            self.policy.setValue(state, [(action, 1)]) # Policy requires [(action, actionProbability)]


    def onEpisodeEnd(self):
        print(f"[{self.name}] : Nothing to do at the end of an episode either.")

