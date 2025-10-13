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
    moment_name = "Calling the First Disciples"
    moment_type = "Building the Team"
    location = "Sea of Galilee"
    participants = "Jesus, Peter, Andrew, James, John"
    main_verse = "Matthew 4:19"
    verse_text = "Come, follow me, and I will send you out to fish for people."
    significance = "began Jesus' ministry of discipleship and mentoring"
    first_disciples = "Peter and Andrew (fishermen brothers)"
    their_response = "At once they left their nets and followed him"
    impact = "These ordinary men became world-changers"
    
    print("=" * 70)
    print(f"🎣 {moment_type}: {jesus_moments.moment6_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f"💬 \"{verse_text}\"")
    print()
    print(f"🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print()
    print(f"👥 THE FIRST CALLED:")
    print(f"   {first_disciples}")
    print()
    print(f"💪 THEIR IMMEDIATE RESPONSE:")
    print(f"   \"{their_response}\" - Matthew 4:20")
    print()
    print(f"🌍 ETERNAL IMPACT:")
    print(f"   {impact}!")
    print()
    print("🙏 Jesus still calls ordinary people to do extraordinary things!")

# MOMENT 7 - FIRST MIRACLE
elif option == "7":
    moment_name = "First Miracle - Water Into Wine"
    moment_type = "First Public Miracle"
    location = "Wedding at Cana in Galilee"
    participants = "Jesus, Mary, disciples, wedding guests"
    main_verse = "John 2:11"
    verse_text = "What Jesus did here in Cana of Galilee was the first of the signs through which he revealed his glory; and his disciples believed in him."
    significance = "revealed Jesus' divine power and glory"
    what_happened = "Transformed 6 stone jars of water (120-180 gallons) into finest wine"
    mary_words = "Do whatever he tells you"
    impact = "His disciples believed in him"
    
    print("=" * 70)
    print(f"🍷 {moment_type}: {jesus_moments.moment7_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f"💬 \"{verse_text}\"")
    print()
    print(f"🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print()
    print(f"✨ THE MIRACLE:")
    print(f"   {what_happened}!")
    print()
    print(f"💡 MARY'S WISDOM:")
    print(f"   \"{mary_words}\" - John 2:5")
    print(f"   The best advice ever given!")
    print()
    print(f"🙏 RESULT:")
    print(f"   {impact}.")
    print()
    print("🔥 Jesus brings transformation, abundance, and joy!")

# MOMENT 8 - HEALING PARALYTIC
elif option == "8":
    moment_name = "Healing the Paralytic Man"
    moment_type = "Authority to Forgive"
    location = "Capernaum, in a house"
    participants = "Jesus, paralytic man, 4 friends, Pharisees"
    main_verse = "Mark 2:10-11"
    verse_text = "But I want you to know that the Son of Man has authority on earth to forgive sins. So I tell you, get up, take your mat and go home."
    significance = "proved Jesus' authority to forgive sins"
    friends_faith = "Lowered him through the roof because of the crowd"
    jesus_first_words = "Son, your sins are forgiven"
    pharisees_thought = "Who can forgive sins but God alone?"
    
    print("=" * 70)
    print(f"🙏 {moment_type}: {jesus_moments.moment8_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f"💬 \"{verse_text}\"")
    print()
    print(f"🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}!")
    print()
    print(f"💪 FAITH IN ACTION:")
    print(f"   The man's friends {friends_faith}.")
    print(f"   Their persistence brought him to Jesus!")
    print()
    print(f"✝️ WHAT JESUS ADDRESSED FIRST:")
    print(f"   \"{jesus_first_words}\" - Mark 2:5")
    print(f"   Jesus knew the greatest need was spiritual healing!")
    print()
    print(f"😲 THE PHARISEES REALIZED:")
    print(f"   \"{pharisees_thought}\" - Mark 2:7")
    print(f"   They were right - only God can forgive sins.")
    print(f"   And Jesus IS God!")
    print()
    print("🙏 Jesus heals both body and soul!")

# MOMENT 9 - CALMING THE STORM
elif option == "9":
    moment_name = "Calming the Storm"
    moment_type = "Authority Over Nature"
    location = "Sea of Galilee"
    participants = "Jesus and His disciples"
    main_verse = "Mark 4:39-41"
    verse_text = "He got up, rebuked the wind and said to the waves, 'Quiet! Be still!' Then the wind died down and it was completely calm. He said to his disciples, 'Why are you so afraid? Do you still have no faith?'"
    significance = "revealed Jesus' authority over creation itself"
    situation = "Furious storm, boat filling with water, Jesus sleeping"
    disciples_cry = "Teacher, don't you care if we drown?"
    jesus_command = "Quiet! Be still!"
    disciples_response = "Who is this? Even the wind and waves obey him!"
    
    print("=" * 70)
    print(f"🌊 {moment_type}: {jesus_moments.moment9_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f"💬 \"{verse_text}\"")
    print()
    print(f"🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}!")
    print()
    print(f"⛈️ THE CRISIS:")
    print(f"   {situation}.")
    print()
    print(f"😰 DISCIPLES' PANIC:")
    print(f"   \"{disciples_cry}\" - Mark 4:38")
    print()
    print(f"⚡ JESUS' COMMAND:")
    print(f"   \"{jesus_command}\" - Mark 4:39")
    print(f"   Instant calm!")
    print()
    print(f"😲 THEIR AWE:")
    print(f"   \"{disciples_response}\" - Mark 4:41")
    print()
    print("🙏 No storm is too big for Jesus to calm!")

# MOMENT 10 - FEEDING 5000
elif option == "10":
    moment_name = "Feeding the Five Thousand"
    moment_type = "Miraculous Provision"
    location = "Remote place near Bethsaida"
    participants = "Jesus, 5000+ men (plus women and children), disciples"
    main_verse = "Matthew 14:19-20"
    verse_text = "Taking the five loaves and the two fish and looking up to heaven, he gave thanks and broke the loaves. Then he gave them to the disciples, and the disciples gave them to the people. They all ate and were satisfied."
    significance = "demonstrated Jesus as the Bread of Life who satisfies"
    starting_resources = "5 loaves of bread and 2 fish (from a boy)"
    people_fed = "Over 5,000 men, plus women and children"
    leftovers = "12 baskets full"
    
    print("=" * 70)
    print(f"🍞 {moment_type}: {jesus_moments.moment10_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f"💬 \"{verse_text}\"")
    print()
    print(f"🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print()
    print(f"🧺 WHAT THEY HAD:")
    print(f"   {starting_resources}")
    print(f"   A boy's lunch became a miracle!")
    print()
    print(f"👥 WHO WAS FED:")
    print(f"   {people_fed}!")
    print(f"   Possibly 15,000-20,000 total people!")
    print()
    print(f"✨ THE ABUNDANCE:")
    print(f"   Everyone ate until satisfied, with {leftovers} remaining!")
    print()
    print(f"💡 John 6:35 - Jesus said:")
    print(f"   'I am the bread of life. Whoever comes to me will never go hungry.'")
    print()
    print("🙏 Jesus multiplies what we offer Him!")

# MOMENT 11 - WALKING ON WATER
elif option == "11":
    moment_name = "Walking on Water"
    moment_type = "Divine Power Displayed"
    location = "Sea of Galilee"
    participants = "Jesus, Peter, the disciples"
    main_verse = "Matthew 14:27"
    verse_text = "But Jesus immediately said to them: 'Take courage! It is I. Don't be afraid.'"
    significance = "revealed Jesus' divine nature - He does what only God can do"
    time = "Fourth watch of the night (3-6 AM)"
    disciples_reaction = "They were terrified, thinking He was a ghost"
    peter_request = "Lord, if it's you, tell me to come to you on the water"
    peter_walked = "Yes! He walked on water too - while keeping his eyes on Jesus"
    lesson = "When Peter looked at the waves, he began to sink"
    
    print("=" * 70)
    print(f"🌊 {moment_type}: {jesus_moments.moment11_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"⏰ Time: {time}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f"💬 \"{verse_text}\"")
    print()
    print(f"🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}!")
    print()
    print(f"😱 INITIAL REACTION:")
    print(f"   {disciples_reaction}!")
    print()
    print(f"💪 PETER'S BOLD FAITH:")
    print(f"   \"{peter_request}\" - Matthew 14:28")
    print()
    print(f"🚶 DID PETER WALK ON WATER?")
    print(f"   {peter_walked}!")
    print()
    print(f"📖 THE LESSON:")
    print(f"   {lesson}.")
    print(f"   Keep your eyes on Jesus, not your circumstances!")
    print()
    print("🙏 With Jesus, the impossible becomes possible!")

# MOMENT 12 - RAISING LAZARUS
elif option == "12":
    moment_name = "Raising Lazarus from the Dead"
    moment_type = "Power Over Death"
    location = "Bethany, at Lazarus' tomb"
    participants = "Jesus, Lazarus, Mary, Martha, mourners"
    main_verse = "John 11:25-26"
    verse_text = "Jesus said to her, 'I am the resurrection and the life. The one who believes in me will live, even though they die; and whoever lives by believing in me will never die.'"
    significance = "foreshadowed Jesus' own resurrection and proved His power over death"
    days_dead = "4 days"
    martha_faith = "I believe that you are the Messiah, the Son of God"
    jesus_emotion = "Jesus wept - the shortest verse, deepest emotion"
    jesus_command = "Lazarus, come out!"
    result = "The dead man came out, wrapped in burial clothes"
    
    print("=" * 70)
    print(f"💀➡️❤️ {moment_type}: {jesus_moments.moment12_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f"💬 \"{verse_text}\"")
    print()
    print(f"🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}!")
    print()
    print(f"⏱️ THE SITUATION:")
    print(f"   Lazarus had been dead for {days_dead}.")
    print(f"   Everyone had lost hope.")
    print()
    print(f"🙏 MARTHA'S CONFESSION:")
    print(f"   \"{martha_faith}\" - John 11:27")
    print()
    print(f"😢 JESUS' COMPASSION:")
    print(f"   {jesus_emotion} (John 11:35)")
    print(f"   God understands our pain!")
    print()
    print(f"⚡ THE COMMAND:")
    print(f"   \"{jesus_command}\" - John 11:43")
    print()
    print(f"🎉 THE MIRACLE:")
    print(f"   {result}!")
    print(f"   Death obeys Jesus!")
    print()
    print("🙏 Jesus has power over your darkest situation!")