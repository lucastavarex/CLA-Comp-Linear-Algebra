from cla import adaptive_simpson_method, gauss_quadrature
import math

class Task1:
    def __init__(self):
        print("╔══════════════════════════════════════════╗")
        print("║       Computacional Linear Algebra       ║")
        print("║         Professor: Luis Sagrilo          ║")
        print("║                                          ║")
        print("║          P2 - Lista 5 - Task 1           ║")
        print("║                                          ║")
        print("║ Student1: Thiago Dias   | DRE: 119019790 ║")
        print("║ Student2: Lucas Tavares | DRE: 120152739 ║")
        print("║                                          ║")
        print("║                   2023.1                 ║")
        print("╠══════════════════════════════════════════╣")
        print("║                                          ║")
        print("║       Welcome to our program, Tchê!      ║")
        print("║                                          ║")
        print("╚══════════════════════════════════════════╝")
        print("")

    def exercise_5(self):
        print("Exercício 5")

        def f(x):
            return 1 / (1 + x**2)

        results, iterations, integration_points = adaptive_simpson_method(
            f, 0, 3
        ).values()

        print("\tIterações: ", iterations)
        print("\tPontos de integração: ", integration_points)
        print("\tResultados: ", results)
        print("")

    def exercise_6(self):
        print("Exercício 6")

        def S_sigma(x):
            return 2 / ((1 - x**2) ** 2 + (x / 10) ** 2)

        def m0(x):
            return S_sigma(x)

        def m2(x):
            return x**2 * S_sigma(x)

        simpson_results = adaptive_simpson_method(m0, 0, 10)["results"]
        print("\tFunção m0 - Regra de Simpson: ", simpson_results[-1])

        gauss_result = gauss_quadrature(m0, 0, 10, points=11)
        print("\tFunção m0 - Método da Quadratura de Gauss (11 pontos): ", gauss_result)

        simpson_results = adaptive_simpson_method(m2, 0, 10)["results"]
        print("\tFunção m2 - Regra de Simpson: ", simpson_results[-1])

        gauss_result = gauss_quadrature(m2, 0, 10, points=11)
        print("\tFunção m2 - Método da Quadratura de Gauss (11 pontos): ", gauss_result)

        print("")

    def exercise_7(self):
        print("Exercício 7")

        def S_n(x):
            return (
                4
                * math.pi**3
                * 3**2
                * math.exp(-16 * math.pi**3 / (x**4 * 5**4))
                / (x**5 * 5**4)
            )

        def S_sigma(x):
            return 1 / ((1 - x**2) ** 2 + (x / 10) ** 2) * S_n(x)

        def m0(x):
            return S_sigma(x)

        def m2(x):
            return x**2 * S_sigma(x)

        simpson_results = adaptive_simpson_method(m0, 0.01, 10)["results"]
        print("\tFunção m0 - Regra de Simpson: ", simpson_results[-1])

        gauss_result = gauss_quadrature(m0, 0.01, 10, points=11)
        print("\tFunção m0 - Método da Quadratura de Gauss (11 pontos): ", gauss_result)

        simpson_results = adaptive_simpson_method(m2, 0.01, 10)["results"]
        print("\tFunção m2 - Regra de Simpson: ", simpson_results[-1])

        gauss_result = gauss_quadrature(m2, 0.01, 10, points=11)
        print("\tFunção m2 - Método da Quadratura de Gauss (11 pontos): ", gauss_result)

        print("")


task1 = Task1()
task1.exercise_5()
task1.exercise_6()
task1.exercise_7()