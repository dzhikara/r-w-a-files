import os


def file_content_and_lines(file_path):  # содержимое файла и количество строк
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        lines = content.split("\n")
    return content, len(lines)


# список файлов в папке
folder_path = (
    "C:/Users/dzhik/OneDrive/Desktop/Py/HW/oop_api/2-open_write_read_file/3/3texts"
)
files = os.listdir(folder_path)
files_with_line_counts = []


for file in files:  # содержимое файлов и количество строк
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        content, line_count = file_content_and_lines(file_path)
        files_with_line_counts.append((file, line_count, content))

# сортировка списка файлов по количеству строк
files_with_line_counts.sort(key=lambda x: x[1])


with open(
    "result.txt", "w", encoding="utf-8"
) as result_file:  # запись содержимого файлов в результирующий файл
    for file_info in files_with_line_counts:
        file_name, line_count, content = file_info
        # служебная информация
        result_file.write(f"{file_name}\n{line_count}\n")
        # содержимое файла
        result_file.write(content)
        result_file.write("\n")
