<<<<<<< HEAD
def solve_linear_equation(a1, b1, c1, a2, b2, c2):
    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        # The system has either no solution or infinitely many solutions
        if c1 == c2:
            print("The system has infinitely many solutions.")
        else:
            print("The system has no solution.")
    else:
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        print("The solution is x =", x, "and y =", y)


# Example usage
a1 = 2
b1 = -3
c1 = 7
a2 = 4
b2 = 1
c2 = 9

solve_linear_equation(a1, b1, c1, a2, b2, c2)
=======

>>>>>>> 294c87c0387da2cd342287fc12f43bf6c1c574c7
