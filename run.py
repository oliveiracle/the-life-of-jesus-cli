import jesus_moments

# 1. TITLE AND MAIN MENU
jesus_moments.show_title()
print("Explore 25 key moments from the life of Jesus Christ:\n")

print("\n🌟 BIRTH & CHILDHOOD:")
print("1-Angel's Announcement | 2-Birth in Bethlehem | 3-Jesus at Temple\n")

print("\n⚡ BEGINNING OF MINISTRY:")
print("4-Baptism | 5-Temptation | 6-First Disciples | 7-First Miracle\n")

print("\n🔥 POWERFUL MIRACLES:")
print("8-Healing Paralytic | 9-Calming Storm | 10-Feeding 5000")
print("11-Walking on Water | 12-Raising Lazarus | 13-Healing Blind\n")

print("\n📖 PROFOUND TEACHINGS:")
print("14-Sermon on Mount | 15-Prodigal Son")
print("16-I Am the Way | 17-Greatest Commandment\n")

print("\n✝ FINAL WEEK:")
print("18-Triumphal Entry | 19-Last Supper | 20-Gethsemane")
print("21-Trial | 22-Crucifixion | 23-It Is Finished")
print("24-Resurrection | 25-Ascension\n")

# 3. CATEGORIZING THE 25 MOMENTS OF JESUS' LIFE
birth_and_childhood = ["Angel's Announcement", "Birth in Bethlehem", "Jesus at Temple"]

beginning_ministry = ["Baptism", "Temptation", "First Disciples", "First Miracle"]

powerful_miracles = [
    "Healing Paralytic",
    "Calming Storm",
    "Feeding 5000",
    "Walking on Water",
    "Raising Lazarus",
    "Healing Blind",
]

profound_teachings = [
    "Sermon on Mount",
    "Prodigal Son",
    "I Am the Way",
    "Greatest Commandment",
]

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

all_moments = (
    birth_and_childhood
    + beginning_ministry
    + powerful_miracles
    + profound_teachings
    + final_week
)

