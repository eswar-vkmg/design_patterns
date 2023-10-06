from subject import WeatherStation
from observer import SamsungDisplay, LGDisplay

if __name__ == "__main__":
    ws = WeatherStation()
    samsung_display = SamsungDisplay()
    lg_display = LGDisplay()

    ws.add(lg_display)
    print()
    ws.add(samsung_display)
    print()
    ws.temperature = 3
    print()
    ws.temperature = 55
    print()
    ws.remove(lg_display)
    print()
    ws.temperature = 10
