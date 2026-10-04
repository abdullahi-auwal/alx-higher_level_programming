#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if len(a_dictionary) == 0:
        return None
    sorted_scores = sorted(a_dictionary.items(),
                           key=lambda items: items[1], reverse=True)
    return sorted_scores[0][0]
