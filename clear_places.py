import pandas as pd

places = pd.read_csv('places_with_moments.csv', index_col=0)
places = places[~places['monday'].isnull()]

places = places.reset_index(drop=True)
places.to_csv('places_cleaned.csv', index=False)