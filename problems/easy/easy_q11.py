#
def day_of_week(day):
    switch = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if day < 1 or day > 7:
        return "Invalid day"
    return switch[day]
if __name__ == "__main__":
    xcd = day_of_week(32)
    print(xcd)

    
    
