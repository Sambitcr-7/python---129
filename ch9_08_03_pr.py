for i in range(2,21):
    with open(f"table/Multiplication_table_of_{i}", 'w') as f:
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}")
    break        