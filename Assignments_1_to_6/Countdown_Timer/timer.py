import time

def countdown(t):
    try:
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        print("\nTime's up! 🔔")
    except KeyboardInterrupt:
        print("\nTimer stopped by user! ⏹️")
        return

def main():
    try:
        # Get input from user
        t = input("Enter the time in seconds: ")
        
        # Validate input
        if not t.isdigit():
            print("Please enter a valid positive number!")
            return
        
        t = int(t)
        if t <= 0:
            print("Please enter a time greater than 0!")
            return
            
        print("\nStarting countdown... ⏱️")
        countdown(t)
        
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nProgram exited by user!")

if __name__ == "__main__":
    main()
