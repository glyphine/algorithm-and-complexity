def dynamic_programming(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    inc = [1] * n
    dec = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < dec[j] + 1:
                inc[i] = dec[j] + 1
            elif arr[i] < arr[j] and dec[i] < inc[j] + 1:
                dec[i] = inc[j] + 1
    
    max_length = max(max(inc), max(dec))
    
    return max_length

def process_test_case(arr):
    length = dynamic_programming(arr)
    return length

def main():
    arr = list(map(int, input("Input: ").split()))
    result = process_test_case(arr)
    
    print(f"Length of the longest alternating subsequence: {result}")

if __name__ == "__main__":
    main()
