arr = [1, 2, 3, 4 ,5]
n = len(arr)
def RecSum(arr, n):
    
    if n <= 0:
        return 0
    return RecSum(arr, n - 1) + arr[n - 1]

def arraysum(arr):
    return RecSum(arr, len(arr))

print(arraysum(arr))


#sum of digit
def sum_of_digit( n ):
    if n == 0:
        return 0
    return (n % 10 + sum_of_digit(int(n / 10)))

num = 12345
result = sum_of_digit(num)
print(result)
