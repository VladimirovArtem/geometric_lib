\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[russian]{babel}
\usepackage{graphicx}
\usepackage{fontspec}
\usepackage{amsmath}
\usepackage[a4paper,top=2cm,bottom=2cm,left=2cm,right=2cm]{geometry}
\usepackage{hyperref}
\usepackage{listings}
\usepackage{xcolor}
\lstset{
    backgroundcolor=\color{white},
    basicstyle=\ttfamily,
    breaklines=true,
    frame=single,
    keywordstyle=\color{blue},
    commentstyle=\color{green},
    stringstyle=\color{red}
}
\usepackage[russian]{babel}

\title{Руководство по использованию калькулятора}
\author{}
\date{}


\setmainfont{Times New Roman}

\title{Руководство по взаимодействию с калькулятором}
\author{}
\date{}

\begin{document}

\begin{titlepage}
    \thispagestyle{empty}
    \begin{center}
        \textbf{\fontsize{18}{21}\selectfont Министр науки и высшего образования \\ Российской Федерации} \\[1em]
        \textbf{\fontsize{18}{21}\selectfont Федеральное государственное автономное \\ образовательное учреждение высшего образования \\ «Национальный исследовательский университет \\ ИТМО»} \\[1em]
        \includegraphics[width=7cm]{1.jpg} \\[2em]
        \text{\fontsize{18}{21}\selectfont Факультет информационных технологий и программирования} \\ [1em]
        \text{\fontsize{12}{21}\selectfont Лабораторная работа №3.} \\ [1em]
        \vspace{7cm}
        \hfill \textbf{\fontsize{12}{21}\selectfont Выполнил студент группы № M3110} \\ [1em]
        \hfill \text{\fontsize{12}{21}\selectfont Владимиров Артём Андреевич} \\ [1em]
        \vspace{1cm}
        \hfill \textbf{\fontsize{12}{21}\selectfont Проверил: } \\ [1em]
        \hfill \text{\fontsize{12}{21}\selectfont Жуйков Артём Сергеевич} \\ [1em]
        \vspace{2cm}
        \text{Cанкт-Петербург} \\ [1em]
        \text{2024} \\ [1em]

    \end{center}
\end{titlepage}


\maketitle

\section{Как использовать калькулятор}
\begin{enumerate}
    \item Запустите \texttt{python calculate.py}
    \item Введите название фигуры. Доступны: Круг, Квадрат.
    \item Введите функцию: Площадь или Периметр.
    \item Введите размеры фигуры. Радиус для круга, одна сторона для квадрата.
    \item Получите ответ
\end{enumerate}

\section{Математические формулы}

\subsection{Площадь}
\begin{itemize}
    \item Круг:
    $$S = \pi R^2$$
    \item Прямоугольник:
    $$S = ab$$
    \item Квадрат:
    $$S = a^2$$
    \item Треугольник:
    $$S = \sqrt{p \cdot (p-a) \cdot (p-b) \cdot (p-c)}$$
    где $ p $ — полупериметр.
\end{itemize}

\subsection{Периметр}
\begin{itemize}
    \item Круг:
    $$P = 2\pi R$$
    \item Прямоугольник:
    $$P = 2a + 2b$$
    \item Квадрат:
    $$P = 4a$$
    \item Треугольник:
    $$P = a + b + c$$
\end{itemize}

\begin{itemize}
    \item \texttt{calculate.py} — основная программа, которая служит калькулятором для выполнения различных геометрических вычислений. Она принимает на вход параметры фигур и возвращает результаты, такие как площадь, периметр и другие характеристики.

    \item \texttt{circle.py} — модуль, который содержит функции для работы с окружностями. Он позволяет вычислять площадь и периметр окружности, а также выполнять другие операции, связанные с этим геометрическим объектом.

    \item \texttt{square.py} — модуль, предназначенный для работы с квадратами. Он включает функции для вычисления площади и периметра квадрата, а также проверки свойств квадрата.

    \item \texttt{triangle.py} — модуль, который предоставляет функции для работы с треугольниками. Он позволяет вычислять площадь треугольника по различным методам (например, по формуле Герона) и определять периметр треугольника.
\end{itemize}


\begin{document}

\maketitle

\section{Как использовать калькулятор}
\begin{enumerate}
    \item Запустите \texttt{python calculate.py}
    \item Введите название фигуры. Доступны: Круг, Квадрат.
    \item Введите функцию: Площадь или Периметр.
    \item Введите размеры фигуры. Радиус для круга, одна сторона для квадрата.
    \item Получите ответ.
\end{enumerate}

Максим, [25.10.2024 18:39]
\section{Математические формулы}
\subsection{Площадь}
\begin{itemize}
    \item Круг:
    $$S = \pi R^2$$
    \item Прямоугольник:
    $$S = ab$$
    \item Квадрат:
    $$S = a^2$$
    \item Треугольник:
    $$S = \sqrt{p \cdot (p-a) \cdot (p-b) \cdot (p-c)}$$
    где $ p $ — полупериметр.
\end{itemize}

