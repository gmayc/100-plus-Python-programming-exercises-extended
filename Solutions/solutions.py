# ***Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.***
universe = range(2000, 3200)
seven_not_five = []
for num in universe:
    if num % 7 == 0 and num % 5 != 0:
        seven_not_five.append(num)

print(seven_not_five)


# > **_Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8
# > Then, the output should be:40320_**
def get_factorial(num):
    temp = 0
    while num > 1:
        if temp == 0:
            temp = num * (num-1)
        else:
            temp = temp * (num-1)
        num = num - 1
    return temp


print(get_factorial(8))

# > **_With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8_**

# > **_Then, the output should be:_**

# ```
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# ```


def gen_dict(num):
    out_dict = {}
    for i in range(1, num+1):
        out_dict[i] = i * i
    return out_dict


print(gen_dict(8))


# Question 10

### **Question**

# >***Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.***

# >***Suppose the following input is supplied to the program:***
# ```
# hello world and practice makes perfect and hello world again
# ```
# >***Then, the output should be:***
# ```
# again and hello makes perfect practice world
# ```

# ----------------------

def remove_and_sort(str):
    word_list = str.split()
    filtered_list = list(dict.fromkeys(word_list))
    filtered_list.sort()
    return ' '.join(filtered_list)

remove_and_sort('hello world and practice makes perfect and hello world again')
