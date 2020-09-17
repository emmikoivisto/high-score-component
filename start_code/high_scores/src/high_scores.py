def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores = high_to_low(scores)
    return scores[:3]


def high_to_low(scores):
    scores.sort(reverse = True)
    return scores
