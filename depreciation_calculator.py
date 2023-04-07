#Program name: Depreciation assignment
#Student name: Mina Abdelnoor
#Option Group: -
#Input validation which prints an error 
#and reruns the while loop if a string to integer
#conversion failed
while True:
    try:
        desc_of_item = input("Enter the description of the item: ")
        yr_of_purchase = int(input("Enter the year of purchase: "))
        cost = int(input("Enter the cost: $"))
        estimated_life = int(input("Enter the estimated life (in years): "))
        dep_method = int(input("""Enter the value corresponding to the depreciation method you want to use:
1. Straight-Line
2. Double-Declining Balance
Here: """))
        #checks if input is 1 or 2, otherwise an error is printed out
        if dep_method not in (1, 2):
            raise ValueError("Invalid depreciation method selected.")
        break
    except ValueError:
        print("Invalid input. Please try again.")
#performs the straight-line depreciation calculation if dep_method equals 1
if dep_method==1:
    print(f"""Description: {desc_of_item}
Year of purchase: {yr_of_purchase}
Cost: ${cost}
Estimated life of item (years): {estimated_life}
Method of depreciation: Straight Line
""")
    current_value=cost
    total_depreciation=0
    #runs the calculation until the value of estimated_life is met
    for i in range(0,estimated_life):
        depreciation=(1/estimated_life)*cost
        total_depreciation+=depreciation
        print(f"""Value at the beginning of {yr_of_purchase}: ${current_value:.2f}
Amount of depreciation during {yr_of_purchase}: ${depreciation:.2f}
Total depreciation during {yr_of_purchase}: ${total_depreciation:.2f}
""")
        yr_of_purchase+=1
        current_value=current_value-depreciation
#performs the double-decllining balance depreciation calculation if dep_method equals 2
elif dep_method==2:
    print(f"""Description: {desc_of_item}
Year of purchase: {yr_of_purchase}
Cost: ${cost:.2f}
Estimated life of item (years): {estimated_life}
Method of depreciation: Double-Declining Balance
""")
    current_value=cost
    total_depreciation=0
    for i in range(0,estimated_life):
        depreciation=(2/estimated_life)*current_value
        total_depreciation+=depreciation
        #runs a different calculation for the last year
        if i==estimated_life-1:
            depreciation=current_value
            total_depreciation=cost
        print(f"""Value at the beginning of {yr_of_purchase}: ${current_value:.2f}
Amount of depreciation during {yr_of_purchase}: ${depreciation:.2f}
Total depreciation during {yr_of_purchase}: ${total_depreciation:.2f}
""")
        yr_of_purchase+=1
        current_value=current_value-depreciation