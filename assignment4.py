def read_and_modify_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.readlines()

        modified_content = [line.upper() for line in content]

        output_filename = "modified_" + filename

        try:
            with open(output_filename, 'w') as outfile:
                outfile.writelines(modified_content)
            print(f"Modified content written to '{output_filename}' successfully!")
        except IOError:
            print("An error occurred while writing to the new file.")
  
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except IOError:
        print(f"Error: The file '{filename}' could not be read.")

        read_and_modify_file()