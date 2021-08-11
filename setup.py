import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="SnakeGame",
    options={"build_exe": {"packages":["turtle", "time"],
                           "include_files":["food.py", "score.py", "snake.py", "main.py"]}},
    executables = executables

    )