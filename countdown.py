import time

# Define the countdown function
def countdown(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  # overwrite the line every second
        time.sleep(1)
        t -= 1

    print("⏰ Time's up!")

# Ask the user to enter the time in seconds
t = input("Enter the time in seconds: ")

# Call the countdown function with the input converted to int
countdown(int(t))
