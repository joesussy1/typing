colors = {
    "GREEN": "\033[32m",
    "RED": "\033[31m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[95m",
    "END": "\033[0m"
}

def print_color(statement, color):
    print(colors[color] + statement + colors["END"])