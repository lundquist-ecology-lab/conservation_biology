import folium

# Create a folium map centered at a given latitude and longitude
m = folium.Map(location=[20, 0], zoom_start=2)

# JavaScript to capture click coordinates
click_js = """
    function(e) {
        var lat = e.latlng.lat;
        var lng = e.latlng.lng;
        var popup = L.popup()
            .setLatLng(e.latlng)
            .setContent("Coordinates: " + lat.toFixed(5) + ", " + lng.toFixed(5))
            .openOn(map);
    }
"""

# Add the click event to the map with the JavaScript
m.add_child(folium.LatLngPopup())

# Save the map as an HTML file
m.save("clickable_map.html")

print("Map has been saved to 'clickable_map.html'. Open this file in a browser to use the interactive map.")
