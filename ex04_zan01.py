# %%
s1 = 'Lorem ipsum dolor sit amet'

s2 = "Lorem ipsum dolor sit amet"

# %%
s3 = '''Lorem ipsum dolor sit amet,
consectetur adipisicing elit, sed do
eiusmod'''

print(s3)


# %%
def foo():
    '''Function foo()
    prints Hello Foo in terminal
    Author: Me
    Created: 20.06.2022
    '''
    print('Hello Foo!')

foo()

# %%

print(foo.__doc__)
# %%

x = 12.4

print(f'value of x is {x * 2:.2f}')

# %%

s1[4]
# %%

s1[0:5]
# %%

s1[0:20:2]
# %%

s1[::-1]
# %%

'HELLO'.lower()
# %%

print('-' * 20)
# %%
