import missions

missions.show_title()
print("Choose a mission to learn more about:")
print("1-Perseverance | 2-James Webb | 3-Voyager 1 | 4-Hubble | 5-Curiosity")
print("6-Spitzer | 7-Cassini-Huygens | 8-New Horizons | 9-Galileo | 10-Kepler")
print("11-Chandra | 12-Juno | 13-TESS | 14-OSIRIS-REx | 15-Dawn")
print("16-SpaceX Starship | 17-Blue Origin | 18-Ariane 5 | 19-Soyuz")
print("20-Falcon 9 | 21-Atlas V | 22-Delta IV | 23-SLS")
print("24-Crew Dragon | 25-Starlink")

# NOVO - aceitar quit em qualquer formato
user_input = input("Enter your choice (1-25): ")
option = user_input.strip()  # Remove espaços em branco

# .lower() para aceitar 'QUIT', 'Quit', etc.
if option.lower() == 'quit' or option.lower() == 'q':
    print("👋 Thanks for exploring space missions!")
    print("🌟 Keep learning about God's amazing universe!")
    exit()
    
# Comparação de strings e validação de entrada
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
    
    # Mirror comparison with others famous telescopes
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
    
    # Using Comparators 
    print(f"🔍 Hubble Mirror Size: {hubble_mirror_size}m diameter")
    print(f"🔍 Spitzer Mirror Size: {spitzer_mirror_size}m diameter")
    print(f"🔍 Chandra Mirror Size: {chandra_mirror_size}m diameter")
    print(f"🔍 James Webb Mirror Size: {james_webb_mirror_size}m diameter")
    
    # Bigger or Smaller?
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
    print(f"Departed