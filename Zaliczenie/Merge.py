# Pseudocode :
#
# •    Declare left variable to 0 and right variable to n-1
# •    Find mid by medium formula. mid = (left+right)/2
# •    Call merge sort on (left,mid)
# •    Call merge sort on (mid+1,rear)
# •    Continue till left is less than right
# •    Then call merge function to perform merge sort.


numbers = [13, 24, 27, 15, 35, 36, 29, 49, 41, 37]
l_idx = 0
r_idx = len(numbers) - 1


def mergesort(numbers):
    if len(numbers) > 1:
        mid_idx = len(numbers) // 2
        left = numbers[:mid_idx]
        right = numbers[mid_idx:]
        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[i]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1
        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1


def printlist(numbers):
    for i in range(len(numbers)):
        print(numbers[i], end=" ")
    print()


def main():
    print('Given array is:', end="\n")
    print(numbers)
    mergesort(numbers)
    print('Sorted array is:', end="\n")
    printlist(numbers)


if __name__ == "__main__":
    main()
