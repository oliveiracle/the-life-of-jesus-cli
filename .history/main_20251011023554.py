# ==============================================================================
# SPACE MISSION MANAGER CLI - Organized and Clean
# ==============================================================================
import missions

# ==============================================================================
# 1. TITLE AND MAIN MENU
# ==============================================================================
missions.show_title()
print("Choose a mission to learn more about:")
print("1-Perseverance | 2-James Webb | 3-Voyager 1 | 4-Hubble | 5-Curiosity")
print("6-Spitzer | 7-Cassini-Huygens | 8-New Horizons | 9-Galileo | 10-Kepler")
print("11-Chandra | 12-Juno | 13-TESS | 14-OSIRIS-REx | 15-Dawn")
print("16-SpaceX Starship | 17-Blue Origin | 18-Ariane 5 | 19-Soyuz")
print("20-Falcon 9 | 21-Atlas V | 22-Delta IV | 23-SLS")
print("24-Crew Dragon | 25-Starlink")

# ==============================================================================
# 2. USER INPUT AND VALIDATION
# ==============================================================================
user_input = input("Enter your choice (1-25): ")
option = user_input.strip()  # Remove whitespace

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

# ==============================================================================
# 3. SPACE MISSIONS (1-25)
# ==============================================================================

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

else:
    print("Invalid option. Please select a number between 1 and 25.")
    exit()
