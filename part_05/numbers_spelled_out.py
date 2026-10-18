def dict_of_numbers():
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"] 
    numbers = {}

    for n in range(0, 100):
        if n < 20:
            numbers[n] = ones[n]
        elif n % 10 == 0:
            numbers[n] = tens[n // 10]
        else:
            numbers[n] = tens[n // 10] + "-" + ones[n % 10]
    return numbers
# Write your solution here

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])    # two
    print(numbers[11])   # eleven
    print(numbers[45])   # forty-five
    print(numbers[99])   # ninety-nine
    print(numbers[0])    # zero