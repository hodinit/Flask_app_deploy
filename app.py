from flask import Flask, request, jsonify, render_template
import folium

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/map", methods=["POST"])
def map():
    lat = float(request.form.get("latitude"))
    lon = float(request.form.get("longitude"))
    m = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Marker([lat, lon], popup="Your Location").add_to(m)
    
    m.save('templates/map.html')
    return render_template("map.html")

app.run(debug=True)