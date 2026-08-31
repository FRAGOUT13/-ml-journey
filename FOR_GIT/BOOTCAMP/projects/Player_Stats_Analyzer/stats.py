# Manual statistics functions — no libraries, just plain Python.

def mean(values):
    """Average of a list of numbers."""
    return sum(values) / len(values)

def median(values):
    """Middle value when sorted; average of the two middle values if even-length."""
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return sorted_vals[mid]

def variance(values):
    """Average squared distance from the mean — spread of the data."""
    avg = mean(values)
    return sum((x - avg) ** 2 for x in values) / len(values)

def std_dev(values):
    """Square root of variance — spread in the same units as the data."""
    return variance(values) ** 0.5