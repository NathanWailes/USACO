i = 23423524234
def foo(x):
    def bar():
        print i,
    # ...
    # A bunch of code here
    # ...
    for i in x:  # Ah, i *is* local to Foo, so this is what Bar sees
        print i,
    i = 23423524234
    bar()

foo([5, 5, 5])
