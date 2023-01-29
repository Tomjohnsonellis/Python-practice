# Reading in files is a pretty fundamental skill

def get_contents_as_string(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()


def get_contents_as_list(file_path: str) -> list:
    lines = []
    with open(file_path) as file:
        raw_lines = file.readlines()
    for line in raw_lines:
        lines.append(line.rstrip())
    return lines


def reading(path_to_a_readable_file: str) -> None:
    print("We will read a in a file in 2 different ways.")
    print("1. All at once")
    print("---")
    print(type(get_contents_as_string(path_to_a_readable_file)))
    print(get_contents_as_string(path_to_a_readable_file))
    print("---")
    print("2. Line by line")
    print("---")
    print(type(get_contents_as_list(path_to_a_readable_file)))
    for line in get_contents_as_list(path_to_a_readable_file):
        print(line)
    print("---")


def write_to_a_new_file(file_path: str) -> None:
    # "w" is for "write" mode
    with open(file_path, "w") as file:
        file.write("I was written to a file!")
    return


def add_lines_to_file(file_path: str) -> None:
    pass


def writing(path_to_write_a_file_to: str) -> None:
    write_to_a_new_file(path_to_write_a_file_to)
    add_lines_to_file(path_to_write_a_file_to)
    pass


if __name__ == "__main__":
    reading_file_path = "a_folder/a_file_to_read.txt"
    reading(reading_file_path)

    writing_file_path = "a_folder/a_file_to_write.txt"
    writing(writing_file_path)

    #
    # print("Let's open a file!")
    # print("-----")
    #
    #
    # contents = get_contents_as_list(my_file_path)
    # print(type(contents))
    #
    # for line in contents:
    #     print(line)
    #
    # print("-----")
    # print("Great!")
