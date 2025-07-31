def is_balanced(expression):
    """Revisa si una expresión está balanceada"""
    stack = []
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    escape = False  # Manejar caracteres escapados
    
    for i, char in enumerate(expression):
        if escape:
            escape = False
            continue
        
        if char == '\\':
            escape = True
            continue
        
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != matching_pairs[char]:
                return False
            stack.pop()
        print(stack)
    
    return len(stack) == 0

def check_file_expressions(filename):
    """Lee un archivo y revisa el balanceo de las ecuaciones"""
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if line:  # Skip empty lines
                    if is_balanced(line):
                        print(f"Línea {line_num}: Balanceada - '{line}'")
                    else:
                        print(f"Línea {line_num}: No balanceada - '{line}'")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    filename = input("Nombre del archivo: ")
    check_file_expressions(filename)