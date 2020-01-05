import import_demo.pkg1 as pkg  # __init__.py 本身就是一个模块，而它的模块名就是所在的包名
import import_demo.pkg1.a
import import_demo.pkg1.b as b
from import_demo.pkg1.c import c_func  # from 模块名 import 具体的功能
from import_demo.pkg3 import *  # 在 import_demo.pkg3 模块设置 __all__ = ['x', 'y']
from import_demo.pkg4 import *  # 在 import_demo.pkg4 模块引入下面模块的具体功能

print(pkg.init_int)
pkg.init_func()

print(import_demo.pkg1.a.int_a)
import_demo.pkg1.a.a_func()

print(b.int_b)
b.b_func()

c_func()  # 不用加前缀，直接使用

x.x_func()
y.y_func()

k_func()
m_func()
a = Animal()
a.run()
