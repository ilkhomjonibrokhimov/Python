# %% [markdown]
# - **Task**: Plot the function $ f(x) = x^2 - 4x + 4 $ for $ x $ values between -10 and 10. Customize the plot with appropriate labels for the axes and a title.
# 

# %%
import numpy as np
from matplotlib import pyplot as plt

# %%
x = np.linspace(-4, 5, 1000)
y = x**2 - 4*x + 4

plt.plot(x, y, c='r', label='$ f(x) = x^2 - 4x + 4 $')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()


# %% [markdown]
# #### **2. Sine and Cosine Plot**
# - **Task**: Plot $ \sin(x) $ and $ \cos(x) $ on the same graph for $ x $ values ranging from 0 to $ 2\pi $. Use different line styles, markers, and colors to distinguish between the two functions. Add a legend.
# 

# %%
x = np.linspace(0, 2*np.pi)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, c='g', linestyle=':', marker=',')
plt.plot(x, y2, marker='.')
plt.show()

# %% [markdown]
# #### **3. Subplots**
# - **Task**: Create a 2x2 grid of subplots. In each subplot, plot:
#   - Top-left: $ f(x) = x^3 $
#   - Top-right: $ f(x) = \sin(x) $
#   - Bottom-left: $ f(x) = e^x $
#   - Bottom-right: $ f(x) = \log(x+1) $ (for $ x \geq 0 $)
# 
#   Customize each plot with titles, axis labels, and different colors.

# %%
x = np.linspace(-10, 10, 1000)
y = x**3
plt.subplot(2, 2, 1)
plt.plot(x, y)

x = np.linspace(-10, 10, 1000)
y = np.sin(x)
plt.subplot(2, 2, 2)
plt.plot(x, y)

x = np.linspace(-10, 10, 1000)
y = np.e**x
plt.subplot(2, 2, 3)
plt.plot(x, y)

x = np.linspace(-10, 10, 1000)
y = np.where(x >= 0, np.log(x + 1), None)
plt.subplot(2, 2, 4)
plt.plot(x, y)

plt.show()


# %% [markdown]
# #### **4. Scatter Plot**
# - **Task**: Create a scatter plot of 100 random points in a 2D space. The x and y values should be randomly generated from a uniform distribution between 0 and 10. Use different colors and markers for the points. Add a title, axis labels, and a grid.
# 

# %%
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
plt.scatter(x, y)
plt.title("Scatter plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(color='green', linestyle=':')

# %% [markdown]
# #### **5. Histogram**
# - **Task**: Generate a random dataset of 1000 values sampled from a normal distribution (mean=0, std=1). Plot a histogram of the data with 30 bins. Add a title and axis labels. Adjust the transparency of the bars using the `alpha` parameter.
# 

# %%
data = np.random.randn(1000)
plt.hist(data, bins=30, color='g', alpha=0.7, edgecolor='k')
plt.title("Normal distribution")
plt.xlabel("Bins")
plt.ylabel("Occurences")

# %% [markdown]
# #### **6. 3D Plotting**
# - **Task**: Create a 3D surface plot for the function $ f(x, y) = \cos(x^2 + y^2) $ over the range of $ x $ and $ y $ values from -5 to 5. Use a suitable colormap and add a colorbar. Set appropriate labels for the axes and title.
# 

# %%
fig = plt.Figure()
ax = plt.axes(projection='3d')

x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
xx, yy = np.meshgrid(x, y)
zz = np.cos(xx**2 + yy**2)

ax.plot_surface(xx, yy, zz, cmap="viridis")
ax.set_title("3D plot")
ax.set_xlabel("X value")
ax.set_ylabel("Y value")
ax.set_zlabel("Cos(x + y)")

# %% [markdown]
# #### **7. Bar Chart**
# - **Task**: Create a vertical bar chart displaying the sales data for five different products: `['Product A', 'Product B', 'Product C', 'Product D', 'Product E']`. The sales values for each product are `[200, 150, 250, 175, 225]`. Customize the chart with a title, axis labels, and different bar colors.
# 
# 

# %%
x = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
y = [200, 150, 250, 175, 225]
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']

plt.bar(x, y, color=colors)
plt.title("Sales")
plt.xlabel("Products")
plt.ylabel("Sales values for each product")
plt.show()

# %% [markdown]
# #### **8. Stacked Bar Chart**
# - **Task**: Create a stacked bar chart that shows the contribution of three different categories (`'Category A'`, `'Category B'`, and `'Category C'`) over four time periods (`'T1'`, `'T2'`, `'T3'`, `'T4'`). Use sample data for each category at each time period. Customize the chart with a title, axis labels, and a legend.

# %%
periods = ['T1', 'T2', 'T3', 'T4']
cat_a = [20, 25, 30, 28]
cat_b = [15, 18, 22, 20]
cat_c = [10, 12, 14, 16]

plt.bar(periods, cat_a, label="Category A")
plt.bar(periods, cat_b, bottom=cat_a, label="Category B")
cat_ab = np.array(cat_a) + np.array(cat_b)
plt.bar(periods, cat_c, bottom=cat_ab, label="Category C")

plt.title("Category contributions over time")
plt.xlabel("Time peiod")
plt.ylabel("Values")
plt.legend()
plt.show()

# %%



