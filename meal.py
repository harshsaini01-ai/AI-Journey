def main():
    time = input("What time is it? ")
    time = convert(time)
    
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <=13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    hours, mins = time.split(":")
    hours = float(hours)
    mins = float(mins)
    return hours + (mins / 60)

if __name__ == "__main__":
    main()