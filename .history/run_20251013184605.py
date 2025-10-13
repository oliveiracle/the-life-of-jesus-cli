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
print("14-Sermon on Mount | 15-Prodigal Son")
print("16-I Am the Way | 17-Greatest Commandment\n")

print("✝️ FINAL WEEK:")
print("18-Triumphal Entry | 19-Last Supper | 20-Gethsemane")
print("21-Trial | 22-Crucifixion | 23-It Is Finished")
print("24-Resurrection | 25-Ascension\n")

# ==============================================================================
# 2. USER INPUT AND VALIDATION
# ==============================================================================
user_input = input("Enter your choice (1-25) or 'quit' to exit: ")
option = user_input.strip()

# Handle quit option
if option.lower() == 'quit' or option.lower() == 'q':
    print("✝️ Thank you for exploring the life of Jesus!")
    print("🙏 'I am with you always, to the very end of the age'")
    print("   - Matthew 28:20")
    exit()

# Validate input
if not option.isdigit() or int(option) < 1 or int(option) > 25:
    print(f"❌ '{option}' is not a valid moment number!")
    print("💡 Please choose a number between 1 and 25, or type 'quit'.")
    exit()

# ==============================================================================
# 3. CATEGORIZING THE 25 MOMENTS OF JESUS' LIFE
# ==============================================================================

# Birth & Childhood (1-3)
birth_and_childhood = [
    "Angel's Announcement",
    "Birth in Bethlehem",
    "Jesus at Temple"
]

# Beginning of Ministry (4-7)
beginning_ministry = [
    "Baptism",
    "Temptation",
    "First Disciples",
    "First Miracle"
]

# Powerful Miracles (8-13)
powerful_miracles = [
    "Healing Paralytic",
    "Calming Storm",
    "Feeding 5000",
    "Walking on Water",
    "Raising Lazarus",
    "Healing Blind"
]

# Profound Teachings (14-17)
profound_teachings = [
    "Sermon on Mount",
    "Prodigal Son",
    "I Am the Way",
    "Greatest Commandment"
]

# Final Week (18-25)
final_week = [
    "Triumphal Entry",
    "Last Supper",
    "Gethsemane",
    "Trial",
    "Crucifixion",
    "It Is Finished",
    "Resurrection",
    "Ascension"
]

# All moments combined
all_moments = (birth_and_childhood + beginning_ministry +
               powerful_miracles + profound_teachings + final_week)

# ==============================================================================
# 4. THE 25 MOMENTS OF JESUS CHRIST
# ==============================================================================

