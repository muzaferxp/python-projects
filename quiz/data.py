quizzes =  [
    {
      "name": "Basics of Python",
      "questions": [
        {
          "question": "What is the correct file extension for Python files?",
          "options": ["a) .py", "b) .pt", "c) .pyt", "d) .python"],
          "answer": "a"
        },
        {
          "question": "Which of the following is a valid variable name in Python?",
          "options": ["a) 2name", "b) name2", "c) -name", "d) name-"],
          "answer": "b"
        },
        {
          "question": "What is the output of the following code? print(2 * 3 + 4)",
          "options": ["a) 14", "b) 10", "c) 24", "d) 8"],
          "answer": "b"
        }
      ]
    },
    {
      "name": "Data Types",
      "questions": [
        {
          "question": "What will type(\"5\") return?",
          "options": ["a) int", "b) str", "c) float", "d) bool"],
          "answer": "b"
        },
        {
          "question": "Which of these is a mutable data type in Python?",
          "options": ["a) List", "b) Tuple", "c) String", "d) Integer"],
          "answer": "a"
        },
        {
          "question": "What is the output of the following code? x = 5.0 print(type(x))",
          "options": [
            "a) <class 'int'>",
            "b) <class 'float'>",
            "c) <class 'complex'>",
            "d) <class 'str'>"
          ],
          "answer": "b"
        }
      ]
    },
    {
      "name": "Strings",
      "questions": [
        {
          "question": "What is the output of this code? s = \"Hello, World!\" print(s[7:12])",
          "options": ["a) World", "b) , Wor", "c) o, Wo", "d) Hello"],
          "answer": "a"
        },
        {
          "question": "What does the len() function do?",
          "options": [
            "a) Count vowels in a string",
            "b) Return the number of elements in a sequence",
            "c) Convert a string to lowercase",
            "d) None of the above"
          ],
          "answer": "b"
        },
        {
          "question": "What will print(\"Python\" * 2) output?",
          "options": [
            "a) PythonPython",
            "b) Python Python",
            "c) SyntaxError",
            "d) None of the above"
          ],
          "answer": "a"
        }
      ]
    },
    {
      "name": "Conditionals and Loops",
      "questions": [
        {
          "question": "What will this code output? for i in range(3): print(i)",
          "options": ["a) 0 1 2", "b) 1 2 3", "c) 0 1 2 3", "d) 1 2"],
          "answer": "a"
        },
        {
          "question": "How do you write an \"if-else\" statement in Python?",
          "options": [
            "a) if x > 5: then print(\"Yes\")",
            "b) if x > 5 print(\"Yes\") else print(\"No\")",
            "c) if x > 5: print(\"Yes\") else: print(\"No\")",
            "d) None of the above"
          ],
          "answer": "c"
        }
      ]
    },
    {
      "name": "Functions",
      "questions": [
        {
          "question": "How do you define a function in Python?",
          "options": [
            "a) function my_function():",
            "b) def my_function:",
            "c) def my_function():",
            "d) my_function():"
          ],
          "answer": "c"
        },
        {
          "question": "What is the default return value of a Python function without a return statement?",
          "options": ["a) 0", "b) None", "c) False", "d) Null"],
          "answer": "b"
        }
      ]
    },
    {
      "name": "Lists and Tuples",
      "questions": [
        {
          "question": "What is the output of this code? lst = [1, 2, 3] lst.append(4) print(lst)",
          "options": ["a) [1, 2, 3, 4]", "b) [4, 1, 2, 3]", "c) [1, 2, 3]", "d) Error"],
          "answer": "a"
        },
        {
          "question": "Can a tuple be modified after creation?",
          "options": ["a) Yes", "b) No"],
          "answer": "b"
        }
      ]
    },
    {
      "name": "Dictionaries",
      "questions": [
        {
          "question": "What will the following code output? my_dict = {'a': 1, 'b': 2} print(my_dict['a'])",
          "options": ["a) 1", "b) 2", "c) a", "d) Error"],
          "answer": "a"
        },
        {
          "question": "Which method is used to get all the keys of a dictionary?",
          "options": ["a) keys()", "b) values()", "c) items()", "d) get()"],
          "answer": "a"
        }
      ]
    },
    {
      "name": "File Handling",
      "questions": [
        {
          "question": "Which mode is used to write to a file?",
          "options": ["a) 'r'", "b) 'w'", "c) 'rw'", "d) 'a'"],
          "answer": "b"
        },
        {
          "question": "What will this code do? with open('test.txt', 'r') as file: print(file.read())",
          "options": [
            "a) Write \"test.txt\" to the file",
            "b) Read and print the content of \"test.txt\"",
            "c) Raise an error if \"test.txt\" doesn't exist",
            "d) Both b and c"
          ],
          "answer": "d"
        }
      ]
    },
    {
      "name": "Object-Oriented Programming",
      "questions": [
        {
          "question": "How do you create a class in Python?",
          "options": [
            "a) class MyClass:",
            "b) def MyClass:",
            "c) function MyClass():",
            "d) None of the above"
          ],
          "answer": "a"
        },
        {
          "question": "What is the purpose of the __init__ method?",
          "options": [
            "a) To initialize an object’s attributes",
            "b) To destroy an object",
            "c) To define a class variable",
            "d) None of the above"
          ],
          "answer": "a"
        }
      ]
    },
    {
      "name": "Advanced Topics",
      "questions": [
        {
          "question": "What will the following code output? x = [1, 2, 3] y = x y.append(4) print(x)",
          "options": ["a) [1, 2, 3, 4]", "b) [1, 2, 3]", "c) Error", "d) None of the above"],
          "answer": "a"
        },
        {
          "question": "How do you handle exceptions in Python?",
          "options": ["a) try and catch", "b) try and except", "c) try and finally", "d) catch and finally"],
          "answer": "b"
        }
      ]
    }
  ]
