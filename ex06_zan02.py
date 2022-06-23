# %%

arr = [11, 22, 33, 44, 55]

print(f'arr = {arr} type: {type(arr)}')

# %%
print(id(arr))

arr[1] = 100

arr.append(200)

print(id(arr))

# %%
tp = 1, 6, 3, 9

arr1 = list(tp)

print(f'arr1 = {arr1}')
# %%

s_arr = list('Hello Python')
print(s_arr)

# %%
