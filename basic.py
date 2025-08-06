def leastsquare():
    x_values = list(map(int, input("Enter all x coordinates separated by commas: ").split(",")))
    y_values = list(map(int, input("Enter all y coordinates separated by commas: ").split(",")))

    if len(x_values) == len(y_values):
        print(x_values)
        print(y_values)
        
    else:
        print("Error. Input again.")
        leastsquare()
        
leastsquare()