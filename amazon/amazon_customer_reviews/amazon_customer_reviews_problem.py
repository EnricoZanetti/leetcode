def get_suggestions(repository, customer_query):
    """
    Return up to three lexicographically-sorted suggestions for each
    incremental prefix (length >= 2) of `customer_query`.
    """

    repo_sorted = sorted(word.lower() for word in repository)
    customer_query = customer_query.lower()

    if len(customer_query) < 2:
        return []

    prefixes = [customer_query[:i] for i in range(2, len(customer_query) + 1)]

    i = 0
    suggestions = []
    while i < len(prefixes):
        intermediate_res = []
        target = prefixes[i]
        for word in repo_sorted:
            if word[: len(target)] == target:
                intermediate_res.append(word)
        i += 1

        intermediate_res.sort()
        suggestions.append(intermediate_res[:3])

    return suggestions
