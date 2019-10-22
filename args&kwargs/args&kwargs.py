
def test_args_kwargs(arg1,arg2,arg3):
    print("arg1:",arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

#*args调用函数
args=("sixbo","one",2)
test_args_kwargs(*args)

#**kwargs 调用

kwargs={"arg1":3,"arg2":"tow","arg3":4}
test_args_kwargs(**kwargs)