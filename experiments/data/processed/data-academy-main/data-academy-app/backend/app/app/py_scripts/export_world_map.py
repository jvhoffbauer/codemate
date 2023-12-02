import pandas as pd
import geopandas
import folium
from datetime import datetime


def get_statistics_df():
    statistic_df = pd.read_csv(
        'https://data.un.org/_Docs/SYB/CSV/SYB61_253_Population%20Growth%20Rates%20in%20Urban%20areas%20and%20Capital%20cities.csv',
        encoding='latin-1',
        header=1,
        usecols=range(1,9)
    )

    statistic_df.rename(
        columns = {
            statistic_df.columns[0]: 'Region or Country', 
            'Value': 'Urban Percentage'
        }, 
        inplace=True
    )

    return statistic_df


def get_urban_statistics_year(statistic_df, year):
    series_filter = statistic_df['Series'] == 'Urban population (percent)'
    year_filter = statistic_df['Year'] == year
    urban_df = statistic_df[series_filter & year_filter]
    urban_df = urban_df[['Region or Country', 'Urban Percentage']]
    return urban_df.astype({'Urban Percentage': 'float'})


def transform_to_geopandas(dataframe):
    country_geopandas = geopandas.read_file(
        geopandas.datasets.get_path('naturalearth_lowres')
    )
    return country_geopandas.merge(
        dataframe, 
        how='inner', 
        left_on=['name'], 
        right_on=['Region or Country']
    )


def generate_and_export_map(dataframe):
    urban_area_map = folium.Map()
    folium.Choropleth(
        geo_data=dataframe,
        name='choropleth',
        data=dataframe,
        columns=['Region or Country', 'Urban Percentage'],
        key_on='feature.properties.name',
        fill_color='Greens',
        nan_fill_color='Grey',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Percentage of population living in Urban areas'
    ).add_to(urban_area_map)
    urban_area_map.save(f'./exports/urban_population_{datetime.now()}.html')


if __name__ == "__main__":
    statistic_df = get_statistics_df()
    urban_df = get_urban_statistics_year(statistic_df, 2018)
    urban_geodf = transform_to_geopandas(urban_df)
    generate_and_export_map(urban_geodf)
