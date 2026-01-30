# It's another statement, but it does exactly the same thing as the switch
color = 'rose'
match color:
    case 'red': print("red")
    case 'green': print("green")
    case _: print("Not in switch") # Default case