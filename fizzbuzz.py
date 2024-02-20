

def solve(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n



if __name__ == "__main__":
    n = int(input("Please enter a number: "))
    print(solve(n))