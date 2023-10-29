def foo(x):
    try:
        return 10/x
    except ZeroDivisionError:
        return "Error"
    finally:
        return 0
result=foo(0)
print(result)


#0
#Finally Block is executed