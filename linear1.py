b, c = 0, 0
quad_list = []
s_list = []
a_1 = []


class Solving:
    def __init__(self, seq):
        self.a = seq[0]
        self.b = seq[1]
        self.c = seq[2]
        self.seq = seq

    def solve_linear(self):
        global b
        a = self.b - self.a
        if a > self.a:
            b = a - self.a
            # a_1.append(a)
            # a_1.append(b)
            print(f"{a}n - {b}")
            input()
        elif a < self.b:
            b = self.a - a
            # a_1.append(a)
            # a_1.append(b)
            print(f"{a}n + {b}")
            input()

    def solve_quadratic(self):
        global b, c
        first = self.b - self.a
        second = self.c - self.b
        final = (second - first) / 2
        for i in range(3):
            f = final * ((i + 1) * (i + 1))
            quad_list.append(f)
        for j in range(3):
            lin_out_of = self.seq[j] - quad_list[j]
            s_list.append(lin_out_of)
        # a_1.append(final)
        print(f"{final}n^2 +", end=" ")
        Solving(s_list).solve_linear()

        # Quadratic(a_1).work_out()


class Sqrt:
    def __init__(self, number):
        self.number = number ** 0.5


class Quadratic:
    def __init__(self, a):
        self.a = a[0]
        self.b = a[1]
        self.c = a[2]

    def work_out(self):
        x = ((-1 * self.b) + Sqrt((self.b * self.b) - (4 * self.a * self.c)).number) / (2 * self.a)
        x_1 = ((-1 * self.b) - Sqrt((self.b * self.b) - (4 * self.a * self.c)).number) / (2 * self.a)
        print(x, x_1)


lin_seq = list(map(float, input("Enter a linear or quadratic sequence: ").split()))
if lin_seq[1] - lin_seq[0] != lin_seq[2] - lin_seq[1]:
    print("Quadratic")
    Solving(lin_seq).solve_quadratic()
elif lin_seq[1] - lin_seq[0] == lin_seq[2] - lin_seq[1]:
    print("Linear")
    Solving(lin_seq).solve_linear()

# Quadratic(a_1).work_out()
