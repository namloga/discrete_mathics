from utils import read_file, write_file

PATH = '../txtf/input.txt'
OUT_PATH = '../txtf/output.txt'

def task1(S, R):
    reflexive = all((a,a) in R for a in S)

    symmetric = all((b , a) in R for (a, b) in R)

    transitive = all((a, c) in R for (a, b) in R for (b2, c) in R if b == b2)

    return reflexive,symmetric, transitive

def main():
    input_data = read_file(PATH)
    lines = input_data.strip().split('\n')
    S = list(map(int, lines[0].strip().split()))
    R = [tuple(map(int, line.strip().split())) for line in lines[1:]]
    reflexive, symmetric, transitive = task1(S, R)
    result = f'Reflexive: {reflexive}\n'
    result += f'Symmetric: {symmetric}\n'
    result += f'Transitive: {transitive}\n'
    print(result)

if __name__ == '__main__':
    main()