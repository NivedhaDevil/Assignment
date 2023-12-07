def generate_pascals_triangle(numRows):
    if numRows == 0:
        return []

    result = [[1]]

    for i in range(1, numRows):
        prev_row = result[-1]
        new_row = [1] + [prev_row[j - 1] + prev_row[j] for j in range(1, i)] + [1]
        result.append(new_row)

    return result

numRows = int(input("Enter the number of rows for Pascal's triangle (1 to 30): "))

if 1 <= numRows <= 30:
    output = generate_pascals_triangle(numRows)
    print(output)
else:
    print("Invalid input. Please enter a number between 1 and 30.")
