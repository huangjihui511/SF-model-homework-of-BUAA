import matplotlib.pyplot as plt
a = 1
while a <= 10:

    b = plt.scatter(a, a ** 2, color='r', label="A")
    plt.pause(0.1)
    if a == 1:
        plt.legend()
    a = a + 1

plt.show()