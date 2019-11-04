!pip install --upgrade git+https://github.com/m-wrzr/populartimes

import pandas as pd
import populartimes

API_KEY = 'AIzaSyAt9G7bpQr158qWnPnR_z1H9qNPlSuOrpI'

places = pd.read_csv('places1.csv', index_col=0)
places['monday'] = None
places['tuesday'] = None
places['wednesday'] = None
places['thursday'] = None
places['friday'] = None
places['saturday'] = None
places['sunday'] = None

def get_place_popular_moments(place_id):
    popular_moments = populartimes.get_id(API_KEY, place_id)
    if 'populartimes' in popular_moments:
        return popular_moments['populartimes']
    else:
        return None

for (index, row) in places.iterrows():
    print("Populating " + str(index))
    moments = get_place_popular_moments(row.place_id)
    if moments != None:
        places.at[index, 'monday'] = moments[0]['data']
        places.at[index, 'tuesday'] = moments[1]['data']
        places.at[index, 'wednesday'] = moments[2]['data']
        places.at[index, 'thursday'] = moments[3]['data']
        places.at[index, 'friday'] = moments[4]['data']
        places.at[index, 'saturday'] = moments[5]['data']
        places.at[index, 'sunday'] = moments[6]['data']

places.to_csv('places_with_moments.csv')
print(places)