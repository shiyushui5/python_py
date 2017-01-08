def make_pizza(size,*tips): 
    print("\nmaking a " + str(size) + "-inch pizza with the following toppings: ")
    for tip in tips:
        print("- " + tip)
def make_bing(color,*tips):
    print("\nset a " + color)
    for tip in tips:
        print("-" + tip)
