"""Copy-file-content"""
first_file = open("file_1.txt")
copy_file = open("file_2.txt", "w+")

content = first_file.read()
copy_file.write(content)
copy_file.seek(0)
copy_content = copy_file.read()

print(copy_content)

first_file.close()
copy_file.close()
