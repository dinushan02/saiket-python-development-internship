try:
    with open("sample.txt", "r") as file:
        content = file.read()

    if content == "":
        print("The file is empty!")
    else:
        if "Python" in content:
            modified_content = content.replace("Python", "Java")

            with open("sample.txt", "w") as file:
                file.write(modified_content)

            print("Text replaced and saved successfully!")
        else:
            print("The word 'Python' was not found in the file.")

except FileNotFoundError:
    print("'sample.txt' was not found.")