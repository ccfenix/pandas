# the asof join is copied from SignalSeeker's GitHub repo
def diffCols(df1, df2):
    """ Find columns in df1 not present in df2
    Return df1.columns  - df2.columns maintaining the order which the resulting
    columns appears in df1.

    Parameters:
    ----------
    df1 : pandas dataframe object
    df2 : pandas dataframe objct
    Pandas already offers df1.columns - df2.columns, but unfortunately
    the original order of the resulting columns is not maintained.
    """
    return [i for i in df1.columns if i not in df2.columns]


def aj(df1, df2, overwriteColumns=True, inplace=False):
    """ KDB+ like asof join.
    Finds prevailing values of df2 asof df1's index. The resulting dataframe
    will have same number of rows as df1.

    Parameters
    ----------
    df1 : Pandas dataframe
    df2 : Pandas dataframe
    overwriteColumns : boolean, default True
         The columns of df2 will overwrite the columns of df1 if they have the same
         name unless overwriteColumns is set to False. In that case, this function
         will only join columns of df2 which are not present in df1.
    inplace : boolean, default False.
        If True, adds columns of df2 to df1. Otherwise, create a new dataframe with
        columns of both df1 and df2.

    *Assumes both df1 and df2 have datetime64 index. """
    joiner = lambda x : x.asof(df1.index)
    if not overwriteColumns:
        # Get columns of df2 not present in df1
        cols = diffCols(df2, df1)
        if len(cols) > 0:
            df2 = df2.ix[:,cols]
    result = df2.apply(joiner)
    if inplace:
        for i in result.columns:
            df1[i] = result[i]
        return df1
    else:
        return result


