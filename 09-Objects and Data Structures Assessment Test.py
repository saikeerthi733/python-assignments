
# coding: utf-8

# # Objects and Data Structures Assessment Test

# ## Test your knowledge. 
# 
# ** Answer the following questions **

# Write a brief description of all the following Object Types and Data Structures we've learned about: 

# Numbers:the numbers can be integers and float type.here no need to mention the type of numbers like int/float
# 
# Strings:which means the collection of variables and they immutable.strings can be concatenated and sliced 
# 
# Lists:lists can have different data types which can be sorted and they mutable,and indexed,sliced and concatenated
# 
# Tuples:tuples are immutable
# 
# Dictionaries:in dictionaries values can be retrieved by keys and cant sorted  
# 

# ## Numbers
# 
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
# 
# Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

# In[ ]:


25*4+(1-0.75)


# Answer these 3 questions without typing code. Then type code to check your answer.
# 
#     What is the value of the expression 4 * (6 + 5)
#     
#     What is the value of the expression 4 * 6 + 5 
#     
#     What is the value of the expression 4 + 6 * 5 

# In[ ]:


44 27 34


# What is the *type* of the result of the expression 3 + 1.5 + 4?<br><br>

# What would you use to find a number’s square root, as well as its square? 

# In[ ]:


# Square root:
x


# In[ ]:


# Square:


# ## Strings

# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

# In[ ]:


s = 'hello'
# Print out 'e' using indexing

s[1]


# Reverse the string 'hello' using slicing:

# In[ ]:


s ='hello'
# Reverse the string using slicing

s.reverse()
s[-1:]


# Given the string hello, give two methods of producing the letter 'o' using indexing.

# In[ ]:


s ='hello'
# Print out the 'o'

# Method 1:

s[4]


# In[ ]:


# Method 2:
s[-1]


# ## Lists

# Build this list [0,0,0] two separate ways.

# In[ ]:


# Method 1:


# In[ ]:


# Method 2:


# Reassign 'hello' in this nested list to say 'goodbye' instead:

# In[ ]:


list3 = [1,2,[3,4,'hello']]

list3[2][2]='goodbye'
print(list3)


# Sort the list below:

# In[ ]:


list4 = [5,3,4,6,1]
list4.sort()
print(list4)


# ## Dictionaries

# Using keys and indexing, grab the 'hello' from the following dictionaries:

# In[ ]:


d = {'simple_key':'hello'}
# Grab 'hello'
d['simple_key']


# In[ ]:


d = {'k1':{'k2':'hello'}}
# Grab 'hello'
d['k1']['k2']


# In[ ]:


# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello
d['k1'][0]['nest_key'][2][0]


# In[ ]:


# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
d['k1'][2]['k2'][1]['tough'][2][0]


# Can you sort a dictionary? Why or why not?<br><br>

# ## Tuples

# What is the major difference between tuples and lists?<br><br>
# tuples are immutablle and lists are mutable

# How do you create a tuple?<br><br>

# ## Sets 

# What is unique about a set?<br><br>
# sets are unordered and they only have unique values

# Use a set to find the unique values of the list below:

# In[ ]:


list5 = [1,2,2,33,4,4,11,22,3,3,2]

list5.set()
print(list5)


# ## Booleans

# For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.
# 
# <table class="table table-bordered">
# <tr>
# <th style="width:10%">Operator</th><th style="width:45%">Description</th><th>Example</th>
# </tr>
# <tr>
# <td>==</td>
# <td>If the values of two operands are equal, then the condition becomes true.</td>
# <td> (a == b) is not true.</td>
# </tr>
# <tr>
# <td>!=</td>
# <td>If values of two operands are not equal, then condition becomes true.</td>
# <td> (a != b) is true.</td>
# </tr>
# <tr>
# <td>&gt;</td>
# <td>If the value of left operand is greater than the value of right operand, then condition becomes true.</td>
# <td> (a &gt; b) is not true.</td>
# </tr>
# <tr>
# <td>&lt;</td>
# <td>If the value of left operand is less than the value of right operand, then condition becomes true.</td>
# <td> (a &lt; b) is true.</td>
# </tr>
# <tr>
# <td>&gt;=</td>
# <td>If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.</td>
# <td> (a &gt;= b) is not true. </td>
# </tr>
# <tr>
# <td>&lt;=</td>
# <td>If the value of left operand is less than or equal to the value of right operand, then condition becomes true.</td>
# <td> (a &lt;= b) is true. </td>
# </tr>
# </table>

# What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# In[ ]:


# Answer before running cell
2 > 3false


# In[ ]:


# Answer before running cell
3 <= 2true


# In[ ]:


# Answer before running cell
3 == 2.0false


# In[ ]:


# Answer before running cell
3.0 == 3false


# In[ ]:


# Answer before running cell
4**0.5 != 2false


# Final Question: What is the boolean output of the cell block below?

# In[ ]:


# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']false


# ## Great Job on your first assessment! 
