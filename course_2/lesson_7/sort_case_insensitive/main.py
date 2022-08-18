sequence = ["Alpha", "bravo", "Charlie", "DELTA", "echo"]

def lower(x):
    return x.lower()


sequence_sorted = sorted(sequence, key=lower)

print(sequence_sorted)
