def compareTriplets(a, b):
    points_alice = 0
    points_bob = 0
    # Write your code here
    for score_alice, score_bob in zip(a,b):
        print(a,b)
        if score_alice < score_bob:
            points_bob += 1
        elif score_alice > score_bob:
            points_alice += 1
        
    return [points_alice, points_bob]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
