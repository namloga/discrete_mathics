from utils import read_file, write_file

PATH = '../txtf/input.txt'
OUT_PATH = '../txtf/output.txt'


def is_derangement(remaining_elements, remaining_indices):
    return all(remaining_elements[i] != remaining_indices[i] + 1 for i in range(len(remaining_elements)))

def combinations(arr, k):
    result = []
    n = len(arr)

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n):
            backtrack(i + 1, path + [arr[i]])

    backtrack(0, [])
    return result

def permutations(arr):
    result = []

    def backtrack(path, used):
        if len(path) == len(arr):
            result.append(path[:])
            return
        for i in range(len(arr)):
            if not used[i]:
                used[i] = True
                path.append(arr[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

    backtrack([], [False] * len(arr))
    return result

def solve(n, k):
    arr = list(range(1, n + 1))
    results = []

    for fix_idx in combinations(range(n), k):
        fix_set = set(fix_idx)

        rem_idx = [i for i in range(n) if i not in fix_set]
        rem_vals = [arr[i] for i in rem_idx]

        for perm in permutations(rem_vals):
            if is_derangement(perm, rem_idx):
                tmp = arr[:]
                for i in fix_idx:
                    tmp[i] = arr[i]
                for i, j in enumerate(rem_idx):
                    tmp[j] = perm[i]
                results.append(' '.join(map(str, tmp)))

    return results

def main():
    # Чтение данных из файла
    input_data = read_file(PATH)
    data = list(map(int, input_data.strip().split()))
    n = data[0]
    k = data[1]

    result = solve(n, k)

    # Запись результатов в файл
    write_file(OUT_PATH, '\n'.join(result))

    print("Результаты были записаны в файл output.txt")


if __name__ == "__main__":
    main()
