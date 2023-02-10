if __name__=="__main__":
    import random

    list = []

    random_numbers = int(input("enter the number of numbers you want to see randomly: "))

    for i in range (random_numbers):
        list.append(random.randrange(10000))


    print(list)