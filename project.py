import sys
import time

def user():
    name = input(f"Whats Your Name: ")
    return name.strip()


def input_time(name):
    while True:
        try:
            minutes = int(input(f"Enter A Timer {name} From (1-60 Minutes): "))
            if minutes <= 0 or minutes > 60:
                raise ValueError
            print("Timer set for", minutes, "minutes.")
            return minutes
        except ValueError:
            print("Invalid input. Type A Number From 1 To 60 ")
        


def Timer(name, minutes):
    try:
        start = time.time()
        end = start + minutes* 60
        while time.time() < end:
            remaining = int(end - time.time())
            minutes = remaining // 60
            seconds = remaining % 60
            print(f"Time Remaining {name}: {minutes:02d}:{seconds:02d}", end="\r")
        print(f"\nTimes Up. Hope You Enjoy The Rest Of Your Day {name} 😊")
    except KeyboardInterrupt:
        print("\nCancelled To Put Another Time In Type (python project.py) Into The Terminal 😊")



def main():
    name = user()
    minutes = input_time(name)
    Timer(name, minutes)


if __name__ == "__main__":
    main()