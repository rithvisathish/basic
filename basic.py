def leastsquare():
    x_values = list(map(int, input("Enter all x coordinates separated by commas: ").split(",")))
    y_values = list(map(int, input("Enter all y coordinates separated by commas: ").split(",")))

    if len(x_values) == len(y_values):
        x_mean = sum(x_values) / len(x_values)
        y_mean = sum(y_values) / len (y_values)
        x_mean_values = []
        y_mean_values = []

        for i in range(len(x_values)):
            a = x_values[i] - x_mean
            b = y_values[i] - y_mean
            x_mean_values.append(round(a, 2))
            y_mean_values.append(round(b, 2))
        print(x_mean_values)
        print(y_mean_values)

        products = []
        x_squares = []
        for i in range(len(x_mean_values)):
            a = x_mean_values[i] * y_mean_values[i]
            b = x_mean_values[i]**2
            products.append(a)
            x_squares.append(b)
        
        m = sum(products) / sum(x_squares)
        print(m)
        b = y_mean - (m * x_mean)
        print(b)
        print(f"y = {round(m,2)}x + {round(b,2)}")


    else:
        print("Error. Input again.")
        leastsquare()

        
leastsquare()