# MOMENT 1 - THE ANNOUNCEMENT
if option == "1":
    moment_name = "The Angel Gabriel Announces Jesus' Birth"
    moment_type = "Divine Announcement"
    location = "Nazareth, Mary's home"
    participants = "Angel Gabriel and Mary"
    main_verse = "Luke 1:30-31"
    verse_text = ("Do not be afraid, Mary; you have found favor with God. "
                  "You will conceive and give birth to a son, and you are "
                  "to call him Jesus.")
    significance = "marked the beginning of God's plan for salvation"
    time_period = "Approximately 6 BC"
    mary_response = ("I am the Lord's servant. May your word to me "
                     "be fulfilled.")

    print("=" * 70)
    print(f"✨ {moment_type}: {jesus_moments.moment1_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Time: {time_period}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print("🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print("   God chose a humble young woman to bear the Savior of "
          "the world.")
    print()
    print("💡 MARY'S FAITHFUL RESPONSE:")
    print(f'   "{mary_response}" - Luke 1:38')
    print()
    print("🙏 May we respond to God's call with the same faith and humility!")

# MOMENT 2 - THE BIRTH
elif option == "2":
    moment_name = "The Birth of Jesus Christ"
    moment_type = "The Incarnation"
    location = "Bethlehem, in a manger"
    participants = "Mary, Joseph, baby Jesus, shepherds, angels"
    main_verse = "Luke 2:10-11"
    verse_text = ("Do not be afraid. I bring you good news that will "
                  "cause great joy for all the people. Today in the town "
                  "of David a Savior has been born to you; he is the "
                  "Messiah, the Lord.")
    significance = "God became flesh and dwelt among us"
    time_period = "Approximately 4-6 BC"
    angel_proclamation = ("Glory to God in the highest heaven, and on "
                          "earth peace to those on whom his favor rests!")

    print("=" * 70)
    print(f"⭐ {moment_type}: {jesus_moments.moment2_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Time: {time_period}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print("🎯 SIGNIFICANCE:")
    print(f"   {significance}!")
    print("   The eternal God took on human form to save humanity.")
    print()
    print("🎵 THE ANGELS' SONG:")
    print(f'   "{angel_proclamation}" - Luke 2:14')
    print()
    print("💡 John 1:14 - 'The Word became flesh and made his "
          "dwelling among us.'")
    print()
    print("🙏 Jesus left heaven's glory to be born in humility - "
          "for you and me!")

# MOMENT 3 - JESUS AT THE TEMPLE
elif option == "3":
    moment_name = "Young Jesus at the Temple"
    moment_type = "Early Wisdom"
    location = "Jerusalem Temple"
    participants = "Jesus (age 12), Mary, Joseph, teachers of the law"
    main_verse = "Luke 2:46-47"
    verse_text = ("They found him in the temple courts, sitting among "
                  "the teachers, listening to them and asking them "
                  "questions. Everyone who heard him was amazed at his "
                  "understanding and his answers.")
    significance = "revealed Jesus' divine wisdom even as a child"
    age = "12 years old"
    jesus_response = ("Why were you searching for me? Didn't you know "
                      "I had to be in my Father's house?")

    print("=" * 70)
    print(f"📚 {moment_type}: {jesus_moments.moment3_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Jesus' Age: {age}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print("🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print("   Even the religious teachers were astonished by "
          "His understanding!")
    print()
    print("💡 JESUS' WORDS TO HIS PARENTS:")
    print(f'   "{jesus_response}" - Luke 2:49')
    print()
    print("🙏 From childhood, Jesus knew His divine purpose!")

# MOMENT 4 - THE BAPTISM
elif option == "4":
    moment_name = "The Baptism of Jesus"
    moment_type = "Public Ministry Begins"
    location = "Jordan River"
    participants = ("Jesus, John the Baptist, the Holy Spirit, "
                    "God the Father")
    main_verse = "Matthew 3:16-17"
    verse_text = ("As soon as Jesus was baptized, he went up out of "
                  "the water. At that moment heaven was opened, and he "
                  "saw the Spirit of God descending like a dove and "
                  "alighting on him. And a voice from heaven said, "
                  "'This is my Son, whom I love; with him I am well pleased.'")
    significance = ("marked the beginning of Jesus' public ministry "
                    "and revealed the Trinity")
    jesus_age = "About 30 years old"
    john_words = "I need to be baptized by you, and do you come to me?"

    print("=" * 70)
    print(f"💧 {moment_type}: {jesus_moments.moment4_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Jesus' Age: {jesus_age}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print("🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print("   The Father spoke, the Spirit descended, and the Son obeyed.")
    print()
    print("💡 JOHN'S HESITATION:")
    print(f'   "{john_words}" - Matthew 3:14')
    print()
    print("🙏 Jesus modeled perfect obedience to God's will!")

# MOMENT 5 - THE TEMPTATION
elif option == "5":
    moment_name = "Jesus' Temptation in the Wilderness"
    moment_type = "Victory Over Temptation"
    location = "Judean Wilderness"
    participants = "Jesus and Satan"
    main_verse = "Matthew 4:4"
    verse_text = ("Man shall not live on bread alone, but on every "
                  "word that comes from the mouth of God.")
    significance = "proved Jesus' sinlessness and authority over Satan"
    duration = "40 days and 40 nights"
    temptations = ("Turn stones to bread, Jump from temple, "
                   "Worship Satan for kingdoms")
    jesus_weapon = "The Word of God - Scripture"

    print("=" * 70)
    print(f"⚔️ {moment_type}: {jesus_moments.moment5_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key Figures: {participants}")
    print(f"⏱️ Duration: {duration}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print("🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print("   Where Adam failed, Jesus succeeded!")
    print()
    print("😈 THE THREE TEMPTATIONS:")
    print(f"   {temptations}")
    print()
    print("⚔️ JESUS' WEAPON:")
    print(f"   {jesus_weapon} - 'It is written...'")
    print()
    print("🙏 Jesus shows us how to overcome temptation - with God's Word!")

# MOMENT 6 - FIRST DISCIPLES
elif option == "6":
    moment_name = "Jesus Calls His First Disciples"
    moment_type = "Beginning of Discipleship"
    location = "Sea of Galilee"
    participants = "Jesus, Simon Peter, Andrew, James, John"
    main_verse = "Matthew 4:19"
    verse_text = ("Come, follow me," Jesus said, "and I will send you "
                  "out to fish for people.")
    significance = "started the formation of Jesus' core group of followers"
    time_period = "Early in Jesus' ministry"
    disciples_response = ("At once they left their nets and followed him.")

    print("=" * 70)
    print(f"🎣 {moment_type}: {jesus_moments.moment6_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Time: {time_period}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print("🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print("   Jesus called ordinary fishermen to become His "
          "extraordinary disciples.")
    print()
    print("💡 DISCIPLES' IMMEDIATE RESPONSE:")
    print(f'   "{disciples_response}" - Matthew 4:20')
    print()
    print("🙏 Jesus calls each of us to follow Him and be His disciples!")
    
# MOMENT 7 - FIRST MIRACLE
elif option == "7":
    moment_name = "Jesus' First Miracle at Cana"
    moment_type = "Miracle of Transformation"
    location = "Cana of Galilee"
    participants = "Jesus, Mary, servants, wedding guests"
    main_verse = "John 2:11"
    verse_text = ("What Jesus did here in Cana of Galilee was the first "
                  "of the signs through which he revealed his glory; and "
                  "his disciples believed in him.")
    significance = "revealed Jesus' divine power and glory"
    event = "a wedding feast"
    miracle_details = ("Turned water into wine, demonstrating His power "
                       "over nature")

    print("=" * 70)
    print(f"🍷 {moment_type}: {jesus_moments.moment7_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Event: {event}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print("🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print("   Jesus demonstrated His authority over creation.")
    print()
    print("💡 DETAILS OF THE MIRACLE:")
    print(f"   {miracle_details}")
    print()
    print("🙏 May we recognize and celebrate Jesus' transformative power in our lives!")

# MOMENT 8 - HEALING THE PARALYTIC
elif option == "8":
    moment_name = "Jesus Heals a Paralytic"
    moment_type = "Miracle of Healing"
    location = "Capernaum"
    participants = "Jesus, paralytic, friends, crowd"
    main_verse = "Mark 2:11-12"
    verse_text = ("I tell you, get up, take your mat and go home."
                  " He got up, took his mat and walked out in full view "
                  "of them all. This amazed everyone and they praised God, "
                  "saying, 'We have never seen anything like this!'")
    significance = "demonstrated Jesus' authority to forgive sins and heal"
    healing_method = ("Lowered through the roof by friends, Jesus "
                      "forgave his sins and healed him")    
    crowd_reaction = "Amazed and praised God"
    time_period = "During Jesus' early ministry"
    friends_faith = ("When Jesus saw their faith, he said to the "
                     "paralytic, 'Son, your sins are forgiven.'")

    print("=" * 70)
    print(f"🍷 {moment_type}: {jesus_moments.moment8_formatted}")
   print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Time: {time_period}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print("🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print("   Jesus showed His power over both physical and spiritual "
          "realms.")
    print()
    print("💡 HEALING METHOD:")
    print(f"   {healing_method}")
    print()
    print("🙏 May we have faith like the paralytic's friends, "
          "bringing others to Jesus for healing and forgiveness!")
    
# MOMENT 9 - CALMING THE STORM
elif option == "9":
    moment_name = "Jesus Calms the Storm"
    moment_type = "Miracle Over Nature"
    location = "Sea of Galilee"
    participants = "Jesus and His disciples"
    main_verse = "Mark 4:39-41"
    verse_text = ("He got up, rebuked the wind and said to the "
                  "waves, 'Quiet! Be still!' Then the wind died down "
                  "and it was completely calm. He said to his disciples, "
                  "'Why are you so afraid? Do you still have no faith?' "
                  "They were terrified and asked each other, 'Who is this? "
                  "Even the wind and the waves obey him!'")
    significance = "revealed Jesus' authority over nature"
    time_period = "During Jesus' ministry"
    disciples_fear = ("They were terrified and asked each other, "
                      "'Who is this? Even the wind and the waves obey him!'")
    jesus_rebuke = ("Quiet! Be still!")
    faith_question = ("Why are you so afraid? Do you still have no faith?")
    
    print("=" * 70)
 print(f"🍷 {moment_type}: {jesus_moments.moment9_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Time: {time_period}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print("🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print("   Jesus demonstrated His divine power over the natural world.")
    print()
    print("💡 DISCIPLES' REACTION:")
    print(f"   {disciples_fear}")
    print()
    print("💡 JESUS' COMMAND:")
    print(f"   {jesus_rebuke}")
    print()
    print("💡 FAITH QUESTION:")
    print(f"   {faith_question}")
    print()
    print("🙏 May we trust in Jesus' power and presence in the storms of life!")
    
# MOMENT 10 - FEEDING THE 5000
elif option == "10":
    moment_name = "Jesus Feeds the 5000"
    moment_type = "Miracle of Provision"
    location = "A remote place near Bethsaida"
    participants = "Jesus, disciples, crowd of 5000 people"
    main_verse = "John 6:11-13"
    verse_text = ("Jesus then took the loaves, gave thanks, and "
                  "distributed to those who were seated as much as they "
                  "wanted. He did the same with the fish. When they had "
                  "all had enough to eat, he said to his disciples, "
                  "'Gather the pieces that are left over. Let nothing be "
                  "wasted.' So they gathered them and filled twelve "
                  "baskets with the pieces of the five barley loaves left "
                  "over by those who had eaten.")
    significance = "demonstrated Jesus' compassion and divine provision"
    time_period = "During Jesus' ministry"
    miracle_details = ("Five loaves and two fish multiplied to feed "
                          "5000 people")
    disciples_observation = ("They gathered twelve baskets with the "
                             "leftovers, showing the abundance of Jesus' provision.")
    crowd_reaction = "Amazed and satisfied"
    jesus_compassion = ("Jesus had compassion on the crowd because "
                        "they were like sheep without a shepherd.")
    
    print("=" * 70)
print(f"🍷 {moment_type}: {jesus_moments.moment10_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Time: {time_period}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print("🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print("   Jesus provided abundantly for the physical needs of the crowd.")
    print()
    print("💡 MIRACLE DETAILS:")
    print(f"   {miracle_details}")
    print()
    print("💡 DISCIPLES' OBSERVATION:")
    print(f"   {disciples_observation}")
    print()
    print("🙏 May we trust in Jesus' ability to provide for our needs, "
          "both physical and spiritual!")
    
# MOMENT 11 - WALKING ON WATER
elif option == "11":
    moment_name = "Jesus Walks on Water"
    moment_type = "Miracle Over Nature"
    location = "Sea of Galilee"
    participants = "Jesus and His disciples"
    main_verse = "Matthew 14:25-27"
    verse_text = ("Shortly before dawn Jesus went out to them, "
                  "walking on the lake. When the disciples saw him "
                  "walking on the lake, they were terrified. 'It's a "
                  "ghost,' they said, and cried out in fear. But Jesus "
                  "immediately said to them: 'Take courage! It is I. Don't "
                  "be afraid.'")
    significance = "demonstrated Jesus' authority over nature"
    time_period = "During Jesus' ministry"
    disciples_fear = ("They were terrified and cried out in fear, "
                      "'It's a ghost!'")
    jesus_words = ("Take courage! It is I. Don't be afraid.")
    faith_challenge = ("Come," Jesus said. "Take courage! It is I. Don't be afraid.")
    peter_response = ("Lord, if it's you, tell me to come to you on the water.")
    peter_walk = ("Then Peter got down out of the boat, walked on the "
                  "water and came toward Jesus.")
    peter_doubt = ("But when he saw the wind, he was afraid and, "
                   "beginning to sink, cried out, 'Lord, save me!'")
    jesus_save = ("Immediately Jesus reached out his hand and caught him. "
                  "'You of little faith,' he said, 'why did you doubt?'")
    disciples_worship = ("Truly you are the Son of God.")       
    
    print("=" * 70)
   print(f"🍷 {moment_type}: {jesus_moments.moment11_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Time: {time_period}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print("🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print("   Jesus demonstrated His divine power over the natural world.")
    print()
    print("💡 DISCIPLES' REACTION:")
    print(f"   {disciples_fear}")
    print()
    print("💡 JESUS' WORDS:")
    print(f"   {jesus_words}")
    print()
    print("💡 FAITH CHALLENGE:")
    print(f"   {faith_challenge}")
    print()
    print("💡 PETER'S RESPONSE:")
    print(f"   {peter_response}")
    print()
    print("💡 PETER WALKS ON WATER:")
    print(f"   {peter_walk}")
    print()
    print("💡 PETER'S DOUBT:")
    print(f"   {peter_doubt}")
    print()
    print("💡 JESUS SAVES PETER:")
    print(f"   {jesus_save}")
    print()
    print("💡 DISCIPLES' WORSHIP:")
    print(f"   {disciples_worship} - Matthew 14:33")
    print()
    print("🙏 May we have faith to step out of the boat and trust in Jesus' power and presence in our lives!")
    
# MOMENT 12 - RAISING LAZARUS
elif option == "12":
    moment_name = "Jesus Raises Lazarus from the Dead"
    moment_type = "Miracle of Resurrection"
    location = "Bethany, near Jerusalem"
    participants = "Jesus, Lazarus, Mary, Martha, crowd"
    main_verse = "John 11:43-44"
    verse_text = ("When he had said this, Jesus called in a loud voice, "
                  "'Lazarus, come out!' The dead man came out, his hands and "
                  "feet wrapped with strips of linen, and a cloth around his "
                  "face. Jesus said to them, 'Take off the grave clothes and "
                  "let him go.'")
    significance = "demonstrated Jesus' power over death and foreshadowed His own resurrection"
    time_period = "Shortly before Jesus' final week"
    miracle_details = ("Lazarus had been dead for four days before "
                       "Jesus raised him to life")
    crowd_reaction = "Amazed and believed in Jesus"
    jesus_emotion = ("Jesus wept, showing His compassion and humanity.")
    faith_statement = ("I am the resurrection and the life. The one who "
                      "believes in me will live, even though they die.")
    martha_response = ("Yes, Lord. I believe that you are the Messiah, "
                       "the Son of God, who is to come into the world.")
    mary_response = ("Lord, if you had been here, my brother would not "
                     "have died.")
    jesus_consolation = ("Your brother will rise again.")   
    jesus_final_statement = ("I am the resurrection and the life. The "
                             "one who believes in me will live, even "
                             "though they die; and whoever lives by "
                             "believing in me will never die. Do you "
                             "believe this?")