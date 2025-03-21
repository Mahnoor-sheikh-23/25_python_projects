import random
DONE_LIKELIHOOD = 0.3  # 30% chance of stopping
def choatic_counting():
    for i in range(1,10):
        if done():
            return 
        print(i)


def done():
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    choatic_counting()
    print("I am done..")

if __name__ == "__main__":
    main()

