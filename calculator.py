import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Калькулятор")
        self.window.geometry("300x400")
        self.window.resizable(False, False)
        
        # Переменные
        self.current_input = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Поле вывода результатов
        result_frame = tk.Frame(self.window, height=50)
        result_frame.pack(fill=tk.X, padx=10, pady=10)
        
        result_label = tk.Label(
            result_frame, 
            textvariable=self.result_var,
            font=("Arial", 20),
            anchor="e",
            bg="white",
            relief="sunken",
            padx=10
        )
        result_label.pack(fill=tk.BOTH, expand=True)
        
        # Клавиши калькулятора
        buttons_frame = tk.Frame(self.window)
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Расположение кнопок
        buttons = [
            ['C', '±', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '']
        ]
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text:  # Пропускаем пустые ячейки
                    if text == '0':
                        btn = tk.Button(
                            buttons_frame, 
                            text=text,
                            font=("Arial", 14),
                            command=lambda t=text: self.button_click(t),
                            height=2
                        )
                        btn.grid(row=i, column=j, columnspan=2, sticky="ew", padx=2, pady=2)
                    else:
                        btn = tk.Button(
                            buttons_frame, 
                            text=text,
                            font=("Arial", 14),
                            command=lambda t=text: self.button_click(t),
                            height=2
                        )
                        btn.grid(row=i, column=j, sticky="ew", padx=2, pady=2)
        
        # Настройка весов строк и столбцов для равномерного распределения
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.grid_columnconfigure(j, weight=1)
    
    def button_click(self, text):
        if text == 'C':
            self.clear()
        elif text == '=':
            self.calculate()
        elif text == '±':
            self.plus_minus()
        elif text == '%':
            self.percentage()
        else:
            self.add_to_input(text)
    
    def add_to_input(self, text):
        if self.current_input == "0" or self.current_input == "Error":
            self.current_input = ""
        
        # Проверка на множественные операторы
        if text in ['+', '-', '*', '/'] and self.current_input and self.current_input[-1] in ['+', '-', '*', '/']:
            self.current_input = self.current_input[:-1] + text
        else:
            self.current_input += text
        
        self.result_var.set(self.current_input)
    
    def clear(self):
        self.current_input = ""
        self.result_var.set("0")
    
    def plus_minus(self):
        if self.current_input and self.current_input != "0":
            if self.current_input[0] == '-':
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
            self.result_var.set(self.current_input)
    
    def percentage(self):
        try:
            if self.current_input:
                value = eval(self.current_input)
                result = value / 100
                self.current_input = str(result)
                self.result_var.set(self.current_input)
        except:
            self.result_var.set("Error")
            self.current_input = ""
    
    def calculate(self):
        try:
            if self.current_input:
                # Заменяем символы для корректного вычисления
                expression = self.current_input.replace('×', '*').replace('÷', '/')
                result = eval(expression)
                self.current_input = str(result)
                self.result_var.set(self.current_input)
        except ZeroDivisionError:
            self.result_var.set("Error: Деление на 0")
            self.current_input = ""
        except:
            self.result_var.set("Error")
            self.current_input = ""
    
    def run(self):
        self.window.mainloop()

# Альтернативная версия калькулятора для консоли
def console_calculator():
    """Простой калькулятор для работы в консоли"""
    print("Консольный калькулятор")
    print("Доступные операции: +, -, *, /, %, ** (степень), sqrt (квадратный корень)")
    print("Введите 'exit' для выхода")
    
    while True:
        try:
            expression = input("\nВведите выражение: ").strip()
            
            if expression.lower() == 'exit':
                break
            
            # Заменяем символы и функции
            expression = expression.replace('^', '**').replace('sqrt', 'math.sqrt')
            
            # Безопасное вычисление
            result = eval(expression, {"__builtins__": None}, {"math": math})
            print(f"Результат: {result}")
            
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль!")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Ошибка: Некорректное выражение!")

# Запуск программы
if __name__ == "__main__":
    print("Выберите тип калькулятора:")
    print("1 - Графический интерфейс")
    print("2 - Консольная версия")
    
    choice = input("Ваш выбор (1 или 2): ")
    
    if choice == "1":
        calc = Calculator()
        calc.run()
    elif choice == "2":
        console_calculator()
    else:
        print("Неверный выбор!")