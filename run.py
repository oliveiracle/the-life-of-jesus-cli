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
if option.lower() == "quit" or option.lower() == "q":
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
birth_and_childhood = ["Angel's Announcement", "Birth in Bethlehem", "Jesus at Temple"]

# Beginning of Ministry (4-7)
beginning_ministry = ["Baptism", "Temptation", "First Disciples", "First Miracle"]

# Powerful Miracles (8-13)
powerful_miracles = [
    "Healing Paralytic",
    "Calming Storm",
    "Feeding 5000",
    "Walking on Water",
    "Raising Lazarus",
    "Healing Blind",
]

# Profound Teachings (14-17)
profound_teachings = [
    "Sermon on Mount",
    "Prodigal Son",
    "I Am the Way",
    "Greatest Commandment",
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
    "Ascension",
]

# All moments combined
all_moments = (
    birth_and_childhood
    + beginning_ministry
    + powerful_miracles
    + profound_teachings
    + final_week
)

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
    verse_text = (
        "Do not be afraid, Mary; you have found favor with God. "
        "You will conceive and give birth to a son, and you are "
        "to call him Jesus."
    )
    significance = "marked the beginning of God's plan for salvation"
    time_period = "Approximately 6 BC"
    mary_response = "I am the Lord's servant. May your word to me " "be fulfilled."

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
    print("   God chose a humble young woman to bear the Savior of " "the world.")
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
    verse_text = (
        "Do not be afraid. I bring you good news that will "
        "cause great joy for all the people. Today in the town "
        "of David a Savior has been born to you; he is the "
        "Messiah, the Lord."
    )
    significance = "God became flesh and dwelt among us"
    time_period = "Approximately 4-6 BC"
    angel_proclamation = (
        "Glory to God in the highest heaven, and on "
        "earth peace to those on whom his favor rests!"
    )

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
    print("💡 John 1:14 - 'The Word became flesh and made his " "dwelling among us.'")
    print()
    print("🙏 Jesus left heaven's glory to be born in humility - " "for you and me!")

# MOMENT 3 - JESUS AT THE TEMPLE
elif option == "3":
    moment_name = "Young Jesus at the Temple"
    moment_type = "Early Wisdom"
    location = "Jerusalem Temple"
    participants = "Jesus (age 12), Mary, Joseph, teachers of the law"
    main_verse = "Luke 2:46-47"
    verse_text = (
        "They found him in the temple courts, sitting among "
        "the teachers, listening to them and asking them "
        "questions. Everyone who heard him was amazed at his "
        "understanding and his answers."
    )
    significance = "revealed Jesus' divine wisdom even as a child"
    age = "12 years old"
    jesus_response = (
        "Why were you searching for me? Didn't you know "
        "I had to be in my Father's house?"
    )

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
    print("   Even the religious teachers were astonished by " "His understanding!")
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
    participants = "Jesus, John the Baptist, the Holy Spirit, " "God the Father"
    main_verse = "Matthew 3:16-17"
    verse_text = (
        "As soon as Jesus was baptized, he went up out of "
        "the water. At that moment heaven was opened, and he "
        "saw the Spirit of God descending like a dove and "
        "alighting on him. And a voice from heaven said, "
        "'This is my Son, whom I love; with him I am well pleased.'"
    )
    significance = (
        "marked the beginning of Jesus' public ministry " "and revealed the Trinity"
    )
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
    verse_text = (
        "Man shall not live on bread alone, but on every "
        "word that comes from the mouth of God."
    )
    significance = "proved Jesus' sinlessness and authority over Satan"
    duration = "40 days and 40 nights"
    temptations = (
        "Turn stones to bread, Jump from temple, " "Worship Satan for kingdoms"
    )
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
    verse_text = (
        '"Come, follow me," Jesus said, "and I will send you '
        'out to fish for people."'
    )
    significance = "started the formation of Jesus' core group of followers"
    time_period = "Early in Jesus' ministry"
    disciples_response = "At once they left their nets and followed him."

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
    print(
        "   Jesus called ordinary fishermen to become His " "extraordinary disciples."
    )
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
    verse_text = (
        "What Jesus did here in Cana of Galilee was the first "
        "of the signs through which he revealed his glory; and "
        "his disciples believed in him."
    )
    significance = "revealed Jesus' divine power and glory"
    event = "a wedding feast"
    miracle_details = "Turned water into wine, demonstrating His power " "over nature"

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
    print(
        "🙏 May we recognize and celebrate Jesus' transformative power " "in our lives!"
    )

# MOMENT 8 - HEALING THE PARALYTIC
elif option == "8":
    moment_name = "Jesus Heals a Paralytic"
    moment_type = "Miracle of Healing"
    location = "Capernaum"
    participants = "Jesus, paralytic, friends, crowd"
    main_verse = "Mark 2:11-12"
    verse_text = (
        "I tell you, get up, take your mat and go home."
        " He got up, took his mat and walked out in full view "
        "of them all. This amazed everyone and they praised God, "
        "saying, 'We have never seen anything like this!'"
    )
    significance = "demonstrated Jesus' authority to forgive sins and heal"
    healing_method = (
        "Lowered through the roof by friends, Jesus " "forgave his sins and healed him"
    )
    crowd_reaction = "Amazed and praised God"
    time_period = "During Jesus' early ministry"
    friends_faith = (
        "When Jesus saw their faith, he said to the "
        "paralytic, 'Son, your sins are forgiven.'"
    )

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
    print("   Jesus showed His power over both physical and spiritual " "realms.")
    print()
    print("💡 HEALING METHOD:")
    print(f"   {healing_method}")
    print()
    print(
        "🙏 May we have faith like the paralytic's friends, "
        "bringing others to Jesus for healing and forgiveness!"
    )

