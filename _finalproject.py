#!/usr/bin/env python3

#This tutorial was made using Python 3.8.5 (type python3 -V in terminal to check).

#All code is commented with quotation marks.
#To run, delete the quotation marks between comment lines unless noted.

#Before we begin, we need to install the matplotlib library using pip.
#To install, type:
#	pip3 install matplotlib
#The matplotlib library will also install numpy if that is not on your computer
#	as well.
#Type this into your command line to check if the pip module is available:
#	python3 -m pip --version
#Pip is typically a feature for Python versions 3.4.2 and above.
#However, some Linux systems (like Debian and Ubuntu) use different commands 
#	to install the module. 
#If there is no pip module recognized, you should use the command lines given in
#	the terminal using sudo (which allows you to use the command as an admin). 
#For Debian/Ubuntu/Minty, I used these command lines:
#	sudo apt install python3-pip (to prompt the pip install)
#	sudo apt-get update (to update Python)
#	sudo apt install python3-pip (to install the pip module)
#	pip3 install matplotlib (to install the matplotlib module)
#To check if the modules are installed, type python3 into your terminal.
#	Type import matplotlib. If another command line pops up, type exit() to
#	resume.
#You can also consult these documentations for future reference:
#	pip: pip.pypa.io/en/stable/installing
#	matplotlib: matplotlib.org/stable/tutorials/index.html

#Now that the matplotlib library is on your computer, we can now import the library.

import matplotlib.pyplot as plt 

#You can refer to pyplot as plt with "as", saving some characters and your fingers.
#You can also use this syntax to import pyplot:
#	from matplotlib import pyplot as plt

#Now let's make a graph using the plot() function. 
"""
plt.plot([1, 2, 3, 4], [0, 1, 2, 3])
plt.show()
"""
#Congrats! You just made a graph! 
#The syntax for plt.plot is as follows: plt.plot([x-axis], [y-axis])
#plt.show() lets the graph display for you to see the output. 
#NOTE: Always put plt.show() as the last line for your plot.

##################### Using the matplotlib Interface ##########################

#On the bottom left, there are buttons to maneuver around the graph.
#You can learn what each button does by hovering over them but a quick summary.
#Home: takes you to the default view (the same view as how it first appeared).
#L/R Arrows: Undo (left) and redo (right) maneuvers in your graph.
#Quad Arrows / Arrow Cross: Manipulate the graph axes.
#Magnifying glass: Zoom in on a specific area of the graph.
#Sliders: Shift around the boundaries of the graph within the window.
#Save: Save the graph wherever you'd like.
#	You can also use plt.savefig('filepath or name') within your code.
#	If you put a filename, the plot will be saved in the same 
#		directory as your code.
#	Otherwise, you can specify with a filepath w/ name included.

###############################################################################

#You can also plot lists and tuples that are previously defined.

x_axis = (2, 16, 17, 24, 37)
y_axis = [1, 3, 4, 7, 23]
"""
plt.plot(x_axis, y_axis)
plt.show()
"""
#NOTE: There will be no plot if the lists/tuples are not the same length.

#Now to add labels to the graph, we can use the following commands:
"""
plt.plot(x_axis, y_axis) #plt.plot() generates the plot
plt.title('Just Some Random Numbers') #The main title of the graph
plt.xlabel('The X-axis label') #The x-axis label
plt.ylabel('The Y-axis label') #The y-axis label
plt.show() #Make sure to put plt.show() last
"""
#You can also plot multiple plots on the same graph and use the same axes.

secondy_axis = [4, 8, 34, 41, 45]
secondx_axis = [9, 10, 32, 33, 52]
"""
plt.plot(x_axis, y_axis) 
plt.plot(secondx_axis, secondy_axis) #Two new lists added to graph
plt.plot(secondx_axis, y_axis) #Using axes previously defined
plt.title('Just Some Random Numbers') 
plt.xlabel('The X-axis label') 
plt.ylabel('The Y-axis label') 
plt.show() 
"""

