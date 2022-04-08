print()
print("Welcome to the fence calculator.")
print()

def num_check(question):
    valid = False
    while not valid:

        error = ("Please enter a number that is more than zero")

        try:

            response = float(input(question))
            
            if response > 0:
                return response

            else:
                print(error)
                print()
        
        except ValueError:
            print(error)


keep_going = ""
while keep_going == "":
    

    width = num_check("width: ")
    length = num_check("length: ")
    cost_per_meter = num_check("cost per meter: ")

    perimeter = 2 * (width + length)
    fence_cost = (perimeter * cost_per_meter)
    print()

    print("perimeter:5 {} units".format(perimeter))
    print("fence cost: ${:.2f}".format(fence_cost))
    print()
    
    keep_going = input("Press <enter> to keep going or any key to quit")

print()
print("Thanks for using the fence calculator")
print()