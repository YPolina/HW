from collections import Counter
import math
def conditional_entropy(x,y,log_base: float=2):
    y_counts = Counter(y)
    xy_counts = Counter(list(zip(x,y)))
    total_counts = len(x)

    for xy in xy_counts.keys():
        p_y = y_counts[xy[1]]/total_counts
        p_xy = xy_counts[xy] / total_counts
        cond_entropy = 0
        cond_entropy += p_y * math.log(p_y/p_xy, log_base)
    return cond_entropy


def entropy(x, log_base: float=2):
    x_counts = Counter(x)
    total_counts = len(x)
    p_x = list(map(lambda n: n/total_counts, x_counts.values()))
    entropy = 0.0
    for p in p_x:
        entropy += -p*math.log(p,2)

    return entropy


def ucoef(x, y, log_base = 2):
    s_xy = conditional_entropy(x, y, log_base)
    s_x = entropy(x, log_base)
    u = (s_x - s_xy)/s_x

    return u