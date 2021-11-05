N = int(input("please enter an integer"))
even_integers = 0
odd_integers = 0
number_of_even = 0
i: int
for i in range(1, int(N) + 1):
    if i % 2 == 0:
        even_integers += i
        number_of_even += 1
    else:
        odd_integers += i
x = even_integers // number_of_even
y = odd_integers
print("Average of even numbers", x)
print("sum of odd integers", y)