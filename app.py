import sys

def main():
    num1 = float(sys.argv[1]) if len(sys.argv) > 1 else 5.0
    num2 = float(sys.argv[2]) if len(sys.argv) > 2 else 10.0
    
    total_sum = num1 + num2
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"The calculated sum is: {total_sum}")

if __name__ == "__main__":
    main()