# Week 1 Project: Personal Introduction Program

def main():
    # Welcome banner
    print("-" * 45)
    print(" Welcome to the Personal Introduction Setup ")
    print("-" * 45)

    # 1. Using input() to get user information
    # 2. Using variables to store the answers
    name = input("What is your name? ")
    age = input("How old are you? ")
    hobby = input("What is your favorite hobby? ")
    field_of_study = input("What are you currently studying? ")

    # 3. Using print() and f-strings to display the welcoming message
    print("\n" + "=" * 45)
    print(f"🎉 Welcome {name}! 🎉")
    print(f"It is great to meet you. You are {age} years old and love {hobby}.")
    print(f"Best of luck with your studies in {field_of_study}!")
    print("=" * 45 + "\n")

if __name__ == "__main__":
    main()
