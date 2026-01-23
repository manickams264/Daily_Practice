def pageCount(n, p):
    front_turns = p//2
    back_turns = (n//2) - front_turns
    if front_turns < back_turns:
        return front_turns
    else:
        return back_turns