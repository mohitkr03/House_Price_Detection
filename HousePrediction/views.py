import pandas as pd
from django.shortcuts import render
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from .models import HouseData


def index(request):
    if request.method=="POST":
        beds=request.POST.get("beds")
        facing=request.POST.get("facing")
        club_house=request.POST.get("club_house")
        play_area=request.POST.get("play_area")
        water_supply=request.POST.get("water_supply")
        lift=request.POST.get("lift")
        nearby_hsptl_km=request.POST.get("nearby_hsptl_km")
        parking=request.POST.get("parking")
        furnished=request.POST.get("furnished")
        baths=request.POST.get("baths")
        size=request.POST.get("size")
        zip_code=request.POST.get("zip_code")
        # Load the CSV file 
        dataset = pd.read_csv('static/housing.csv')

        # Preprocess the data
        X = dataset.drop(['price'], axis=1)
        y = dataset['price']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create a linear regression model
        model = LinearRegression()

        # Train the model
        model.fit(X_train, y_train)

        # Predict the price of a new house
        # new_house = pd.DataFrame({'bedrooms': [beds], 'bathrooms': [baths], 'size': [size],'nearby_hsptl_km': [nearby_hsptl_km], 'zipcode': [zip_code]})
        new_house = pd.DataFrame({'bedrooms': [beds], 'bathrooms': [baths], 'size': [size],'facing': [facing],'club_house': [club_house],'play_area': [play_area],'water_supply': [water_supply],'lift': [lift],'nearby_hsptl_km': [nearby_hsptl_km],'parking': [parking],'furnished': [furnished], 'zipcode': [zip_code]})
        predicted_price = model.predict(new_house)
        return render(request, 'result.html', {'predicted_price': predicted_price[0]})
        
    dataset = pd.read_csv('static/housing.csv')
    bedrooms = sorted(dataset['bedrooms'].unique())
    bathrooms = sorted(dataset['bathrooms'].unique())
    sizes = sorted(dataset['size'].unique())
    nearby_hsptl_km = sorted(dataset['nearby_hsptl_km'].unique())
    zip_codes = sorted(dataset['zipcode'].unique())
    facing = sorted(dataset['facing'].unique())
    club_house = sorted(dataset['club_house'].unique())
    play_area = sorted(dataset['play_area'].unique())
    water_supply = sorted(dataset['water_supply'].unique())
    lift = sorted(dataset['lift'].unique())
    parking = sorted(dataset['parking'].unique())
    furnished = sorted(dataset['furnished'].unique())
    # return render(request,'index.html', {"bedrooms":bedrooms,"bathrooms":bathrooms, "sizes":sizes,"nearby_hsptl_km":nearby_hsptl_km, "zip_codes":zip_codes})
    return render(request,'index.html', {"bedrooms":bedrooms,"bathrooms":bathrooms, "sizes":sizes,"facing":facing,"club_house":club_house,"play_area":play_area,"water_supply":water_supply,"lift":lift,"nearby_hsptl_km":nearby_hsptl_km,"parking":parking,"furnished":furnished, "zip_codes":zip_codes})


def home(request):
    return render(request, 'base.html')