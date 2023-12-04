def collect_data():
  """Gathers data relevant to traffic light control."""
  traffic_volume = int(input("Enter current traffic volume (vehicles/hour): "))
  rush_hour = bool(input("Is it rush hour? (y/n): "))
  pedestrian_crossing = bool(input("Are pedestrians crossing? (y/n): "))
  weather_condition = input("Enter current weather condition: ")
  special_event = bool(input("Is there a special event nearby? (y/n): "))
  return {
      "traffic_volume": traffic_volume,
      "rush_hour": rush_hour,
      "pedestrian_crossing": pedestrian_crossing,
      "weather_condition": weather_condition,
      "special_event": special_event,
  }

def analyze_traffic(data):
  """Analyzes traffic data and assigns a traffic level (low, medium, high)."""
  if data["traffic_volume"] < 500:
    traffic_level = "low"
  elif data["traffic_volume"] < 1500:
    traffic_level = "medium"
  else:
    traffic_level = "high"

  # Adjust traffic level based on additional factors
  if data["rush_hour"]:
    traffic_level = "high"
  if data["pedestrian_crossing"]:
    traffic_level = max(traffic_level, "medium")
  if data["weather_condition"] in ["rain", "snow"]:
    traffic_level = "medium"
  if data["special_event"]:
    traffic_level = "high"

  return traffic_level

def set_signal_timing(traffic_level):
  """Sets green light duration and other signal parameters based on traffic level."""
  green_light_duration = {
      "low": 30,
      "medium": 20,
      "high": 10,
  }[traffic_level]

  # Adjust other parameters (e.g., yellow light duration, pedestrian crossing phase)
  yellow_light_duration = 5
  pedestrian_phase_duration = 15 if traffic_level == "low" else 10

  return {
      "green_light_duration": green_light_duration,
      "yellow_light_duration": yellow_light_duration,
      "pedestrian_phase_duration": pedestrian_phase_duration,
  }

def main():
  """Runs the expert system and displays signal timing."""
  data = collect_data()
  traffic_level = analyze_traffic(data)
  signal_timing = set_signal_timing(traffic_level)

  print(f"Traffic level detected: {traffic_level}")
  print(f"Green light duration set to: {signal_timing['green_light_duration']} seconds")
  print(f"Yellow light duration set to: {signal_timing['yellow_light_duration']} seconds")
  print(f"Pedestrian phase duration set to: {signal_timing['pedestrian_phase_duration']} seconds")

if __name__ == "__main__":
  main()

#   Sample Input
# Enter current traffic volume (vehicles/hour): 800
# Is it rush hour? (y/n): y
# Are pedestrians crossing? (y/n): n
# Enter current weather condition: cloudy
# Is there a special event nearby? (y/n): n


