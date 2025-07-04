def split_and_join(line):
    splited_line = line.split()
    result = "-".join(splited_line)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
