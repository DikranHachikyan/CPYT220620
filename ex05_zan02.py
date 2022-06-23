# %%

tp = (11, 23, 55, 67)

print(f'tp = {tp} id: {id(tp)}')

# %%

print(tp[1])

# %%

# tp[0] = 100

# %%
a, b, c, d = tp

print(f'a={a}, b={b}, c={c}, d={d}')

# %%

a, b, *_ = tp

print(f'a = {a}, b = {b}')


# %%


*_, c, d = tp

print(f'c = {c}, d = {d}')

# %%

tp = 9, 4, 6, 7

print(f'tp = {tp} id:{id(tp)}')

# %%

t1 = (55,)

print(f't1 = {t1} type of t1:{type(t1)}')

# %%

9 in tp

# %%

1 not in tp

# %%

type(tp) is tuple

# %%
