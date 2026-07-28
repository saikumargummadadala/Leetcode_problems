"""# Step 1: Read N (number of locations)
n = int(input())

# Step 2: Read the N x N distance matrix
matrix = []
for _ in range(n):
    # Read one row, split space-separated values, and convert them to integers
    row = list(map(int, input().split()))
    matrix.append(row)
print(matrix)
"""
def check_arm(n):
    n=str(n)
    power=len(n)
    m=0
    for i in range(power):
        m+=int(n[i])**power
    return m
print(check_arm(135))
