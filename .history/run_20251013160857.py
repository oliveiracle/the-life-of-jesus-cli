# ==============================================================================
# THE LIFE OF JESUS CHRIST CLI
# ==============================================================================
import jesus_moments

# ==============================================================================
# 1. TITLE AND MAIN MENU
# ==============================================================================
jesus_moments.show_title()
print("Explore 25 key moments from the life of Jesus Christ:\n")

print("🌟 BIRTH & CHILDHOOD:")
print("1-Angel's Announcement | 2-Birth in Bethlehem | 3-Jesus at Temple\n")

print("⚡ BEGINNING OF MINISTRY:")
print("4-Baptism | 5-Temptation | 6-First Disciples | 7-First Miracle\n")

print("🔥 POWERFUL MIRACLES:")
print("8-Healing Paralytic | 9-Calming Storm | 10-Feeding 5000")
print("11-Walking on Water | 12-Raising Lazarus | 13-Healing Blind\n")

print("📖 PROFOUND TEACHINGS:")
print("14-Sermon on Mount | 15-Prodigal Son | 16-I Am the Way | 17-Greatest Commandment\n")

print("✝️ FINAL WEEK:")
print("18-Triumphal Entry | 19-Last Supper | 20-Gethsemane")
print("21-Trial | 22-Crucifixion | 23-It Is Finished")
print("24-Resurrection | 25-Ascension\n")
# ==============================================================================
# 2. USER INPUT AND VALIDATION
# ==============================================================================
user_input = input("Enter your choice (1-25): ")
option = user_input.strip()  # REMOVE WHITESPACE

# USE .LOWER() TO ACCEPT 'QUIT', 'QUIT', ETC.
if option.lower() == 'quit' or option.lower() == 'q':
    print("👋 Thanks for exploring space missions!")
    print("🌟 Keep learning about God's amazing universe!")
    exit()
    
# STRING COMPARISON AND INPUT VALIDATION
if not option.isdigit() or int(option) < 1 or int(option) > 25:
    print(f"❌ '{option}' is not a valid mission number!")
    print("💡 Please choose a number between 1 and 25, or type 'quit' to exit.")
    exit()

# ==============================================================================
# 3. SPACE MISSIONS CATEGORIZATION (1-25)
# ==============================================================================
rovers = ["Perseverance", "Curiosity"]
space_probes = ["Voyager 1", "New Horizons", "Galileo", "Juno", "Dawn"]
space_telescopes = ["James Webb", "Hubble", "Spitzer", "Chandra", "Kepler",
                    "TESS"]
launch_vehicles = ["Ariane 5", "Soyuz", "Falcon 9", "Atlas V",
                   "Delta IV Heavy", "SLS"]
commercial_spacecraft = ["SpaceX Starship", "Blue Origin New Shepard",
                         "Crew Dragon"]
space_agencies = ["NASA", "ESA", "CSA", "Roscosmos", "ISRO", "CNSA"]
satellites = ["Starlink"]
orbiters = ["Cassini-Huygens", "OSIRIS-REx"]

# ==============================================================================
# 4. SPACE MISSIONS (1-25)
# ==============================================================================

# MISSION 1 - PERSEVERANCE
if option == "1":
    # PERSEVERANCE DETAILS
    mission_name = "Perseverance"
    mission_type = "Mars Rover"
    
    # IN OPERATOR AND NOT IN OPERATOR
    if mission_name in rovers:
        print(f"{mission_name} is one of the rovers exploring Mars, "
              "along with Curiosity")
    if mission_name not in space_probes:
        print(f"{mission_name} is NOT a space probe like Voyager 1 or Juno.")
        print("It's a rover designed to explore the Martian surface.")
        print("More information below:\n")
    
    # MISSION DETAILS
    planet = "Mars"
    purpose = "search for signs of past life"
    builder = "NASA's Jet Propulsion Laboratory"
    launch_year = 2020
    landing_year = 2021
    cost = 2_700_000_000  # 2.7 BILLION USD
    location = "Jezero Crater"
    current_situation = "actively exploring and sending data back to Earth"
    current_situation_formatted = current_situation.capitalize()
    
    # DISPLAY MISSION DETAILS
    print(jesus_moments.mission1_formatted)
    print(f"🔴 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose} and analyze Martian geology")
    print(f"🚀 Launched: {launch_year} | 🛬 Landed: {landing_year}")
    print(f"💰 Cost: ${cost:,} USD")
    print(f"📌 Current Location: {location}")
    print(f"📡 Current Status: {current_situation_formatted}")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Exploring God's creation on {planet} since {landing_year}!")

