import os

def scan_file(file_path, file_type):
    with open(file_path, 'r') as f:
        content = f.read()
    potential_vulnerabilities = []
    if file_type == 'python':
        if 'os.system(' in content:
            potential_vulnerabilities.append('Potential command injection vulnerability detected.')
        if 'pickle.loads(' in content:
            potential_vulnerabilities.append('Potential pickle deserialization vulnerability detected.')
        if 'subprocess.run(' in content:
            potential_vulnerabilities.append('Potential command injection vulnerability detected.')
        if 'eval(' in content:
            potential_vulnerabilities.append('Potential eval vulnerability detected.')
        if 'exec(' in content:
            potential_vulnerabilities.append('Potential command injection vulnerability detected.')
        if 'open(' in content:
            potential_vulnerabilities.append('Potential path traversal vulnerability detected.')
        if 'input(' in content:
            potential_vulnerabilities.append('Potential input validation vulnerability detected.')
        if 'shlex.split(' in content:
            potential_vulnerabilities.append('Potential shell injection vulnerability detected.')
        if '__import__(' in content:
            potential_vulnerabilities.append('Potential code injection vulnerability detected.')
        if 'file.write(' in content:
            potential_vulnerabilities.append('Potential file write vulnerability detected.')
        if 'file.read(' in content:
            potential_vulnerabilities.append('Potential file read vulnerability detected.')
        if 'subprocess.Popen(' in content:
            potential_vulnerabilities.append('Potential command injection vulnerability detected.')
        if 'subprocess.call(' in content:
            potential_vulnerabilities.append('Potential command injection vulnerability detected.')
        if 'subprocess.Popen(' in content:
            potential_vulnerabilities.append('Potential command injection vulnerability detected.')
        if 'pickle.load(' in content:
            potential_vulnerabilities.append('Potential pickle deserialization vulnerability detected.')
        if 'sqlite3.connect(' in content:
            potential_vulnerabilities.append('Potential SQL injection vulnerability detected.')
        if 'MySQLdb.connect(' in content:
            potential_vulnerabilities.append('Potential SQL injection vulnerability detected.')
    elif file_type == 'javascript':
        if 'eval(' in content:
            potential_vulnerabilities.append('Potential eval vulnerability detected.')
        if 'document.write(' in content:
            potential_vulnerabilities.append('Potential XSS vulnerability detected.')
        if 'innerHTML' in content:
            potential_vulnerabilities.append('Potential XSS vulnerability detected.')
        if 'setTimeout(' in content:
            potential_vulnerabilities.append('Potential script injection vulnerability detected.')
        if 'setInterval(' in content:
            potential_vulnerabilities.append('Potential script injection vulnerability detected.')
        if 'Function(' in content:
            potential_vulnerabilities.append('Potential code injection vulnerability detected.')
        if 'new Function(' in content:
            potential_vulnerabilities.append('Potential code injection vulnerability detected.')
        if 'document.cookie=' in content:
            potential_vulnerabilities.append('Potential cookie manipulation vulnerability detected.')
        if 'location=' in content:
            potential_vulnerabilities.append('Potential URL manipulation vulnerability detected.')
        if 'history.replaceState(' in content:
            potential_vulnerabilities.append('Potential URL manipulation vulnerability detected.')
        if 'window.location.replace(' in content:
            potential_vulnerabilities.append('Potential URL manipulation vulnerability detected.')
    elif file_type == 'php':
        if 'exec(' in content:
            potential_vulnerabilities.append('Potential command injection vulnerability detected.')
        if 'shell_exec(' in content:
            potential_vulnerabilities.append('Potential command injection vulnerability detected.')
        if 'eval(' in content:
            potential_vulnerabilities.append('Potential eval vulnerability detected.')
        if 'assert(' in content:
            potential_vulnerabilities.append('Potential code injection vulnerability detected.')
        if 'file_put_contents(' in content:
            potential_vulnerabilities.append('Potential file write vulnerability detected.')
        if 'file_get_contents(' in content:
            potential_vulnerabilities.append('Potential file read vulnerability detected.')
        if 'include(' in content:
            potential_vulnerabilities.append('Potential LFI vulnerability detected.')
        if 'require(' in content:
            potential_vulnerabilities.append('Potential LFI vulnerability detected.')
        if 'header(' in content:
            potential_vulnerabilities.append('Potential header injection vulnerability detected.')
        if 'setcookie(' in content:
            potential_vulnerabilities.append('Potential cookie manipulation vulnerability detected.')
        if 'mysqli_query(' in content:
            potential_vulnerabilities.append('Potential SQL injection vulnerability detected.')
        if 'mysql_query(' in content:
            potential_vulnerabilities.append('Potential SQL injection vulnerability detected.')
      
    elif file_type == 'sql':
        if 'SELECT *' in content.upper():
            potential_vulnerabilities.append('Potential SQL injection vulnerability detected.')
        if 'DELETE' in content.upper():
            potential_vulnerabilities.append('Potential SQL injection vulnerability detected.')
        if 'UPDATE' in content.upper():
            potential_vulnerabilities.append('Potential SQL injection vulnerability detected.')
        if 'INSERT INTO' in content.upper():
            potential_vulnerabilities.append('Potential SQL injection vulnerability detected.')
    return potential_vulnerabilities

def main():
    file_path = input('Enter the path to the file: ')
    file_type = input('Enter the type of code in the file (python, javascript, php, sql): ')
    while not os.path.isfile(file_path):
        file_path = input('Invalid path. Enter the path to the file: ')

          
    potential_vulnerabilities = scan_file(file_path, file_type)
    if potential_vulnerabilities:
        print('Potential vulnerabilities detected:')
        for vulnerability in potential_vulnerabilities:
            print('- ' + vulnerability)
    else:
        print('No potential vulnerabilities detected.')

if __name__ == '__main__':
    main()
