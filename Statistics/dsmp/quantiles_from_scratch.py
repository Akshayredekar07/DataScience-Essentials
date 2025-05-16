
def percentile_ungrouped(data, p):
    """Calculate the p-th percentile for ungrouped data."""
    data = sorted(data)
    N = len(data)
    # Calculate position
    PL = (p / 100) * (N + 1)
    
    if PL.is_integer():
        return data[int(PL) - 1]
    
    # Interpolation
    k = int(PL)
    fraction = PL - k
    if k < 1 or k >= N:
        return data[k - 1] if k < 1 else data[-1]
    return data[k - 1] + fraction * (data[k] - data[k - 1])

def quartile_ungrouped(data):
    """Calculate quartiles (Q1, Q2, Q3) for ungrouped data."""
    return {
        'Q1': percentile_ungrouped(data, 25),
        'Q2': percentile_ungrouped(data, 50),
        'Q3': percentile_ungrouped(data, 75)
    }

def decile_ungrouped(data, d):
    """Calculate the d-th decile (e.g., d=4 for D4) for ungrouped data."""
    return percentile_ungrouped(data, d * 10)

def quintile_ungrouped(data, q):
    """Calculate the q-th quintile (e.g., q=2 for 40th percentile) for ungrouped data."""
    return percentile_ungrouped(data, q * 20)

def percentile_rank_ungrouped(data, value):
    """Calculate the percentile rank of a value in ungrouped data."""
    x = sum(1 for x in data if x < value)
    y = sum(1 for x in data if x == value)
    N = len(data)
    return ((x + 0.5 * y) / N) * 100

def percentile_grouped(intervals, frequencies, p):
    """Calculate the p-th percentile for grouped data."""
    N = sum(frequencies)
    target = (p / 100) * N
    
    # Calculate cumulative frequencies
    cum_freq = 0
    for i, freq in enumerate(frequencies):
        cum_freq += freq
        if cum_freq >= target:
            # Percentile class found
            L = intervals[i][0]  # Lower boundary
            CF = cum_freq - freq  # Cumulative frequency before
            f = freq  # Frequency of percentile class
            h = intervals[i][1] - intervals[i][0]  # Class width
            return L + ((target - CF) / f) * h
    return None

def quartile_grouped(intervals, frequencies):
    """Calculate quartiles for grouped data."""
    return {
        'Q1': percentile_grouped(intervals, frequencies, 25),
        'Q2': percentile_grouped(intervals, frequencies, 50),
        'Q3': percentile_grouped(intervals, frequencies, 75)
    }

def decile_grouped(intervals, frequencies, d):
    """Calculate the d-th decile for grouped data."""
    return percentile_grouped(intervals, frequencies, d * 10)

def quintile_grouped(intervals, frequencies, q):
    """Calculate the q-th quintile for grouped data."""
    return percentile_grouped(intervals, frequencies, q * 20)

# Example usage
if __name__ == "__main__":
    # Ungrouped data example
    data = [78, 82, 84, 88, 91, 93, 94, 96, 98, 99]
    print("Ungrouped Data:", data)
    print("75th Percentile:", percentile_ungrouped(data, 75))
    print("Quartiles:", quartile_ungrouped(data))
    print("4th Decile:", decile_ungrouped(data, 4))
    print("3rd Quintile:", quintile_ungrouped(data, 3))
    print("Percentile Rank of 84:", percentile_rank_ungrouped(data, 84))
    
    # Grouped data example
    intervals = [(50, 60), (60, 70), (70, 80), (80, 90), (90, 100)]
    frequencies = [5, 10, 15, 12, 8]
    print("\nGrouped Data:")
    print("Intervals:", intervals)
    print("Frequencies:", frequencies)
    print("60th Percentile:", percentile_grouped(intervals, frequencies, 60))
    print("Quartiles:", quartile_grouped(intervals, frequencies))
    print("7th Decile:", decile_grouped(intervals, frequencies, 7))
    print("4th Quintile:", quintile_grouped(intervals, frequencies, 4))

# Dry Run for Ungrouped Data (75th Percentile):
# Data: [78, 82, 84, 88, 91, 93, 94, 96, 98, 99], N = 10
# p = 75, PL = (75/100) * (10 + 1) = 0.75 * 11 = 8.25
# k = int(8.25) = 8, fraction = 8.25 - 8 = 0.25
# 8th value = 96, 9th value = 98
# P75 = 96 + 0.25 * (98 - 96) = 96 + 0.25 * 2 = 96 + 0.5 = 96.5
# Output: 75th Percentile = 96.5

