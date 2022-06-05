# Distance Calculation App
This app helps to evaluate traveling distance between two adresses (origin-destination). 
The objective of this app is to facilitate the usage of the [Google Maps Distance API](https://developers.google.com/maps/documentation/distance-matrix/overview) by providing a user-friendly interface for making the rest to the Google API

Please visite the following [link](https://distance-calculation-app.herokuapp.com/) to enjoy a demo of the app or to use it to make actual calculations.
Please note that in order to be able to make an API request to the Google servers you will need a valid API key.
The app will not store the API credentials.

I'm always looking to improve and I know that this project could have been written differently so please don't hesitate to initiate issues or pull requests. 

## Installation

This repo is ready to run the app in a heroku like environement and will spin-up a web dyno automatically.

## main packages in the app :

```python
googlemaps
streamlit
```
a complete list of required packages can be found in requirements.txt

## Avalaible features
* upload a xlsx/xls file in the app and display it as a dataframe
* select the origin column and one or more distination columns
* define basic request parameters in order to configure API requests
* loading bar to display distance calculation progress
* download output file as CSV format with distances

## Planned features (not in delivery order)
* add OpenStreetMap client in order to be able to make free requests.
    * will need to add a sub procedure to geocode the adresses
* support for uploading csv files in the app
* insert succefull API calls as data in a POSTGRES table and display them in a line chart.


## License
[MIT](https://choosealicense.com/licenses/mit/)