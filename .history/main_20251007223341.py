import stat
import missions

missions.show_title()
print("Choose a mission to learn more about:")
print("1-Perseverance | 2-James Webb | 3-Voyager 1 | 4-Hubble | 5-Curiosity")
print("6-Spitzer | 7-Cassini-Huygens | 8-New Horizons | 9-Galileo | 10-Kepler")
print("11-Chandra | 12-Juno | 13-TESS | 14-OSIRIS-REx | 15-Dawn")
print("16-SpaceX Starship | 17-Blue Origin | 18-Ariane 5 | 19-Soyuz")
print("20-Falcon 9 | 21-Atlas V | 22-Delta IV | 23-SLS")
print("24-Crew Dragon | 25-Starlink")

option = input("Enter your choice (1-25): ")

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
    status = "active"
    
    print(missions.mission1)
    print(f"🔴 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose} and analyze Martian geology")
    print(f"🚀 Launched: {launch_year} | 🛬 Landed: {landing_year}")
    print(f"💰 Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"📡 Current Status: {status}")
    print(f"🌟 Exploring God's creation on {planet} since {landing_year}!")

elif option == "2":
    # James Webb details
    mission_name = "James Webb Space Telescope"
    mission_type = "Space Telescope"
    specialty = "infrared observations"
    partners = "NASA, ESA, and CSA"
    launch_year = 2021
    orbit_location = "L2 Lagrange Point"
    mirror_size = 6.5  # meters
    cost = 10_000_000_000  # 10 billion USD
    
    print(missions.mission2)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: Advanced {specialty}")
    print(f"🪞 Primary Mirror: {mirror_size}m diameter")
    print(f"📍 Operating Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🤝 International Partnership: {partners}")
    print(f"✨ Revealing the wonders of God's universe since {launch_year}!")

elif option == "3":
    # Voyager 1 details
    mission_name = "Voyager 1"
    mission_type = "Space Probe"
    specialty = "interstellar exploration"
    partners = "NASA"
    launch_year = 1977
    orbit_location = "Interstellar Space"
    cost = 250_000_000  # 250 million USD
    
    print(missions.mission3)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: {specialty}")
    print(f"📍 Current Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🤝 Built by: {partners}")
    print(f"✨ Exploring the vastness of God's universe since {launch_year}!")

elif option == "4":
    # Hubble details
    mission_name = "Hubble Space Telescope"
    mission_type = "Space Telescope"
    specialty = "high-resolution imaging"
    partners = "NASA and ESA"
    launch_year = 1990
    orbit_location = "Low Earth Orbit"
    cost = 10_000_000_000  # 10 billion USD
    service_missions = 5
    
    print(missions.mission4)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: {specialty}")
    print(f"📍 Operating Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🛠️ Service Missions: {service_missions}")
    print(f"🤝 International Partnership: {partners}")
    print(f"🏭 Built by: {partners}")
    print(f"✨ Unveiling the beauty of God's universe since {launch_year}!")

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
    
    print(missions.mission5)
    print(f"🔴 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Mission: To {purpose} to understand Mars' geology")
    print(f"🚀 Launched: {launch_year} | 🛬 Landed: {landing_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Exploring God's creation on {planet} since {landing_year}!")

elif option == "6":
    # Spitzer details
    mission_name = "Spitzer Space Telescope"
    mission_type = "Space Telescope"
    specialty = "infrared observations"
    partners = "NASA and JPL"
    launch_year = 2003
    orbit_location = "Heliocentric Orbit"
    mirror_size = 0.85  # meters
    cost = 720_000_000  # 720 million USD
    
    print(missions.mission6)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: Advanced {specialty}")
    print(f"🪞 Primary Mirror: {mirror_size}m diameter")
    print(f"📍 Operating Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🤝 Built by: {partners}")
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
    
    print(missions.mission7)
    print(f"🪐 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose} and analyze Saturn's rings")
    print(f"🚀 Launched: {launch_year} | Arrived: {arrival_year}")
    print(f"Ended: {end_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
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
    
    print(missions.mission8)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("and gather data on these distant objects")
    print(f"🚀 Launched: {launch_year} | Arrived: {arrival_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
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
    
    print(missions.mission9)
    print(f"🪐 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("and analyze its atmosphere and magnetosphere")
    print(f"🚀 Launched: {launch_year} | Arrived: {arrival_year}")
    print(f"Ended: {end_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Exploring God's creation on {planet} from "
          f"{arrival_year} to {end_year}!")

elif option == "10":
    # Kepler details
    mission_name = "Kepler Space Telescope"
    mission_type = "Space Telescope"
    specialty = "exoplanet discovery"
    partners = "NASA and JPL"
    launch_year = 2009
    end_year = 2018
    mirror_size = 0.95  # meters
    cost = 600_000_000  # 600 million USD
    
    print(missions.mission10)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: {specialty}")
    print(f"🪞 Primary Mirror: {mirror_size}m diameter")
    print("📍 Operating Location: Earth-trailing heliocentric orbit")
    print(f"🚀 Launched: {launch_year} | Ended: {end_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🤝 Built by: {partners}")
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
    
    print(missions.mission11)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: Advanced {specialty}")
    print(f"🪞 Primary Mirror: {mirror_size}m diameter")
    print(f"📍 Operating Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🤝 Built by: {partners}")
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
    
    print(missions.mission12)
    print(f"🪐 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("and understand its formation and evolution")
    print(f"🚀 Launched: {launch_year} | Arrived: {arrival_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Exploring God's creation on {planet} since {arrival_year}!")

elif option == "13":
    # TESS details
    mission_name = "Transiting Exoplanet Survey Satellite (TESS)"
    mission_type = "Space Telescope"
    specialty = "exoplanet discovery"
    partners = "NASA and MIT"
    launch_year = 2018
    orbit_location = "High Earth Orbit"
    mirror_size = 0.1  # meters
    cost = 337_000_000  # 337 million USD
    
    print(missions.mission13)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: {specialty}")
    print(f"🪞 Primary Mirror: {mirror_size}m diameter")
    print(f"📍 Operating Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🤝 Built by: {partners}")
    print(f"✨ Discovering new worlds in God's universe since {launch_year}!")

elif option == "14":
    # OSIRIS-REx details
    mission_name = "OSIRIS-REx"
    mission_type = "Sample Return Mission"
    asteroid = "Bennu"
    purpose = "collect samples from the asteroid and return them to Earth"
    builder = "Lockheed Martin"
    launch_year = 2016
    arrival_year = 2018
    return_year = 2023
    cost = 800_000_000  # 800 million USD
    
    print(missions.mission14)
    print(f"🪐 {mission_type}: {mission_name}")
    print(f"📍 Target Asteroid: {asteroid}")
    print(f"🎯 Primary Mission: To {purpose} for analysis")
    print(f"🚀 Launched: {launch_year} | Arrived: {arrival_year}")
    print(f"Returned: {return_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
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
    
    print(missions.mission16)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("and revolutionize space travel")
    print(f"🚀 First Test Flight: {launch_year}")
    print(f"💰 Estimated Cost: {cost}")
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
    
    print(missions.mission17)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("and provide commercial space tourism")
    print(f"🚀 First Test Flight: {launch_year}")
    print(f"💰 Estimated Cost: {cost}")
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
    
    print(missions.mission18)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("for commercial and government clients")
    print(f"🚀 First Flight: {launch_year}")
    print(f"💰 Cost per Launch: ${cost_per_launch:,} USD")
    print(f"📊 Total Launches: {total_launches} as of 2023")
    print(f"🏭 Built by: {builder}")
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
    
    print(missions.mission19)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("and ensure safe crew transport")
    print(f"🚀 First Flight: {first_flight_year}")
    print(f"💰 Cost per Mission: ${cost_per_mission:,} USD")
    print(f"📊 Total Crewed Missions: {total_missions} as of 2023")
    print(f"🏭 Built by: {builder}")
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
    
    print(missions.mission20)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("for refurbishment and reuse, revolutionizing space access")
    print(f"🚀 First Flight: {first_flight_year}")
    print(f"💰 Cost per Launch: ${cost_per_launch:,} USD")
    print(f"📊 Total Launches: {total_launches} as of 2023")
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
    cost_per_launch = 109_000_000  # 109 million USD per launch
    
    print(missions.mission21)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("for commercial, government, and military clients")
    print(f"🚀 First Flight: {first_flight_year}")
    print(f"💰 Cost per Launch: ${cost_per_launch:,} USD")
    print(f"📊 Total Launches: {total_launches} as of 2023")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Delivering payloads into God's orbit "
          f"since {first_flight_year}!")

elif option == "22":
    # Delta IV details
    mission_name = "Delta IV"
    mission_type = "Heavy-Lift Launch Vehicle"
    purpose = "deliver large payloads to orbit"
    builder = "United Launch Alliance (ULA)"
    first_flight_year = 2002
    total_launches = 43  # Total launches as of 2023
    cost_per_launch = 164_000_000  # 164 million USD per launch
    
    print(missions.mission22)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("for government and military clients")
    print(f"🚀 First Flight: {first_flight_year}")
    print(f"💰 Cost per Launch: ${cost_per_launch:,} USD")
    print(f"📊 Total Launches: {total_launches} as of 2023")
    print(f"🏭 Built by: {builder}")
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
    
    print(missions.mission23)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print(f"and support Artemis missions to the {mission_location}")
    print(f"🚀 First Test Flight: {first_flight_year}")
    print(f"💰 Estimated Cost per Launch: ${cost_per_launch:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 The {mission_name} is the most powerful rocket "
          "ever built by humans!")

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
    
    print(missions.mission25)
    print(f"🛰️ {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("and connect underserved areas")
    print(f"🚀 First Satellite Launch: {launch_year}")
    print(f"💰 Estimated Total Cost: ${cost:,} USD")
    print(f"📊 Total Satellites Launched: {total_satellites} as of 2023")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Bringing internet access to all corners of "
          f"God's creation since {launch_year}!")

else:
    print("Invalid option. Please select a number between 1 and 25.")
    exit()