def calculate_weights(string, queries):
    weights = set()

    i = 0
    while i < len(string):
        char_weight = ord(string[i]) - ord('a') + 1
        count = 1  

        weights.add(char_weight)
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count += 1
            char_weight += ord(string[i]) - ord('a') + 1
            weights.add(char_weight)
            i += 1

        i += 1

    result = ["Yes" if q in weights else "No" for q in queries]
    return result

string = input("Masukkan string: ")
queries = list(map(int, input("Masukkan daftar query (dipisahkan dengan spasi): ").split()))

output = calculate_weights(string, queries)
print(output)
