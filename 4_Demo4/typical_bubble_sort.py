import random
import time

def generate_random_list(n):
    #want to do random swaps 2n times 
    start_list = list(range(1, n+1))
    for i in range(2*n): 
        # pick a random index 
        randIndex1 = random.randint(0, n-1)
        randIndex2 = random.randint(0, n-1)
        # swap the elements at the random indices 
        start_list[randIndex1], start_list[randIndex2] = start_list[randIndex2], start_list[randIndex1]
    return start_list


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr) 
                time.sleep(0.1)


if __name__ == "__main__":
    n = 10 
    randomList = generate_random_list(n)
    print(f"Original list: {randomList}")
    bubble_sort(randomList)
    print(f"Sorted list: {randomList}")






