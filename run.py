import jesus_moments
from colorama import Fore, init
init(autoreset=True)

# Dictionary with all 25 moments titles for search
moments_data = {
    # ... (unchanged, omitted for brevity)
}

# 1. TITLE
jesus_moments.show_title()

# MAIN LOOP
while True:
    # MAIN MENU
    print("\n" + "=" * 70)
    print(Fore.CYAN + "\n✝\n  MAIN MENU - THE LIFE OF JESUS")
    print("=" * 70)
    print("\n📖 What would you like to explore?\n")
    print("1 - The 25 Key Moments of Jesus' Life")
    print("2 - The Parables of Jesus (5 important teachings)")
    print("3 - Search moments by keyword")
    print("\nType 'quit' to exit\n")
    print("=" * 70)
    
    main_choice = input("\nYour choice (1, 2, 3, or 'quit'): ").strip()
    
    # QUIT
    if main_choice.lower() == "quit" or main_choice.lower() == "q":
        print("\n✝ Thank you for exploring the life of Jesus!")
        print("\n🙏 'I am with you always, to the very end of the age'")
        print("   - Matthew 28:20")
        break
    
    # OPTION 1: THE 25 MOMENTS
    if main_choice == "1":
        while True:  # Moments loop
            print("\n" + "=" * 70)
            print("Explore 25 key moments from the life of Jesus Christ:")
            print("=" * 70)
            
            print("\n👶 BIRTH & CHILDHOOD:")
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
            print("=" * 70)
            
            user_input = input("\nEnter your choice (1-25), 'back' for main menu, or 'quit': ")
            option = user_input.strip()
            
            # QUIT
            if option.lower() == "quit" or option.lower() == "q":
                print("\n✝ Thank you for exploring the life of Jesus!")
                print("\n🙏 'I am with you always, to the very end of the age'")
                print("   - Matthew 28:20")
                exit()
            
            # BACK to main menu
            if option.lower() == "back" or option.lower() == "b":
                break  # Exit moments loop, return to main menu
            
            #  TRY/EXCEPT VALIDATION
            try:
                option_num = int(option)
                if option_num < 1 or option_num > 25:
                    print(Fore.RED + f"\n❌ '{option}' is not a valid moment number!")
                    print("\n💡 Please choose a number between 1 and 25.")
                    continue
            except ValueError:
                print(Fore.RED + f"\n❌ '{option}' is not a number!")
                print("\n💡 Please enter a NUMBER between 1-25, 'back', or 'quit'.")
                continue
            
            # IF/ELIF FOR MOMENTS
            # ... (unchanged, omitted for brevity)
            print("\n--- Enter another number or 'back' to main menu! ---")

    # OPTION 2: THE PARABLES
    elif main_choice == "2":
        while True:  # Parables loop
            print("\n" + "=" * 70)
            print("\n📖\n THE PARABLES OF JESUS")
            print("=" * 70)
            print("\nType a parable to learn more about Jesus' teachings:\n")
            print("1 - Parable of the Sower")
            print("2 - Parable of the Good Samaritan")
            print("3 - Parable of the Prodigal Son")
            print("4 - Parable of the Talents")
            print("5 - Parable of the Mustard Seed")
            print("\nType 'back' to return to main menu or 'quit' to exit")
            print("=" * 70)
            
            parable_choice = input("\nYour choice (1-5), 'back', or 'quit': ").strip()
            
            # QUIT
            if parable_choice.lower() == "quit" or parable_choice.lower() == "q":
                print(Fore.CYAN + "\n✝ Thank you for exploring the life of Jesus!")
                print(Fore.YELLOW + "\n🙏 'I am with you always, to the very end of the age'")
                print("   - Matthew 28:20")
                exit()
            
            # BACK
            if parable_choice.lower() == "back" or parable_choice.lower() == "b":
                break  # Return to main menu
            
            # PARABLE 1: Sower
            if parable_choice == "1":
                print("\n" + "=" * 70)
                print("\n📖\n The Parable of the Sower")
                print("=" * 70)
                print("\nA farmer sows seeds on different types of soil,")
                print("representing how people receive God's word.")
                print("Some hear and accept it, while others reject it.")
                print("\n\n🌱\n 'But the seed on good soil stands for those with")
                print("   a noble and good heart' - Luke 8:15")
                print("\n\n💡\n Reflect: How do you receive God's word in your life?")
                input("\nPress enter to continue.r...")
            
            # PARABLE 2: Good Samaritan
            elif parable_choice == "2":
                print("\n" + "=" * 70)
                print("\n📖\n The Parable of the Good Samaritan")
                print("=" * 70)
                print("\nA man is beaten and left for dead.")
                print("A priest and Levite pass by, but a Samaritan helps him,")
                print("showing love and mercy to a stranger.")
                print("\n\n🤝\n 'Love your neighbor as yourself.' - Luke 10:27")
                print("\n\n💡\n Reflect: Who is your neighbor, and how can you show them love?")
                input("\nPress enter to continue...")
            
            # PARABLE 3: Prodigal Son
            elif parable_choice == "3":
                print("\n" + "=" * 70)
                print("\n📖\n The Parable of the Prodigal Son")
                print("=" * 70)
                print("\nA son squanders his inheritance but is welcomed back by his father,")
                print("illustrating God's forgiving love and joy over repentance.")
                print("\n\n🧑🧒\n 'This son of mine was dead and is alive again;' - Luke 15:24")
                print("\n\n💡\n Reflect: Are you in need of forgiveness or ready to forgive?")
                input("\nPress enter to continue....")
            
            # PARABLE 4: Talents
            elif parable_choice == "4":
                print("\n" + "=" * 70)
                print("\n📖\n The Parable of the Talents")
                print("=" * 70)
                print("\nServants are entrusted with talents (money) by their master.")
                print("Two invest and double their amounts, while one buries his.")
                print("The master rewards the faithful and punishes the lazy.")
                print("\n\n💰\n 'Well done, good and faithful servant!' - Matthew 25:21")
                print("\n\n💡\n Reflect: How are you using your gifts for God's kingdom?")
                input("\nPress enter to continue...")
            
            # PARABLE 5: Mustard Seed
            elif parable_choice == "5":
                print("\n" + "=" * 70)
                print("\n📖\n The Parable of the Mustard Seed")
                print("=" * 70)
                print("\nA tiny mustard seed grows into a large tree,")
                print("symbolizing how the kingdom of God starts small but grows immensely.")
                print("\n\n🌳\n 'The kingdom of heaven is like a mustard seed...'")
                print("   - Matthew 13:31-32")
                print("\n\n💡\n Reflect: How is your faith growing, even from small beginnings?")
                input("\nPress enter to continue....")
            
            else:
                print(f"\n❌ '{parable_choice}' is not valid!")
                print("\n💡 Choose 1-5, 'back', or 'quit'")
                continue
            
            print("\n--- Type another number, 'back' for menu, or 'quit'! ---")
    
    # OPTION 3: SEARCH MOMENTS
    elif main_choice == "3":
        while True:
            print("\n" + "=" * 70)
            print("\n🔍 SEARCH MOMENTS BY KEYWORD")
            print("=" * 70)
            print("\nType a keyword to search (e.g., 'water', 'healing', 'miracle')")
            print("or 'back' to return to main menu\n")
            print("=" * 70)
            
            search_term = input("\nEnter keyword or 'back': ").strip()
            
            # Back to main menu
            if search_term.lower() == "back" or search_term.lower() == "b":
                break
            
            # Quit
            if search_term.lower() == "quit" or search_term.lower() == "q":
                print(Fore.CYAN + "\n✝ Thank you for exploring the life of Jesus!")
                print(Fore.YELLOW + "\n🙏 'I am with you always, to the very end of the age'")
                print(Fore.YELLOW + "   - Matthew 28:20")
                exit()
            
            # Empty search
            if not search_term:
                print(Fore.RED + "\n❌ Please enter a keyword to search!")
                continue
            
            # Search in moments
            results = []
            for num, moment_dict in moments_data.items():
                # Search in moment title
                if search_term.lower() in moment_dict['title'].lower():
                    results.append((num, moment_dict['title']))
            
            # Display results
            if results:
                print(Fore.GREEN + f"\n✅ Found {len(results)} moment(s) matching '{search_term}':\n")
                for num, title in results:
                    print(f"   {num} - {title}")
                
                print("\n" + "=" * 70)
                choice = input("\nEnter a number to view details, or 'back' to search again: ").strip()
                
                if choice.lower() == "back" or choice.lower() == "b":
                    continue
                
                if choice.lower() == "quit" or choice.lower() == "q":
                    print(Fore.CYAN + "\n✝ Thank you for exploring the life of Jesus!")
                    print(Fore.YELLOW + "\n🙏 'I am with you always, to the very end of the age'")
                    print(Fore.YELLOW + "   - Matthew 28:20")
                    exit()
                
                # Validate number choice
                if choice.isdigit() and int(choice) in [r[0] for r in results]:
                    print(f"\n💡 Please go to main menu, select option 1, then choose moment {choice}")
                    input("\nPress Enter to continue...")
                else:
                    print(Fore.RED + f"\n❌ '{choice}' is not in the search results!")
                    input("\nPress Enter to continue...")
            else:
                print(Fore.RED + f"\n❌ No moments found matching '{search_term}'")
                print("\n💡 Try different keywords like: miracle, water, healing, teaching")
                input("\nPress Enter to continue...")
   
    # INVALID CHOICE
    else:
        print(f"\n❌ '{main_choice}' is not valid!")
        print("\n💡 Choose 1 (Moments), 2 (Parables), 3 (Search), or 'quit'")
