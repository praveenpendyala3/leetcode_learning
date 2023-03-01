
## Definitions:
# State --> A partial or complete solution, valid or invalid
#  Valid state --> A complete solution that meets our criteria
# An invalid state --> A partial or complete solution that fails to meet the criteria

# candidate states : Possible candidates to move to the next state.


# HELPER FUNCTION 1
def isValidState(state):
    # Check if state is a valid complete solution
    return False

# HELPER FUNCTION 2
def get_candidates(state):
    # Get the candidates that can be used to create a next state from the partial state argument and return them as a list
    return []

# HELPER FUNCTION 3
def search(state,solutions):

    if isValidState(state):
        solutions.append(state.copy()) #We want to create a deep copy (instead of a shallow copy or link)
        # return out of the recursion if only one solution is needed, else find all

    # If the state is incomplete:
    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)


def solve():
    solutions = []
    state = set()
    search(state,solutions)
    return solutions

