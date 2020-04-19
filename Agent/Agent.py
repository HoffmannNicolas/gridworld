

from abc import abstractmethod
import copy
import random


class Agent():

    def __init__(self):
        print("New agent created")

        self.state = None
        self.V = None # Value-function of the states
        self.Q = None # Value-function of (state-action) paires
        self.policy = None # PI, policy : {State} -> {Action}

        self.gamma = None
        self.epsilon = None # Used for epsilon-greedy action selection

    @abstractmethod
    def onEpisodeStart(self): pass
        # Set-up ressources specific for an episode

    @abstractmethod
    def choseAction(self, possibleActions): pass

    @abstractmethod
    def onTransition(self): pass
        # Computations after the environment computed the transition (some agents update their value-function or policy)

    @abstractmethod
    def onEpisodeEnd(self, previousEpisodesStates): pass
        # Computations at the end of an episode (some agent update their value-function or policy)


    def _choseRandomAction(self, environment, verbose=False):
        action = random.choice(environment.possibleActions(self.state))
        if (verbose): print(f"[{self.name}] Action {action} chosen !")
        return action


    def _sampleActionFromPolicy(self, environment, verbose=False):
        actionDistribution = self.policy(self.state) # Select action distribution from policy
        actionDistribution = sorted(actionDistribution, key=lambda x : x[1]) # Sort action distribution
        actionWeights = [actionProbability for action, actionProbability in actionDistribution]
        actionPair = random.choices(actionDistribution, weights=actionWeights, k=1)[0]
        action = actionPair[0] # (action, actionProbability) -> action
        if (verbose): print(f"[{self.name}] Action {action} chosen !")
        return action


    def _epsilonGreedyActionFromPolicy(self, environment, verbose=False):
        if (random.random() < self.epsilon): return self._sampleActionFromPolicy(environment, verbose=verbose)
        else: return self._choseRandomAction(environment)


    def _computeGreedyPolicy(self, environment):
        # "Reinforcement Learning, An Introduction" Second edition, Sutton & Barto (p.80 "Policy Improvement")
        for state in environment.emptyStates():

            highestReturnActions = []
            highestReturnActions_value = None

            for action in environment.possibleActions(state):
                actionValue = 0

                for nextState, nextStatesProbability, nextReward, _ in environment._transition(state, action): # episodeEnded is discarted
                    transitionValue = nextReward + self.gamma * self.V(nextState)
                    actionValue += transitionValue * nextStatesProbability

                if (len(highestReturnActions) == 0):
                    highestReturnActions = [action]
                    highestReturnActions_value = actionValue
                elif (actionValue > highestReturnActions_value):
                    highestReturnActions = [action]
                    highestReturnActions_value = actionValue
                elif (actionValue == highestReturnActions_value):
                    highestReturnActions.append(action)

            actionDistribution = [[action, 1 / len(highestReturnActions)] for action in highestReturnActions]
            self.policy.setValue(state, actionDistribution) # Policy requires [(action, actionProbability), ...]


    def _valueIteration(self, environment):
        # "Reinforcement Learning, An Introduction" Second edition, Sutton & Barto (p.83)
        old_V = copy.deepcopy(self.V)

        for state in environment.emptyStates():
            maxActionValue = -1

            for action in environment.possibleActions(state):
                actionValue = 0

                for nextState, nextStatesProbability, nextReward, _ in environment._transition(state, action): # episodeEnded is discarted
                    transitionValue = nextReward + self.gamma * old_V(nextState)
                    actionValue += transitionValue

                maxActionValue = max(actionValue, maxActionValue)
                actionValue = 0

            self.V.setValue(state, maxActionValue)


    def _policyEvaluation(self, environment):
        # "Reinforcement Learning, An Introduction" Second edition, Sutton & Barto (p.80, "Policy Evaluation")
        old_V = copy.deepcopy(self.V)

        for state in environment.emptyStates():
            newStateValue = 0

            for actionProbability, action in self.policy(state):
                actionValue = 0

                for nextState, nextStatesProbability, nextReward, _ in environment._transition(state, action): # episodeEnded is discarted
                    print("nextState, nextStatesProbability, nextReward, _ : ", nextState, nextStatesProbability, nextReward, _)
                    if (nextReward != 0) : print("Policy Eval : nextReward = ", nextReward)
                    exit()
                    transitionValue = nextReward + self.gamma * old_V(nextState)
                    actionValue += transitionValue * nextStatesProbability

                newStateValue += actionValue
                if (newStateValue > 1) : print("newStateValue : ", newStateValue)

            self.V.setValue(state, newStateValue)

