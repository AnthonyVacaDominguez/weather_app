from flask import Flask,render_template
import requests
from dotenv import load_dotenv, dotenv_values

config = dotenv_values(".env")

app =Flask(__name__)

def get_weather_data(city):
    API_KEY = config["API_KEY"]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=es&units=metric"
    r = requests.get(url).json()
    print(r)
    return(r)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/weather")
def prueba():
    resultados= get_weather_data("Quito")
    ###print("-------------------------temp",resultados.get("temp"))obtener solo una parte
    temperatura=str(resultados["main"]["temp"])
    descripcion=str(resultados["weather"][0]["description"])
    icono=str(resultados["weather"][0]["icon"])
    r_json={'temperatura':temperatura,
            'descripcion':descripcion,
            'icono':icono,
            'ciudad':'Quito'
            }
    return render_template("weather.html",clima= r_json)
    
    
if __name__=="__main__":
    app.run(debug=True)