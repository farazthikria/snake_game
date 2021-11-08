from distutils import version
from cx_Freeze import setup , Executable

version = '1.0'

author = "faraz"
description = "a simple snake game"

executable = [Executable(r"D:\tictactoe_python")]
