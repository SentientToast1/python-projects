# def square(n):
#     return n**2

# origList = list(map(int,input().split()))

# evenList = list(filter(lambda x : x%2==0,origList))

# squareList = list(map(square, evenList))
# print(f'Original list:\n{origList}')
# print(f'Even numbers list:\n{evenList}')
# print(f'Squares List:\n{squareList}')


# numbers = list(map(int, input().split()))
# triplets = [(a, b, c) for a in numbers for b in numbers for c in numbers]
# is_pythagorean = lambda triplet: triplet[0]**2 + triplet[1]**2 == triplet[2]**2
# valid_triplets = list(filter(is_pythagorean, triplets))
# print("Valid Pythagorean Triplets:", valid_triplets)