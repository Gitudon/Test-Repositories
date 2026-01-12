import matplotlib.pyplot as plt
import math

x = list(range(1, 101))
y1 = [i for i in x]
y2 = [i**2 for i in x]
y3 = [i**3 for i in x]
y4 = [i**4 for i in x]
y5 = [math.log(i) for i in x]
y6 = [i * math.log(i) for i in x]
x_exp_fact = list(range(1, 20))
y7 = [2**i for i in x_exp_fact]
y8 = [math.factorial(i) for i in x_exp_fact]

plt.plot(x, y1, label="O(N)")
plt.plot(x, y2, label="O(N^2)")
plt.plot(x, y3, label="O(N^3)")
plt.plot(x, y4, label="O(N^4)")
plt.plot(x, y5, label="O(log(N))")
plt.plot(x, y6, label="O(Nlog(N))")
plt.plot(x_exp_fact, y7, label="O(2^N)")
plt.plot(x_exp_fact, y8, label="O(N!)")

plt.ylim(0, 1000)
plt.xlabel("N")
plt.ylabel("")
plt.legend()
plt.show()
