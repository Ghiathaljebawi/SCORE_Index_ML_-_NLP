# Function to one-hot encode multi-valued columns and sum the dummies
def encode_cat(df, column):
    """
    one-hot encode multi-valued columns and sum the dummies
    """
    col_data = df[column].str.split(',')
    dummies = pd.get_dummies(col_data.apply(pd.Series).stack())
    dummies = dummies.groupby(level=0).sum()    
    dummies.columns = [f"{column}_{val.strip()}" for val in dummies.columns]
    
    return dummies