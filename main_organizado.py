# ==============================================================================
# SPACE MISSION MANAGER CLI
# ==============================================================================
import missions

# ==============================================================================
# 1. TÍTULO E MENU PRINCIPAL
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
# 2. ENTRADA E VALIDAÇÃO DO USUÁRIO
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
# 3. MISSÕES ESPACIAIS (1-25)
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

# [Continua com as outras 22 missões...]

else:
    print("Invalid option. Please select a number between 1 and 25.")
    exit()

# ==============================================================================
# 4. SEÇÃO EDUCATIVA - EXEMPLOS DE OPERADORES PYTHON
# ==============================================================================

print("\n" + "="*50)
print("🔍 SPACE MISSION SEARCH FEATURE:")
print("="*50)

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

# Create mission database for searching
all_missions = [
    "Perseverance", "James Webb", "Voyager 1", "Hubble", "Curiosity",
    "Spitzer", "Cassini-Huygens", "New Horizons", "Galileo", "Kepler",
    "Chandra", "Juno", "TESS", "OSIRIS-REx", "Dawn", "SpaceX Starship",
    "Blue Origin", "Ariane 5", "Soyuz", "Falcon 9", "Atlas V",
    "Delta IV", "SLS", "Crew Dragon", "Starlink"
]

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

# Current planet exploration mission using 'not in' operator
current_missions = [
    "Mars", "Jupiter", "Saturn", "Pluto", "Asteroid Belt", "Exoplanets",
    "Interstellar Space", "Low Earth Orbit", "Deep Space", "Infrared Space",
    "X-ray Space", "Suborbital Spaceflight", "Heavy Lift Launch",
    "Human Spaceflight", "Satellite Internet"
]

print("\n🌍 Checking what planets we DON'T have missions to:")
if "Venus" not in current_missions:
    print("❌ No current missions to Venus.")
if "Mars" not in current_missions:
    print("❌ No current missions to Mars.")
if "Jupiter" not in current_missions:
    print("❌ No current missions to Jupiter.")