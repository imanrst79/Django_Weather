
from django.shortcuts import render


def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get(
            f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=5&API_KEY=1BAA8E93-B105-4532-A660-00F6B7AF53BD")

        try:
            api = json.loads(api_request.content)
        except Exception:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = 'Air quality is satisfactory, and air pollution poses little or no risk'
            category_color = "good"

        elif api[0]['Category']['Name'] == "Moderate":
            category_description = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution'
            category_color = "moderate"

        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
            category_color = "usg"

        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
            category_color = "unhealthy"

        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = 'Health alert: The risk of health effects is increased for everyone.'
            category_color = "veryunhealty"

        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = 'Health warning of emergency conditions: everyone is more likely to be affected.'
            category_color = "hazardous"

        return render(request, 'home.html', {
            'api': api,
            "category_description": category_description,
            "category_color": category_color
        })

    else:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=1BAA8E93-B105-4532-A660-00F6B7AF53BD")

        try:
            api = json.loads(api_request.content)
        except Exception:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = 'Air quality is satisfactory, and air pollution poses little or no risk'
            category_color = "good"

        elif api[0]['Category']['Name'] == "Moderate":
            category_description = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution'
            category_color = "moderate"

        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
            category_color = "usg"

        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
            category_color = "unhealthy"

        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = 'Health alert: The risk of health effects is increased for everyone.'
            category_color = "veryunhealty"

        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = 'Health warning of emergency conditions: everyone is more likely to be affected.'
            category_color = "hazardous"

        return render(request, 'home.html', {
            'api': api,
            "category_description": category_description,
            "category_color": category_color
        })


def about(request):
    return render(request, 'about.html', {})
