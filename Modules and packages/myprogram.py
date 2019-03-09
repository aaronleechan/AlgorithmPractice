# want to code to use from mymodule.py
# from mymodule import my_func


# my_func()

# def sub_report():
# 	print("Hey I'm a function inside mysubscript")

from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

some_main_script.report_main()
mysubscript.report_main()
# print(mysubscrip())