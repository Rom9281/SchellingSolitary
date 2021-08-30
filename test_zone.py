# TEST de la conversion de la martrice en array.

matrix = [[0,1,0],[1,0,0],[1,1,1]]

def get_array(matrix):
    final_array = []
    for line in matrix:
        final_array.extend(line)
    
    return final_array
print("ok")
print(get_array(matrix))

