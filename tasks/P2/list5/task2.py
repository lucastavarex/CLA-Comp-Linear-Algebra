from cla import central_derivative, forward_derivative, backward_derivative, richard_extrapolation, second_derivative
import math

class Task2:
    def __init__(self):
        print("╔══════════════════════════════════════════╗")
        print("║       Computacional Linear Algebra       ║")
        print("║         Professor: Luis Sagrilo          ║")
        print("║                                          ║")
        print("║          P2 - Lista 5 - Task 2           ║")
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

    def f1(self, x):
            return x**3 + math.exp(-x)
    def f2(self, x):
        return x ** (1 / 3) + math.log(x)
    def f3(self, x):
        return 1 - math.exp(-((x / 5) ** 2))

    def exercise_1(self):
        print("Exercício 1 - Diferenciação numérica")
        
        for f, x, analytical_value in [(self.f1, 3, 26.9502), (self.f2, 2, 0.709987), (self.f3, 6, 0.113725)]:
            print(f"\t{f.__name__}) Valor analítico: {analytical_value}")
            for derivation_function in [central_derivative, forward_derivative, backward_derivative]:
                for delta in [0.1, 0.001]:
                    print(f"\t    {derivation_function.__name__} (∆x={delta}): {derivation_function(f, x, delta)}")
            print("")

    def exercise_2(self):
        print("Exercício 2 - Extrapolador de Richardson")
        
        for f, x, analytical_value in [(self.f1, 3, 26.9502), (self.f2, 2, 0.709987), (self.f3, 6, 0.113725)]:
            print(f"\t{f.__name__}) Valor analítico: {analytical_value}")
            for derivation_function in [central_derivative, forward_derivative, backward_derivative]:
                for delta in [0.1, 0.001]:
                    print(f"\t    {derivation_function.__name__} (∆x={delta}): {richard_extrapolation(f, x, delta, 1, derivation_function)}")
            print("")

    def exercise_3(self):
        print("Exercício 2 - Extrapolador de Richardson")

        for f, x, analytical_value in [(self.f1, 3, 18.04979), (self.f2, 2, -0.31999), (self.f3, 6, -0.03563)]:
            print(f"\t{f.__name__}) Valor analítico: {analytical_value}")
            for delta in [0.1, 0.001]:
                print(f"\t    (∆x={delta}): {second_derivative(f, x, delta, forward_derivative)}")
            print("")
    
task2 = Task2()
task2.exercise_1()
task2.exercise_2()
task2.exercise_3()