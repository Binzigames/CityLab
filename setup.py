from cx_Freeze import setup, Executable

# Налаштування
build_exe_options = {"packages": ["pygame"]}

# Виконуваний файл
executables = [
    Executable(
        "main.py",
        base=None,
        icon="icon.ico"
    )
]

setup(
    name="CityLab",
    version="0.1",
    description="City Labs is an exciting retro game where you become the architect and manager of your own city. Feel the nostalgia of the era of 8-bit games as you build and develop your city in the style of the 80s. Design buildings, plan infrastructure and manage resources to create the perfect city for your residents. Put your creativity and strategic skills to the test in this retro journey to the golden age of video games!",
    author="Porko",
    options={"build_exe": build_exe_options},
    executables=executables
)
