
price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}


def total_cost_shopping():
    my_list=[]
    total_cost = 0
    for key in price_list.keys():
        total_cost = price_list[key] * quantity_list[key]
        print("Therfore the cost is =" + str(total_cost))
        my_list.append(total_cost)#for extra practise to understand how to sum is up using a list
    x=sum(my_list)
    print("Therfore the total cost is =" + str(x)) 
    return x   
    


def cost_of_fruits(fruit, quantity):
    for key in price_list.keys():
        if key == fruit:
            cost = quantity*price_list[key]
            break

    print("cost of ", quantity, fruit, "=", cost)


def main():
    cost_of_fruits('apple', 10)
    print(total_cost_shopping())



if __name__ == "__main__":
    main()