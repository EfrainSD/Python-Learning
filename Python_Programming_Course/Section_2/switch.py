# It doesn't exist, but you can create something similar (emulate it) using dictionaries
def getMonth(num):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return months.get(num, "Invalid month")

month = input("Give the number of a month: ")
print(getMonth(int(month)))