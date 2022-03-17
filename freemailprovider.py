def freemailpro(domain):
    file = open("freemail", "r")
    for line in file:
        if line == domain:
            return True

    return False
