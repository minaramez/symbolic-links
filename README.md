# Symbolic Links Script

Symbolic links are commonly used in Linux systems to provide easy access to files or maintain different versions of the same library. They can be thought of as similar to shortcuts in Windows. This scripting exercise aims to familiarize you with the commands used to find and create symbolic links and their associated target paths. Both Bash and Python commands can be used in the script.

## Usage

1. Ensure that you have a Linux system with Bash and Python installed.
2. Open a terminal and navigate to the directory where the script is located.
3. Run the script using the following command:

   ```shell
   python3 symbolic_links_script.py
   ```

4. The script will display a menu with the following options:

   - Create symbolic link (Option 1)
   - Delete symbolic link (Option 2)
   - Generate summary report (Option 3)

5. Enter the corresponding number for the operation you want to perform.
6. Follow the prompts and provide the required inputs based on the selected option.
7. The script will execute the chosen operation and display the result.

   - If the operation is successful, it will provide relevant information or a success message.
   - If the operation fails, it will display an error message.

8. After viewing the result, you can choose another operation or exit the script by typing 'quit'.

**Note:** Make sure to refer to the man pages and Python documentation to find the syntax needed for the various commands.

## Script Details

The script utilizes the following:

- Bash commands
- Python commands

The script consists of the following functions:

- `create_symbolic_link()`: Allows the user to create a symbolic link. It prompts for a filename or path and checks if the file exists in the specified directory. If the file is found, it asks for confirmation to proceed and creates the symbolic link using the appropriate command (`ln -s` in Bash or `os.symlink` in Python).
- `delete_symbolic_link()`: Allows the user to delete a symbolic link. It prompts for the filename of the symbolic link and checks if it exists in the `/home` directory. If the symbolic link is found, it asks for confirmation to proceed and deletes the symbolic link using the appropriate command (`rm` in Bash or `os.remove` in Python).
- `generate_summary_report()`: Generates a summary report of symbolic links in the `/home` directory. It extracts the list of symbolic links, summarizes them in a table format with the link number, symbolic link name, and target path.

**Note:** The script uses the `os` module in Python for system-related operations and the `clear` command to clear the terminal screen.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