# MISSION 2 - JAMES WEBB
elif option == "2":
    # JAMES WEBB DETAILS
    mission_name = "James Webb Space Telescope"
    mission_type = "Space Telescope"
    
    # IN OPERATOR AND NOT IN OPERATOR
    if mission_name in space_telescopes:
        print(f"{mission_name} is one of the premier space telescopes, "
              "along with Hubble and Spitzer.")
    if mission_name not in rovers:
        print(f"{mission_name} is NOT a rover like Perseverance or "
              "Curiosity.")
        print("It's a space telescope designed to observe the universe.")
        print("More information below:\n")
    
    # MISSION DETAILS
    specialty = "infrared observations"
    specialty_formatted = specialty.capitalize()  # "INFRARED OBSERVATIONS"
    launch_year = 2021
    orbit_location = "L2 Lagrange Point"
    mirror_size = 6.5  # METERS
    cost = 10_000_000_000  # 10 BILLION USD
    current_situation = "operational and sending stunning images"
    partners = "NASA, ESA, and CSA"
    partners_formatted = partners.replace(", ", " | ")
    
    print(jesus_moments.mission2_formatted)
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
    # VOYAGER 1 DETAILS
    mission_name = "Voyager 1"
    mission_type = "Space Probe"
    specialty = "interstellar exploration"
    specialty_formatted = specialty.capitalize()  # "INTERSTELLAR EXPLORATION"
    partners = "NASA"
    launch_year = 1977
    orbit_location = "Interstellar Space"
    cost = 250_000_000  # 250 MILLION USD
    current_situation = "still communicating with Earth"
    
    print(jesus_moments.mission3_formatted)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: {specialty_formatted}")
    print(f"📍 Current Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"📡 Current Status: {current_situation}")
    print(f"🤝 Built by: {partners}")
    print(f"✨ Exploring the vastness of God's universe since {launch_year}!")

elif option == "4":
    # HUBBLE DETAILS
    mission_name = "Hubble Space Telescope"
    mission_type = "Space Telescope"
    specialty = "high-resolution imaging"
    specialty_formatted = specialty.capitalize()  # "HIGH-RESOLUTION IMAGING"
    partners = "NASA and ESA"
    launch_year = 1990
    orbit_location = "Low Earth Orbit"
    cost = 10_000_000_000  # 10 BILLION USD
    service_missions = 5
    current_situation = "still operational and capturing breathtaking images"
    
    # MIRROR COMPARISON WITH OTHER FAMOUS TELESCOPES
    hubble_mirror_size = 2.4  # METERS
    spitzer_mirror_size = 0.85  # METERS
    james_webb_mirror_size = 6.5  # METERS
    chandra_mirror_size = 1.2  # METERS
    
    print(jesus_moments.mission4_formatted)
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
    
    # USING COMPARISON OPERATORS
    print(f"🔍 Hubble Mirror Size: {hubble_mirror_size}m diameter")
    print(f"🔍 Spitzer Mirror Size: {spitzer_mirror_size}m diameter")
    print(f"🔍 Chandra Mirror Size: {chandra_mirror_size}m diameter")
    print(f"🔍 James Webb Mirror Size: {james_webb_mirror_size}m diameter")
    

elif option == "5":
    # CURIOSITY DETAILS
    mission_name = "Curiosity"
    mission_type = "Mars Rover"
    planet = "Mars"
    purpose = "analyze soil and rock samples"
    builder = "NASA's Jet Propulsion Laboratory"
    launch_year = 2011
    landing_year = 2012
    cost = 2_500_000_000  # 2.5 BILLION USD
    location = "Gale Crater"
    current_situation = "actively exploring and sending data back to Earth"
    
    print(jesus_moments.mission5_formatted)
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
    # SPITZER DETAILS
    mission_name = "Spitzer Space Telescope"
    mission_type = "Space Telescope"
    specialty = "infrared observations"
    specialty_formatted = specialty.capitalize()  # "INFRARED OBSERVATIONS"
    partners = "NASA and JPL"
    launch_year = 2003
    orbit_location = "Heliocentric Orbit"
    mirror_size = 0.85  # METERS
    cost = 720_000_000  # 720 MILLION USD
    current_situation = "retired in 2020 after 16 years of service"
    active = False
    
    print(jesus_moments.mission6_formatted)
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
    # CASSINI-HUYGENS DETAILS
    mission_name = "Cassini-Huygens"
    mission_type = "Orbiter and Lander"
    
    
# IN OPERATOR AND NOT IN OPERATOR
    if mission_name in orbiters:
        print(f"{mission_name} is one of the famous orbiters, "
              "along with OSIRIS-REx.")
        if mission_name not in rovers:
            print(f"{mission_name} is NOT a rover like Perseverance or "
                  "Curiosity.")
            print("It's an orbiter designed to study Saturn and its moons.")
            print("More information below:\n")
            
            # MISSION DETAILS
    planet = "Saturn"
    purpose = "study Saturn and its moons"
    builder = "NASA and Italy's ASI"
    launch_year = 1997
    arrival_year = 2004
    end_year = 2017
    cost = 3_900_000_000  # 3.9 BILLION USD
    current_situation = "mission ended in 2017 after 13 years of service"
    
    print(jesus_moments.mission7_formatted)
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
    # NEW HORIZONS DETAILS
    mission_name = "New Horizons"
    mission_type = "Space Probe"
    planet = "Pluto and Kuiper Belt"
    purpose = "conduct a flyby of Pluto and study Kuiper Belt objects"
    builder = "Johns Hopkins University Applied Physics Laboratory"
    launch_year = 2006
    arrival_year = 2015
    cost = 700_000_000  # 700 MILLION USD
    current_situation = "still exploring the Kuiper Belt"
    
    print(jesus_moments.mission8_formatted)
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
    # GALILEO DETAILS
    mission_name = "Galileo"
    mission_type = "Orbiter and Probe"
    planet = "Jupiter"
    purpose = "study Jupiter and its moons"
    builder = "NASA's Jet Propulsion Laboratory"
    launch_year = 1989
    arrival_year = 1995
    end_year = 2003
    cost = 1_600_000_000  # 1.6 BILLION USD
    current_situation = "mission ended in 2003 after 14 years of service"
    current_situation_formatted = current_situation.capitalize()
    partners = "NASA, ESA and Germany's DLR"
    partners_formatted = partners.replace(", ", " | ")
    
    print(jesus_moments.mission9_formatted)
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
    # KEPLER DETAILS
    mission_name = "Kepler Space Telescope"
    mission_type = "Space Telescope"
    specialty = "exoplanet discovery"
    specialty_formatted = specialty.capitalize()  # "EXOPLANET DISCOVERY"
    partners = "NASA and JPL"
    launch_year = 2009
    end_year = 2018
    mirror_size = 0.95  # METERS
    cost = 600_000_000  # 600 MILLION USD
    current_situation = ("retired in 2018 after discovering thousands "
                         "of exoplanets")
    current_situation_formatted = current_situation.capitalize()
    
    print(jesus_moments.mission10_formatted)
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
    # CHANDRA DETAILS
    mission_name = "Chandra X-ray Observatory"
    mission_type = "Space Telescope"
    specialty = "X-ray observations"
    partners = "NASA and Smithsonian Astrophysical Observatory"
    launch_year = 1999
    orbit_location = "High Earth Orbit"
    mirror_size = 1.2  # METERS
    cost = 1_600_000_000  # 1.6 BILLION USD
    current_situation = "still operational and capturing high-energy phenomena"
    current_situation_formatted = current_situation.capitalize()
    
    print(jesus_moments.mission11_formatted)
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
    # JUNO DETAILS
    mission_name = "Juno"
    mission_type = "Orbiter"
    planet = "Jupiter"
    purpose = "study Jupiter's atmosphere, magnetic field, and structure"
    builder = "Lockheed Martin"
    launch_year = 2011
    arrival_year = 2016
    cost = 1_100_000_000  # 1.1 BILLION USD
    current_situation = "actively orbiting and sending data back to Earth"
    current_situation_formatted = current_situation.capitalize()
    size = "20 feet tall"
    weight = 3_600  # POUNDS
    solar_panels_span = 66  # FEET
    
    print(jesus_moments.mission12_formatted)
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
    # TESS DETAILS
    mission_name = "Transiting Exoplanet Survey Satellite (TESS)"
    mission_type = "Space Telescope"
    specialty = "exoplanet discovery"
    partners = "NASA, MIT, and Harvard"
    partners_formatted = partners.replace(", ", " | ")
    launch_year = 2018
    orbit_location = "High Earth Orbit"
    mirror_size = 0.1  # METERS
    cost = 337_000_000  # 337 MILLION USD
    current_situation = "actively discovering new exoplanets"
    current_situation_formatted = current_situation.capitalize()
    size = "13.2 feet tall"
    weight = 1_200  # POUNDS
    mirror_count = 4

    print(jesus_moments.mission13_formatted)
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
    # OSIRIS-REX DETAILS
    mission_name = "OSIRIS-REx"
    mission_type = "Sample Return Mission"
    asteroid = "Bennu"
    purpose = "collect samples from the asteroid and return them to Earth"
    purpose_formatted = purpose.capitalize()  # .CAPITALIZE()
    builder = "Lockheed Martin"
    launch_year = 2016
    arrival_year = 2018
    return_year = 2023
    cost = 800_000_000  # 800 MILLION USD
    current_situation = "sample capsule returned to Earth in 2023"
    orbit_location = "Near-Earth Asteroid"

    print(jesus_moments.mission14_formatted)
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
    # DAWN DETAILS
    mission_name = "Dawn"
    mission_type = "Orbiter"
    purpose = "study the two largest objects in the asteroid belt"
    builder = "Orbital ATK"
    launch_year = 2007
    arrival_vesta_year = 2011
    departure_vesta_year = 2012
    arrival_ceres_year = 2015
    end_year = 2018
    cost = 500_000_000  # 500 MILLION USD
    current_situation = "mission ended in 2018 after running out of fuel"

    print(jesus_moments.mission15_formatted)
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
    # SPACEX STARSHIP DETAILS
    mission_name = "SpaceX Starship"
    mission_type = "Interplanetary Spacecraft"
    purpose = "enable human missions to Mars and beyond"
    
    # IN OPERATOR AND NOT IN OPERATOR
    if mission_name in commercial_spacecraft:
        print(f"{mission_name} is one of the commercial spacecraft, "
              "along with Blue Origin New Shepard and Crew Dragon.")
    if mission_name not in rovers:
        print(f"{mission_name} is NOT a rover like Perseverance or Curiosity.")
        print("It's a spacecraft designed for interplanetary travel.")
        print("More information below:\n")
        # MISSION DETAILS
    builder = "SpaceX"
    launch_year = 2023  # FIRST TEST FLIGHT YEAR
    cost = "TBD"  # COST IS STILL TO BE DETERMINED
    reusable = True
    capacity = "100+ tons to LEO"
    payload = "100+ people"
    reliability = "In development"

    print(jesus_moments.mission16_formatted)
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
    # BLUE ORIGIN DETAILS
    mission_name = "Blue Origin New Shepard"
    mission_type = "Suborbital Spaceflight Vehicle"
    purpose = "take passengers to the edge of space"
    builder = "Blue Origin"
    launch_year = 2015  # FIRST TEST FLIGHT YEAR
    cost = "TBD"  # COST IS STILL TO BE DETERMINED
    horsepower = 110_000  # 110,000 POUNDS OF THRUST
    reusable = True
    reliability = "100% success rate in its last 15 flights"

    print(jesus_moments.mission17_formatted)
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
    # ARIANE 5 DETAILS
    mission_name = "Ariane 5"
    mission_type = "Heavy-Lift Launch Vehicle"
    purpose = "deliver payloads to orbit"
    builder = "Arianespace and ESA"
    launch_year = 1996  # FIRST FLIGHT YEAR
    cost_per_launch = 165_000_000  # 165 MILLION USD PER LAUNCH
    total_launches = 111  # TOTAL LAUNCHES AS OF 2023
    horsepower = 2_200_000  # 2.2 MILLION POUNDS OF THRUST
    size = "171 feet tall"
    reliability = "95% success rate"

    print(jesus_moments.mission18_formatted)
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
    # SOYUZ DETAILS
    mission_name = "Soyuz"
    mission_type = "Crewed Spacecraft"
    purpose = "transport astronauts to and from the ISS"
    builder = "Roscosmos"
    first_flight_year = 1967
    total_missions = 140  # TOTAL CREWED MISSIONS AS OF 2023
    cost_per_mission = 90_000_000  # 90 MILLION USD PER MISSION
    current_situation = "still in use for crewed missions to the ISS"
    size = "49.5 feet tall"
    payload = "7,000 pounds to LEO"

    print(jesus_moments.mission19_formatted)
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
    # FALCON 9 DETAILS
    mission_name = "Falcon 9"
    mission_type = "Reusable Rocket"
    purpose = "deliver payloads to orbit and return to Earth"
    builder = "SpaceX"
    first_flight_year = 2010
    total_launches = 200  # TOTAL LAUNCHES AS OF 2023
    cost_per_launch = 62_000_000  # 62 MILLION USD PER LAUNCH
    horsepower = 1_710_000  # 1.71 MILLION POUNDS OF THRUST
    reusable = True
    reliability = "98% success rate"

    print(jesus_moments.mission20_formatted)
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
    # ATLAS V DETAILS
    mission_name = "Atlas V"
    mission_type = "Launch Vehicle"
    purpose = "deliver payloads to a variety of orbits"
    builder = "United Launch Alliance (ULA)"
    first_flight_year = 2002
    total_launches = 87  # TOTAL LAUNCHES AS OF 2023
    horsepower = 940_000  # 940,000 POUNDS OF THRUST
    size = "191 feet tall"
    reliability = "100% success rate in its last 29 launches"
    bigger_than_falcon_heavy = False
    bigger_than_sls = False
    
    # USING COMPARISON OPERATORS
    cost_per_launch = 109_000_000  # 109 MILLION USD PER LAUNCH
    ariane5_cost_per_launch = 165_000_000  # 165 MILLION USD PER LAUNCH
    sls_cost_per_launch = 2_000_000_000  # 2 BILLION USD PER LAUNCH
    falcon_cost_per_launch = 62_000_000  # 62 MILLION USD PER LAUNCH
    delta_iv_cost_per_launch = 164_000_000  # 164 MILLION USD PER LAUNCH

    print(jesus_moments.mission21_formatted)
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
    
    # COST COMPARISON WITH OTHER ROCKETS
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
    # DELTA IV DETAILS
    mission_name = "Delta IV"
    mission_type = "Heavy-Lift Launch Vehicle"
    purpose = "deliver large payloads to orbit"
    builder = "United Launch Alliance (ULA)"
    first_flight_year = 2002
    total_launches = 43  # TOTAL LAUNCHES AS OF 2023
    cost_per_launch = 164_000_000  # 164 MILLION USD PER LAUNCH
    horsepower = 2_100_000  # 2.1 MILLION POUNDS OF THRUST
    size = "235 feet tall"
    bigger_than_sls = False
    bigger_than_falcon_heavy = True

    print(jesus_moments.mission22_formatted)
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
    # SLS DETAILS
    mission_name = "Space Launch System (SLS)"
    mission_location = "Moon and beyond"
    mission_type = "Heavy-Lift Launch Vehicle"
    purpose = "enable human exploration beyond low Earth orbit"
    builder = "NASA and Boeing"
    first_flight_year = 2022  # FIRST TEST FLIGHT YEAR
    cost_per_launch = 2_000_000_000  # 2 BILLION USD PER LAUNCH
    horsepower = 8_800_000  # 8.8 MILLION POUNDS OF THRUST
    size = "322 feet tall"
    bigger_than_falcon_heavy = True
    
    # ROCKET HEIGHT COMPARISONS (IN FEET)
    delta_iv_height = 235      # DELTA IV
    sls_height = 322           # SLS (ALREADY DEFINED ABOVE)
    falcon_heavy_height = 229  # FALCON HEAVY (REAL DATA)

    print(jesus_moments.mission23_formatted)
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
    
    # HEIGHT COMPARISON WITH OTHER HEAVY ROCKETS
    print(f"📏 Delta IV Height: {delta_iv_height} feet")
    print(f"🔍 Compared to SLS ({sls_height} feet): "
          f"{delta_iv_height - sls_height:+d} feet")
    print(f"🔍 Compared to Falcon Heavy ({falcon_heavy_height} feet): "
          f"{delta_iv_height - falcon_heavy_height:+d} feet")
    print(f"🌟 Delivering heavy payloads into God's orbit "
          f"since {first_flight_year}!")

elif option == "24":
    # CREW DRAGON DETAILS
    mission_name = "Crew Dragon"
    mission_type = "Crewed Spacecraft"
    purpose = "transport astronauts to and from the ISS"
    builder = "SpaceX"
    first_flight_year = 2020  # FIRST CREWED FLIGHT YEAR
    cost_per_mission = 55_000_000  # 55 MILLION USD PER MISSION

    print(jesus_moments.mission24_formatted)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🎯 Primary Mission: To {purpose}")
    print("and ensure safe crew transport")
    print(f"🚀 First Crewed Flight: {first_flight_year}")
    print(f"💰 Estimated Cost per Mission: ${cost_per_mission:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Safely transporting astronauts in God's creation "
          f"since {first_flight_year}!")

elif option == "25":
    # STARLINK DETAILS
    mission_name = "Starlink"
    mission_type = "Satellite Constellation"
    purpose = "provide global internet coverage"
    
    # IN OPERATOR AND NOT IN OPERATOR
    if mission_name in commercial_spacecraft:
        print(f"{mission_name} is one of the commercial spacecraft, "
              "along with Blue Origin New Shepard and Crew Dragon.")
    if mission_name not in rovers:
        print(f"{mission_name} is NOT a rover like Perseverance or Curiosity.")
        print("It's a satellite constellation designed for global internet.")
        print("More information below:\n")
        # MISSION DETAILS
    builder = "SpaceX"
    launch_year = 2019  # FIRST SATELLITE LAUNCH YEAR
    total_satellites = 4000  # TOTAL SATELLITES LAUNCHED AS OF 2023
    cost = 10_000_000_000  # 10 BILLION USD (ESTIMATED TOTAL COST)
    number_of_launches = 60  # TOTAL LAUNCHES AS OF 2023
    number_of_satellites_orbit = 4000  # TOTAL SATELLITES IN ORBIT AS OF 2023

    print(jesus_moments.mission25_formatted)
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

