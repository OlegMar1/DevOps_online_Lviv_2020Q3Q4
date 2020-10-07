#FizBuz function

def FizzBuzz_test(i):
    if (((i % 3) == 0) & ((i % 5) == 0)):
        return (str(i) + "\tFizzBuzz")

    elif ((i % 3) == 0):
        return(str(i) + "\tFizz")

    elif ((i % 5) == 0):
        return(str(i) + "\tBuzz")

    else:
        return i


for i in range(100):
    print(FizzBuzz_test(i + 1))