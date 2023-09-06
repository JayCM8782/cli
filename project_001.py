Project_001.py

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def main():
    num = int(input("Tell me a number: "))
    print(f"The answer is {factorial(num)}.")

if __name__ == "__main__":
    main()

my_function()