# Dry Run for Ungrouped Quartiles:
# Q1 (p=25): PL = (25/100) * 11 = 2.75
# k = 2, fraction = 0.75, 2nd value = 82, 3rd value = 84
# Q1 = 82 + 0.75 * (84 - 82) = 82 + 0.75 * 2 = 83.5
# Q2 (p=50): PL = (50/100) * 11 = 5.5
# k = 5, fraction = 0.5, 5th value = 91, 6th value = 93
# Q2 = 91 + 0.5 * (93 - 91) = 91 + 0.5 * 2 = 92
# Q3: Same as 75th percentile = 96.5
# Output: {'Q1': 83.5, 'Q2': 92, 'Q3': 96.5}

# Dry Run for 4th Decile (D4):
# D4 = 40th percentile, PL = (40/100) * 11 = 4.4
# k = 4, fraction = 0.4, 4th value = 88, 5th value = 91
# D4 = 88 + 0.4 * (91 - 88) = 88 + 0.4 * 3 = 88 + 1.2 = 89.2
# Output: 4th Decile = 89.2

# Dry Run for 3rd Quintile:
# 3rd Quintile = 60th percentile, PL = (60/100) * 11 = 6.6
# k = 6, fraction = 0.6, 6th value = 93, 7th value = 94
# Q3 = 93 + 0.6 * (94 - 93) = 93 + 0.6 * 1 = 93.6
# Output: 3rd Quintile = 93.6

# Dry Run for Percentile Rank of 84:
# x = values < 84: [78, 82] -> 2
# y = values = 84: [84] -> 1
# N = 10
# Rank = ((2 + 0.5 * 1) / 10) * 100 = (2.5 / 10) * 100 = 25%
# Output: Percentile Rank of 84 = 25.0

# Dry Run for Grouped Data (60th Percentile):
# Intervals: [(50, 60), (60, 70), (70, 80), (80, 90), (90, 100)]
# Frequencies: [5, 10, 15, 12, 8], N = 5 + 10 + 15 + 12 + 8 = 50
# p = 60, target = (60/100) * 50 = 30
# Cumulative frequencies: [5, 15, 30, 42, 50]
# 30 falls in 70-80 (cum_freq = 30)
# L = 70, CF = 15, f = 15, h = 80 - 70 = 10
# P60 = 70 + ((30 - 15) / 15) * 10 = 70 + (15/15) * 10 = 70 + 10 = 80
# Output: 60th Percentile = 80.0

# Dry Run for Grouped Quartiles:
# Q1 (p=25): target = (25/100) * 50 = 12.5
# Cum_freq = 15 at 60-70, L = 60, CF = 5, f = 10, h = 10
# Q1 = 60 + ((12.5 - 5) / 10) * 10 = 60 + (7.5/10) * 10 = 60 + 7.5 = 67.5
# Q2 (p=50): target = (50/100) * 50 = 25
# Cum_freq = 30 at 70-80, L = 70, CF = 15, f = 15, h = 10
# Q2 = 70 + ((25 - 15) / 15) * 10 = 70 + (10/15) * 10 = 70 + 6.67 = 76.67
# Q3 (p=75): target = (75/100) * 50 = 37.5
# Cum_freq = 42 at 80-90, L = 80, CF = 30, f = 12, h = 10
# Q3 = 80 + ((37.5 - 30) / 12) * 10 = 80 + (7.5/12) * 10 = 80 + 6.25 = 86.25
# Output: {'Q1': 67.5, 'Q2': 76.67, 'Q3': 86.25}

# Dry Run for 7th Decile (D7):
# D7 = 70th percentile, target = (70/100) * 50 = 35
# Cum_freq = 42 at 80-90, L = 80, CF = 30, f = 12, h = 10
# D7 = 80 + ((35 - 30) / 12) * 10 = 80 + (5/12) * 10 = 80 + 4.17 = 84.17
# Output: 7th Decile = 84.17

# Dry Run for 4th Quintile:
# 4th Quintile = 80th percentile, target = (80/100) * 50 = 40
# Cum_freq = 42 at 80-90, L = 80, CF = 30, f = 12, h = 10
# Q4 = 80 + ((40 - 30) / 12) * 10 = 80 + (10/12) * 10 = 80 + 8.33 = 88.33
# Output: 4th Quintile = 88.33