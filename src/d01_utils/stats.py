# stats.py

# cumulative
def cumulative_sum(data: list[float]) -> list[float]:
    """
    summary:
        sum data succesively to create a trend
    args:
        data (list[float]): profit | losses per trade
    returns:
        list[float]: list of averages based on passed in count
    """
    r_a = [0]
    [r_a.append(round(r_a[-1] + i, 2)) for i in data]
    return r_a


def cumulative_avg(data: list[float], avg: int) -> list[float]:
    """
    summary:
        sum data succesively to create a trend
    args:
        data (list[float]): profit | losses per trade
        avg (int): average length | count
    returns:
        list[float]: list of averages based on passed in count
    """
    c_a = [0]
    [
        c_a.append(round(c_a[-1] + sum([data[_] for _ in range(i - avg, i)])))
        for i in range(avg, len(data), avg)
    ]
    return c_a
