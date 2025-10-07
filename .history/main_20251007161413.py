
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
    # Mission details com f-strings
    # Perseverance details
    mission_name = "Perseverance"
    mission_type = "Mars Rover"
    planet = "Mars"
    purpose = "search for signs of past life"
    builder = "NASA's Jet Propulsion Laboratory"
    launch_year = 2020
    landing_year = 2021
    cost = 2_700_000_000  # 2.7 billion USD
    
    print(missions.mission1)
    print(f"🔴 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose} and analyze Martian geology")
    print(f"🚀 Launched: {launch_year} | 🛬 Landed: {landing_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Exploring God's magnificent creation on {planet} since {landing_year}!")
    
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
    print(f"🌌 Speciality: Advanced {specialty}")
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
    print("description: A space probe that has traveled beyond our")
    print("solar system, providing valuable data about interstellar space.")
    print("It is the farthest human-made object from Earth,")
    print("continuing to send data back to NASA as it journeys through the")
    print("interstellar medium.")
    print("Launched in 1977, it has provided invaluable insights into")
    print("the outer planets and the heliosphere.")
    print("and was built by NASA.")
    
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
    print(f"📍 Operating Location: {orbit_location}"
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🛠️ Service Missions: {service_missions}")
    print(f"🤝 International Partnership: {partners}")
    print(f"✨ Unveiling the beauty of God's universe since {launch_year}!")
    print(f"🏭 Built by: {partners}")
   
elif option == "5":
    print(missions.mission5)
    print("description: A rover that explores the surface of Mars,")
    print("analyzing soil and rock samples to understand the planet's")
    print("geology and climate,")
    print("providing insights into past water activity and habitability.")
    print("The rover has made significant discoveries, including")
    print("evidence of ancient microbial life and organic molecules.")
    print("Was built by NASA's Jet Propulsion Laboratory.")
    
elif option == "6":
    print(missions.mission6)
    print("description: A space telescope that observes the universe")
    print("in infrared light, studying objects such as stars,")
    print("galaxies, and black holes.")
    print("It has provided valuable data on the formation")
    print("and evolution of galaxies and the lifecycle of stars.")
    print("Was built by NASA and JPL.")
    
elif option == "7":
    print(missions.mission7)
    print("description: A mission that studied Saturn and its moons,")
    print("providing detailed information about the planet's rings")
    print("and atmosphere.")
    print("It provided unprecedented insights into the Saturnian system,")
    print("including the discovery of water-ice plumes on Enceladus")
    print("and the complex structure of Saturn's rings.")
    print("Was built by NASA and Italy's ASI.")
    
elif option == "8":
    print(missions.mission8)
    print("description: A space probe that conducted a flyby of Pluto")
    print("and is now exploring the Kuiper Belt.")
    print("It provided the first close-up images of Pluto,")
    print("revealing a complex and geologically active world.")
    print("The mission has expanded our understanding of the outer")
    print("solar system and the diversity of objects within it.")   
    print("Was built by Johns Hopkins University Applied Physics Laboratory.")
    
elif option == "9":
    print(missions.mission9)
    print("description: A mission that studied Jupiter and its moons,")
    print("providing insights into the planet's atmosphere and")
    print("magnetic field.")
    print("It provided valuable data on Jupiter's complex system,")
    print("including the discovery of water vapor in its atmosphere")
    print("and detailed observations of its largest moons.")
    print("Was built by NASA's Jet Propulsion Laboratory.")
elif option == "10":
    print(missions.mission10)
    print("description: A space telescope that searched for exoplanets")
    print("by monitoring the brightness of stars.")
    print("It discovered thousands of potential exoplanets and")
    print("revolutionized our understanding of planetary systems.")
    print("Was built by NASA's Ames Research Center.")
elif option == "11":
    print(missions.mission11)
    print("description: A space telescope that observes X-rays from")
    print("high-energy regions of the universe, such as black holes")
    print("and supernovae.")
    print("It has provided detailed images of X-ray sources")
    print("and helped understand cosmic phenomena.")
    print("Was built by NASA and the Smithsonian Astrophysical Observatory.")
elif option == "12":
    print(missions.mission12)
    print("description: A mission that studies Jupiter's polar regions")
    print("and its magnetic field.")
    print("It has revealed Jupiter's complex internal structure")
    print("and provided stunning images of its polar regions.")
    print("Was built by Lockheed Martin for NASA.")
elif option == "13":
    print(missions.mission13)
    print("description: A space telescope that searches for exoplanets")
    print("by monitoring the brightness of stars.")
    print("It surveys the entire sky to find Earth-sized planets")
    print("in the habitable zones of nearby stars.")
    print("Was built by MIT and NASA's Goddard Space Flight Center.")
elif option == "14":
    print(missions.mission14)
    print("description: A mission that collected samples from the")
    print("asteroid Bennu and is returning them to Earth for analysis.")
    print("It successfully collected pristine samples that may contain")
    print("clues about the early solar system and origins of life.")
    print("Was built by Lockheed Martin for NASA.")
elif option == "15":
    print(missions.mission15)
    print("description: A mission that studied the two largest objects")
    print("in the asteroid belt, Vesta and Ceres.")
    print("It provided detailed maps and composition data")
    print("of these ancient remnants from the early solar system.")
    print("Was built by Orbital ATK for NASA.")
elif option == "16":
    print(missions.mission16)
    print("description: A spacecraft designed for interplanetary travel,")
    print("with the goal of enabling human missions to Mars and beyond.")
    print("It's designed to be fully reusable and carry large crews")
    print("and cargo to the Moon, Mars, and other destinations.")
    print("Was built by SpaceX.")
elif option == "17":
    print(missions.mission17)
    print("description: A suborbital spaceflight vehicle designed")
    print("to take passengers to the edge of space.")
    print("It offers commercial space tourism flights")
    print("providing a few minutes of weightlessness.")
    print("Was built by Blue Origin.")
elif option == "18":
    print(missions.mission18)
    print("description: A heavy-lift launch vehicle used to")
    print("deliver payloads to orbit.")
    print("It has been one of the most reliable launch vehicles")
    print("for commercial and scientific satellites.")
    print("Was built by Arianespace and ESA.")
elif option == "19":
    print(missions.mission19)
    print("description: A spacecraft used for human spaceflight")
    print("missions to the International Space Station and other")
    print("destinations.")
    print("It has been the most reliable human spaceflight system")
    print("with over 140 crewed missions.")
    print("Was built by Roscosmos (Russia).")
elif option == "20":
    print(missions.mission20)
    print("description: A reusable rocket designed to deliver payloads")
    print("to orbit and return to Earth for refurbishment and reuse.")
    print("It revolutionized the space industry by making")
    print("launches more cost-effective through reusability.")
    print("Was built by SpaceX.")
elif option == "21":
    print(missions.mission21)
    print("description: A versatile launch vehicle used to deliver")
    print("payloads to a variety of orbits.")
    print("It has launched many important NASA missions")
    print("including Mars rovers and space telescopes.")
    print("Was built by United Launch Alliance (ULA).")
elif option == "22":
    print(missions.mission22)
    print("description: A heavy-lift launch vehicle used to deliver")
    print("large payloads to orbit.")
    print("It specializes in launching large government")
    print("and military satellites to high orbits.")
    print("Was built by United Launch Alliance (ULA).")
elif option == "23":
    print(missions.mission23)
    print("description: A next-generation launch vehicle designed")
    print("for deep space exploration missions.")
    print("It's designed to launch Artemis missions")
    print("and send humans back to the Moon.")
    print("Was built by NASA and Boeing.")
elif option == "24":
    print(missions.mission24)
    print("description: A spacecraft designed for human spaceflight")
    print("missions to the International Space Station and beyond.")
    print("It restored America's capability to launch astronauts")
    print("from US soil after the Space Shuttle retirement.")
    print("Was built by SpaceX.")
elif option == "25":
    print(missions.mission25)
    print("description: A satellite constellation designed to provide")
    print("global internet coverage.")
    print("It aims to provide high-speed internet access")
    print("to underserved and remote areas worldwide.")
    print("Was built by SpaceX.")
else:
    print("Invalid option. Please select a number between 1 and 25.")
    raise SystemExit()

