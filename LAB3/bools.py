import numpy as np

a = np.array([True, False, True, False])
b = np.array([True, True, False, False])

def false_(a, b):
    return a * 0  # Zwraca zawsze False (0)

def and_(a, b):
    return a & b  # AND - Zwraca True, tylko gdy oba elementy są True

def or_(a, b):
    return a | b  # OR - Zwraca True, jeśli przynajmniej jeden element jest True

def xor(a, b):
    return a != b  # XOR - Zwraca True, jeśli dokładnie jeden z elementów jest True

def nand(a, b):
    return ~(a & b)  # NAND - Negacja AND, zwraca True, chyba że oba elementy są True

def nor(a, b):
    return ~(a | b)  # NOR - Negacja OR, zwraca True, gdy oba elementy są False

def xnor(a, b):
    return ~(a != b)  # XNOR - Negacja XOR, zwraca True, gdy oba elementy są równe

def implies(a, b):
    return ~a | b  # Implies - Zwraca True, chyba że pierwszy element jest True, a drugi False

def equiv(a, b):
    return a == b  # Equivalence (równość) - Zwraca True, jeśli oba elementy są równe

def not_a(a, b):
    return ~a  # NOT A - Negacja pierwszego elementu

def not_b(a, b):
    return ~b  # NOT B - Negacja drugiego elementu

def a_and_not_b(a, b):
    return a & ~b  # A AND NOT B - Zwraca True, jeśli pierwszy element jest True, a drugi False

def b_and_not_a(a, b):
    return b & ~a  # B AND NOT A - Zwraca True, jeśli drugi element jest True, a pierwszy False

def a_or_not_b(a, b):
    return a | ~b  # A OR NOT B - Zwraca True, jeśli pierwszy element jest True, lub drugi False

def b_or_not_a(a, b):
    return b | ~a  # B OR NOT A - Zwraca True, jeśli drugi element jest True, lub pierwszy False

def a_xor_not_b(a, b):
    return (a != b) & ~b  # A XOR NOT B - Zwraca True, jeśli pierwszy element jest True, a drugi False, lub odwrotnie

def b_xor_not_a(a, b):
    return (a != b) & ~a  # B XOR NOT A - Zwraca True, jeśli drugi element jest True, a pierwszy False, lub odwrotnie

if __name__ == '__main__':
    print('Array a:\n', a, '\n')
    print('Array b:\n', b)
    print('a and b (AND):\n', and_(a, b))
    print('a or b (OR):\n', or_(a, b))
    print('a xor b (XOR):\n', xor(a, b))
    print('a nand b (NAND):\n', nand(a, b))
    print('a nor b (NOR):\n', nor(a, b))
    print('a xnor b (XNOR):\n', xnor(a, b))
    print('a implies b (Implies):\n', implies(a, b))
    print('a equiv b (Equivalence):\n', equiv(a, b))
    print('not a (NOT A):\n', not_a(a, b))
    print('not b (NOT B):\n', not_b(a, b))
    print('a and not b (A AND NOT B):\n', a_and_not_b(a, b))
    print('b and not a (B AND NOT A):\n', b_and_not_a(a, b))
    print('a or not b (A OR NOT B):\n', a_or_not_b(a, b))
    print('b or not a (B OR NOT A):\n', b_or_not_a(a, b))
    print('a xor not b (A XOR NOT B):\n', a_xor_not_b(a, b))
    print('b xor not a (B XOR NOT A):\n', b_xor_not_a(a, b))
