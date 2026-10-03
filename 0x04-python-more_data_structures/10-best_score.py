#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    sorted_scores = sorted(a_dictionary.items(), key=lambda items: items[1], reverse=True)
    return sorted_scores[0][0]
