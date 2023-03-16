ALPHABETE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input())

def print_row(n):
    print(" ".join(ALPHABETE[:n + 1]) + " ")
def main():
    for i in range(n):
        print_row(i)

if __name__ == "__main__":
    main()