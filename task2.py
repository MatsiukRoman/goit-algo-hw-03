from random import randint

def get_numbers_ticket(min:int, max:int, quantity:int)->list:
    try:
        if min<1 or max >1000:
            print("The minimum possible number in the set (at least 1) and the maximum possible number (at most 1000).")
            return list()
        elif (max-min)+1 < quantity:
            print(f"The range of the random sequence {(max-min)+1} is less than the value {quantity} of winning numbers!")
            return list()
        elif quantity <= 0 :
            print("Enter the positive value of the winning numbers!")
            return list()   
        else:
            result_array = set()
            while len(result_array) != quantity:
                result_array.add(randint(min, max))
            
            return sorted(list(result_array)) 
    except Exception as e:
        print("Exception: ", e)
        return list()

try:
    lottery_numbers = get_numbers_ticket(10,14,6)
    print("Ваші лотерейні числа:", lottery_numbers)
except Exception as e:
    print("Exception: ", e)
    lottery_numbers = list()
    print("Ваші лотерейні числа:", lottery_numbers)
