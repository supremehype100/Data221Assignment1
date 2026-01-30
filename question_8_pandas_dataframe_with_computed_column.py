import pandas as pd

#Making dictionary
data = {
    "A":[1,2,2,1],
    "B":[3.1,4.2,1.5,6.3],
    "C":[800,150,400,210]
}
#Create a DataFrame using the provided column data.
dataframe = pd.DataFrame(data)


#Adding a new column, "D", derived from multiplying columns "A", and "C".
dataframe ["D"] = dataframe ["A"] * dataframe ["C"]

#Print the final DataFrame.
print(dataframe)