# MOMENT 9 - CALMING THE STORM
elif option == "9":
    moment_name = "Jesus Calms the Storm"
    moment_type = "Miracle Over Nature"
    location = "Sea of Galilee"
    participants = "Jesus and His disciples"
    main_verse = "Mark 4:39-41"
    verse_text = (
        "He got up, rebuked the wind and said to the "
        "waves, 'Quiet! Be still!' Then the wind died down "
        "and it was completely calm. He said to his disciples, "
        "'Why are you so afraid? Do you still have no faith?' "
        "They were terrified and asked each other, 'Who is this? "
        "Even the wind and the waves obey him!'"
    )
    significance = "revealed Jesus' authority over nature"
    time_period = "During Jesus' ministry"
    disciples_fear = (
        "They were terrified and asked each other, "
        "'Who is this? Even the wind and the waves obey him!'"
    )
    jesus_rebuke = "Quiet! Be still!"
    faith_question = "Why are you so afraid? Do you still have no faith?"

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
    verse_text = (
        "Jesus then took the loaves, gave thanks, and "
        "distributed to those who were seated as much as they "
        "wanted. He did the same with the fish. When they had "
        "all had enough to eat, he said to his disciples, "
        "'Gather the pieces that are left over. Let nothing be "
        "wasted.' So they gathered them and filled twelve "
        "baskets with the pieces of the five barley loaves left "
        "over by those who had eaten."
    )
    significance = "demonstrated Jesus' compassion and divine provision"
    time_period = "During Jesus' ministry"
    miracle_details = "Five loaves and two fish multiplied to feed " "5000 people"
    disciples_observation = (
        "They gathered twelve baskets with the "
        "leftovers, showing the abundance of Jesus' "
        "provision."
    )
    crowd_reaction = "Amazed and satisfied"
    jesus_compassion = (
        "Jesus had compassion on the crowd because "
        "they were like sheep without a shepherd."
    )

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
    print(
        "🙏 May we trust in Jesus' ability to provide for our needs, "
        "both physical and spiritual!"
    )

# MOMENT 11 - WALKING ON WATER
elif option == "11":
    moment_name = "Jesus Walks on Water"
    moment_type = "Miracle Over Nature"
    location = "Sea of Galilee"
    participants = "Jesus and His disciples"
    main_verse = "Matthew 14:25-27"
    verse_text = (
        "Shortly before dawn Jesus went out to them, "
        "walking on the lake. When the disciples saw him "
        "walking on the lake, they were terrified. 'It's a "
        "ghost,' they said, and cried out in fear. But Jesus "
        "immediately said to them: 'Take courage! It is I. Don't "
        "be afraid.'"
    )
    significance = "demonstrated Jesus' authority over nature"
    time_period = "During Jesus' ministry"
    disciples_fear = "They were terrified and cried out in fear, " "'It's a ghost!'"
    jesus_words = "Take courage! It is I. Don't be afraid."
    faith_challenge = '"Come," Jesus said.'
    peter_response = "Lord, if it's you, tell me to come to you on the " "water."
    peter_walk = (
        "Then Peter got down out of the boat, walked on the "
        "water and came toward Jesus."
    )
    peter_doubt = (
        "But when he saw the wind, he was afraid and, "
        "beginning to sink, cried out, 'Lord, save me!'"
    )
    jesus_save = (
        "Immediately Jesus reached out his hand and caught him. "
        "'You of little faith,' he said, 'why did you doubt?'"
    )
    disciples_worship = "Truly you are the Son of God."

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
    print(
        "🙏 May we have faith to step out of the boat and trust in "
        "Jesus' power and presence in our lives!"
    )

# MOMENT 12 - RAISING LAZARUS
elif option == "12":
    moment_name = "Jesus Raises Lazarus from the Dead"
    moment_type = "Miracle of Resurrection"
    location = "Bethany, near Jerusalem"
    participants = "Jesus, Lazarus, Mary, Martha, crowd"
    main_verse = "John 11:43-44"
    verse_text = (
        "When he had said this, Jesus called in a loud voice, "
        "'Lazarus, come out!' The dead man came out, his hands and "
        "feet wrapped with strips of linen, and a cloth around his "
        "face. Jesus said to them, 'Take off the grave clothes and "
        "let him go.'"
    )
    significance = (
        "demonstrated Jesus' power over death and " "foreshadowed His own resurrection"
    )
    time_period = "Shortly before Jesus' final week"
    miracle_details = (
        "Lazarus had been dead for four days before " "Jesus raised him to life"
    )
    crowd_reaction = "Amazed and believed in Jesus"
    jesus_emotion = "Jesus wept, showing His compassion and humanity."
    faith_statement = (
        "I am the resurrection and the life. The one who "
        "believes in me will live, even though they die."
    )
    martha_response = (
        "Yes, Lord. I believe that you are the Messiah, "
        "the Son of God, who is to come into the world."
    )
    mary_response = "Lord, if you had been here, my brother would not " "have died."
    jesus_consolation = "Your brother will rise again."
    jesus_final_statement = (
        "I am the resurrection and the life. The "
        "one who believes in me will live, even "
        "though they die; and whoever lives by "
        "believing in me will never die. Do you "
        "believe this?"
    )
    disciples_reaction = "After this, many of his disciples believed in him."

    print("=" * 70)
    print(f"🍷 {moment_type}: {jesus_moments.moment12_formatted}")
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
    print("   Jesus demonstrated His divine authority over life and death.")
    print()
    print("💡 MIRACLE DETAILS:")
    print(f"   {miracle_details}")
    print()
    print("💡 CROWD'S REACTION:")
    print(f"   {crowd_reaction}")
    print()
    print("💡 JESUS' EMOTION:")
    print(f"   {jesus_emotion} - John 11:35")
    print()
    print("💡 FAITH STATEMENT:")
    print(f"   {faith_statement} - John 11:25-26")
    print()
    print("💡 MARTHA'S RESPONSE:")
    print(f"   {martha_response} - John 11:27")
    print()
    print("💡 MARY'S RESPONSE:")
    print(f"   {mary_response} - John 11:32")
    print()
    print("💡 JESUS' CONSOLATION:")
    print(f"   {jesus_consolation} - John 11:23")
    print()
    print("💡 JESUS' FINAL STATEMENT:")
    print(f"   {jesus_final_statement} - John 11:25-26")
    print()
    print("💡 DISCIPLES' REACTION:")
    print(f"   {disciples_reaction} - John 11:45")
    print()
    print(
        "🙏 May we believe in Jesus as the resurrection and the life, "
        "trusting in His power over death!"
    )


