import plotly.express as px

# create the dataset from gapminder
# lets filter out the data focusing on a subset to reduce complexity.

# First lets look at what gapminder dataset contains
dataset = px.data.gapminder()

# print(dataset.columns)


# so it conatins these columns
# ['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap', 'iso_alpha', 'iso_num']

# lets see what there in 'country' column

# print(dataset['country'].value_counts())

# so it has a list of countries ... lets focus on the data for just one country for now ... Canada

# filtering the data
data_canada = dataset.query("country == 'Canada'")
# print(data_canada.head())

# so we got our sample data
# lets check some stats

# print(data_canada.info())


# lets try to create a simple bar chart that would show the year-on-year population status

# there is a method call 'bar' that can plot a simple bar chart
# lets use that. The output will be a plotly.express object
# fig = px.bar(data_canada, x='year', y='pop')

# simple ... just choose the year field as x axis and population field as y axis.

# now to plot this on a browser, we will have to use another function called show()
# fig.show()

# lets run this and check

# coool right!


# lets try to add some more customization to this bar chart. 
# For example - hover-data, labels, color etc

# doing that is just achieved by setting up the relevant properties/attributes
fig = px.bar(data_canada, x='year', y='pop',
hover_data=['lifeExp', 'gdpPercap'], color='lifeExp', 
labels={'pop':'Population of Canada'})

# please note that there are gazillion other options and properties to set. You can explore them .. would be fun !

fig.show()

# lets try to run this and see the results 

# again coool !! isnt it :)

# Thanks a lot for watching
# Please share your suggestions, if any.


