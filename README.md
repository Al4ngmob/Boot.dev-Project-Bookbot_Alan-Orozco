# Boot.dev-Project-Bookbot_Alan-Orozco
this repository is where i have my bookbot project from boot.dev:

## Bookbot

Bookbot is a command-line Python tool that analyzes `.txt` books and generates a detailed word and character frequency report.

### How to Use

1. Place your `.txt` book files inside the `books/` directory.
2. Run the program from your terminal by passing the file path as an argument:
   ```bash
   python3 main.py <path_to_book>
   ```
   * **Example:** `python3 main.py books/prideandprejudice.txt`

### Features & Behavior

* **Missing File Path Handling**
  * If you run the script without providing a book path, it displays the correct usage instructions and terminates with exit code `1`:
    ```text
    Usage: python3 main.py <path_to_book>
    ```
* **Book Analysis Report**
  * When a valid book path is provided, Bookbot prints a structured report containing:
    * **Book Path:** The file path of the analyzed text.
    * **Total Word Count:** The total number of words found in the book.
    * **Character Frequency Count:**
      * Converts all characters to lowercase so uppercase and lowercase letters are counted together.
      * Counts alphabetical characters only, ignoring spaces, numbers, and punctuation symbols.
      * Displays the results sorted from most frequently used to least frequently used.


[![Boot.dev Build a BookBot in Python certificate](https://qvault-webapp-dynamic-assets.storage.googleapis.com/certificates/ee83b57a-0490-405b-9276-d306f51c645f.jpeg?v=1794782096)](https://www.boot.dev/certificates/ee83b57a-0490-405b-9276-d306f51c645f)
