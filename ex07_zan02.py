# %%

conn = dict(
    port=1521,
    host='localhost',
    db='northwind',
    keepalive=True
)

print(conn['db'])

# %%
user = {
    'firstname':'Anna',
    'lastname':'Smith',
    'age':36,
    'phone':'222-33-44'
}


print(user['lastname'])
# %%

user1 = [ 'Anna', 'Smith', 36,'222-33-44', True ]

print(user1)
# %%

user.keys()

# %%
user.values()
# %%

user.items()
# %%

'age' in user

# %%

user['email']

# %%

user.get('email', 'no@no.com')

# %%
