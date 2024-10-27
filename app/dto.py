from dataclasses import dataclass

@dataclass
class Condition:
    text: str
    icon: str
    code: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            text=data["text"],
            icon=data["icon"],
            code=data["code"]
        )

@dataclass
class CurrentWeather:
    last_updated_epoch: int
    last_updated: str
    temp_c: float
    temp_f: float
    is_day: int
    condition: Condition
    wind_mph: float
    wind_kph: float
    wind_degree: int
    wind_dir: str
    pressure_mb: float
    pressure_in: float
    precip_mm: float
    precip_in: float
    humidity: int
    cloud: int
    feelslike_c: float
    feelslike_f: float
    windchill_c: float
    windchill_f: float
    heatindex_c: float
    heatindex_f: float
    dewpoint_c: float
    dewpoint_f: float
    vis_km: float
    vis_miles: float
    uv: float
    gust_mph: float
    gust_kph: float

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            last_updated_epoch=data["last_updated_epoch"],
            last_updated=data["last_updated"],
            temp_c=data["temp_c"],
            temp_f=data["temp_f"],
            is_day=data["is_day"],
            condition=Condition.from_dict(data["condition"]),
            wind_mph=data["wind_mph"],
            wind_kph=data["wind_kph"],
            wind_degree=data["wind_degree"],
            wind_dir=data["wind_dir"],
            pressure_mb=data["pressure_mb"],
            pressure_in=data["pressure_in"],
            precip_mm=data["precip_mm"],
            precip_in=data["precip_in"],
            humidity=data["humidity"],
            cloud=data["cloud"],
            feelslike_c=data["feelslike_c"],
            feelslike_f=data["feelslike_f"],
            windchill_c=data["windchill_c"],
            windchill_f=data["windchill_f"],
            heatindex_c=data["heatindex_c"],
            heatindex_f=data["heatindex_f"],
            dewpoint_c=data["dewpoint_c"],
            dewpoint_f=data["dewpoint_f"],
            vis_km=data["vis_km"],
            vis_miles=data["vis_miles"],
            uv=data["uv"],
            gust_mph=data["gust_mph"],
            gust_kph=data["gust_kph"]
        )

@dataclass
class Location:
    name: str
    region: str
    country: str
    lat: float
    lon: float
    tz_id: str
    localtime_epoch: int
    localtime: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data["name"],
            region=data["region"],
            country=data["country"],
            lat=data["lat"],
            lon=data["lon"],
            tz_id=data["tz_id"],
            localtime_epoch=data["localtime_epoch"],
            localtime=data["localtime"]
        )

@dataclass
class WeatherData:
    location: Location
    current: CurrentWeather

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            location=Location.from_dict(data["location"]),
            current=CurrentWeather.from_dict(data["current"])
        )