#You can also add a legend with plt.legend(['list with labels'])
"""
plt.plot(x_axis, y_axis) 
plt.plot(secondx_axis, secondy_axis) 
plt.plot(secondx_axis, y_axis) 
plt.title('Just Some Random Numbers') 
plt.xlabel('The X-axis label') 
plt.ylabel('The Y-axis label') 
plt.legend(['Original Plot', 'Two New Axes', 'Old + New']) #list of strings 
plt.show() 
"""
#You can also label your plots by adding a label argument to plot()
"""
plt.plot(x_axis, y_axis, label = 'Original Plot') #see the label here
plt.plot(secondx_axis, secondy_axis, label = 'Two New Axes') 
plt.plot(secondx_axis, y_axis, label = 'Old + New') 
plt.title('Just Some Random Numbers') 
plt.xlabel('The X-axis label') 
plt.ylabel('The Y-axis label') 
plt.legend() #keep the parens empty
plt.show() 
"""
#If you wanted to style your lines, you can add arguments for that as well
#Most are self-explanatory. 
#There are many options available that you can use using this website
#	matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
#Just a quick example:
"""
plt.plot(x_axis, y_axis, color = 'k', linestyle = '--', 
	linewidth = 3, label = 'Original Plot') #black/dashed/thicker
plt.plot(secondx_axis, secondy_axis, color = '#ff0000', 
	marker = '.', label = 'Two New Axes') #red (using hexadecmial) points
plt.plot(secondx_axis, y_axis, color = 'b', linestyle = '-.', 
	marker = '*', label = 'Old + New') #run it to find out
plt.title('Just Some Random Numbers') 
plt.xlabel('The X-axis label') 
plt.ylabel('The Y-axis label') 
plt.legend() 
plt.show() 
"""
#You can also use a format string to condense the code
#Syntax is '[linemarker][linestyle][color]'
"""
plt.plot(x_axis, y_axis, 'k--', linewidth = 3, label = 'Original Plot') #same as previous
plt.plot(secondx_axis, secondy_axis, '.r', label = 'Two New Axes') #no line here
plt.plot(secondx_axis, y_axis, '*-.b', label = 'Old + New') #same as previous
plt.title('Just Some Random Numbers') 
plt.xlabel('The X-axis label') 
plt.ylabel('The Y-axis label') 
plt.legend() 
plt.show() 
"""
#Some other formatting for your graphs.
"""
plt.plot(x_axis, y_axis, color = 'k', linestyle = '--', 
	linewidth = 3, label = 'Original Plot') 
plt.plot(secondx_axis, secondy_axis, color = '#ff0000', 
	marker = '.', label = 'Two New Axes')
plt.plot(secondx_axis, y_axis, color = 'b', linestyle = '-.', 
	marker = '*', label = 'Old + New') 
plt.title('Just Some Random Numbers') 
plt.xlabel('The X-axis label') 
plt.ylabel('The Y-axis label') 
plt.legend() 
plt.grid(True) #shows gridlines
plt.tight_layout() #less empty space for the graph
plt.show() 
"""
#There are also some default styles available.
"""
print(plt.style.available) #prints styles in terminal

plt.style.use('ggplot') #the style you want to use
plt.plot(x_axis, y_axis, color = 'k', label = 'Original Plot') 
plt.plot(secondx_axis, secondy_axis, color = '#ff0000', label = 'Two New Axes')
plt.plot(secondx_axis, y_axis, color = 'b', label = 'Old + New') 
plt.title('Just Some Random Numbers') 
plt.xlabel('The X-axis label') 
plt.ylabel('The Y-axis label') 
plt.legend() 
plt.tight_layout() 
plt.show() 
"""
#More customization for graphs
"""
plt.style.use('ggplot') #the style you want to use
plt.xticks(ticks=x_axis, labels = x_axis) #customize ticks on x-axis
plt.plot(x_axis, y_axis, color = 'k', label = 'Original Plot') 
plt.fill_between(x_axis, y_axis, alpha = 0.25) #fill underneath the line
#alpha dictates opacity of fill, can use for other arguments
#You can also fill about a specific value by denoting a third argument
#Also can use where = (condition), interpolate = True to further customize.
#You can also have multiple fill_between() arguments
plt.axvline(25, label = 'Just Because') #vertical line where dictated
plt.xscale('log') #logarithmic x scale
plt.yscale('log') #log y scale
plt.title('Just Some Random Numbers') 
plt.xlabel('The X-axis label') 
plt.ylabel('The Y-axis label') 
plt.legend() 
plt.tight_layout() 
plt.show() 
"""
#There are other types of plots that you can use.
"""
plt.bar(x_axis, y_axis, width = 1) #prints a bar graph
#width allows you to edit the width of the bars
plt.show() #delete this line and run to line 185 to overlap graphs

import numpy as np #need numpy to not have overlap
x_array = np.arange(len(secondx_axis)) #new x values for non-overlapping bars
#CAN ONLY USE THIS WITH LISTS!
width = 0.125 #define a width for the bars to separate by 
#even bars: bar width/2, odd: bar width
plt.bar(x_array - width, y_axis, width = 0.25) #plots to the left of value
plt.bar(x_array + width, secondy_axis, width = 0.25) #right
plt.show()

plt.barh(x_axis, y_axis) #horizontal bar graph
#no width function here
plt.show() 

#pie chart (ONE DATA ARGUMENT ONLY)
labels = ['2', '16', '17', '24', '37']
colors = ['red', 'purple', 'yellow', '#022851', 'white'] #can use hexadecimal too
explode = [0, 0, 0.1, 0, 0] #for popping our pieces of the pie (relative to radius)
plt.pie(x_axis, labels = labels, colors = colors, 
	wedgeprops={'edgecolor': 'black'}, explode = explode,
	shadow = True, startangle = 180, #shadow for drop shadow, start angle of chart
	autopct = '%1.1f%%') #displaying percentages in pie piece
plt.show()

#histogram
bins = [10, 20, 30, 40]
plt.hist(x_axis, bins = 3, edgecolor = 'black') #bins: get data and divide by bin #
plt.hist(x_axis, bins = bins, edgecolor = 'black') #divide by defined bins
#Can plot with a log = True argument for a logarithmic scale.
plt.show()

#scatter plot
plt.scatter(x_axis, y_axis, s = 50, c = 'red', marker = 'X',
	edgecolor = 'black', linewidth = 1, alpha = 0.5) 
#s = size, c = color
#marker gives custom dots
#edgecolor for the edge of dots, linewidth for the edge thickness
#alpha makes the dots transparent
plt.scatter(x_axis, y_axis, s = 50, c = secondx_axis, cmap = 'Greens',
	marker = 'X', edgecolor = 'black', linewidth = 1, 
	alpha = 0.5) 
#c can be denoted by a list, cmap for more customization of color range
plt.scatter(x_axis, y_axis, s = secondy_axis, c = secondx_axis, cmap = 'Greens',
	marker = 'X', edgecolor = 'black', linewidth = 1, 
	alpha = 0.5) 
#s can also be denoted by a list
cbar = plt.colorbar()
cbar.set_label('Colors') #allows for showing what the dot color means
plt.show()
"""
#You can import .csv files to plot data (important for analyzing real-world data)
"""
import csv #imports ability to open csv files

with open('2002kings.csv') as csv_file: 
	csv_open = csv.DictReader(csv_file) #this creates a dictionary for the csv

	for line in csv_open:
		#print(line) #prints lines in the dictionary
#NOTE: Run the previous loop and the next lop separately.
g_count = 0 #counts PGs or SGs in dataset
f_count = 0 #counts SFs or PFs in dataset
c_count = 0 #counts Cs in dataset
for line in csv_open:
	player = line #because csv_open is not a dictionary, this allows us to use each line as a dictionary
	if 'G' in player['Position']: g_count += 1
	if 'F' in player['Position']: f_count += 1
	if 'C' in player['Position']: c_count += 1

	pos_counts = [g_count, f_count, c_count]
	print(pos_counts)

pos_xaxis = ['Guards', 'Forwards', 'Centers']
plt.bar(pos_xaxis, pos_counts)
plt.title('2002 Sacramento Kings by Position') 
plt.xlabel('Positions') 
plt.ylabel('# of Players') 
plt.show()

#There is so much more you can do with matplotlib now that you can use .csv files
#This is the end to my matplotlib tutorial.
#There is more to learn and there is a ton of documentation on it.
"""