\subsection{Периметр}
\begin{itemize}
    \item Круг:
    $$P = 2\pi R$$
    \item Прямоугольник:
    $$P = 2a + 2b$$
    \item Квадрат:
    $$P = 4a$$
    \item Треугольник:
    $$P = a + b + c$$
\end{itemize}

\begin{itemize}
    \item \texttt{calculate.py} — основная программа, которая служит калькулятором для выполнения различных геометрических вычислений. Она принимает на вход параметры фигур и возвращает результаты, такие как площадь, периметр и другие характеристики.

    \item \texttt{circle.py} — модуль, который содержит функции для работы с окружностями. Он позволяет вычислять площадь и периметр окружности, а также выполнять другие операции, связанные с этим геометрическим объектом.

    \item \texttt{square.py} — модуль, предназначенный для работы с квадратами. Он включает функции для вычисления площади и периметра квадрата, а также проверки свойств квадрата.

    \item \texttt{triangle.py} — модуль, который предоставляет функции для работы с треугольниками. Он позволяет вычислять площадь треугольника по различным методам (например, по формуле Герона) и определять периметр треугольника.
\end{itemize}
\section{Описание программы}

В данной секции представлена программа, которая вычисляет полупериметр и периметр треугольника. Программа состоит из двух функций: \texttt{area} и \texttt{perimeter}.

\subsection{Код программы}

\begin{lstlisting}[language=Python]
def area(a, b, c):
    return (a + b + c) / 2

def perimeter(a, b, c):
    return a + b + c
\end{lstlisting}

\subsection{Описание логики программы}

Данная программа содержит две функции: \texttt{area} и \texttt{perimeter}, которые предназначены для вычисления площади и периметра треугольника соответственно.

\begin{itemize}
    \item Функция \texttt{area(a, b, c)} принимает три аргумента: длины сторон треугольника $a$, $b$ и $c$. Она возвращает полупериметр треугольника, который вычисляется по формуле:
    $$s = \frac{a + b + c}{2}$$
    где $s$ — полупериметр треугольника.

    \item Функция \texttt{perimeter(a, b, c)} также принимает три аргумента: длины сторон треугольника $a$, $b$ и $c$. Она возвращает периметр треугольника, который вычисляется по формуле:
    $$P = a + b + c$$
    где $P$ — периметр треугольника.
\end{itemize}
\section{Описание программы}
\subsection{Код программы}

\begin{lstlisting}[language=Python]
def area(a):
    return a * a

def perimeter(a):
    return 4 * a
\end{lstlisting}

\subsection{Описание логики программы}
\begin{itemize}
    \item Функция \texttt{area(a)} принимает один аргумент: длину стороны квадрата $a$. Она возвращает площадь квадрата, которая вычисляется по формуле:
    $$S = a^2$$
    где $S$ — площадь квадрата.

    \item Функция \texttt{perimeter(a)} также принимает один аргумент: длину стороны квадрата $a$. Она возвращает периметр квадрата, который вычисляется по формуле:
    $$P = 4a$$
    где $P$ — периметр квадрата.
\end{itemize}
\section{Описание программы}
\subsection{Код программы}

\begin{lstlisting}[language=Python]
import math

def area(r):
    return math.pi * r * r

def perimeter(r):
    return 2 * math.pi * r
\end{lstlisting}

\subsection{Описание логики программы}

\begin{itemize}
    \item Функция \texttt{area(r)} принимает один аргумент: радиус круга $r$. Она возвращает площадь круга, которая вычисляется по формуле:
    $$S = \pi r^2$$
    где $S$ — площадь круга, а $\pi$ — математическая константа, равная примерно 3.14159.

    \item Функция \texttt{perimeter(r)} также принимает один аргумент: радиус круга $r$. Она возвращает периметр (длину окружности) круга, который вычисляется по формуле:
    $$P = 2\pi r$$
    где $P$ — периметр круга.
\end{itemize}
\section{Описание программы}
\subsection{Код программы}

\begin{lstlisting}[language=Python]
import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
    assert fig in figs
    assert func in funcs

    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
    calc(fig, func, size)
\end{lstlisting}


\subsection{Описание логики программы}

Данная программа позволяет пользователю вычислять периметр и площадь для двух фигур: круга и квадрата. Программа состоит из следующих компонентов:

\begin{itemize}
    \item Импортируются модули \texttt{circle} и \texttt{square}, которые содержат функции для вычисления периметра и площади соответствующих фигур.

    \item Переменные \texttt{figs} и \texttt{funcs} содержат доступные фигуры и функции, соответственно.

    \item Функция \texttt{calc(fig, func, size)} принимает три аргумента: имя фигуры, имя функции и размеры фигуры. Она проверяет, что фигура и функция находятся в списках доступных фигур и функций, затем вычисляет результат с помощью функции \texttt{eval} и выводит его на экран.

    \item В блоке \texttt{if \_\_name\_\_ == "\_\_main\_\_"} программа запрашивает у пользователя ввод имени фигуры и функции, а также размеров фигуры. Ввод продолжается до тех пор, пока не будут введены корректные значения.

    \item После получения всех необходимых данных вызывается функция \texttt{calc} для выполнения расчета и вывода результата.
\end{itemize}
\end{document}
