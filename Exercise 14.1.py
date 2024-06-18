def sed(pattern, replacement, input_filename, output_filename):
    try:
        # Open the input file and read the contents
        with open(input_filename, 'r') as file_input:
            content = file_input.read()

        # Replace the pattern with the replacement string
        updated_content = content.replace(pattern, replacement)

        # Write the updated content to the output file
        with open(output_filename, 'w') as file_output:
            file_output.write(updated_control)

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    # Example usage of the sed function
    sed('hello', 'world', 'test.txt', 'output.txt')
