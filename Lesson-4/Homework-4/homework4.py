# %% [markdown]
# 1. Return uncommon elements of lists. Order of elements does not matter.

# %%
list1 = [1, 1, 2]
list2 = [2, 3, 4]

r = [i for i in list1 if i not in list2] + [j for j in list2 if j not in list1]
print(r)

# %% [markdown]
# 2. Print the square of each number which is less than n on a separate line.

# %%
n = 5
for i in range(1, n):
    print(i**2)

# %%



