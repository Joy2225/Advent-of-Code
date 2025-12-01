data = list(map(int, open("D11.txt", "r").read().split()))
cache = {}
total = 0  # Variable to keep track of the total length added in iterations
seq_cache = {}

# Function to compute sequence for 25 iterations for a single number
def count_stones_after_blinks(stone, blinks):
    # Use dynamic programming to store results of previous states
    memo = {}

    def process_stone(stone):
        if stone in memo:
            return memo[stone]

        if stone == 0:
            result = [1]
        elif len(str(stone)) % 2 == 0:  # Even number of digits
            digits = str(stone)
            mid = len(digits) // 2
            left, right = int(digits[:mid]), int(digits[mid:])
            result = [left, right]
        else:
            result = [stone * 2024]

        memo[stone] = result
        return result

    def compute_sequence(num):

        sequence = [num]
        for _ in range(blinks):
            next_sequence = []
            for stone in sequence:
                next_sequence.extend(process_stone(stone))
            sequence = next_sequence
        return sequence

    # Compute the new list after all blinks
    final_sequences = compute_sequence(stone)
    return final_sequences
# print(count_stones_after_blinks(84, 25))
# Main processing loop
with open("c.txt", "w") as file:
    for iteration in range(1, 2):
        print(f"Iteration: {iteration}")
        new_data = []  # To store newly added elements in the current iteration
        i = 0
        if iteration <= 2:
            print("Iteration " + str(iteration))
            while i < len(data):
                # file.write(str(i)+"\n")
                element = data[i]
                if element in cache:
                    # Use precomputed sequence from cache
                    # file.write(str(i)+" already "+str(element)+"\n")
                    total += len(cache[element])
                    

                    
                else:
                    # Compute sequence, store in cache
                    file.write(str(i)+" "+str(element)+"\n")
                    expansion = count_stones_after_blinks(element, 25)
                    cache[element] = expansion
                    total += len(expansion)
                    
                new_data.extend(cache[element])
                # with open("b.txt", "w") as fa:
                #     fa.write(' '.join(str(val) for val in (cache[element]))+" ")
                i += 1
        
        # Only consider newly added elements for subsequent iterations
        data = new_data
        with open("b.txt", "w") as f:
            print("writing")
            f.write(' '.join(str(val) for val in data))
        print(len(data))

        print(total)
        with open("a.txt", "w") as f:
            f.write(str(cache)+"\n")




data = list(map(int, open("b.txt", "r").read().split()))
print("len",len(data))
cache = eval(open("a.txt", "r").read())
total = 0  # Variable to keep track of the total length added in iterations
seq_cache = {}

# Function to compute sequence for 25 iterations for a single number
def count_stones_after_blinks(stone, blinks):
    # Use dynamic programming to store results of previous states
    memo = {}

    def process_stone(stone):
        if stone in memo:
            return memo[stone]

        if stone == 0:
            result = [1]
        elif len(str(stone)) % 2 == 0:  # Even number of digits
            digits = str(stone)
            mid = len(digits) // 2
            left, right = int(digits[:mid]), int(digits[mid:])
            result = [left, right]
        else:
            result = [stone * 2024]

        memo[stone] = result
        return result

    def compute_sequence(num):

        sequence = [num]
        for _ in range(blinks):
            next_sequence = []
            for stone in sequence:
                next_sequence.extend(process_stone(stone))
            sequence = next_sequence
        return sequence

    # Compute the new list after all blinks
    final_sequences = compute_sequence(stone)
    return final_sequences

for iteration in range(1, 2):
    print(f"Iteration: {iteration}")
    new_data = []  # To store newly added elements in the current iteration
    i = 0
    if iteration <= 2:
        # print("Iteration " + str(iteration))
        while i < len(data):

            if i%10000 == 0:
                print("i", i)
            element = data[i]
            if element in cache:
                pass
            else:

                expansion = count_stones_after_blinks(element, 25)
                cache[element] = expansion

            j = 0
            # print("Length of cache: ", len(cache[element]))
            while j < len(cache[element]):
                # print(j, cache[element][j])
                ele = cache[element][j]
                if ele in cache:
                    # Use precomputed sequence from cache
                    total += len(cache[ele])

                else:
                    # Compute sequence, store in cache
                    expansion = count_stones_after_blinks(ele, 25)
                    cache[ele] = expansion
                    total += len(expansion)
                    # new_data.extend(expansion)
                j += 1
            # print(total)
            i += 1
    
    print(len(data))

    print(total)
    # Ans :- 241394363462435
    with open("total.txt", "w") as f:
        f.write(str(total)+"\n")