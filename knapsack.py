def knapsack(parcels, capacity):
    """
    Solve the 0/1 Knapsack Problem using Dynamic Programming.
    Select parcels to maximize total value within weight capacity.
    """

    n = len(parcels)

    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    for i in range(1, n + 1):

        weight = parcels[i - 1]["weight"]
        value = parcels[i - 1]["value"]

        for w in range(capacity + 1):

            if weight > w:
                dp[i][w] = dp[i - 1][w]

            else:
                include = value + dp[i - 1][w - weight]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

    selected_parcels = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            selected_parcels.append(parcels[i - 1])
            w -= parcels[i - 1]["weight"]

    selected_parcels.reverse()

    total_weight = sum(p["weight"] for p in selected_parcels)
    total_value = sum(p["value"] for p in selected_parcels)

    return selected_parcels, total_weight, total_value