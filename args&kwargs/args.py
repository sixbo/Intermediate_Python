def test_var_args(first_arg,*argv):
    print("Firse normal arg:",first_arg)
    for arg in argv:
        print("Anather arg through * argv:",arg)

#调用函数test_var_args并传参
test_var_args("tom","six","ten","one")