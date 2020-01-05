# 请注意，每一个包目录下面都会有一个__init__.py 的文件，这个文件是必须存在的，否则，Python 就把这个目录当成普通目录，
# 而不是一个包。__init__.py 可以是空文件，也可以有 Python 代码，
# 因为__init__.py 本身就是一个模块，而它的模块名就是所在包的目录名
init_int = 0


def init_func():
    print("this is init_func")
