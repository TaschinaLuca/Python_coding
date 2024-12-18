import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import texttable

table = texttable.Texttable()
x = np.linspace(-100, 100, 100)
f = np.zeros([100, len(x)])
e = 2.71828

def Function(x) -> float:
    return e ** (- x * x)

f[1, :] = Function(x)
matplotlib.pyplot.text(-5, 4, "The graph of the given function", fontdict=None, fontsize = 12)
plt.plot(x, f[1], "--", label=r"$f_" + "(x)$", )

distance_between_intervals = 1

table.add_row(["The length of the intervals", "Approximating the area under the curve using the trapezium rule",
               "Approximating the area under the curve using the rectangle rule"])

for i in range(7):
    distance_between_intervals *= 0.5
    area_under_the_curve_using_trapezium_rule = 0
    area_under_the_curve_using_rectangle_rule = 0
    a = -10

    while a <= 10:
        area_under_the_curve_using_trapezium_rule += distance_between_intervals * (Function(a) + Function(a + distance_between_intervals)) / 2
        area_under_the_curve_using_rectangle_rule += distance_between_intervals * Function(a)
        a += distance_between_intervals

    table.add_row([distance_between_intervals, area_under_the_curve_using_trapezium_rule, area_under_the_curve_using_rectangle_rule])

table.add_row(["", "", ""])
table.add_row(["Sqrt(π)", 1.772, ""])
print(table.draw())
plt.grid()
plt.xlim((-10, 10))
plt.ylim(-5, 5)
plt.show()

