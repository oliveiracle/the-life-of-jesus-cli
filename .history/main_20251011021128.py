import missions

# importing the missions module
missions.show_title()
print("Choose a mission to learn more about:")
print("1-Perseverance | 2-James Webb | 3-Voyager 1 | 4-Hubble | 5-Curiosity")
print("6-Spitzer | 7-Cassini-Huygens | 8-New Horizons | 9-Galileo | 10-Kepler")
print("11-Chandra | 12-Juno | 13-TESS | 14-OSIRIS-REx | 15-Dawn")
print("16-SpaceX Starship | 17-Blue Origin | 18-Ariane 5 | 19-Soyuz")
print("20-Falcon 9 | 21-Atlas V | 22-Delta IV | 23-SLS")
print("24-Crew Dragon | 25-Starlink")

# Accept quit in any format
user_input = input("Enter your choice (1-25): ")
option = user_input.strip()  # Remove whitespace

# Check for space agencies using 'in' operator
space_agencies = ["NASA", "ESA", "SpaceX", "Roscosmos", "CSA"]
agency_budget = {
    "NASA": 25_000_000_000,      # 25 billion USD
    "ESA": 7_000_000_000,        # 7 billion USD
    "SpaceX": 3_000_000_000,     # 3 billion USD
    "Roscosmos": 2_500_000_000,  # 2.5 billion USD
    "CSA": 1_500_000_000         # 1.5 billion USD
} 

if "NASA" in space_agencies:
    print(f"\n✅ NASA is involved with a budget of ${agency_budget['NASA']:,} USD") 
elif "ESA" in space_agencies:
    print(f"✅ ESA is involved with a budget of ${agency_budget['ESA']:,} USD")
elif "SpaceX" in space_agencies:
    print(f"✅ SpaceX is involved with a budget of ${agency_budget['SpaceX']:,} USD")   
elif "Roscosmos" in space_agencies:
    print(f"✅ Roscosmos is involved with a budget of ${agency_budget['Roscosmos']:,} USD")
elif "CSA" in space_agencies:
    print(f"✅ CSA is involved with a budget of ${agency_budget['CSA']:,} USD")







# Use .lower() to accept 'QUIT', 'Quit', etc.
if option.lower() == 'quit' or option.lower() == 'q':
    print("👋 Thanks for exploring space missions!")
    print("🌟 Keep learning about God's amazing universe!")
    exit()
    
# String comparison and input validation
if not option.isdigit() or int(option) < 1 or int(option) > 25:
    print(f"❌ '{option}' is not a valid mission number!")
    print("💡 Please choose a number between 1 and 25, or type 'quit' to exit.")
    exit()

if option == "1":
    # Perseverance details
    mission_name = "Perseverance"
    mission_type = "Mars Rover"
    planet = "Mars"
    purpose = "search for signs of past life"
    builder = "NASA's Jet Propulsion Laboratory"
    launch_year = 2020
    landing_year = 2021
    cost = 2_700_000_000  # 2.7 billion USD
    location = "Jezero Crater"
    current_situation = "actively exploring and sending data back to Earth"
    current_situation_formatted = current_situation.capitalize()
    
    print(missions.mission1)
    print(f"🔴 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose} and analyze Martian geology")
    print(f"🚀 Launched: {launch_year} | 🛬 Landed: {landing_year}")
    print(f"💰 Cost: ${cost:,} USD")
    print(f"📌 Current Location: {location}")
    print(f"📡 Current Status: {current_situation_formatted}")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Exploring God's creation on {planet} since {landing_year}!")

