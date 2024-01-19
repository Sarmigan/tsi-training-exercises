if __name__ == '__main__':
    #################
    ## Exercise 1  ##
    #################
    # print("Hello my name is Sarmigan!")
    # print("I like making music and going to the gym.")
    
    #################
    ## Exercise 2  ##
    #################
    # name = "Sarmigan"
    # age = 22

    # print(f"Hello my name is {name} and I am {age} years old!")

    #################
    ## Exercise 3  ##
    #################
    # variables = [14,
    #              "Y",
    #              "Hello!",
    #              2.5,
    #              307,
    #              -1,
    #              438000000,
    #              False]

    # for var in variables:
    #     print(type(var))

    #################
    ## Exercise 4  ##
    #################
    # print(10 * 5)
    # print(10 / 5)
    # x = 10
    # X = x + 1
    # x = 10
    # x += 5

    #################
    ## Exercise 5  ##
    #################
    # x = 50
    # y = 10

    # if x > y:
    #     print("Greater")

    #################
    ## Exercise 6  ##
    #################
    # x = 50
    # y = 50

    # if x == y:
    #     print("Equal")

    #################
    ## Exercise 7  ##
    #################
    # x = 50
    # y = 50

    # if x == y:
    #     print("Equal")
    # else:
    #     print("Unequal")

    #################
    ## Exercise 8  ##
    #################
    # x = 51
    # y = 49

    # x = 50
    # y = 50

    # if x == y:
    #     print("1")
    # elif x > y:
    #     print("2")
    # else:
    #     print("3")

    # x = 57
    # y = 50

    # if x == y:
    #     print("1")
    # elif x > y:
    #     print("2")
    # else:
    #     print("3")

    # x = 5
    # y = 50

    # if x == y:
    #     print("1")
    # elif x > y:
    #     print("2")
    # else:
    #     print("3")

    #################
    ## Exercise 9  ##
    #################
    # day = 2

    # match day:
    #     case 1:
    #         print("Saturday")
    #     case 2:
    #         print("Sunday")

    #################
    ## Exercise 10  ##
    #################
    # day = 4

    # match day:
    #     case 1:
    #         print("Saturday")
    #     case 2:
    #         print("Sunday")
    #     case _:
    #         print("Weekday")

    #################
    ## Exercise 11 ##
    #################
    # i = 0
    # while(i<6):
    #     print(i)
    #     i+=1

    #################
    ## Exercise 12 ##
    #################
    # for i in range(6):
    #     print(i)
    #     if i == 3:
    #         break

    #################
    ## Exercise 13 ##
    #################
    # i = 3
    # while(i<9):
    #     if i == 6:
    #         i+=1
    #         continue
    #     else:
    #         print(i)
    #         i+=1

    #################
    ## Exercise 14 ##
    #################
    # list1 = [1, 2, 3, 4, 5]
    # list2 = ["apple", "banana", "cherry"]

    # for num in list1:
    #     for fruit in list2:
    #         print(f"{num} {fruit}")

    #################
    ## Exercise 15 ##
    #################
    # values = [2, 5, 5, 6, 8, 10, 4, 5]
    # a = 0
    # while(values[a] <= values[a+1]):
    #     print(values[a])
    #     a = a + 1

    #################
    ## Exercise 16 ##
    #################
    # values = [2, 1, 5, 3, 8, 10, 13, 5]
    # b = 0
    # while(b <= values[b]):
    #     print(values[b])
    #     b+=1

    #################
    ## Exercise 17 ##
    #################
    # def getTotal(a, b):
    #     return a+b
    
    # print(getTotal(1, 2))

    #################
    ## Exercise 18 ##
    #################
    # class Car:
    #     def __init__(self, model, color):
    #         self.model = model
    #         self.color = color

    #     def print_info(self):
    #         print("Model: " + self.model)
    #         print("Color: " + self.color)
    
    # if __name__ == "__main__":
    #     my_car = Car("Civic", "Black")
    #     my_car.print_info()

    #################
    ## Exercise 19 ##
    #################
        
    # scores = {
    #     "Jordan": [100, 90, 32],
    #     "Tyrell": [100, 90, 32],
    #     "Henry": [100, 90, 32],
    #     "Jhavin": [100, 90, 32],
    #     "Abbenayan": [100, 90, 32],
    #     "Abel": [100, 90, 32],
    #     "Sarmigan": [100, 90, 32],}

    # for key in scores.keys():
    #     print(f"{key}'s highest score is {max(scores[key])}")

    #################
    ## Exercise 20 ##
    #################
        
    # scores = {
    #     "Jordan": [100, 90, 32],
    #     "Tyrell": [100, 90, 32],
    #     "Henry": [100, 90, 32],
    #     "Jhavin": [100, 90, 32],
    #     "Abbenayan": [100, 90, 32],
    #     "Abel": [100, 90, 32],
    #     "Sarmigan": [100, 90, 32],}
        
    # mean = {key : sum(values)/len(values) for key,values in scores.items()}

    #################
    ## Exercise 21 ##
    #################

    # from collections import deque

    # queue = deque([1, 2, 3, 4])

    # q_len = len(queue)

    # def reverse_queue(queue):
    #     for i in range(q_len // 2):
    #         r_i = q_len-i-1
    #         queue[i], queue[r_i] = queue[r_i], queue[i]

    # reverse_queue(queue)
    # print(queue)

    #################
    ## Exercise 22 ##
    #################

    # from collections import ChainMap

    # def add_to_price_history(history, product, price):
    #     if product in history:
    #         history = history.new_child(dict(history, **{product: price}))
    #     else:
    #         history.maps[0][product] = price

    #     return history

    # history = ChainMap({'apple': 2.5, 'orange': 1.5})

    # history = add_to_price_history(history, 'apple', 3.0)
    # print(history)

    # history = add_to_price_history(history, 'kiwi', 3.0)
    # print(history)

    #################
    ## Exercise 23 ##
    #################

    import json
    import csv

    json_file = open("fruits.json", "r") 

    data = json.load(json_file)

    json_file.close()

    csv_file = open("fruits.csv", "w")
    csv_writer = csv.writer(csv_file)

    index = 0    
    for item in data:
        if index == 0:
            header = item.keys()
            csv_writer.writerow(header)
            index += 1

        csv_writer.writerow(item.values())
    
    csv_file.close()