# 2. USER INPUT AND VALIDATION + PROCESSAMENTO
while True:
    user_input = input("Enter your choice (1-25) or 'quit' to exit: ")
    option = user_input.strip()

    # Handle quit option
    if option.lower() == "quit" or option.lower() == "q":
        print("\n✝ Thank you for exploring the life of Jesus!")
        print("\n🙏 'I am with you always, to the very end of the age'")
        print("   - Matthew 28:20")
        break

    # Validate input
    if not option.isdigit() or int(option) < 1 or int(option) > 25:
        print(f"\n❌ '{option}' is not a valid moment number!")
        print("\n💡 Please choose a number between 1 and 25, or type 'quit'.")
        continue

    # 4. THE 25 MOMENTS OF JESUS CHRIST
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
        mary_response = "I am the Lord's servant. May your word to me be fulfilled."

        print("=" * 70)
        print(f"\n✨ {moment_type}: {jesus_moments.moment1_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   This moment {significance}.")
        print("   God chose a humble young woman to bear the Savior of the world.")
        print()
        print("\n💡 MARY'S FAITHFUL RESPONSE:")
        print(f'   "{mary_response}" - Luke 1:38')
        print()
        print("\n🙏 May we respond to God's call with the same faith and humility!")

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
        print(f"\n⭐ {moment_type}: {jesus_moments.moment2_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}!")
        print("   The eternal God took on human form to save humanity.")
        print()
        print("\n🎵 THE ANGELS' SONG:")
        print(f'   "{angel_proclamation}" - Luke 2:14')
        print()
        print(
            "\n💡 John 1:14 - 'The Word became flesh and made his dwelling among us.'"
        )
        print()
        print("\n🙏 Jesus left heaven's glory to be born in humility - for you and me!")

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
        print(f"\n📚 {moment_type}: {jesus_moments.moment3_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Jesus' Age: {age}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   Even as a boy, Jesus showed His divine nature.")
        print()
        print(f'\n💡 "{jesus_response}" - Luke 2:49')
        print()
        print("\n🙏 Even as a child, Jesus knew His divine purpose!")

    elif option == "4":
        moment_name = "The Baptism of Jesus"
        moment_type = "Public Ministry Begins"
        location = "Jordan River"
        participants = "Jesus, John the Baptist"
        main_verse = "Matthew 3:16"
        verse_text = (
            "As soon as Jesus was baptized, he went up out of "
            "the water. At that moment heaven was opened, and "
            "he saw the Spirit of God descending like a dove."
        )
        significance = "inaugurated Jesus' public ministry with divine affirmation"
        time_period = "Approximately AD 26"
        god_affirmation = "This is my Son, whom I love; with him I am well pleased."

        print("=" * 70)
        print(f"\n💧 {moment_type}: {jesus_moments.moment4_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   The Trinity is revealed in this pivotal moment.")
        print()
        print("\n💡 GOD'S VOICE FROM HEAVEN:")
        print(f'   "{god_affirmation}" - Matthew 3:17')
        print()
        print("\n🙏 May we seek God's approval in all we do!")

    elif option == "5":
        moment_name = "The Temptation of Jesus"
        moment_type = "Victory Over Sin"
        location = "Wilderness"
        participants = "Jesus, the devil"
        main_verse = "Matthew 4:1"
        verse_text = (
            "Then Jesus was led by the Spirit into the wilderness "
            "to be tempted by the devil."
        )
        significance = "demonstrated Jesus' obedience and reliance on Scripture"
        time_period = "Approximately AD 26"
        jesus_quote = "It is written: 'Man shall not live on bread alone...'"

        print("=" * 70)
        print(f"\n🛡️ {moment_type}: {jesus_moments.moment5_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   Jesus resisted temptation using God's Word.")
        print()
        print("\n💡 JESUS' RESPONSE TO TEMPTATION:")
        print(f'   "{jesus_quote}" - Matthew 4:4')
        print()
        print("\n🙏 Let us arm ourselves with Scripture against trials!")

    elif option == "6":
        moment_name = "Calling the First Disciples"
        moment_type = "Building the Team"
        location = "Near Jordan River"
        participants = "Jesus, John the Baptist, Andrew, Simon Peter, Philip, Nathanael"
        main_verse = "John 1:35-36"
        verse_text = (
            "The next day John was there again with two of his "
            "disciples. When he saw Jesus passing by, he said, "
            "'Look, the Lamb of God!'"
        )
        significance = "began gathering followers who would spread the Gospel"
        time_period = "Approximately AD 26"
        disciple_response = "We have found the one Moses wrote about..."

        print("=" * 70)
        print(f"\n👥 {moment_type}: {jesus_moments.moment6_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   The foundation of the early church was laid.")
        print()
        print("\n💡 DISCIPLES' EXCITEMENT:")
        print(f'   "{disciple_response}" - John 1:45')
        print()
        print("\n🙏 May we follow Jesus with the same zeal!")

    elif option == "7":
        moment_name = "The First Miracle at Cana"
        moment_type = "Sign of Glory"
        location = "Cana"
        participants = "Jesus, Mary, servants"
        main_verse = "John 2:7-8"
        verse_text = (
            "Jesus said to the servants, 'Fill the jars with water'; "
            "so they filled them to the brim. Then he told them, "
            "'Now draw some out and take it to the master of the banquet.'"
        )
        significance = "revealed Jesus' glory and strengthened the disciples' faith"
        time_period = "Approximately AD 27"
        mary_instruction = "Do whatever he tells you."

        print("=" * 70)
        print(f"\n🍷 {moment_type}: {jesus_moments.moment7_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   Water turned to wine, a sign of abundance.")
        print()
        print("\n💡 MARY'S WORDS:")
        print(f'   "{mary_instruction}" - John 2:5')
        print()
        print("\n🙏 Obey Jesus in every situation!")

    elif option == "8":
        moment_name = "Healing the Paralytic"
        moment_type = "Authority Over Sin"
        location = "Capernaum"
        participants = "Jesus, paralyzed man, friends, scribes, Pharisees"
        main_verse = "Luke 5:18"
        verse_text = (
            "Some men came carrying a paralyzed man on a mat and "
            "tried to take him into the house to lay him before Jesus."
        )
        significance = "demonstrated Jesus' power to forgive sins and heal bodies"
        time_period = "Approximately AD 28"
        jesus_forgiveness = "Friend, your sins are forgiven."

        print("=" * 70)
        print(f"\n🛏️ {moment_type}: {jesus_moments.moment8_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   Faith of friends led to healing.")
        print()
        print("\n💡 JESUS' WORDS:")
        print(f'   "{jesus_forgiveness}" - Luke 5:20')
        print()
        print("\n🙏 Bring others to Jesus in faith!")

    elif option == "9":
        moment_name = "Calming the Storm"
        moment_type = "Power Over Nature"
        location = "Sea of Galilee"
        participants = "Jesus, disciples"
        main_verse = "Matthew 8:23-24"
        verse_text = (
            "Then he got into the boat and his disciples followed him. "
            "Suddenly a furious storm came up on the lake, so that the "
            "waves swept over the boat."
        )
        significance = "showed Jesus' authority over creation and taught faith"
        time_period = "Approximately AD 28"
        disciples_cry = "Lord, save us! We're going to drown!"

        print("=" * 70)
        print(f"\n⛈️ {moment_type}: {jesus_moments.moment9_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   'Why are you so afraid?' Jesus asked.")
        print()
        print("\n💡 DISCIPLES' FEAR:")
        print(f'   "{disciples_cry}" - Matthew 8:25')
        print()
        print("\n🙏 Trust Jesus in life's storms!")

    elif option == "10":
        moment_name = "Feeding the 5000"
        moment_type = "Miracle of Provision"
        location = "Near Sea of Galilee"
        participants = "Jesus, disciples, crowd of 5000 men"
        main_verse = "Matthew 14:19"
        verse_text = (
            "Taking the five loaves and the two fish and looking up "
            "to heaven, he gave thanks and broke the loaves. Then he "
            "gave them to the disciples..."
        )
        significance = "affirmed Jesus as the provider and foreshadowed the Eucharist"
        time_period = "Approximately AD 28"
        leftover = "Twelve basketfuls of broken pieces."

        print("=" * 70)
        print(f"\n🍞 {moment_type}: {jesus_moments.moment10_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   Abundance from scarcity.")
        print()
        print("\n💡 THE REMAINDER:")
        print(f"   {leftover} - Matthew 14:20")
        print()
        print("\n🙏 God provides more than enough!")

    elif option == "11":
        moment_name = "Walking on Water"
        moment_type = "Master of the Sea"
        location = "Sea of Galilee"
        participants = "Jesus, disciples (including Peter)"
        main_verse = "Matthew 14:25-26"
        verse_text = (
            "During the fourth watch of the night Jesus went out to "
            "them, walking on the lake. When the disciples saw him "
            "walking on the lake, they were terrified."
        )
        significance = "demonstrated Jesus' divine power and Peter's brief faith"
        time_period = "Approximately AD 28"
        peter_step = "Lord, if it's you, tell me to come to you on the water."

        print("=" * 70)
        print(f"\n🌊 {moment_type}: {jesus_moments.moment11_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   'It is I; don't be afraid.'")
        print()
        print("\n💡 PETER'S BOLD STEP:")
        print(f'   "{peter_step}" - Matthew 14:28')
        print()
        print("\n🙏 Step out in faith toward Jesus!")

    elif option == "12":
        moment_name = "Raising Lazarus"
        moment_type = "Victory Over Death"
        location = "Bethany"
        participants = "Jesus, Lazarus, Mary, Martha"
        main_verse = "John 11:43-44"
        verse_text = (
            "Jesus called in a loud voice, 'Lazarus, come out!' "
            "The dead man came out, his hands and feet wrapped "
            "with strips of linen..."
        )
        significance = "powerful sign pointing to Jesus' own resurrection"
        time_period = "Approximately AD 30"
        martha_faith = "I believe that you are the Messiah, the Son of God."

        print("=" * 70)
        print(f"\n⚰️ {moment_type}: {jesus_moments.moment12_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   'I am the resurrection and the life.'")
        print()
        print("\n💡 MARTHA'S CONFESSION:")
        print(f'   "{martha_faith}" - John 11:27')
        print()
        print("\n🙏 Believe in Jesus, the giver of life!")

    elif option == "13":
        moment_name = "Healing the Blind Man"
        moment_type = "Light of the World"
        location = "Jerusalem"
        participants = "Jesus, blind man, Pharisees"
        main_verse = "John 9:25"
        verse_text = (
            "He replied, 'Whether he is a sinner or not, I don’t know. "
            "One thing I do know. I was blind but now I see!'"
        )
        significance = "revealed Jesus as the light and led to bold testimony"
        time_period = "Approximately AD 30"
        blind_man_defense = "If this man were not from God, he could do nothing."

        print("=" * 70)
        print(f"\n👁️ {moment_type}: {jesus_moments.moment13_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   Simple faith transformed a life.")
        print()
        print("\n💡 BLIND MAN'S TESTIMONY:")
        print(f'   "{blind_man_defense}" - John 9:33')
        print()
        print("\n🙏 Share your story of transformation!")

    elif option == "14":
        moment_name = "The Sermon on the Mount"
        moment_type = "Kingdom Teachings"
        location = "Mountainside near Sea of Galilee"
        participants = "Jesus, disciples, crowds"
        main_verse = "Matthew 5:1-2"
        verse_text = (
            "Now when Jesus saw the crowds, he went up on a mountainside "
            "and sat down. His disciples came to him, and he began to teach them."
        )
        significance = "taught kingdom ethics, the Beatitudes, and true righteousness"
        time_period = "Approximately AD 28"
        beatitude = (
            "Blessed are the poor in spirit, for theirs is the kingdom of heaven."
        )

        print("=" * 70)
        print(f"\n⛰️ {moment_type}: {jesus_moments.moment14_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   The blueprint for Christian living.")
        print()
        print("\n💡 A BEATITUDE:")
        print(f'   "{beatitude}" - Matthew 5:3')
        print()
        print("\n🙏 Live by the Sermon on the Mount!")

    elif option == "15":
        moment_name = "The Parable of the Prodigal Son"
        moment_type = "Parable of Forgiveness"
        location = "Not specified"
        participants = "Jesus (teaching), father, prodigal son, older brother"
        main_verse = "Luke 15:20"
        verse_text = (
            "But while he was still a long way off, his father saw him "
            "and was filled with compassion for him; he ran to his son, "
            "threw his arms around him and kissed him."
        )
        significance = "illustrates God's forgiving love and the joy of repentance"
        time_period = "Approximately AD 30"
        father_welcome = "This son of mine was dead and is alive again..."

        print("=" * 70)
        print(f"\n🏃 {moment_type}: {jesus_moments.moment15_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   God's grace runs to the lost.")
        print()
        print("\n💡 FATHER'S JOY:")
        print(f'   "{father_welcome}" - Luke 15:24')
        print()
        print("\n🙏 Run back to the Father's arms!")

    elif option == "16":
        moment_name = "I Am the Way, the Truth, and the Life"
        moment_type = "Exclusive Path"
        location = "Upper room in Jerusalem"
        participants = "Jesus, disciples"
        main_verse = "John 14:6"
        verse_text = (
            "Jesus answered, 'I am the way and the truth and the life. "
            "No one comes to the Father except through me.'"
        )
        significance = "affirms Jesus as the only way to God"
        time_period = "Approximately AD 30"
        comfort_promise = "Do not let your hearts be troubled."

        print("=" * 70)
        print(f"\n🛤️ {moment_type}: {jesus_moments.moment16_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   Bold claim of divinity.")
        print()
        print("\n💡 COMFORT IN FAREWELL:")
        print(f'   "{comfort_promise}" - John 14:1')
        print()
        print("\n🙏 Follow the Way today!")

    elif option == "17":
        moment_name = "The Greatest Commandment"
        moment_type = "Essence of the Law"
        location = "Jerusalem (Temple)"
        participants = "Jesus, Pharisees"
        main_verse = "Matthew 22:37-38"
        verse_text = (
            "Jesus replied: 'Love the Lord your God with all your heart "
            "and with all your soul and with all your mind.' This is "
            "the first and greatest commandment."
        )
        significance = "summarizes all Scripture in love for God and neighbor"
        time_period = "Approximately AD 30"
        second_command = "Love your neighbor as yourself."

        print("=" * 70)
        print(f"\n❤️ {moment_type}: {jesus_moments.moment17_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   Love fulfills the law.")
        print()
        print("\n💡 THE SECOND:")
        print(f'   "{second_command}" - Matthew 22:39')
        print()
        print("\n🙏 Love God wholly and others fully!")

    elif option == "18":
        moment_name = "The Triumphal Entry"
        moment_type = "Messianic Welcome"
        location = "Jerusalem"
        participants = "Jesus, crowds, disciples"
        main_verse = "John 12:12-13"
        verse_text = (
            "The next day the great crowd that had come for the festival "
            "heard that Jesus was on his way to Jerusalem. They took palm "
            "branches and went out to meet him, shouting, 'Hosanna!'"
        )
        significance = "fulfilled Zechariah's prophecy of the king on a donkey"
        time_period = "Approximately AD 30"
        crowd_shout = "Blessed is he who comes in the name of the Lord!"

        print("=" * 70)
        print(f"\n🐴 {moment_type}: {jesus_moments.moment18_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   Joyful yet sorrowful entry.")
        print()
        print("\n💡 CROWD'S PRAISE:")
        print(f'   "{crowd_shout}" - John 12:13')
        print()
        print("\n🙏 Welcome Jesus as King of your life!")

    elif option == "19":
        moment_name = "The Last Supper"
        moment_type = "New Covenant"
        location = "Upper room in Jerusalem"
        participants = "Jesus, disciples (including Judas)"
        main_verse = "Matthew 26:26"
        verse_text = (
            "While they were eating, Jesus took bread, and when he had "
            "given thanks, he broke it and gave it to his disciples, "
            "saying, 'Take and eat; this is my body.'"
        )
        significance = "instituted the Lord's Supper as remembrance of his sacrifice"
        time_period = "Approximately AD 30"
        blood_covenant = "This is my blood of the covenant, poured out for many."

        print("=" * 70)
        print(f"\n🍞 {moment_type}: {jesus_moments.moment19_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   Do this in remembrance of me.")
        print()
        print("\n💡 THE CUP:")
        print(f'   "{blood_covenant}" - Matthew 26:28')
        print()
        print("\n🙏 Remember Jesus' sacrifice often!")

    elif option == "20":
        moment_name = "The Agony in Gethsemane"
        moment_type = "Submission to Will"
        location = "Garden of Gethsemane"
        participants = "Jesus, disciples (Peter, James, John)"
        main_verse = "Matthew 26:36"
        verse_text = (
            "Then Jesus went with his disciples to a place called "
            "Gethsemane, and he said to them, 'Sit here while I go "
            "over there and pray.'"
        )
        significance = "Jesus submitted to the Father's will amid deep sorrow"
        time_period = "Approximately AD 30"
        cup_prayer = "My Father, if it is possible, may this cup be taken from me."

        print("=" * 70)
        print(f"\n🌿 {moment_type}: {jesus_moments.moment20_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   'Not my will, but yours be done.'")
        print()
        print("\n💡 THE PRAYER:")
        print(f'   "{cup_prayer}" - Matthew 26:39')
        print()
        print("\n🙏 Surrender your will to God's!")

    elif option == "21":
        moment_name = "The Trial Before Pilate"
        moment_type = "Unjust Judgment"
        location = "Jerusalem (before Sanhedrin, Pilate, Herod)"
        participants = "Jesus, Pilate, Caiaphas, Herod Antipas, Sanhedrin"
        main_verse = "Matthew 27:1-2"
        verse_text = (
            "Early in the morning, all the chief priests and the elders "
            "of the people made their plans how to have Jesus executed. "
            "So they bound Jesus, led him away and handed him over to Pilate."
        )
        significance = "unjust trials leading to the cross fulfilled prophecy"
        time_period = "Approximately AD 30"
        pilate_question = "Are you the king of the Jews?"

        print("=" * 70)
        print(f"\n⚖️ {moment_type}: {jesus_moments.moment21_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   Silence before accusers.")
        print()
        print("\n💡 PILATE'S QUESTION:")
        print(f'   "{pilate_question}" - Matthew 27:11')
        print()
        print("\n🙏 Stand firm in truth amid injustice!")

    elif option == "22":
        moment_name = "The Crucifixion"
        moment_type = "Atoning Sacrifice"
        location = "Golgotha (near Jerusalem)"
        participants = "Jesus, soldiers, criminals, crowds"
        main_verse = "Matthew 27:33, 38"
        verse_text = (
            "They came to a place called Golgotha (which means 'the place "
            "of the skull'). There they crucified him, and with him two "
            "robbers, one on his right and one on his left."
        )
        significance = "Jesus' death paid the penalty for our sins"
        time_period = "Approximately AD 30"
        forgiveness_prayer = (
            "Father, forgive them, for they do not know what they are doing."
        )

        print("=" * 70)
        print(f"\n✝️ {moment_type}: {jesus_moments.moment22_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   The ultimate act of love.")
        print()
        print("\n💡 FROM THE CROSS:")
        print(f'   "{forgiveness_prayer}" - Luke 23:34')
        print()
        print("\n🙏 Thank God for the cross!")

    elif option == "23":
        moment_name = "It Is Finished"
        moment_type = "Mission Accomplished"
        location = "Golgotha (cross)"
        participants = "Jesus, soldiers"
        main_verse = "John 19:30"
        verse_text = (
            "When he had received the drink, Jesus said, 'It is finished.' "
            "With that, he bowed his head and gave up his spirit."
        )
        significance = "declared the completion of redemption's work"
        time_period = "Approximately AD 30"
        final_breath = "Tetelestai - It is finished."

        print("=" * 70)
        print(f"\n✅ {moment_type}: {jesus_moments.moment23_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   Debt paid in full.")
        print()
        print("\n💡 THE CRY:")
        print(f'   "{final_breath}"')
        print()
        print("\n🙏 Rest in the finished work of Christ!")

    elif option == "24":
        moment_name = "The Resurrection"
        moment_type = "Conquest of Death"
        location = "Tomb near Jerusalem"
        participants = "Jesus, Mary Magdalene, disciples, angels"
        main_verse = "Matthew 28:5-6"
        verse_text = (
            "The angel said to the women, 'Do not be afraid, for I know "
            "that you are looking for Jesus, who was crucified. He is "
            "not here; he has risen, just as he said.'"
        )
        significance = "victory over sin and death, foundation of faith"
        time_period = "Approximately AD 30"
        empty_tomb = "Come and see the place where he lay."

        print("=" * 70)
        print(f"\n🌅 {moment_type}: {jesus_moments.moment24_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   He is risen indeed!")
        print()
        print("\n💡 ANGEL'S INVITATION:")
        print(f'   "{empty_tomb}" - Matthew 28:6')
        print()
        print("\n🙏 Rejoice in the risen Lord!")

    elif option == "25":
        moment_name = "The Ascension"
        moment_type = "Return to Glory"
        location = "Near Bethany"
        participants = "Jesus, disciples"
        main_verse = "Luke 24:51"
        verse_text = (
            "While he was blessing them, he left them and was taken " "up into heaven."
        )
        significance = "Jesus exalted at the Father's right hand, sending the Spirit"
        time_period = "Approximately AD 30 (40 days after resurrection)"
        promise_return = "This same Jesus... will come back in the same way."

        print("=" * 70)
        print(f"\n☁️ {moment_type}: {jesus_moments.moment25_formatted}")
        print("=" * 70)
        print(f"\n📍 Location: {location}")
        print(f"\n👥 Key People: {participants}")
        print(f"\n📅 Time: {time_period}")
        print()
        print(f"\n📖 KEY VERSE: {main_verse}")
        print(f'\n💬 "{verse_text}"')
        print()
        print("\n🎯 SIGNIFICANCE:")
        print(f"   {significance}.")
        print("   From earth to throne.")
        print()
        print("\n💡 ANGELS' PROMISE:")
        print(f'   "{promise_return}" - Acts 1:11')
        print()
        print("\n🙏 Look up, your redemption draws near!")

        print("\n--- Enter another number or 'quit' to exit! ---")
# Commit 1: Add while loop feature
# Commit 2: Add break statement for clean exit
# Commit 3: Add continue for invalid input handling
