
# coding: utf-8

# ## Christina Chappell
# ### Geoprocessing Tool Assignment
# #### GEOG 458, 10 February 2017

# In[5]:

import arcpy


# This first cell creates the space for the geoprocessing tool. All of the parameters are set in this part, with user inputed values for the parameters. I also create the new feature class at the end.

# In[10]:

arcpy.env.overwriteOutput = True

##this will be the shapefile that will eventually be user provided
orig_shapefile = arcpy.GetParameterAsText(0)
##the created copy of the user provided
outclass =arcpy.GetParameterAsText(1)

#specified field that will be classifed. Will be doubles
infield = arcpy.GetParameterAsText(2)

# new field created with the reclassification. user generated
outfield = arcpy.GetParameterAsText(3)

# this will be the value used if the field is not 
# within the bounds in the table. notfoundvalue
default_value = arcpy.GetParameterAsText(4)

# table provided to classify with. 
# columns: lowerbound, upperbound, value
reclasstable = arcpy.GetParameterAsText(5)


arcpy.AddMessage("Parameters I am seeing:")

arcpy.AddMessage("0: "+ orig_shapefile + "this shapefile")
arcpy.AddMessage("1: "+ outclass +"new copy of shapefile")
arcpy.AddMessage("2: "+ infield + "field to classify")
arcpy.AddMessage("3: "+ outfield + "name of new field")
arcpy.AddMessage("4: "+ reclasstable + "table to classify with")

# Adds the original features to the copy file
arcpy.CopyFeatures_management(orig_shapefile, outclass)


# The second part does all of the work with the above parameters. Here I create a new field and use an Update Cursor to input values to the new field based on if the chosen field (infield) is between the values in the reclass table. If the value is not between the lower/upper bound then it is set to the default value chosen by the user. 

# In[11]:

# creates the new field in the copy of the original shapefile.
# this is the file we will be editing and adding the results to
arcpy.AddField_management(outclass, outfield, "DOUBLE", 9)

#To update the newly created field, using a double for loop
outclass_cursor = arcpy.da.UpdateCursor(outclass, [infield, outfield])

# this for loop runs through each row to populate the new field with the reclassification
for row in outclass_cursor:
    table_cursor = arcpy.da.SearchCursor(reclasstable, "*")
    hasUpdated = False
    for row2 in table_cursor:
        if (row[0] >= row2[1] and row[0] <= row2[2]): # within the ranges provided
            row[1] = row2[3]
            hasUpdated = True
    # This will put the default value for everything that does not fall within ranges.
    if (hasUpdated == False):
        row[1] = default_value
        hasUpdated = True
    outclass_cursor.updateRow(row)

    # I had help from a friend, informatics student,
    # to think through some of the logic of this part. 

del outclass_cursor
del table_cursor


# When I would encounter an error or a function/method that I was unfamiliar with, I would used the esri pages for definitions and stackoverflow to see code that had similar problems. None of the code was copied, it was all done by me. My friend in informatics helped with logic and trying to debug, but his focus is with java so it was broad help not specific coding. 
# 
# Overall time spent on this assignment: ~ 15 hours

# In[ ]:



