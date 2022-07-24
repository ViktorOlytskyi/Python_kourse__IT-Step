import re

pattern = re.compile(
    r"^([0]?[1-9]|[1|2][0-9]|[3][0|1])[./-]([0]?[1-9]|[1][0-2])[./-]([0-9]{4}|[0-9]{2}) ([01]?[0-9]|[2][0-3]:[0-5][0-9]) (Description:) (need [a-z A-Z]+)$")
text = input("Input in format \"24/02/2001 23:12 Description: need....\" \n")

test = "24/02/2001 23:12 Description: need go to school"
if (re.match(pattern, text)):
    result = list(pattern.findall(text)[0])

    if (result[1] == "01"):
        month = "Jan"
    elif (result[1] == "02"):
        month = "Feb"
    elif (result[1] == "03"):
        month = "Mar"
    elif (result[1] == "04"):
        month = "Apr"
    elif (result[1] == "05"):
        month = "May"
    elif (result[1] == "06"):
        month = "Jun"
    elif (result[1] == "07"):
        month = "Jul"
    elif (result[1] == "08"):
        month = "Aug"
    elif (result[1] == "09"):
        month = "Sept"
    elif (result[1] == "10"):
        month = "Oct"
    elif (result[1] == "11"):
        month = "Nov"
    elif (result[1] == "12"):
        month = "Dec"
    else:
        print("Hm...  Smth go wrong :(")

    print(
        f"Your message on {result[0]}/{month}/{result[2]} at {result[3]} oc. can be written\nYour {result[4]} {result[5]}")
else:
    print("Error, Input must be in format \"24/02/2001 23:12 Description: need....\"\n")