elif option == "2":
    # James Webb details
    mission_name = "James Webb Space Telescope"
    mission_type = "Space Telescope"
    specialty = "infrared observations"
    specialty_formatted = specialty.capitalize()  # "Infrared Observations"
    launch_year = 2021
    orbit_location = "L2 Lagrange Point"
    mirror_size = 6.5  # meters
    cost = 10_000_000_000  # 10 billion USD
    current_situation = "operational and sending stunning images"
    partners = "NASA, ESA, and CSA"
    partners_formatted = partners.replace(", ", " | ")
    
    print(missions.mission2)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: Advanced {specialty_formatted}")
    print(f"🪞 Primary Mirror: {mirror_size}m diameter")
    print(f"📍 Operating Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"📡 Current Status: {current_situation}")
    print(f"🤝 International Partnership: {partners_formatted}")
    print(f"✨ Revealing the wonders of God's universe since {launch_year}!")

elif option == "3":
    # Voyager 1 details
    mission_name = "Voyager 1"
    mission_type = "Space Probe"
    specialty = "interstellar exploration"
    specialty_formatted = specialty.capitalize()  # "Interstellar Exploration"
    partners = "NASA"
    launch_year = 1977
    orbit_location = "Interstellar Space"
    cost = 250_000_000  # 250 million USD
    current_situation = "still communicating with Earth"
    
    print(missions.mission3)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: {specialty_formatted}")
    print(f"📍 Current Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"📡 Current Status: {current_situation}")
    print(f"🤝 Built by: {partners}")
    print(f"✨ Exploring the vastness of God's universe since {launch_year}!")

elif option == "4":
    # Hubble details
    mission_name = "Hubble Space Telescope"
    mission_type = "Space Telescope"
    specialty = "high-resolution imaging"
    specialty_formatted = specialty.capitalize()  # "High-resolution Imaging"
    partners = "NASA and ESA"
    launch_year = 1990
    orbit_location = "Low Earth Orbit"
    cost = 10_000_000_000  # 10 billion USD
    service_missions = 5
    current_situation = "still operational and capturing breathtaking images"
    
    # Mirror comparison with other famous telescopes
    hubble_mirror_size = 2.4  # meters
    spitzer_mirror_size = 0.85  # meters
    james_webb_mirror_size = 6.5  # meters
    chandra_mirror_size = 1.2  # meters
    
    print(missions.mission4)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: {specialty_formatted}")
    print(f"📍 Operating Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🛠️ Service Missions: {service_missions}")
    print(f"🤝 International Partnership: {partners}")
    print(f"🏭 Built by: {partners}")
    print(f"📡 Current Status: {current_situation}")
    print(f"✨ Unveiling the beauty of God's universe since {launch_year}!")
    
    # Using comparison operators
    print(f"🔍 Hubble Mirror Size: {hubble_mirror_size}m diameter")
    print(f"🔍 Spitzer Mirror Size: {spitzer_mirror_size}m diameter")
    print(f"🔍 Chandra Mirror Size: {chandra_mirror_size}m diameter")
    print(f"🔍 James Webb Mirror Size: {james_webb_mirror_size}m diameter")
    
    # Size comparison logic
    if hubble_mirror_size > spitzer_mirror_size:
        print(f"📏 Hubble's mirror is larger than Spitzer's by "
              f"{hubble_mirror_size - spitzer_mirror_size:.2f}m")
    elif hubble_mirror_size > chandra_mirror_size:
        print(f"📏 Hubble's mirror is larger than Chandra's by "
              f"{hubble_mirror_size - chandra_mirror_size:.2f}m")
    elif hubble_mirror_size < james_webb_mirror_size:
        print(f"📏 Hubble's mirror is smaller than James Webb's by "
              f"{james_webb_mirror_size - hubble_mirror_size:.2f}m")
    else:
        print("📏 Hubble's mirror size is unique among these telescopes.")

elif option == "5":
    # Curiosity details
    mission_name = "Curiosity"
    mission_type = "Mars Rover"
    planet = "Mars"
    purpose = "analyze soil and rock samples"
    builder = "NASA's Jet Propulsion Laboratory"
    launch_year = 2011
    landing_year = 2012
    cost = 2_500_000_000  # 2.5 billion USD
    location = "Gale Crater"
    current_situation = "actively exploring and sending data back to Earth"
    
    print(missions.mission5)
    print(f"🔴 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Mission: To {purpose} to understand Mars' geology")
    print(f"🚀 Launched: {launch_year} | 🛬 Landed: {landing_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"📌 Current Location: {location}")
    print(f"📡 Current Status: {current_situation}")
    print(f"🌟 Exploring God's creation on {planet} since {landing_year}!")

elif option == "6":
    # Spitzer details
    mission_name = "Spitzer Space Telescope"
    mission_type = "Space Telescope"
    specialty = "infrared observations"
    specialty_formatted = specialty.capitalize()  # "Infrared Observations"
    partners = "NASA and JPL"
    launch_year = 2003
    orbit_location = "Heliocentric Orbit"
    mirror_size = 0.85  # meters
    cost = 720_000_000  # 720 million USD
    current_situation = "retired in 2020 after 16 years of service"
    active = False
    
    print(missions.mission6)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: Advanced {specialty_formatted}")
    print(f"🪞 Primary Mirror: {mirror_size}m diameter")
    print(f"📍 Operating Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🤝 Built by: {partners}")
    print(f"📡 Current Status: {current_situation}")
    print(f"✨ Revealing God's universe wonders since {launch_year}!")

elif option == "7":
    # Cassini-Huygens details
    mission_name = "Cassini-Huygens"
    mission_type = "Orbiter and Lander"
    planet = "Saturn"
    purpose = "study Saturn and its moons"
    builder = "NASA and Italy's ASI"
    launch_year = 1997
    arrival_year = 2004
    end_year = 2017
    cost = 3_900_000_000  # 3.9 billion USD
    current_situation = "mission ended in 2017 after 13 years of service"
    
    print(missions.mission7)
    print(f"🪐 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose} and analyze Saturn's rings")
    print(f"🚀 Launched: {launch_year} | Arrived: {arrival_year}")
    print(f"Ended: {end_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"📡 Current Status: {current_situation}")
    print(f"🌟 Exploring God's creation on {planet} from "
          f"{arrival_year} to {end_year}!")

elif option == "8":
    # New Horizons details
    mission_name = "New Horizons"
    mission_type = "Space Probe"
    planet = "Pluto and Kuiper Belt"
    purpose = "conduct a flyby of Pluto and study Kuiper Belt objects"
    builder = "Johns Hopkins University Applied Physics Laboratory"
    launch_year = 2006
    arrival_year = 2015
    cost = 700_000_000  # 700 million USD
    current_situation = "still exploring the Kuiper Belt"
    
    print(missions.mission8)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("and gather data on these distant objects")
    print(f"🚀 Launched: {launch_year} | Arrived: {arrival_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"📡 Current Status: {current_situation}")
    print(f"🌟 Exploring God's creation in the outer solar system "
          f"since {arrival_year}!")

elif option == "9":
    # Galileo details
    mission_name = "Galileo"
    mission_type = "Orbiter and Probe"
    planet = "Jupiter"
    purpose = "study Jupiter and its moons"
    builder = "NASA's Jet Propulsion Laboratory"
    launch_year = 1989
    arrival_year = 1995
    end_year = 2003
    cost = 1_600_000_000  # 1.6 billion USD
    current_situation = "mission ended in 2003 after 14 years of service"
    current_situation_formatted = current_situation.capitalize()
    partners = "NASA, ESA and Germany's DLR"
    partners_formatted = partners.replace(", ", " | ")
    
    print(missions.mission9)
    print(f"🪐 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("and analyze its atmosphere and magnetosphere")
    print(f"🚀 Launched: {launch_year} | Arrived: {arrival_year}")
    print(f"Ended: {end_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"📡 Current Status: {current_situation_formatted}")
    print(f"🤝 International Partnership: {partners_formatted}")
    print(f"🌟 Exploring God's creation on {planet} from "
          f"{arrival_year} to {end_year}!")

elif option == "10":
    # Kepler details
    mission_name = "Kepler Space Telescope"
    mission_type = "Space Telescope"
    specialty = "exoplanet discovery"
    specialty_formatted = specialty.capitalize()  # "Exoplanet Discovery"
    partners = "NASA and JPL"
    launch_year = 2009
    end_year = 2018
    mirror_size = 0.95  # meters
    cost = 600_000_000  # 600 million USD
    current_situation = ("retired in 2018 after discovering thousands "
                         "of exoplanets")
    current_situation_formatted = current_situation.capitalize()
    
    print(missions.mission10)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: {specialty_formatted}")
    print(f"🪞 Primary Mirror: {mirror_size}m diameter")
    print("📍 Operating Location: Earth-trailing heliocentric orbit")
    print(f"🚀 Launched: {launch_year} | Ended: {end_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🤝 Built by: {partners}")
    print(f"📡 Current Status: {current_situation_formatted}")
    print(f"✨ Discovering new worlds in God's universe from "
          f"{launch_year} to {end_year}!")

elif option == "11":
    # Chandra details
    mission_name = "Chandra X-ray Observatory"
    mission_type = "Space Telescope"
    specialty = "X-ray observations"
    partners = "NASA and Smithsonian Astrophysical Observatory"
    launch_year = 1999
    orbit_location = "High Earth Orbit"
    mirror_size = 1.2  # meters
    cost = 1_600_000_000  # 1.6 billion USD
    current_situation = "still operational and capturing high-energy phenomena"
    current_situation_formatted = current_situation.capitalize()
    
    print(missions.mission11)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: Advanced {specialty}")
    print(f"🪞 Primary Mirror: {mirror_size}m diameter")
    print(f"📍 Operating Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🤝 Built by: {partners}")
    print(f"📡 Current Status: {current_situation_formatted}")
    print(f"✨ Revealing the high-energy universe of God's creation "
          f"since {launch_year}!")

elif option == "12":
    # Juno details
    mission_name = "Juno"
    mission_type = "Orbiter"
    planet = "Jupiter"
    purpose = "study Jupiter's atmosphere, magnetic field, and structure"
    builder = "Lockheed Martin"
    launch_year = 2011
    arrival_year = 2016
    cost = 1_100_000_000  # 1.1 billion USD
    current_situation = "actively orbiting and sending data back to Earth"
    current_situation_formatted = current_situation.capitalize()
    size = "20 feet tall"
    weight = 3_600  # pounds
    solar_panels_span = 66  # feet
    
    print(missions.mission12)
    print(f"🪐 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("and understand its formation and evolution")
    print(f"🚀 Launched: {launch_year} | Arrived: {arrival_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"📏 Size: {size} | Weight: {weight} pounds")
    print(f"📐 Solar Panel Span: {solar_panels_span} feet")
    print(f"📡 Current Status: {current_situation_formatted}")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Exploring God's creation on {planet} since {arrival_year}!")

elif option == "13":
    # TESS details
    mission_name = "Transiting Exoplanet Survey Satellite (TESS)"
    mission_type = "Space Telescope"
    specialty = "exoplanet discovery"
    partners = "NASA, MIT, and Harvard"
    partners_formatted = partners.replace(", ", " | ")
    launch_year = 2018
    orbit_location = "High Earth Orbit"
    mirror_size = 0.1  # meters
    cost = 337_000_000  # 337 million USD
    current_situation = "actively discovering new exoplanets"
    current_situation_formatted = current_situation.capitalize()
    size = "13.2 feet tall"
    weight = 1_200  # pounds
    mirror_count = 4

    print(missions.mission13)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: {specialty}")
    print(f"🪞 Primary Mirror: {mirror_size}m diameter")
    print(f"📍 Operating Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"📏 Size: {size} | Weight: {weight} pounds")
    print(f"🔍 Number of Mirrors: {mirror_count}")
    print(f"📡 Current Status: {current_situation_formatted}")
    print(f"🤝 Built by: {partners_formatted}")
    print(f"✨ Discovering new worlds in God's universe since {launch_year}!")

elif option == "14":
    # OSIRIS-REx details
    mission_name = "OSIRIS-REx"
    mission_type = "Sample Return Mission"
    asteroid = "Bennu"
    purpose = "collect samples from the asteroid and return them to Earth"
    purpose_formatted = purpose.capitalize()  # .capitalize()
    builder = "Lockheed Martin"
    launch_year = 2016
    arrival_year = 2018
    return_year = 2023
    cost = 800_000_000  # 800 million USD
    current_situation = "sample capsule returned to Earth in 2023"
    orbit_location = "Near-Earth Asteroid"

    print(missions.mission14)
    print(f"🪐 {mission_type}: {mission_name}")
    print(f"📍 Target Asteroid: {asteroid}")
    print(f"🎯 Primary Mission: {purpose_formatted} for analysis")
    print(f"🚀 Launched: {launch_year} | Arrived: {arrival_year}")
    print(f"Returned: {return_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"📍 Operating Location: {orbit_location}")
    print(f"📡 Current Status: {current_situation}")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Exploring God's creation in the asteroid belt "
          f"since {arrival_year}!")

elif option == "15":
    # Dawn details
    mission_name = "Dawn"
    mission_type = "Orbiter"
    purpose = "study the two largest objects in the asteroid belt"
    builder = "Orbital ATK"
    launch_year = 2007
    arrival_vesta_year = 2011
    departure_vesta_year = 2012
    arrival_ceres_year = 2015
    end_year = 2018
    cost = 500_000_000  # 500 million USD
    current_situation = "mission ended in 2018 after running out of fuel"

    print(missions.mission15)
    print(f"🪐 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}, Vesta and Ceres")
    print("and understand their formation and evolution")
    print(f"🚀 Launched: {launch_year}")
    print(f"🛬 Arrived at Vesta: {arrival_vesta_year}")
    print(f"Departed Vesta: {departure_vesta_year}")
    print(f"🛬 Arrived at Ceres: {arrival_ceres_year}")
    print(f"Mission Ended: {end_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"📡 Current Status: {current_situation}")
    print(f"🌟 Exploring God's creation in asteroid belt from "
          f"{arrival_vesta_year} to {end_year}!")

elif option == "16":
    # SpaceX Starship details
    mission_name = "SpaceX Starship"
    mission_type = "Interplanetary Spacecraft"
    purpose = "enable human missions to Mars and beyond"
    builder = "SpaceX"
    launch_year = 2023  # First test flight year
    cost = "TBD"  # Cost is still to be determined
    reusable = True
    capacity = "100+ tons to LEO"
    payload = "100+ people"
    reliability = "In development"

    print(missions.mission16)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("and revolutionize space travel")
    print(f"🚀 First Test Flight: {launch_year}")
    print(f"💰 Estimated Cost: {cost}")
    print(f"♻️ Reusable: {reusable}")
    print(f"📦 Payload Capacity: {capacity}")
    print(f"👨‍🚀 Crew Capacity: {payload}")
    print(f"📈 Reliability: {reliability}")
    print(f"🏭 Built by: {builder}")
    print("🌟 Pioneering human exploration of God's universe!")

elif option == "17":
    # Blue Origin details
    mission_name = "Blue Origin New Shepard"
    mission_type = "Suborbital Spaceflight Vehicle"
    purpose = "take passengers to the edge of space"
    builder = "Blue Origin"
    launch_year = 2015  # First test flight year
    cost = "TBD"  # Cost is still to be determined
    horsepower = 110_000  # 110,000 pounds of thrust
    reusable = True
    reliability = "100% success rate in its last 15 flights"

    print(missions.mission17)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("and provide commercial space tourism")
    print(f"🚀 First Test Flight: {launch_year}")
    print(f"💰 Estimated Cost: {cost}")
    print(f"💪 Thrust: {horsepower:,} pounds")
    print(f"♻️ Reusable: {reusable}")
    print(f"📈 Reliability: {reliability}")
    print(f"🏭 Built by: {builder}")
    print("🌟 Offering a glimpse of God's creation from space!")

elif option == "18":
    # Ariane 5 details
    mission_name = "Ariane 5"
    mission_type = "Heavy-Lift Launch Vehicle"
    purpose = "deliver payloads to orbit"
    builder = "Arianespace and ESA"
    launch_year = 1996  # First flight year
    cost_per_launch = 165_000_000  # 165 million USD per launch
    total_launches = 111  # Total launches as of 2023
    horsepower = 2_200_000  # 2.2 million pounds of thrust
    size = "171 feet tall"
    reliability = "95% success rate"

    print(missions.mission18)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("for commercial and government clients")
    print(f"🚀 First Flight: {launch_year}")
    print(f"💰 Cost per Launch: ${cost_per_launch:,} USD")
    print(f"📊 Total Launches: {total_launches} as of 2023")
    print(f"🏭 Built by: {builder}")
    print(f"💪 Thrust: {horsepower:,} pounds")
    print(f"📏 Size: {size}")
    print(f"📈 Reliability: {reliability}")
    print(f"🌟 Delivering payloads into God's orbit since {launch_year}!")

elif option == "19":
    # Soyuz details
    mission_name = "Soyuz"
    mission_type = "Crewed Spacecraft"
    purpose = "transport astronauts to and from the ISS"
    builder = "Roscosmos"
    first_flight_year = 1967
    total_missions = 140  # Total crewed missions as of 2023
    cost_per_mission = 90_000_000  # 90 million USD per mission
    current_situation = "still in use for crewed missions to the ISS"
    size = "49.5 feet tall"
    payload = "7,000 pounds to LEO"

    print(missions.mission19)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("and ensure safe crew transport")
    print(f"🚀 First Flight: {first_flight_year}")
    print(f"💰 Cost per Mission: ${cost_per_mission:,} USD")
    print(f"📊 Total Crewed Missions: {total_missions} as of 2023")
    print(f"🏭 Built by: {builder}")
    print(f"📏 Size: {size}")
    print(f"📦 Payload Capacity: {payload}")
    print(f"📡 Current Status: {current_situation}")
    print(f"🌟 Safely transporting astronauts in God's creation "
          f"since {first_flight_year}!")

elif option == "20":
    # Falcon 9 details
    mission_name = "Falcon 9"
    mission_type = "Reusable Rocket"
    purpose = "deliver payloads to orbit and return to Earth"
    builder = "SpaceX"
    first_flight_year = 2010
    total_launches = 200  # Total launches as of 2023
    cost_per_launch = 62_000_000  # 62 million USD per launch
    horsepower = 1_710_000  # 1.71 million pounds of thrust
    reusable = True
    reliability = "98% success rate"

    print(missions.mission20)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("for refurbishment and reuse, revolutionizing space access")
    print(f"🚀 First Flight: {first_flight_year}")
    print(f"💰 Cost per Launch: ${cost_per_launch:,} USD")
    print(f"📊 Total Launches: {total_launches} as of 2023")
    print(f"💪 Thrust: {horsepower:,} pounds")
    print(f"♻️ Reusable: {reusable}")
    print(f"📈 Reliability: {reliability}")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Making space more accessible in God's creation "
          f"since {first_flight_year}!")

elif option == "21":
    # Atlas V details
    mission_name = "Atlas V"
    mission_type = "Launch Vehicle"
    purpose = "deliver payloads to a variety of orbits"
    builder = "United Launch Alliance (ULA)"
    first_flight_year = 2002
    total_launches = 87  # Total launches as of 2023
    horsepower = 940_000  # 940,000 pounds of thrust
    size = "191 feet tall"
    reliability = "100% success rate in its last 29 launches"
    bigger_than_falcon_heavy = False
    bigger_than_sls = False
    
    # Using comparison operators
    cost_per_launch = 109_000_000  # 109 million USD per launch
    ariane5_cost_per_launch = 165_000_000  # 165 million USD per launch
    sls_cost_per_launch = 2_000_000_000  # 2 billion USD per launch
    falcon_cost_per_launch = 62_000_000  # 62 million USD per launch
    delta_iv_cost_per_launch = 164_000_000  # 164 million USD per launch

    print(missions.mission21)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("for commercial, government, and military clients")
    print(f"🚀 First Flight: {first_flight_year}")
    print(f"💰 Cost per Launch: ${cost_per_launch:,} USD")
    print(f"📊 Total Launches: {total_launches} as of 2023")
    print(f"🏭 Built by: {builder}")
    print(f"💪 Thrust: {horsepower:,} pounds")
    print(f"📏 Size: {size}")
    print(f"🔍 Is it bigger than Falcon Heavy? {bigger_than_falcon_heavy}")
    print(f"🔍 Is it bigger than SLS? {bigger_than_sls}")
    print(f"🌟 Delivering payloads into God's orbit "
          f"since {first_flight_year}!")
    
    # Cost comparison with other rockets
    if ariane5_cost_per_launch < sls_cost_per_launch:
        print(f"📏 SLS is way more expensive than Ariane 5 by "
              f"${sls_cost_per_launch - ariane5_cost_per_launch:,} USD")
    if ariane5_cost_per_launch > falcon_cost_per_launch:
        print(f"📏 Ariane 5 is more expensive than Falcon 9 by "
              f"${ariane5_cost_per_launch - falcon_cost_per_launch:,} USD")
    elif ariane5_cost_per_launch > delta_iv_cost_per_launch:
        print(f"📏 Ariane 5 is more expensive than Delta IV by "
              f"${ariane5_cost_per_launch - delta_iv_cost_per_launch:,} USD")
    elif sls_cost_per_launch > falcon_cost_per_launch:
        print(f"📏 SLS is way more expensive than Falcon 9 by "
              f"${sls_cost_per_launch - falcon_cost_per_launch:,} USD")
    else:
        print("📏 Ariane 5's cost per launch is unique among these rockets.")

elif option == "22":
    # Delta IV details
    mission_name = "Delta IV"
    mission_type = "Heavy-Lift Launch Vehicle"
    purpose = "deliver large payloads to orbit"
    builder = "United Launch Alliance (ULA)"
    first_flight_year = 2002
    total_launches = 43  # Total launches as of 2023
    cost_per_launch = 164_000_000  # 164 million USD per launch
    horsepower = 2_100_000  # 2.1 million pounds of thrust
    size = "235 feet tall"
    bigger_than_sls = False
    bigger_than_falcon_heavy = True

    print(missions.mission22)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("for government and military clients")
    print(f"🚀 First Flight: {first_flight_year}")
    print(f"💰 Cost per Launch: ${cost_per_launch:,} USD")
    print(f"📊 Total Launches: {total_launches} as of 2023")
    print(f"🏭 Built by: {builder}")
    print(f"💪 Thrust: {horsepower:,} pounds")
    print(f"📏 Size: {size}")
    print(f"🔍 Is it bigger than Falcon Heavy? {bigger_than_falcon_heavy}")
    print(f"🔍 Is it bigger than SLS? {bigger_than_sls}")
    print(f"🌟 Delivering heavy payloads into God's orbit "
          f"since {first_flight_year}!")

elif option == "23":
    # SLS details
    mission_name = "Space Launch System (SLS)"
    mission_location = "Moon and beyond"
    mission_type = "Heavy-Lift Launch Vehicle"
    purpose = "enable human exploration beyond low Earth orbit"
    builder = "NASA and Boeing"
    first_flight_year = 2022  # First test flight year
    cost_per_launch = 2_000_000_000  # 2 billion USD per launch
    horsepower = 8_800_000  # 8.8 million pounds of thrust
    size = "322 feet tall"
    bigger_than_falcon_heavy = True
    
    # Rocket height comparisons (in feet)
    delta_iv_height = 235      # Delta IV
    sls_height = 322           # SLS (already defined above)
    falcon_heavy_height = 229  # Falcon Heavy (real data)

    print(missions.mission23)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print(f"and support Artemis missions to the {mission_location}")
    print(f"🚀 First Test Flight: {first_flight_year}")
    print(f"💰 Estimated Cost per Launch: ${cost_per_launch:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"💪 Thrust: {horsepower:,} pounds")
    print(f"📏 Size: {size}")
    print(f"🔍 Bigger than Falcon Heavy: {bigger_than_falcon_heavy}")
    print(f"🌟 The {mission_name} is the most powerful rocket "
          "ever built by humans!")
    
    # Height comparison with other heavy rockets
    print(f"📏 Delta IV Height: {delta_iv_height} feet")
    print(f"🔍 Compared to SLS ({sls_height} feet): "
          f"{delta_iv_height - sls_height:+d} feet")
    print(f"🔍 Compared to Falcon Heavy ({falcon_heavy_height} feet): "
          f"{delta_iv_height - falcon_heavy_height:+d} feet")
    print(f"🌟 Delivering heavy payloads into God's orbit "
          f"since {first_flight_year}!")

elif option == "24":
    # Crew Dragon details
    mission_name = "Crew Dragon"
    mission_type = "Crewed Spacecraft"
    purpose = "transport astronauts to and from the ISS"
    builder = "SpaceX"
    first_flight_year = 2020  # First crewed flight year
    cost_per_mission = 55_000_000  # 55 million USD per mission

    print(missions.mission24)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("and ensure safe crew transport")
    print(f"🚀 First Crewed Flight: {first_flight_year}")
    print(f"💰 Estimated Cost per Mission: ${cost_per_mission:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Safely transporting astronauts in God's creation "
          f"since {first_flight_year}!")

elif option == "25":
    # Starlink details
    mission_name = "Starlink"
    mission_type = "Satellite Constellation"
    purpose = "provide global internet coverage"
    builder = "SpaceX"
    launch_year = 2019  # First satellite launch year
    total_satellites = 4000  # Total satellites launched as of 2023
    cost = 10_000_000_000  # 10 billion USD (estimated total cost)
    number_of_launches = 60  # Total launches as of 2023
    number_of_satellites_orbit = 4000  # Total satellites in orbit as of 2023

    print(missions.mission25)
    print(f"🛰️ {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("and connect underserved areas")
    print(f"🚀 First Satellite Launch: {launch_year}")
    print(f"💰 Estimated Total Cost: ${cost:,} USD")
    print(f"📊 Total Satellites Launched: {total_satellites} as of 2023")
    print(f"🏭 Built by: {builder}")
    print(f"📡 Total Launches: {number_of_launches} as of 2023")
    print(f"🛰️ Total Satellites in Orbit: {number_of_satellites_orbit}")
    print(f"🌟 Bringing internet access to all corners of "
          f"God's creation since {launch_year}!")

else:
    print("Invalid option. Please select a number between 1 and 25.")
    exit()

# Containment Operators - Space Mission Search Feature
print("\n🔍 SPACE MISSION SEARCH FEATURE:")
print("=" * 50)

# Create mission database for searching
all_missions = [
    "Perseverance", "James Webb", "Voyager 1", "Hubble", "Curiosity",
    "Spitzer", "Cassini-Huygens", "New Horizons", "Galileo", "Kepler",
    "Chandra", "Juno", "TESS", "OSIRIS-REx", "Dawn", "SpaceX Starship",
    "Blue Origin", "Ariane 5", "Soyuz", "Falcon 9", "Atlas V",
    "Delta IV", "SLS", "Crew Dragon", "Starlink"
]

# Mission categories using containment operators
telescope_missions = [
    "James Webb", "Hubble", "Spitzer", "Chandra", "Kepler", "TESS"
]
rover_missions = ["Perseverance", "Curiosity"]
spacecraft_missions = [
    "Voyager 1", "New Horizons", "Galileo", "Juno", "OSIRIS-REx"
]
rocket_missions = [
    "SpaceX Starship", "Ariane 5", "Soyuz", "Falcon 9", "Atlas V",
    "Delta IV", "SLS"
]


# Check for space agencies using 'in' operator
space_agencies = ["NASA", "ESA", "SpaceX", "Roscosmos", "CSA"]
mission_description = "NASA's Perseverance Mars Rover built by JPL"








# Search functionality using 'in' operator
search_term = "Webb"
print(f"🔎 Searching for missions containing '{search_term}':")
for mission in all_missions:
    if search_term in mission:
        print(f"✅ Found: {mission}")

# Mission type checker using 'in' operator
example_mission = "Hubble"
print(f"\n🔬 Analyzing mission type for: {example_mission}")

if example_mission in telescope_missions:
    print(f"🔭 {example_mission} is a TELESCOPE mission!")
elif example_mission in rover_missions:
    print(f"🚗 {example_mission} is a ROVER mission!")
elif example_mission in spacecraft_missions:
    print(f"🚀 {example_mission} is a SPACECRAFT mission!")
elif example_mission in rocket_missions:
    print(f"🚀 {example_mission} is a ROCKET/LAUNCH VEHICLE!")
else:
    print(f"❓ {example_mission} mission type not categorized")

# Check for space agencies using 'in' operator
space_agencies = ["NASA", "ESA", "SpaceX", "Roscosmos", "CSA"]
mission_description = "NASA's Perseverance Mars Rover built by JPL"

print("\n🏢 Space agencies involved in this mission:")
for agency in space_agencies:
    if agency in mission_description:
        print(f"✅ {agency} is involved!")

# Check for planets/targets using 'not in' operator
planets_targets = [
    "Mars", "Jupiter", "Saturn", "Earth", "Moon", "Asteroid", "Pluto"
]
example_description = "James Webb Space Telescope observing distant galaxies"

print(f"\n🌍 Checking planetary targets in: '{example_description}'")
planets_found = []
for planet in planets_targets:
    if planet in example_description:
        planets_found.append(planet)

if planets_found:
    print(f"🎯 Targets found: {', '.join(planets_found)}")
else:
    print("🌌 This mission explores deep space/general universe!")

# Validate mission numbers using 'in' operator
valid_options = "123456789101112131415161718192021222324925"
user_example = "7"

if user_example in valid_options:
    print(f"\n✅ '{user_example}' is a valid mission choice!")
else:
    print(f"\n❌ '{user_example}' is not a valid mission choice!")
