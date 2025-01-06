from utils import read_file, write_file
from collections import defaultdict

PATH = '../txtf/input.txt'
OUT_PATH = '../txtf/output.txt'

def check_transitive(S, R):
    R_set = set(R)
    forward_map = defaultdict(set)

    for a, b in R:
        if a != b:
            forward_map[a].add(b)

    for a, b in R:
        if a == b:
            continue
        for c in forward_map.get(b, []):
            if a != c and (a, c) not in R_set:
                return False

    return True



def check_anti_transitive(S, R):
    R_set = set(R)
    forward_map = defaultdict(set)

    for a, b in R:
        if a != b:
            forward_map[a].add(b)

    for a, b in R:
        if a == b:
            continue
        for c in forward_map.get(b, []):
            if a != c and (a, c) in R_set:
                return False

    return True

def task1(S, R):
    R_set = set(R)

    # Рефлексивность
    reflexive = all((a, a) in R_set for a in S)
    anti_reflexive = all((a, a) not in R_set for a in S)
    not_reflexive = not reflexive and not anti_reflexive

    # Симметричность
    symmetric = all((b, a) in R_set for (a, b) in R_set)
    asymmetric = all((b, a) not in R_set for (a, b) in R_set if a != b)
    anti_symmetric = all((b, a) not in R_set or a == b for (a, b) in R_set)
    not_symmetric = not symmetric and not anti_symmetric

    # Транзитивность
    transitive = check_transitive(S, R)
    anti_transitive = check_anti_transitive(S, R)
    not_transitive = not transitive and not anti_transitive

    return {
        "Reflexive": reflexive,
        "Anti-reflexive": anti_reflexive,
        "Not-reflexive": not_reflexive,
        "Symmetric": symmetric,
        "Asymmetric": asymmetric,
        "Anti-symmetric": anti_symmetric,
        "Not-symmetric": not_symmetric,
        "Transitive": transitive,
        "Anti-transitive": anti_transitive,
        "Not-transitive": not_transitive
    }


def main():
    # Чтение данных из файла
    input_data = read_file(PATH)
    lines = input_data.strip().split('\n')

    S = list(map(int, lines[0].strip().split()))
    R = [tuple(map(int, line.strip().split())) for line in lines[1:]]

    properties = task1(S, R)

    # Запись результатов в файл
    result = '\n'.join(f"{prop}: {value}" for prop, value in properties.items())
    write_file(OUT_PATH, result)

    print("Результаты были записаны в файл output.txt")


if __name__ == '__main__':
    main()
