# Vulnerability Scanner

This is a Python3 script that scans a file for potential vulnerabilities. It currently supports Python, JavaScript, PHP, and SQL code.

## How to Use

1. Clone this repository on your system or download the ZIP file and extract it.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script with the following command: 

    ```
    python3 main.py
    ```

4. Enter the path to the file you want to scan when prompted.
5. Enter the type of code in the file (python, javascript, php, sql) when prompted.
6. Wait for the script to finish scanning the file.
7. Review the potential vulnerabilities detected, if any.

## Example

Suppose you have a PHP file named `example.php` that contains the following code:

```php
<?php
$username = $_POST['username'];
$password = $_POST['password'];
$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = mysqli_query($conn, $query);
?>
```

You can scan this file for potential vulnerabilities using the script as follows:

1. Open a terminal or command prompt and navigate to the directory containing the script.
2. Run the script with the following command: 

    ```
    python3 main.py
    ```

3. Enter the path to the `example.php` file when prompted.
4. Enter `php` when prompted for the type of code.
5. Wait for the script to finish scanning the file.
6. Review the potential vulnerabilities detected, which should include "Potential SQL injection vulnerability detected.".
