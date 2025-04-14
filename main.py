import streamlit as st
import random
import time

# Set page config
st.set_page_config(page_title="Python Quiz Application", page_icon="💻", layout="centered")

# Custom CSS for gradient background
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #ff758c, #ff7eb3);
            color: white;
        }
        .stApp {
            background: linear-gradient(to right, #ff758c, #ff7eb3);
        }
        .stButton > button {
            background-color: #ff4b5c;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stButton > button:hover {
            background-color: #ff1e42;
        }
        .stRadio > div {
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('💻 Python Quiz Application')

# List of Python-related questions
questions = [
    
  {
    "question": "What is the correct way to create a variable in Python to store the value 5?",
    "options": ["int x = 5", "x = 5", "x := 5", "let x = 5"],
    "answer": "x = 5"
  },
  {
    "question": "What will be the output of the following code?\n\nprint(type(3.14))",
    "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'double'>"],
    "answer": "<class 'float'>"
  },
  {
    "question": "Which of the following is used to define a function in Python?",
    "options": ["function myFunc():", "def myFunc():", "func myFunc():", "define myFunc():"],
    "answer": "def myFunc():"
  },
  {
    "question": "Which of the following is the correct syntax to print 'Hello World' in Python?",
    "options": ["echo 'Hello World'", "print('Hello World')", "printf('Hello World')", "cout << 'Hello World'"],
    "answer": "print('Hello World')"
  },
  {
    "question": "Which keyword is used for conditional branching in Python?",
    "options": ["switch", "case", "if", "for"],
    "answer": "if"
  },
  {
    "question": "What is the output of the following code?\n\nprint(2 ** 3)",
    "options": ["5", "6", "8", "9"],
    "answer": "8"
  },
  {
    "question": "What will the following code do?\n\nfile = open('file.txt', 'w')\nfile.write('Hello')\nfile.flush()\nfile.close()",
    "options": ["Flush the content of 'file.txt' to disk", "Write 'Hello' to 'file.txt'", "Write 'Hello' to 'file.txt' and keep it open", "None of the above"],
    "answer": "Write 'Hello' to 'file.txt'"
  },
  {
    "question": "Which of the following is a valid list in Python?",
    "options": ["{1, 2, 3}", "[1, 2, 3]", "(1, 2, 3)", "<1, 2, 3>"],
    "answer": "[1, 2, 3]"
  },
  {
    "question": "What is the correct way to start a for loop in Python?",
    "options": ["for i to range(5):", "for (i = 0; i < 5; i++):", "for i in range(5):", "foreach i in range(5):"],
    "answer": "for i in range(5):"
  },
  {
    "question": "What will be the output of the following code?\n\nx = '5'\ny = int(x) + 2\nprint(y)",
    "options": ["52", "7", "TypeError", "None"],
    "answer": "7"
  },
   {
    "question": "What is Google Colab mainly used for?",
    "options": ["Video editing", "Data science and machine learning coding", "Web design", "Game development"],
    "answer": "Data science and machine learning coding"
  },
  {
    "question": "What type of file does Google Colab use?",
    "options": [".docx", ".xlsx", ".ipynb", ".pptx"],
    "answer": ".ipynb"
  },
  {
    "question": "Which language is primarily used in Google Colab notebooks?",
    "options": ["Java", "C++", "Python", "JavaScript"],
    "answer": "Python"
  },
  {
    "question": "Which of the following allows you to mount Google Drive in Colab?",
    "options": [
      "from google.colab import mount\ndrive.mount('/content/drive')",
      "import drive.mount('/colab')",
      "mount.drive('/colab')",
      "drive.mount('colab.google.com')"
    ],
    "answer": "from google.colab import mount\ndrive.mount('/content/drive')"
  },
  {
    "question": "What will the following code do in Google Colab?\n\n!pip install numpy",
    "options": [
      "It uninstalls numpy package",
      "It installs numpy package in the current environment",
      "It updates Python",
      "It clears the Colab runtime"
    ],
    "answer": "It installs numpy package in the current environment"
  },
  {
    "question": "How can you upload a file from your computer into Google Colab?",
    "options": [
      "upload.file()",
      "from google.colab import files\nfiles.upload()",
      "import upload.files()",
      "files.upload('filename')"
    ],
    "answer": "from google.colab import files\nfiles.upload()"
  },
  {
    "question": "What does the exclamation mark (!) before a command mean in Colab?",
    "options": [
      "It is used for comments",
      "It is used to run shell commands",
      "It is used to exit the notebook",
      "It is used for debugging"
    ],
    "answer": "It is used to run shell commands"
  },
  {
    "question": "Which shortcut runs the current cell in Google Colab?",
    "options": ["Shift + Enter", "Ctrl + R", "Alt + C", "Shift + Space"],
    "answer": "Shift + Enter"
  },
  {
    "question": "What does this code do in Google Colab?\n\n!ls",
    "options": [
      "Lists the variables in the environment",
      "Lists the files in the current working directory",
      "Starts a local server",
      "Loads saved files"
    ],
    "answer": "Lists the files in the current working directory"
  },
  {
    "question": "What does 'Runtime > Factory Reset Runtime' do in Google Colab?",
    "options": [
      "Saves all variables",
      "Deletes all files and variables and restarts the environment",
      "Saves your notebook as PDF",
      "Changes the Python version"
    ],
    "answer": "Deletes all files and variables and restarts the environment"
  },
  
  {
    "question": "Which of the following is an immutable data type in Python?",
    "options": ["List", "Dictionary", "Set", "Tuple"],
    "answer": "Tuple"
  },
  {
    "question": "What is the output of the following code?\n\nx = type(10)\nprint(x)",
    "options": ["<class 'float'>", "<class 'str'>", "<class 'int'>", "<class 'bool'>"],
    "answer": "<class 'int'>"
  },
  {
    "question": "Which data type is used to store True or False values?",
    "options": ["str", "int", "bool", "float"],
    "answer": "bool"
  },
  {
    "question": "What will the following code output?\n\nx = [1, 2, 3]\nprint(type(x))",
    "options": ["<class 'tuple'>", "<class 'set'>", "<class 'list'>", "<class 'dict'>"],
    "answer": "<class 'list'>"
  },
  {
    "question": "Which of the following is a floating-point number?",
    "options": ["10", "'10.5'", "10.0", "'10'"],
    "answer": "10.0"
  },
  {
    "question": "Which of the following represents a dictionary in Python?",
    "options": ["[1, 2, 3]", "(1, 2, 3)", "{'a': 1, 'b': 2}", "{1, 2, 3}"],
    "answer": "{'a': 1, 'b': 2}"
  },
  {
    "question": "Which function is used to check the data type of a variable?",
    "options": ["typeof()", "type()", "checktype()", "datatype()"],
    "answer": "type()"
  },
  {
    "question": "What is the result of the following code?\n\nx = (1, 2, 3)\nprint(type(x))",
    "options": ["<class 'list'>", "<class 'tuple'>", "<class 'set'>", "<class 'dict'>"],
    "answer": "<class 'tuple'>"
  },
  {
    "question": "Which of these is a valid set in Python?",
    "options": ["{1, 2, 3}", "[1, 2, 3]", "(1, 2, 3)", "{'a': 1, 'b': 2}"],
    "answer": "{1, 2, 3}"
  },
  {
    "question": "What is the output of the following code?\n\nx = '123'\nprint(type(x))",
    "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'bool'>"],
    "answer": "<class 'str'>"
  },{
    "question": "Which of the following is a valid Python variable name?",
    "options": ["2name", "my-name", "_name", "class"],
    "answer": "_name"
  },
  {
    "question": "Which operator is used for exponentiation in Python?",
    "options": ["^", "**", "exp()", "//"],
    "answer": "**"
  },
  {
    "question": "What will be the output of this code?\n\nx = 10\ny = 5\nprint(x % y)",
    "options": ["0", "2", "5", "10"],
    "answer": "0"
  },
  {
    "question": "Which keyword is used to create a function in Python?",
    "options": ["func", "define", "def", "function"],
    "answer": "def"
  },
  {
    "question": "Which of the following is NOT a valid Python keyword?",
    "options": ["finally", "return", "define", "lambda"],
    "answer": "define"
  },
  {
    "question": "What will be the result of 10 // 3?",
    "options": ["3.33", "3", "4", "0"],
    "answer": "3"
  },
  {
    "question": "What does the '==' operator check for?",
    "options": ["Assigns value", "Checks if not equal", "Checks equality", "Divides two numbers"],
    "answer": "Checks equality"
  },
  {
    "question": "Which keyword is used to start a loop in Python?",
    "options": ["iterate", "for", "loop", "repeat"],
    "answer": "for"
  },
  {
    "question": "What type of operator is '+' in Python?",
    "options": ["Logical", "Bitwise", "Arithmetic", "Comparison"],
    "answer": "Arithmetic"
  },
  {
    "question": "Which of the following will cause an error in variable naming?",
    "options": ["_value", "value_1", "1value", "valueOne"],
    "answer": "1value"
  },
  {
    "question": "Which keyword is used to define a class in Python?",
    "options": ["struct", "class", "define", "object"],
    "answer": "class"
  },
  {
    "question": "What does the 'not' operator do?",
    "options": ["Performs addition", "Reverses a boolean value", "Compares strings", "Multiplies values"],
    "answer": "Reverses a boolean value"
  },
  {
    "question": "Which of the following is an assignment operator?",
    "options": ["==", "=", "!=", ">="],
    "answer": "="
  },
  {
    "question": "Which of the following are logical operators in Python?",
    "options": ["and, or, not", "add, sub, mul", "==, !=, >", "if, else, elif"],
    "answer": "and, or, not"
  },
  {
    "question": "What is the output of:\n\nx = 5\ny = 2\nprint(x ** y)",
    "options": ["10", "25", "7", "5"],
    "answer": "25"
  },
  {
    "question": "Which operator checks for identity?",
    "options": ["==", "is", "=", "!="],
    "answer": "is"
  },
  {
    "question": "Which operator is used to compare values?",
    "options": ["=", "==", "&", "or"],
    "answer": "=="
  },
  {
    "question": "Which is NOT a valid logical operator in Python?",
    "options": ["and", "or", "not", "nor"],
    "answer": "nor"
  },
  {
    "question": "Which of the following is a Python keyword?",
    "options": ["value", "while", "method", "printline"],
    "answer": "while"
  },
  {
    "question": "How can we assign multiple variables at once in Python?",
    "options": ["a, b = 1, 2", "a = b = 1, 2", "assign(a, b) = (1, 2)", "var a, b = 1, 2"],
    "answer": "a, b = 1, 2"
  },
  {
    "question": "Which operator is used for bitwise AND?",
    "options": ["&", "|", "^", "~"],
    "answer": "&"
  },
  {
    "question": "Which operator is used for logical OR?",
    "options": ["|", "||", "or", "&"],
    "answer": "or"
  },
  {
    "question": "Which operator is used to check if a value is NOT equal?",
    "options": ["==", "!=", "not", "<>"],
    "answer": "!="
  },
  {
    "question": "Which of the following are valid ways to assign a value to a variable in Python?",
    "options": ["x := 5", "x = 5", "int x = 5", "x <- 5"],
    "answer": "x = 5"
  },
  {
    "question": "Which of these operators is used for floor division?",
    "options": ["//", "/", "%", "**"],
    "answer": "//"
  },
  {
    "question": "Which operator gives the remainder of division?",
    "options": ["/", "//", "%", "**"],
    "answer": "%"
  },
  {
    "question": "What is the keyword used to exit a loop?",
    "options": ["exit", "stop", "end", "break"],
    "answer": "break"
  },
  {
    "question": "Which of the following is NOT a comparison operator?",
    "options": [">=", "<", "+", "=="],
    "answer": "+"
  },
  {
    "question": "Which keyword is used to skip the current loop iteration?",
    "options": ["stop", "pass", "continue", "skip"],
    "answer": "continue"
  },
  {
    "question": "Which of the following will declare a variable named `count` with value 10?",
    "options": ["int count = 10", "count := 10", "count = 10", "var count = 10"],
    "answer": "count = 10"
  },
  {
    "question": "What will be the output of the following code?\n\nx = int('5')\nprint(type(x))",
    "options": ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'bool'>"],
    "answer": "<class 'int'>"
  },
  {
    "question": "Which function converts a number to a string?",
    "options": ["str()", "int()", "float()", "bool()"],
    "answer": "str()"
  },
  {
    "question": "What is the result of the following code?\n\nx = float('3.14')\nprint(x)",
    "options": ["3", "3.0", "3.14", "Error"],
    "answer": "3.14"
  },
  {
    "question": "Which of the following will raise an error?",
    "options": ["int('10')", "str(20)", "float('3.5')", "int('hello')"],
    "answer": "int('hello')"
  },
  {
    "question": "What is the output of:\n\nx = str(100)\nprint(x + '1')",
    "options": ["101", "1001", "Error", "100"],
    "answer": "1001"
  },
  {
    "question": "Which function converts a float to an integer by removing decimal?",
    "options": ["str()", "round()", "int()", "float()"],
    "answer": "int()"
  },
  {
    "question": "What is the type of the result?\n\nx = bool('False')\nprint(x)",
    "options": ["False", "True", "<class 'str'>", "<class 'int'>"],
    "answer": "True"
  },
  {
    "question": "What will be the output of the following code?\n\nx = int(5.9)\nprint(x)",
    "options": ["6", "5.9", "Error", "5"],
    "answer": "5"
  },
  {
    "question": "How to convert string '123' to float in Python?",
    "options": ["float('123')", "str(123.0)", "int('123.0')", "bool('123')"],
    "answer": "float('123')"
  },
  {
    "question": "What is the type of value returned by input() function in Python?",
    "options": ["int", "float", "bool", "str"],
    "answer": "str"
  },
  {
    "question": "Which keyword is used for decision-making in Python?",
    "options": ["choose", "if", "select", "check"],
    "answer": "if"
  },
  {
    "question": "What will be the output of this code?\n\nx = 10\nif x > 5:\n    print('Yes')\nelse:\n    print('No')",
    "options": ["Yes", "No", "Error", "Nothing"],
    "answer": "Yes"
  },
  {
    "question": "Which of the following is used for multiple conditions?",
    "options": ["elseif", "elif", "else if", "ifelse"],
    "answer": "elif"
  },
  {
    "question": "What does the `continue` statement do?",
    "options": ["Stops the loop", "Skips the current iteration", "Exits the program", "Repeats the current iteration"],
    "answer": "Skips the current iteration"
  },
  {
    "question": "What will be the output?\n\nx = 3\nif x == 3:\n    print('Three')\nelse:\n    print('Not Three')",
    "options": ["Three", "Not Three", "Error", "None"],
    "answer": "Three"
  },
  {
    "question": "Which of these is used to stop a loop completely?",
    "options": ["stop", "end", "break", "exit"],
    "answer": "break"
  },
  {
    "question": "What does the `pass` statement do in Python?",
    "options": ["Exits a loop", "Skips an iteration", "Does nothing", "Prints a message"],
    "answer": "Does nothing"
  },
  {
    "question": "Which of the following is correct syntax for a while loop?",
    "options": ["while x > 0 {", "while(x > 0):", "while x > 0:", "while x > 0 then:"],
    "answer": "while x > 0:"
  },
  {
    "question": "What is the output?\n\nx = 2\nif x > 3:\n    print('High')\nelif x == 2:\n    print('Equal')\nelse:\n    print('Low')",
    "options": ["High", "Equal", "Low", "None"],
    "answer": "Equal"
  },
  {
    "question": "What will be the output of this code?\n\nfor i in range(3):\n    if i == 1:\n        continue\n    print(i)",
    "options": ["0 1 2", "0 2", "1 2", "0 1"],
    "answer": "0 2"
  },{
    "question": "How do you create a list in Python?",
    "options": ["list = {}", "list = ()", "list = []", "list = <>"],
    "answer": "list = []"
  },
  {
    "question": "What is the output?\n\nx = [1, 2, 3]\nprint(x[1])",
    "options": ["1", "2", "3", "Error"],
    "answer": "2"
  },
  {
    "question": "Which method is used to add an item to a list?",
    "options": ["add()", "append()", "push()", "insert()"],
    "answer": "append()"
  },
  {
    "question": "How do you remove an item by value from a list?",
    "options": ["del list[1]", "list.pop()", "list.remove('value')", "list.delete()"],
    "answer": "list.remove('value')"
  },
  {
    "question": "What does `list.pop()` do?",
    "options": ["Removes first item", "Removes last item", "Deletes the list", "Clears the list"],
    "answer": "Removes last item"
  },
  {
    "question": "How can you find the length of a list?",
    "options": ["count(list)", "len(list)", "length(list)", "size(list)"],
    "answer": "len(list)"
  },
  {
    "question": "Which of these is used to slice a list?",
    "options": ["list(slice)", "list.cut()", "list[1:3]", "list.slice()"],
    "answer": "list[1:3]"
  },
  {
    "question": "What is the output of:\n\nx = [10, 20, 30]\nprint(30 in x)",
    "options": ["True", "False", "None", "Error"],
    "answer": "True"
  },
  {
    "question": "How to combine two lists?",
    "options": ["list1 + list2", "list1.append(list2)", "list1.add(list2)", "combine(list1, list2)"],
    "answer": "list1 + list2"
  },
  {
    "question": "What will `list.clear()` do?",
    "options": ["Delete list", "Return list", "Empty the list", "Copy the list"],
    "answer": "Empty the list"
  },
  
  {
    "question": "How do you define a tuple in Python?",
    "options": ["tuple = []", "tuple = {}", "tuple = ()", "tuple = <>"],
    "answer": "tuple = ()"
  },
  {
    "question": "What is the key difference between a list and a tuple?",
    "options": ["Tuples are slower", "Lists use ()", "Tuples are immutable", "Lists store strings only"],
    "answer": "Tuples are immutable"
  },
  {
    "question": "Which of these is a correct tuple?",
    "options": ["(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}", "'1', '2', '3'"],
    "answer": "(1, 2, 3)"
  },
  {
    "question": "Can you change values inside a tuple?",
    "options": ["Yes", "No", "Only if it's a string", "Only in Python 3.10+"],
    "answer": "No"
  },
  {
    "question": "How do you access the first element of a tuple?",
    "options": ["tuple.first()", "tuple[1]", "tuple(1)", "tuple[0]"],
    "answer": "tuple[0]"
  },
  {
    "question": "What is the output?\n\nt = (5,)\nprint(type(t))",
    "options": ["<class 'tuple'>", "<class 'int'>", "<class 'list'>", "<class 'set'>"],
    "answer": "<class 'tuple'>"
  },
  {
    "question": "Which function returns the number of items in a tuple?",
    "options": ["count()", "length()", "len()", "size()"],
    "answer": "len()"
  },
  {
    "question": "How can you convert a list to a tuple?",
    "options": ["list()", "tuple()", "set()", "dict()"],
    "answer": "tuple()"
  },
  {
    "question": "What does tuple.count(x) do?",
    "options": ["Removes x", "Adds x", "Returns count of x", "Replaces x"],
    "answer": "Returns count of x"
  },
  {
    "question": "Are tuples ordered in Python?",
    "options": ["Yes", "No", "Only in lists", "Depends on version"],
    "answer": "Yes"
  },
  
  {
    "question": "Which of the following defines a dictionary in Python?",
    "options": ["dict = []", "dict = {}", "dict = ()", "dict = <>"],
    "answer": "dict = {}"
  },
  {
    "question": "What is a dictionary in Python?",
    "options": ["Ordered collection", "Unordered key-value pairs", "Single values", "Tuple of values"],
    "answer": "Unordered key-value pairs"
  },
  {
    "question": "How do you access a value by key?",
    "options": ["dict.get(key)", "dict.key()", "dict.key", "dict#key"],
    "answer": "dict.get(key)"
  },
  {
    "question": "Which method is used to remove a key-value pair?",
    "options": ["remove()", "pop()", "delete()", "clear()"],
    "answer": "pop()"
  },
  {
    "question": "What does dict.keys() return?",
    "options": ["All values", "Only numbers", "All keys", "All items"],
    "answer": "All keys"
  },
  {
    "question": "How to check if a key exists?",
    "options": ["key in dict", "dict.has(key)", "key.exists()", "key in dict.values()"],
    "answer": "key in dict"
  },
  {
    "question": "What is the output?\n\nd = {'a': 1, 'b': 2}\nprint(d['b'])",
    "options": ["1", "2", "b", "Error"],
    "answer": "2"
  },
  {
    "question": "Which method returns both key and value?",
    "options": ["dict.items()", "dict.all()", "dict.getall()", "dict.data()"],
    "answer": "dict.items()"
  },
  {
    "question": "What will `dict.clear()` do?",
    "options": ["Delete dict", "Empty the dictionary", "Return keys", "Return values"],
    "answer": "Empty the dictionary"
  },
  {
    "question": "Can dictionary keys be integers?",
    "options": ["No", "Yes", "Only strings allowed", "Only lists allowed"],
    "answer": "Yes"
  },
  
  {
    "question": "Which of these defines a set in Python?",
    "options": ["set = []", "set = ()", "set = {}", "set = set()"],
    "answer": "set = set()"
  },
  {
    "question": "What is the key feature of a set?",
    "options": ["Ordered", "Allows duplicates", "Unordered and unique", "Always sorted"],
    "answer": "Unordered and unique"
  },
  {
    "question": "How do you add an item to a set?",
    "options": ["append()", "add()", "insert()", "push()"],
    "answer": "add()"
  },
  {
    "question": "Which method removes a specific item from a set?",
    "options": ["pop()", "delete()", "remove()", "discard()"],
    "answer": "remove()"
  },
  {
    "question": "What is the result of:\n\nlen({1, 2, 2, 3})",
    "options": ["4", "3", "2", "Error"],
    "answer": "3"
  },
  {
    "question": "Can a set contain different data types?",
    "options": ["No", "Only strings", "Only integers", "Yes"],
    "answer": "Yes"
  },
  {
    "question": "Which of these operations finds common items in two sets?",
    "options": ["union()", "intersection()", "difference()", "symmetric_difference()"],
    "answer": "intersection()"
  },
  {
    "question": "Which of these returns all items from both sets without duplicates?",
    "options": ["merge()", "union()", "add()", "extend()"],
    "answer": "union()"
  },
  {
    "question": "What does set.pop() do?",
    "options": ["Removes random item", "Removes last item", "Removes first item", "Clears set"],
    "answer": "Removes random item"
  },
  {
    "question": "Are sets mutable in Python?",
    "options": ["No", "Yes", "Only if sorted", "Only if converted to list"],
    "answer": "Yes"
  },
  
  {
    "question": "What is a module in Python?",
    "options": ["A loop", "A class", "A file with Python code", "An input"],
    "answer": "A file with Python code"
  },
  {
    "question": "How do you import a module in Python?",
    "options": ["include module", "import module", "using module", "load module"],
    "answer": "import module"
  },
  {
    "question": "What is the purpose of the `def` keyword in Python?",
    "options": ["To define a class", "To define a function", "To delete data", "To define a loop"],
    "answer": "To define a function"
  },
  {
    "question": "Which of the following is the correct way to define a function?",
    "options": ["function myFunc():", "def myFunc():", "def = myFunc():", "define myFunc()"],
    "answer": "def myFunc():"
  },
  {
    "question": "What will the following code print?\n\ndef greet():\n    print('Hello')\ngreet()",
    "options": ["Hello", "greet", "Nothing", "Error"],
    "answer": "Hello"
  },
  {
    "question": "Which module is used to generate random numbers in Python?",
    "options": ["math", "os", "random", "time"],
    "answer": "random"
  },
  {
    "question": "What does the `return` keyword do in a function?",
    "options": ["Prints output", "Stops loop", "Exits function", "Sends back a result"],
    "answer": "Sends back a result"
  },
  {
    "question": "How do you import only a specific function from a module?",
    "options": ["import function from module", "from module import function", "use module.function", "get function of module"],
    "answer": "from module import function"
  },
  {
    "question": "Which keyword is used to call a function in Python?",
    "options": ["call", "use", "run", "just use function_name()"],
    "answer": "just use function_name()"
  },
  {
    "question": "Which of the following is a built-in module in Python?",
    "options": ["numpy", "flask", "math", "django"],
    "answer": "math"
  },
  
  {
    "question": "What is exception handling in Python used for?",
    "options": ["Debugging code", "Handling runtime errors", "Compiling programs", "Writing loops"],
    "answer": "Handling runtime errors"
  },
  {
    "question": "Which keyword is used to handle exceptions?",
    "options": ["except", "final", "raise", "tryexcept"],
    "answer": "except"
  },
  {
    "question": "What is the correct syntax for a try-except block?",
    "options": [
      "try { } except { }",
      "try: code except: code",
      "try -> except",
      "if error: catch"
    ],
    "answer": "try: code except: code"
  },
  {
    "question": "Which keyword is used to raise a custom exception?",
    "options": ["throw", "except", "raise", "error"],
    "answer": "raise"
  },
  {
    "question": "What will the following code do?\n\ntry:\n  x = 1/0\nexcept ZeroDivisionError:\n  print('Error')",
    "options": ["Print 0", "Error", "Print 'Error'", "No output"],
    "answer": "Print 'Error'"
  },
  {
    "question": "What does the `finally` block do?",
    "options": [
      "Executes only if error occurs",
      "Executes always",
      "Executes before try",
      "Skips the code"
    ],
    "answer": "Executes always"
  },
  {
    "question": "Which of the following is a built-in exception?",
    "options": ["ZeroDivisionError", "DivideByZero", "NullPointer", "LoopError"],
    "answer": "ZeroDivisionError"
  },
  {
    "question": "What is the output?\n\ntry:\n  print(5/0)\nexcept:\n  print('error')",
    "options": ["5", "0", "error", "None"],
    "answer": "error"
  },
  {
    "question": "Can multiple except blocks be used for one try block?",
    "options": ["No", "Yes", "Only in Python 3+", "Only if error occurs"],
    "answer": "Yes"
  },
  {
    "question": "Which keyword ensures execution of code regardless of exception?",
    "options": ["finally", "else", "raise", "catch"],
    "answer": "finally"
  }

]



# Initialize session state for current question
if 'current_question' not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Fetch the current question
current_question = st.session_state.current_question

# Display question
st.subheader(current_question['question'])

# Radio button for answer selection
selected_option = st.radio('‼ Choose Your Answer:', current_question['options'], key='Answer')

# Submit button
if st.button('Submit Your Answer'):
    if selected_option == current_question['answer']:
        st.success('✨ Correct Answer!')
    else:
        st.error(f'❌ Wrong Answer! The correct answer is: {current_question["answer"]}')
    
    time.sleep(2)  # Small delay before loading next question

    # Load a new random question
    st.session_state.current_question = random.choice(questions)
    st.rerun()
    
st.markdown('<h5 style="text-align: center; margin-top: 50px;">Built with ❤️ By Shan E Zehra</h5>', unsafe_allow_html=True)