# MOMENT 13 - HEALING THE BLIND
elif option == "13":
    moment_name = "Jesus Heals a Man Born Blind"
    moment_type = "Miracle of Healing"
    location = "Jerusalem"
    participants = "Jesus, the blind man, Pharisees, crowd"
    main_verse = "John 9:6-7"
    verse_text = (
        "After saying this, he spit on the ground, made some "
        "mud with the saliva, and put it on the man's eyes. "
        "'Go,' he told him, 'wash in the Pool of Siloam' "
        "(this word means 'Sent'). So the man went and washed, "
        "and came home seeing."
    )
    significance = "demonstrated Jesus' power to give both physical and spiritual sight"
    time_period = "During Jesus' ministry"
    healing_method = (
        "Made mud with saliva, applied to eyes, " "instructed to wash in Pool of Siloam"
    )
    crowd_reaction = "Amazed and questioned Jesus' authority"
    pharisees_reaction = (
        "They were divided, some saying he was not "
        "from God because he did not keep the Sabbath, "
        "others asking how a sinner could perform such "
        "signs."
    )
    blind_mans_faith = "One thing I do know. I was blind but now I see!"
    jesus_spiritual_sight = (
        "For judgment I have come into this world, "
        "so that the blind will see and those who see "
        "will become blind."
    )
    pharisees_final_reaction = (
        "They hurled insults at him and said, "
        "'You are this fellow's disciple! We are "
        "disciples of Moses!'"
    )
    jesus_final_statement = (
        "If you were blind, you would not be guilty "
        "of sin; but now that you claim you can see, "
        "your guilt remains."
    )
    disciples_reaction = "After this, many of his disciples believed in him."

    print("=" * 70)
    print(f"🍷 {moment_type}: {jesus_moments.moment13_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Time: {time_period}")
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print("🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print("   Jesus demonstrated His divine power to heal and give sight.")
    print()
    print("💡 HEALING METHOD:")
    print(f"   {healing_method}")
    print()
    print("💡 CROWD'S REACTION:")
    print(f"   {crowd_reaction}")
    print()
    print("💡 PHARISEES' REACTION:")
    print(f"   {pharisees_final_reaction}")
    print()
    print("💡 JESUS' FINAL STATEMENT:")
    print(f"   {jesus_final_statement}")
    print()
    print("💡 DISCIPLES REACTION:")
    print(f"   {disciples_reaction}")
    print()
    print(
        "🙏 May we have faith to see both physically and spiritually, "
        "trusting in Jesus."
    )

# MOMENT 14 - SERMON ON THE MOUNT
elif option == "14":
    moment_name = "The Sermon on the Mount"
    moment_type = "Profound Teaching"
    location = "A mountainside in Galilee"
    participants = "Jesus and His disciples, large crowd"
    main_verse = "Matthew 5:3-12"
    verse_text = (
        "Blessed are the poor in spirit, for theirs is the "
        "kingdom of heaven. Blessed are those who mourn, for "
        "they will be comforted. Blessed are the meek, for they "
        "will inherit the earth. Blessed are those who hunger and "
        "thirst for righteousness, for they will be filled. "
        "Blessed are the merciful, for they will be shown mercy. "
        "Blessed are the pure in heart, for they will see God. "
        "Blessed are the peacemakers, for they will be called "
        "children of God. Blessed are those who are persecuted "
        "because of righteousness, for theirs is the kingdom of "
        "heaven. Blessed are you when people insult you, "
        "persecute you and falsely say all kinds of evil against "
        "you because of me. Rejoice and be glad, because great is "
        "your reward in heaven, for in the same way they "
        "persecuted the prophets who were before you."
    )
    significance = "outlined the values and ethics of the Kingdom of God"
    time_period = "Early in Jesus' ministry"
    beatitudes_summary = (
        "Blessed are the poor in spirit, those who "
        "mourn, the meek, those who hunger and thirst "
        "for righteousness, the merciful, the pure in "
        "heart, the peacemakers, and those persecuted "
        "for righteousness."
    )
    disciples_reaction = (
        "When Jesus had finished saying these things, "
        "the crowds were amazed at his teaching."
    )
    teaching_style = "He taught with authority, unlike the teachers " "of the law."
    kingdom_values = (
        "Love your enemies, turn the other cheek, "
        "give to the needy, pray in secret, and store up "
        "treasures in heaven."
    )
    disciples_challenge = (
        "Be perfect, therefore, as your heavenly " "Father is perfect."
    )
    disciples_response = (
        "When Jesus had finished saying these things, "
        "the crowds were amazed at his teaching."
    )
    print("=" * 70)
    print(f"🍷 {moment_type}: {jesus_moments.moment14_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Time: {time_period}")
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print("🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print(
        "   Jesus presented a radical new way of living according to " "God's values."
    )
    print()
    print("💡 BEATITUDES SUMMARY:")
    print(f"   {beatitudes_summary}")
    print()
    print("💡 TEACHING STYLE:")
    print(f"   {teaching_style}")
    print()
    print("💡 KINGDOM VALUES:")
    print(f"   {kingdom_values}")
    print()
    print("💡 DISCIPLES' CHALLENGE:")
    print(f"   {disciples_challenge}")
    print()
    print("💡 DISCIPLES' RESPONSE:")
    print(f"   {disciples_response}")
    print()
    print(
        "🙏 May we live out the teachings of Jesus, embodying the values "
        "of the Kingdom of God in our daily lives!"
    )


# MOMENT 15 - PRODIGAL SON
elif option == "15":
    moment_name = "The Parable of the Prodigal Son"
    moment_type = "Profound Teaching"
    location = "Somewhere in Galilee"
    participants = "Jesus and His disciples, Pharisees, Crowd"
    main_verse = "Luke 15:20-24"
    verse_text = (
        "But while he was still a long way off, his father "
        "saw him and was filled with compassion for him; he ran "
        "to his son, threw his arms around him and kissed him. "
        "The son said to him, 'Father, I have sinned against "
        "heaven and against you. I am no longer worthy to be "
        "called your son.' But the father said to his servants, "
        "'Quick! Bring the best robe and put it on him. Put a "
        "ring on his finger and sandals on his feet. Bring the "
        "fattened calf and kill it. Let's have a feast and "
        "celebrate. For this son of mine was dead and is alive "
        "again; he was lost and is found.' So they began to "
        "celebrate."
    )
    significance = "illustrated God's boundless grace and forgiveness"
    time_period = "During Jesus' ministry"
    parable_summary = (
        "A younger son squanders his inheritance but is "
        "forgiven and welcomed back by his father."
    )
    pharisees_reaction = (
        "The Pharisees and the teachers of the law "
        "muttered, 'This man welcomes sinners and eats "
        "with them.'"
    )
    jesus_response = (
        "It is not the healthy who need a doctor, but "
        "the sick. I have not come to call the righteous, "
        "but sinners to repentance."
    )
    father_character = (
        "The father represents God, who is loving, "
        "forgiving, and eager to restore those who "
        "repent."
    )
    elder_son_reaction = (
        "The elder son represents the self-righteous "
        "who struggle to accept God's grace for others."
    )
    disciples_reaction = (
        "When Jesus had finished saying these things, "
        "the crowds were amazed at his teaching."
    )

    print("=" * 70)
    print(f"🍷 {moment_type}: {jesus_moments.moment15_formatted}")
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Time: {time_period}")
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print("🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print("   Jesus illustrated the depth of God's love and mercy.")
    print()
    print("💡 PARABLE SUMMARY:")
    print(f"   {parable_summary}")
    print()
    print("💡 PHARISEES' REACTION:")
    print(f"   {pharisees_reaction}")
    print()
    print("💡 JESUS' RESPONSE:")
    print(f"   {jesus_response}")
    print()
    print("💡 FATHER'S CHARACTER:")
    print(f"   {father_character}")
    print()
    print("💡 ELDER SON'S REACTION:")
    print(f"   {elder_son_reaction}")
    print()
    print("💡 DISCIPLES' REACTION:")
    print(f"   {disciples_reaction}")
    print()
    print(
        "🙏 May we embrace God's grace and extend forgiveness to others, "
        "just as the father in the parable did!"
    )

    # MOMENT 16 - I AM THE WAY, THE TRUTH, AND THE LIFE
elif option == "16":
    moment_name = "Jesus Declares: I Am the Way, the Truth, and the Life"
    moment_type = "Profound Declaration"
    location = "Upper Room, Jerusalem"
    participants = "Jesus and His disciples"
    main_verse = "John 14:6"
    verse_text = (
        "I am the way and the truth and the life. No one comes "
        "to the Father except through me."
    )
    significance = "declared Jesus as the ONLY way to salvation"
    context = "Last Supper discourse, before His arrest"
    thomas_question = (
        "Lord, we don't know where you are going, so how " "can we know the way?"
    )
    jesus_promise = "I am going there to prepare a place for you"
    philip_request = "Lord, show us the Father and that will be enough " "for us"
    jesus_response = "Anyone who has seen me has seen the Father"
    three_claims = (
        "THE WAY (path to God), THE TRUTH (reality incarnate), "
        "THE LIFE (source of eternal life)"
    )

    print("=" * 70)
    print(f"🛤️ {moment_type}: {jesus_moments.moment16_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"⏰ Context: {context}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print("🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print("   The most exclusive claim in all of Christianity!")
    print()
    print("❓ THOMAS' CONFUSION:")
    print(f'   "{thomas_question}" - John 14:5')
    print()
    print("✝️ JESUS' THREE-FOLD CLAIM:")
    print(f"   {three_claims}")
    print()
    print("   • THE WAY = The only path to God the Father")
    print("   • THE TRUTH = All truth is found in Him alone")
    print("   • THE LIFE = Eternal life comes only through Him")
    print()
    print("🏠 JESUS' PROMISE:")
    print(f'   "{jesus_promise}" - John 14:2')
    print("   He's preparing heaven for us!")
    print()
    print("👀 PHILIP'S REQUEST:")
    print(f'   "{philip_request}" - John 14:8')
    print()
    print("💡 JESUS' PROFOUND ANSWER:")
    print(f'   "{jesus_response}" - John 14:9')
    print("   Jesus IS God in human form!")
    print()
    print("⚠️ THE EXCLUSIVE TRUTH:")
    print("   'NO ONE comes to the Father EXCEPT through me'")
    print("   Not through good works, not through religion,")
    print("   not through philosophy - ONLY through Jesus Christ!")
    print()
    print("🙏 Salvation is found in Him alone! Jesus is THE way!")

    # MOMENT 17 - THE GREATEST COMMANDMENT
elif option == "17":
    moment_name = "The Greatest Commandment: Love God and Love Others"
    moment_type = "Essential Teaching"
    location = "Jerusalem Temple Courts"
    participants = "Jesus, Pharisees, teachers of the law"
    main_verse = "Matthew 22:37-39"
    verse_text = (
        "Love the Lord your God with all your heart and with "
        "all your soul and with all your mind. This is the first "
        "and greatest commandment. And the second is like it: "
        "Love your neighbor as yourself."
    )
    significance = "summarized all of God's law into two commands"
    context = "Pharisees testing Jesus with difficult questions"
    the_question = "Teacher, which is the greatest commandment in " "the Law?"
    first_commandment = "Love the Lord your God with ALL your heart, " "soul, and mind"
    second_commandment = "Love your neighbor as yourself"
    jesus_conclusion = "All the Law and the Prophets hang on these " "two commandments"

    print("=" * 70)
    print(f"❤️ {moment_type}: {jesus_moments.moment17_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print("🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print("   Jesus simplified 613 Jewish laws into TWO principles!")
    print()
    print("❓ THE PHARISEE'S TEST:")
    print(f'   "{the_question}" - Matthew 22:36')
    print("   They wanted to trap Him with a difficult question.")
    print()
    print("💕 THE FIRST COMMANDMENT:")
    print(f'   "{first_commandment}"')
    print()
    print("   ❤️ Heart = Love Him with emotions and affections")
    print("   👻 Soul = Love Him with your inner being")
    print("   🧠 Mind = Love Him with intellect and thoughts")
    print()
    print("🤝 THE SECOND COMMANDMENT:")
    print(f'   "{second_commandment}" - Matthew 22:39')
    print()
    print("   Not just 'be nice' - but love others as you love yourself!")
    print("   This includes enemies, strangers, and the difficult!")
    print()
    print("📜 JESUS' CONCLUSION:")
    print(f'   "{jesus_conclusion}" - Matthew 22:40')
    print()
    print("✨ THE BEAUTIFUL SIMPLICITY:")
    print("   Want to obey God? Do these TWO things:")
    print("   1. Love God completely")
    print("   2. Love people genuinely")
    print()
    print("💡 1 John 4:20 reminds us:")
    print('   "Whoever claims to love God yet hates a brother or sister')
    print("   is a liar. For whoever does not love their brother and sister,")
    print("   whom they have seen, cannot love God, whom they have " 'not seen."')
    print()
    print("🙏 Love God with everything. Love others like yourself!")

# MOMENT 18 - TRIUMPHAL ENTRY
elif option == "18":
    moment_name = "Triumphal Entry into Jerusalem"
    moment_type = "Prophetic Fulfillment"
    location = "Jerusalem, Mount of Olives to the Temple"
    participants = "Jesus, disciples, massive crowds, Pharisees"
    main_verse = "Matthew 21:9"
    verse_text = "Hosanna to the Son of David! Blessed is he who comes in the name of the Lord! Hosanna in the highest heaven!"
    significance = "fulfilled prophecy and began Jesus' final week before crucifixion"
    day = "Sunday (Palm Sunday)"
    prophecy_fulfilled = "Zechariah 9:9 - Your king comes gentle and riding on a donkey"
    what_happened = "Jesus rode a donkey's colt into Jerusalem"
    crowd_reaction = "Spread cloaks and palm branches on road, shouting praises"
    pharisees_complaint = "Teacher, rebuke your disciples!"
    jesus_response = "If they keep quiet, the stones will cry out"
    irony = "Same crowds shouting 'Hosanna!' would shout 'Crucify Him!' five days later"

    print("=" * 70)
    print(f"🌴 {moment_type}: {jesus_moments.moment18_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Day: {day}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print(f"🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print(f"   Jesus publicly declared Himself as Messiah-King!")
    print()
    print(f"📜 PROPHECY FULFILLED:")
    print(f"   {prophecy_fulfilled}")
    print(f"   Written 500 years before - fulfilled perfectly!")
    print()
    print(f"🐴 THE HUMBLE KING:")
    print(f"   {what_happened}.")
    print(f"   Not a war horse - a humble donkey!")
    print(f"   Jesus came as Prince of Peace, not military conqueror.")
    print()
    print(f"🎉 THE CROWD'S WORSHIP:")
    print(f"   {crowd_reaction}.")
    print(f"   'Hosanna' means 'Save us now!'")
    print()
    print(f"😤 PHARISEES' ANGER:")
    print(f'   "{pharisees_complaint}" - Luke 19:39')
    print()
    print(f"💬 JESUS' POWERFUL REPLY:")
    print(f'   "{jesus_response}" - Luke 19:40')
    print(f"   Creation itself recognizes the King!")
    print()
    print(f"💔 THE TRAGIC IRONY:")
    print(f"   {irony}.")
    print(f"   Human praise is fickle - only God's love is constant.")
    print()
    print(f"🔮 JESUS WEPT:")
    print(f"   Even amid celebration, Jesus wept over Jerusalem,")
    print(f"   knowing they would reject Him and face judgment.")
    print()
    print("🙏 Hosanna! Blessed is the King who comes in the Lord's name!")

    # MOMENT 19 - THE LAST SUPPER
elif option == "19":
    moment_name = "The Last Supper with the Disciples"
    moment_type = "Final Meal Together"
    location = "Upper Room, Jerusalem"
    participants = "Jesus and the twelve disciples (including Judas)"
    main_verse = "Luke 22:19-20"
    verse_text = "This is my body given for you; do this in remembrance of me. This cup is the new covenant in my blood, which is poured out for you."
    significance = "established communion and revealed Jesus' sacrificial purpose"
    day = "Thursday evening (Passover meal)"
    meal = "Passover feast celebrating Israel's exodus from Egypt"
    what_jesus_did = "Washed disciples' feet, instituted communion, revealed betrayer"
    bread_meaning = "His body, broken for us"
    wine_meaning = "His blood, shed for forgiveness of sins"
    new_command = "Love one another as I have loved you"
    judas_moment = "Jesus revealed Judas would betray Him, Judas left"

    print("=" * 70)
    print(f"🍞 {moment_type}: {jesus_moments.moment19_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Day: {day}")
    print(f"🍽️ Meal: {meal}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print(f"🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print(f"   The most important meal in human history!")
    print()
    print(f"💧 JESUS WASHES FEET:")
    print(f"   The Master became a servant, washing His disciples' feet.")
    print(f"   Teaching: True greatness is found in humble service.")
    print()
    print(f"🍞 THE BREAD:")
    print(f'   "Take and eat; this is my body" - Matthew 26:26')
    print(f"   Meaning: {bread_meaning}")
    print()
    print(f"🍷 THE WINE:")
    print(f'   "Drink from it, all of you. This is my blood" - Matthew 26:27-28')
    print(f"   Meaning: {wine_meaning}")
    print()
    print(f"📜 THE NEW COVENANT:")
    print(f"   Not the old law of Moses, but a NEW covenant of grace!")
    print(f"   Sealed not with animal blood, but with Jesus' precious blood.")
    print()
    print(f"💕 THE NEW COMMANDMENT:")
    print(f'   "{new_command}" - John 13:34')
    print(f"   Love like Jesus loves - sacrificially!")
    print()
    print(f"💔 THE BETRAYAL REVEALED:")
    print(f"   {judas_moment}.")
    print(f'   Jesus said: "What you are about to do, do quickly."')
    print()
    print(f"⛪ COMMUNION TODAY:")
    print(f"   Every time Christians take communion, we remember:")
    print(f"   • Jesus' body broken for our sins")
    print(f"   • Jesus' blood shed for our forgiveness")
    print(f"   • His sacrifice until He returns!")
    print()
    print("🙏 We remember His death until He comes again!")

    # MOMENT 20 - PRAYER IN THE GARDEN OF GETHSEMANE
elif option == "20":
    moment_name = "Prayer in the Garden of Gethsemane"
    moment_type = "Agonizing Prayer"
    location = "Garden of Gethsemane, Mount of Olives"
    participants = "Jesus, Peter, James, John (sleeping)"
    main_verse = "Matthew 26:39"
    verse_text = "My Father, if it is possible, may this cup be taken from me. Yet not as I will, but as you will."
    significance = "showed Jesus' full humanity and complete submission to God's will"
    time = "Thursday night, after Last Supper"
    jesus_emotion = "Overwhelmed with sorrow to the point of death"
    what_happened = "Jesus prayed three times while disciples slept"
    the_cup = "The cup of God's wrath for humanity's sin"
    sweat_like_blood = "His anguish was so intense, sweat became like drops of blood"
    disciples_failure = "Could you not keep watch with me for one hour?"
    jesus_resolve = "Yet not my will, but yours be done"

    print("=" * 70)
    print(f"🌿 {moment_type}: {jesus_moments.moment20_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"⏰ Time: {time}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print(f"🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print(f"   Jesus faced the cross with full knowledge of its horror.")
    print()
    print(f"😢 JESUS' ANGUISH:")
    print(f"   {jesus_emotion} - Matthew 26:38")
    print(f"   The weight of ALL humanity's sin was upon Him!")
    print()
    print(f"🩸 INTENSE SUFFERING:")
    print(f"   {sweat_like_blood} - Luke 22:44")
    print(f"   Medical condition: Hematidrosis (extreme stress)")
    print()
    print(f"🍷 THE CUP:")
    print(f"   {the_cup}.")
    print(f"   Jesus would drink OUR cup of judgment!")
    print()
    print(f"🙏 THREE PRAYERS:")
    print(f"   {what_happened}.")
    print(f"   Each time: 'Father, if possible, take this cup...'")
    print(f"   Each time: 'Yet not my will, but yours.'")
    print()
    print(f"😴 DISCIPLES SLEEP:")
    print(f'   "{disciples_failure}" - Matthew 26:40')
    print(f"   Jesus faced His darkest hour alone.")
    print()
    print(f"✊ THE FINAL RESOLVE:")
    print(f'   "{jesus_resolve}" - Luke 22:42')
    print(f"   Complete surrender to God's plan!")
    print()
    print(f"💪 THEN HE AROSE:")
    print(f"   'Rise! Let us go! Here comes my betrayer!'")
    print(f"   Jesus chose the cross. For you. For me.")
    print()
    print("🙏 He could have called 12 legions of angels, but chose to save us!")

    # MOMENT 21 - THE TRIAL AND CONDEMNATION OF JESUS
elif option == "21":
    moment_name = "The Trial and Condemnation of Jesus"
    moment_type = "Illegal Trials"
    location = "Multiple locations: High Priest, Pilate, Herod, Pilate again"
    participants = "Jesus, Caiaphas, Pilate, Herod, false witnesses, angry mob"
    main_verse = "Isaiah 53:7"
    verse_text = "He was oppressed and afflicted, yet he did not open his mouth; he was led like a lamb to the slaughter."
    significance = "fulfilled prophecy of the suffering servant"
    time = "Thursday night through Friday morning"
    six_trials = "Three religious (Jewish) and three civil (Roman)"
    charges = "Blasphemy (religious), claiming to be king (political)"
    jesus_silence = "Jesus remained silent before false accusations"
    pilate_question = "Are you the king of the Jews?"
    jesus_answer = "You have said so"
    pilate_verdict = "I find no basis for a charge against this man"
    crowd_response = "Crucify him! Crucify him!"
    barabbas = "Pilate offered to release Jesus or Barabbas - crowd chose Barabbas"

    print("=" * 70)
    print(f"⚖️ {moment_type}: {jesus_moments.moment21_formatted}")
    print("=" * 70)
    print(f"📍 Locations: {location}")
    print(f"👥 Key People: {participants}")
    print(f"⏰ Time: {time}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print(f"🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print(f"   The most unjust trial in human history!")
    print()
    print(f"⚖️ SIX ILLEGAL TRIALS:")
    print(f"   {six_trials}.")
    print(f"   All conducted illegally - at night, without proper witnesses.")
    print()
    print(f"🤐 JESUS' SILENCE:")
    print(f"   {jesus_silence}.")
    print(f"   Fulfilling Isaiah's prophecy perfectly!")
    print()
    print(f"❓ PILATE'S QUESTION:")
    print(f'   "{pilate_question}" - John 18:33')
    print()
    print(f"💬 JESUS' RESPONSE:")
    print(f'   "{jesus_answer}"')
    print(f'   "My kingdom is not of this world" - John 18:36')
    print()
    print(f"✋ PILATE FINDS NO GUILT:")
    print(f'   "{pilate_verdict}" - Luke 23:4')
    print(f"   THREE times Pilate declared Jesus innocent!")
    print()
    print(f"😤 THE CROWD'S RAGE:")
    print(f'   "{crowd_response}" - Luke 23:21')
    print(f"   The innocent died so the guilty could go free.")
    print()
    print(f"🔄 BARABBAS RELEASED:")
    print(f"   {barabbas} (murderer and rebel).")
    print(f"   Picture of substitution: Jesus took our place!")
    print()
    print(f"💧 PILATE WASHES HANDS:")
    print(f'   "I am innocent of this man\'s blood" - Matthew 27:24')
    print(f"   But cowardice doesn't equal innocence.")
    print()
    print("🙏 The sinless one was condemned so sinners could be justified!")

    # MOMENT 22 - THE CRUCIFIXION AT CALVARY
elif option == "22":
    moment_name = "The Crucifixion at Calvary"
    moment_type = "Ultimate Sacrifice"
    location = "Golgotha (Place of the Skull), outside Jerusalem"
    participants = "Jesus, two criminals, Mary, John, Roman soldiers, mockers"
    main_verse = "John 19:30"
    verse_text = "It is finished."
    significance = "accomplished salvation for all humanity through Jesus' death"
    time = "Friday, 9 AM to 3 PM (six hours on the cross)"
    the_journey = "Jesus carried cross, fell, Simon of Cyrene helped"
    crucified_with = "Two criminals, one on each side"
    seven_sayings = "Father forgive them; Today in paradise; Woman behold your son; My God why; I thirst; It is finished; Into your hands"
    darkness = "From noon to 3 PM, darkness covered the land"
    jesus_cry = "My God, my God, why have you forsaken me?"
    the_moment = "Jesus bore the weight of ALL sin - past, present, future"

    print("=" * 70)
    print(f"✝️ {moment_type}: {jesus_moments.moment22_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"⏰ Time: {time}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print(f"🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}!")
    print(f"   The pivotal moment in all of human history!")
    print()
    print(f"🚶 THE JOURNEY TO GOLGOTHA:")
    print(f"   {the_journey}.")
    print(f"   Jesus, already beaten, carried the instrument of His death.")
    print()
    print(f"🔨 NAILED TO THE CROSS:")
    print(f"   {crucified_with}.")
    print(f"   Jesus in the middle - between heaven and earth, between two thieves.")
    print()
    print(f"💬 THE SEVEN LAST SAYINGS:")
    print(f"   {seven_sayings}")
    print()
    print(f"🙏 'FATHER, FORGIVE THEM':")
    print(f'   "They do not know what they are doing" - Luke 23:34')
    print(f"   Even in agony, Jesus forgave!")
    print()
    print(f"🌑 SUPERNATURAL DARKNESS:")
    print(f"   {darkness} - Matthew 27:45")
    print(f"   Creation mourned as Creator died!")
    print()
    print(f"😢 THE CRY OF ABANDONMENT:")
    print(f'   "{jesus_cry}" - Matthew 27:46')
    print(f"   {the_moment}.")
    print(f"   God the Father turned away - Jesus experienced hell for us!")
    print()
    print(f"💔 JESUS SUFFERED:")
    print(f"   • Physical: Beaten, whipped, nailed, suffocating")
    print(f"   • Emotional: Mocked, abandoned, betrayed")
    print(f"   • Spiritual: Bore God's wrath for sin")
    print()
    print(f"🩸 HIS BLOOD:")
    print(f"   Not just physical death - but spiritual separation from God.")
    print(f"   He paid the price we could never pay!")
    print()
    print("🙏 Thank You, Jesus, for dying in my place! The cross changes everything!")

    # MOMENT 23 - IT IS FINISHED - JESUS' FINAL WORDS
elif option == "23":
    moment_name = "It Is Finished - Jesus' Final Words"
    moment_type = "Victory Declaration"
    location = "The cross at Golgotha"
    participants = "Jesus, watching crowd, Roman centurion"
    main_verse = "John 19:30"
    verse_text = "When he had received the drink, Jesus said, 'It is finished.' With that, he bowed his head and gave up his spirit."
    significance = "declared that salvation was complete"
    greek_word = "Tetelestai - paid in full, accomplished, completed"
    what_finished = (
        "Sin's penalty, God's wrath, prophecies, old covenant, Satan's power"
    )
    not_defeat = "Not 'I am finished' but 'IT is finished' - VICTORY!"
    centurion_confession = "Surely he was the Son of God!"
    supernatural_signs = "Temple curtain torn, earthquake, rocks split, tombs opened"

    print("=" * 70)
    print(f"🏆 {moment_type}: {jesus_moments.moment23_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print(f"🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print(f"   Three words that changed eternity!")
    print()
    print(f"📜 THE GREEK WORD:")
    print(f"   '{greek_word}'")
    print(f"   A commercial term meaning: PAID IN FULL!")
    print(f"   Written on receipts when debt was completely paid.")
    print()
    print(f"✅ WHAT WAS FINISHED:")
    print(f"   • Sin's penalty - PAID")
    print(f"   • God's wrath - SATISFIED")
    print(f"   • Old Testament prophecies - FULFILLED")
    print(f"   • Old covenant - COMPLETED")
    print(f"   • Satan's power - DEFEATED")
    print(f"   • The work of salvation - ACCOMPLISHED")
    print()
    print(f"💪 NOT DEFEAT BUT VICTORY:")
    print(f"   {not_defeat}")
    print(f"   Jesus didn't die as victim - He died as VICTOR!")
    print()
    print(f"⛪ THE TEMPLE CURTAIN TORN:")
    print(f"   {supernatural_signs}.")
    print(f"   The curtain separating God from people - TORN TOP TO BOTTOM!")
    print(f"   God tore it - the way to Him is now OPEN!")
    print()
    print(f"🎖️ CENTURION'S CONFESSION:")
    print(f'   "{centurion_confession}" - Matthew 27:54')
    print(f"   Even the Roman soldier recognized who Jesus was!")
    print()
    print(f"💡 WHAT IT MEANS FOR YOU:")
    print(f"   • Your sins - PAID FOR")
    print(f"   • Your debt - CANCELLED")
    print(f"   • Your access to God - OPENED")
    print(f"   • Your salvation - SECURED")
    print()
    print(f"📖 Hebrews 10:10:")
    print(f'   "We have been made holy through the sacrifice of')
    print(f'   the body of Jesus Christ ONCE FOR ALL."')
    print()
    print("🙏 It is finished! Nothing to add, nothing to earn - just BELIEVE!")

    # MOMENT 24 - THE RESURRECTION - HE IS RISEN!
elif option == "24":
    moment_name = "The Resurrection - He Is Risen!"
    moment_type = "Victory Over Death"
    location = "Joseph's tomb, outside Jerusalem"
    participants = "Jesus, Mary Magdalene, angels, disciples, guards"
    main_verse = "Matthew 28:6"
    verse_text = "He is not here; he has risen, just as he said. Come and see the place where he lay."
    significance = "proved Jesus is God and conquered death forever"
    day = "Sunday morning (Resurrection Sunday)"
    buried = "Friday evening in Joseph of Arimathea's tomb"
    tomb_secured = "Sealed with stone, guarded by Roman soldiers"
    earthquake = "Angel descended, rolled back stone, guards fell like dead men"
    empty_tomb = "Grave clothes left behind, body gone"
    first_witness = "Mary Magdalene - Jesus appeared to her first"
    jesus_words = "Do not be afraid. Go and tell my brothers"
    proof = "Appeared to over 500 people over 40 days"

    print("=" * 70)
    print(f"🌅 {moment_type}: {jesus_moments.moment24_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Day: {day}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print(f"🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}!")
    print(f"   THE most important event in human history!")
    print()
    print(f"⚰️ THE BURIAL:")
    print(f"   {buried}.")
    print(f"   {tomb_secured}.")
    print(f"   Impossible to steal the body!")
    print()
    print(f"🌍 SUNDAY MORNING:")
    print(f"   {earthquake}!")
    print(f"   The angel's message: 'Do not be afraid!'")
    print()
    print(f"😲 THE EMPTY TOMB:")
    print(f"   {empty_tomb}.")
    print(f"   The stone wasn't rolled away to let Jesus OUT...")
    print(f"   ...but to let the disciples IN to see He was gone!")
    print()
    print(f"👩 FIRST WITNESS:")
    print(f"   {first_witness}.")
    print(f"   In a culture that didn't value women's testimony,")
    print(f"   God chose a woman to be the first evangelist!")
    print()
    print(f"💬 JESUS' FIRST WORDS:")
    print(f'   "{jesus_words}" - Matthew 28:10')
    print()
    print(f"✅ UNDENIABLE PROOF:")
    print(f"   {proof} - 1 Corinthians 15:6")
    print(f"   Not hallucination - FACT!")
    print()
    print(f"💪 WHAT THE RESURRECTION PROVES:")
    print(f"   • Jesus IS God - death couldn't hold Him")
    print(f"   • His sacrifice was ACCEPTED - God raised Him")
    print(f"   • We WILL rise - He is the firstfruits")
    print(f"   • Death is DEFEATED - the grave has no power")
    print(f"   • Christianity is TRUE - it all hinges on this!")
    print()
    print(f"📖 1 Corinthians 15:17:")
    print(f'   "If Christ has not been raised, your faith is futile."')
    print()
    print(f"🎉 BUT HE IS RISEN!")
    print(f"   Death could not hold Him!")
    print(f"   The tomb is EMPTY!")
    print(f"   Jesus is ALIVE!")
    print()
    print("🙌 HE IS RISEN! HE IS RISEN INDEED! Hallelujah!")

    # MOMENT 25 - THE ASCENSION INTO HEAVEN
elif option == "25":
    moment_name = "The Ascension into Heaven"
    moment_type = "Glorious Return"
    location = "Mount of Olives, near Bethany"
    participants = "Jesus, the eleven disciples, angels"
    main_verse = "Acts 1:9"
    verse_text = "After he said this, he was taken up before their very eyes, and a cloud hid him from their sight."
    significance = "marked Jesus' return to heaven and commissioning of His church"
    day = "Thursday, 40 days after resurrection"
    forty_days = "Jesus appeared many times, teaching about the Kingdom"
    great_commission = "Go and make disciples of all nations"
    promise = "You will receive power when the Holy Spirit comes"
    how_he_left = "Lifted up before their eyes into a cloud"
    angels_message = "This same Jesus will come back the same way"
    what_now = "Jesus is seated at God's right hand, interceding for us"
    he_will_return = "He is coming back - physically, visibly, gloriously"

    print("=" * 70)
    print(f"☁️ {moment_type}: {jesus_moments.moment25_formatted}")
    print("=" * 70)
    print(f"📍 Location: {location}")
    print(f"👥 Key People: {participants}")
    print(f"📅 Day: {day}")
    print()
    print(f"📖 KEY VERSE: {main_verse}")
    print(f'💬 "{verse_text}"')
    print()
    print(f"🎯 SIGNIFICANCE:")
    print(f"   This moment {significance}.")
    print(f"   Jesus completed His earthly mission!")
    print()
    print(f"📅 THE 40 DAYS:")
    print(f"   {forty_days}.")
    print(f"   Proving His resurrection and preparing His disciples.")
    print()
    print(f"🌍 THE GREAT COMMISSION:")
    print(f'   "{great_commission}" - Matthew 28:19')
    print(f"   This is OUR mission until He returns!")
    print()
    print(f"🔥 THE PROMISE:")
    print(f'   "{promise}" - Acts 1:8')
    print(f"   Ten days later: Pentecost - the Spirit came!")
    print()
    print(f"☁️ THE ASCENSION:")
    print(f"   {how_he_left}.")
    print(f"   Not death, not disappearing - ASCENDING in glory!")
    print()
    print(f"👼 THE ANGELS' PROMISE:")
    print(f'   "{angels_message}" - Acts 1:11')
    print(f"   He went up from Mount of Olives...")
    print(f"   He will RETURN to Mount of Olives!")
    print()
    print(f"👑 WHERE IS JESUS NOW:")
    print(f"   {what_now}.")
    print(f"   'He always lives to intercede' - Hebrews 7:25")
    print()
    print(f"📖 Hebrews 1:3:")
    print(f'   "After he had provided purification for sins,')
    print(f'   he sat down at the right hand of the Majesty in heaven."')
    print()
    print(f"⏰ HE IS COMING BACK:")
    print(f"   {he_will_return}!")
    print(f"   Are you ready?")
    print()
    print(f"🎺 Revelation 1:7:")
    print(f'   "Look, he is coming with the clouds, and every eye will see him."')
    print()
    print("🙏 From manger to cross to throne - Jesus is LORD!")
    print("🙌 Even so, come Lord Jesus! Maranatha!")

else:
    print(f"❌ Invalid option: {option}")
    print("💡 Please choose a number between 1 and 25.")

