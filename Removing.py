import numpy as np

# Load the data
var = np.genfromtxt(r"C:\Users\Pc Store\Downloads\Lending-company-Numeric-NAN\Lending-company-Numeric-NAN.csv"

               # fname: Name of the file to load
    ,dtype=float,              # dtype: Desired data type (e.g., float, int)
    delimiter=',',            # delimiter: Character used to separate values (default is whitespace)
    skip_header=1,            # skip_header: Skip the first line (useful for headers)
    skip_footer=1,            # skip_footer: Skip the last line (if necessary)
    usecols=(0, 1, 2),        # usecols: Read specific columns (e.g., 1st, 2nd, 3rd)
    filling_values=0,         # filling_values: Replace missing values with this value (0 in this case)
    comments='#',             # comments: Character indicating the start of comment lines
    converters={0: lambda x: float(x) * 2},  # converters: Custom function for converting the 1st column (multiply by 2)
    unpack=True,              # unpack: If True, the returned array is transposed
    ndmin=2,                  
    encoding='utf-8'
)

print(data)

