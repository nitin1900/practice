#i have to pratice more like this questions...(as i took heavy help from ai tho...)

class SpaceAge:
    def __init__(self,second):
        self.second=second
        self.earth_age=self.second/31557600
    
    def on_mercury(self):
        mercury_age=self.earth_age/0.2408467
        return round(mercury_age,2)
    
    def on_venus(self):
        venus_age=self.earth_age/0.61519726
        return round(venus_age,2)
    
    def on_earth(self):
        age=self.earth_age/1.0
        return round(age,2)
    
    def on_mars(self):
        mars_age=self.earth_age/1.8808158
        return round(mars_age,2)
    
    def on_jupiter(self):
        jupiter_age=self.earth_age/11.862615
        return round(jupiter_age,2)
    
    def on_saturn(self):
        saturn_age=self.earth_age/29.447498
        return round(saturn_age,2)
    
    def on_uranus(self):
        uranus_age=self.earth_age/84.016846
        return round(uranus_age,2)
    
    def on_neptune(self):
        neptune_age=self.earth_age/164.79132
        return round(neptune_age,2)

# --- THE DASHBOARD ---(by AI)

user_year= int(input("Enter your age in year: "))*31557600
age_other = SpaceAge(user_year)

planet = input("Enter a planet to see your age: ").lower()

if planet == "mercury":
    print(f"Your age on Mercury is: {age_other.on_mercury()}")
elif planet == "venus":
    print(f"Your age on Venus is: {age_other.on_venus()}")
elif planet == "earth":
    print(f"Your age on Earth is: {age_other.on_earth()}")
elif planet == "mars":
    print(f"Your age on mars is: {age_other.on_mars()}")
elif planet == "jupiter":
    print(f"Your age on jupiter is: {age_other.on_jupiter()}")
elif planet == "saturn":
    print(f"Your age on satuen is: {age_other.on_saturn()}")
elif planet == "uranus":
    print(f"Your age on uranus is: {age_other.on_uranus()}")
elif planet == "neptune":
    print(f"Your age on neptune is: {age_other.on_neptune()}")
else:
    print("Error: Planet not found in our solar system.")


#solution...(it was same no doubt...)

class SpaceAge:
    def __init__(self, seconds):
        self.earth_age = seconds / 31557600
    
    def on_earth(self):
        return round(self.earth_age,2)

    def on_mercury(self):
        return round(self.earth_age / 0.2408467,2)

    def on_venus(self):
        return round(self.earth_age / 0.61519726,2)

    def on_mars(self):
        return round(self.earth_age / 1.8808158,2)
        
    def on_jupiter(self):
        return round(self.earth_age / 11.862615,2)
        
    def on_saturn(self):
        return round(self.earth_age / 29.447498,2)
        
    def on_uranus(self):
        return round(self.earth_age / 84.016846,2)
        
    def on_neptune(self):
        return round(self.earth_age / 164.79132,2)