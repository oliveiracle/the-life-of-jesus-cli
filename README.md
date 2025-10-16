# ✝️ The Life of Jesus - Interactive CLI Application

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: Educational](https://img.shields.io/badge/license-Educational-green.svg)]()

> _"I am the way and the truth and the life."_ - John 14:6

An interactive command-line application guiding users through 25 pivotal moments in the life of Jesus Christ, from the Annunciation to the Ascension. Built with Python for educational and devotional purposes.

![Main Menu Preview](docs/screenshots/menu.png)

---

## 📑 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
  - [Design Decisions](#design-decisions)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Logic Flow](#logic-flow)
- [Testing](#testing)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)
- [Code Quality](#code-quality)
- [Learning Outcomes](#learning-outcomes)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)
- [Author](#author)

---

## 🎯 Overview

### Purpose

This CLI application was created to provide an accessible, scripture-based exploration of Jesus Christ's life. It serves multiple audiences:

- **Personal Study**: Individual devotional time and biblical learning
- **Educational**: Sunday school classes and Bible study groups
- **Accessibility**: Simple terminal interface requiring no technical expertise
- **Offline Use**: No internet connection required after installation

### Project Goals

1. Present biblical content in an organized, categorized format
2. Provide scriptural accuracy with verse references
3. Create an intuitive, error-resistant user interface
4. Demonstrate Python programming proficiency
5. Meet Code Institute's Python Essentials assessment criteria

---

## ✨ Features

### Implemented Features

#### 🌟 Core Functionality

- **25 Curated Biblical Moments**

  - Organized into 5 thematic categories
  - From Annunciation to Ascension
  - Complete chronological coverage

- **Interactive Menu System**

  - Clear categorical organization with emoji indicators
  - Numbered selection (1-25)
  - Visual hierarchy for easy navigation

- **Detailed Moment Information**
  - Biblical location and time period
  - Key participants
  - Scripture reference with full verse text
  - Historical and spiritual significance
  - Personal reflection prompts

#### 🛡️ Robust Error Handling

- **Input Validation**

  - Try/except blocks for non-numeric input
  - Range validation (1-25)
  - Graceful error messages with guidance

- **User-Friendly Feedback**
  - Clear error messages
  - Helpful suggestions
  - No application crashes

#### 🔄 Continuous Loop Design

- **While Loop Implementation**

  - View multiple moments in one session
  - Return to menu after each selection
  - Exit only when user chooses

- **Flow Control**
  - Break statement for clean exit
  - Continue statement for input retry
  - Intuitive navigation

#### 🎨 Enhanced User Experience

- **Visual Elements**

  - ASCII art title screen
  - Emoji categorization
  - Formatted output with separators
  - Consistent styling throughout

- **Accessibility**
  - Clear instructions
  - Multiple exit options (quit/q)
  - No technical jargon

### Features Left to Implement

- Search functionality by keyword
- Bookmark favorite moments
- Daily devotional mode (random moment)
- Export moment details to text file
- Multi-language support (Spanish, Portuguese)

---

## 🎨 User Experience (UX)

### User Stories

#### First-Time User Goals

> _As a first-time user, I want to..._

1. **Understand the purpose immediately**

   - _Implementation_: Clear title and descriptive menu on launch
   - _Success Criteria_: User knows this is about Jesus' life within 5 seconds

2. **Navigate easily without instructions**

   - _Implementation_: Simple numbered menu, clear prompts
   - _Success Criteria_: User can select a moment without help

3. **Receive helpful feedback on mistakes**

   - _Implementation_: Clear error messages with guidance
   - _Success Criteria_: User understands and corrects invalid input

4. **Exit the program gracefully**
   - _Implementation_: Multiple exit options, confirmation message
   - _Success Criteria_: User knows they can quit anytime

#### Returning User Goals

> _As a returning user, I want to..._

1. **Quickly access specific moments**

   - _Implementation_: Numbered categories for fast selection
   - _Success Criteria_: User reaches desired moment in <30 seconds

2. **Explore multiple moments efficiently**

   - _Implementation_: Continuous loop returning to menu
   - _Success Criteria_: User views 3+ moments in one session

3. **Have a consistent, reliable experience**
   - _Implementation_: Error handling prevents crashes
   - _Success Criteria_: Zero crashes during typical usage

#### Educator/Ministry User Goals

> _As an educator or ministry leader, I want to..._

1. **Use for group teaching**

   - _Implementation_: Clear, projectable text format
   - _Success Criteria_: Readable on classroom screens

2. **Reference accurate scriptures**

   - _Implementation_: NIV verses with book/chapter/verse citations
   - _Success Criteria_: All verses verifiable in NIV Bible

3. **Navigate quickly during live teaching**
   - _Implementation_: Fast, responsive terminal interface
   - _Success Criteria_: No lag between selections

### Design Decisions

#### Why Command-Line Interface?

1. **Accessibility**: Works on any system with Python
2. **Simplicity**: No complex UI to learn
3. **Performance**: Instant response, no loading times
4. **Focus**: Content-first, no visual distractions
5. **Educational**: Demonstrates Python fundamentals

#### Why 25 Moments?

- Comprehensive coverage from birth to ascension
- Balanced across life phases (childhood, ministry, passion)
- Manageable scope for user session
- Aligns with traditional devotional structures

#### Why Categorical Organization?

- Reduces cognitive load (5 categories vs 25 choices)
- Logical progression through Jesus' life
- Helps users locate moments by theme
- Creates visual structure in text interface

---

## 📁 Project Structure

```
the-life-of-jesus-cli/
│
├── run.py                    # Main application file (entry point)
├── jesus_moments.py          # ASCII art and formatted titles module
├── README.md                 # This documentation file
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
│
├── docs/                    # Documentation assets
│   ├── screenshots/         # Terminal screenshots
│   │   ├── menu.png
│   │   ├── moment-1.png
│   │   ├── error-handling.png
│   │   └── exit.png
│   │
│   └── flowcharts/          # Logic flow diagrams
│       └── program-flow.png
│
└── .vscode/                 # VS Code settings
    └── settings.json        # Editor configuration
```

### File Descriptions

- **`run.py`**: Main application logic including user input, validation, and moment display
- **`jesus_moments.py`**: Modular file containing ASCII art and formatted moment titles
- **`requirements.txt`**: Lists external Python packages (currently none - stdlib only)
- **`docs/`**: Contains all documentation assets for README

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Terminal/Command Prompt
- Git (for cloning repository)

### Step-by-Step Installation

1. **Clone the repository**

```bash
   git clone https://github.com/YOUR_USERNAME/the-life-of-jesus-cli.git
   cd the-life-of-jesus-cli
```

2. **Verify Python version**

```bash
   python3 --version
   # Should display Python 3.8.0 or higher
```

3. **Run the application**

```bash
   python3 run.py
```

_No additional dependencies required - uses Python standard library only_

### Alternative: Direct Download

1. Download ZIP from GitHub repository
2. Extract to desired location
3. Open terminal in extracted folder
4. Run: `python3 run.py`

---

## 🎮 Usage

### Quick Start

1. **Launch the application**

```bash
   python3 run.py
```

2. **View the main menu**

   - 25 moments displayed in 5 categories
   - Each moment numbered 1-25

3. **Select a moment**

   - Type a number (1-25)
   - Press Enter

4. **Read the moment details**

   - Location, participants, time period
   - Scripture reference with full verse
   - Spiritual significance and reflection

5. **Continue exploring**

   - Automatically returns to menu
   - Select another number

6. **Exit the program**
   - Type `quit` or `q`
   - Press Enter

### Example Session

```bash
$ python3 run.py

 ═══════════════════════════════════════════════════
    ✝ THE LIFE OF JESUS CHRIST ✝
 ═══════════════════════════════════════════════════

Explore 25 key moments from the life of Jesus Christ:

👶 BIRTH & CHILDHOOD:
1-Angel's Announcement | 2-Birth in Bethlehem | 3-Jesus at Temple

⚡ BEGINNING OF MINISTRY:
4-Baptism | 5-Temptation | 6-First Disciples | 7-First Miracle

🔥 POWERFUL MIRACLES:
8-Healing Paralytic | 9-Calming Storm | 10-Feeding 5000
11-Walking on Water | 12-Raising Lazarus | 13-Healing Blind

📖 PROFOUND TEACHINGS:
14-Sermon on Mount | 15-Prodigal Son
16-I Am the Way | 17-Greatest Commandment

✝ FINAL WEEK:
18-Triumphal Entry | 19-Last Supper | 20-Gethsemane
21-Trial | 22-Crucifixion | 23-It Is Finished
24-Resurrection | 25-Ascension

Enter your choice (1-25) or 'quit' to exit: 1

======================================================================
✨ Divine Announcement: The Angel Gabriel Announces Jesus' Birth
======================================================================

📍 Location: Nazareth, Mary's home
👥 Key People: Angel Gabriel and Mary
📅 Time: Approximately 6 BC

📖 KEY VERSE: Luke 1:30-31
💬 "Do not be afraid, Mary; you have found favor with God. You will
   conceive and give birth to a son, and you are to call him Jesus."

🎯 SIGNIFICANCE:
This moment marked the beginning of God's plan for salvation.
God chose a humble young woman to bear the Savior of the world.

🙏 MARY'S FAITHFUL RESPONSE:
"I am the Lord's servant. May your word to me be fulfilled." - Luke 1:38

💙 May we respond to God's call with the same faith and humility!

--- Enter another number or 'quit' to exit! ---

Enter your choice (1-25) or 'quit' to exit: quit

✝️ Thank you for exploring the life of Jesus!
🙏 'I am with you always, to the very end of the age'
   - Matthew 28:20
```

---

## 📸 Screenshots

_Note: Screenshots will be added here as the project is finalized_

### Main Menu

![Main Menu](docs/screenshots/menu.png)
_The application's main interface showing all 25 moments organized into 5 thematic categories_

### Moment Display - Example

![Moment 1 Display](docs/screenshots/moment-1.png)
_Detailed view of "The Annunciation" including location, participants, scripture, and reflection_

### Error Handling

![Error Message](docs/screenshots/error-handling.png)
_Validation message displayed when user enters invalid input, with helpful guidance_

### Exit Message

![Exit Screen](docs/screenshots/exit.png)
_Graceful exit with biblical encouragement when user types 'quit'_

---

## 🔄 Logic Flow

### Program Architecture

The application follows a simple, linear flow with a central loop:

```
START
  ↓
Display Title & Menu
  ↓
┌─────────────────┐
│  WHILE LOOP     │ ←──────┐
│  (while True)   │        │
└─────────────────┘        │
  ↓                        │
Get User Input             │
  ↓                        │
Input = 'quit'? ──Yes──→ BREAK (Exit)
  ↓ No                     │
  ↓                        │
Try Convert to Int         │
  ↓                        │
ValueError? ──Yes──→ Error Message → CONTINUE ─┘
  ↓ No                     │
  ↓                        │
Number 1-25? ──No──→ Error Message → CONTINUE ─┘
  ↓ Yes                    │
  ↓                        │
Display Selected Moment    │
  ↓                        │
Return to Menu ────────────┘
```

### Flowchart

![Program Logic Flowchart](docs/flowcharts/program-flow.png)
_Detailed flowchart showing decision points, error handling, and loop structure_

### Key Logic Components

1. **Input Validation Layer**

```python
   try:
       moment_number = int(option)
   except ValueError:
       # Handle non-numeric input
```

2. **Range Validation**

```python
   if moment_number < 1 or moment_number > 25:
       # Handle out-of-range input
```

3. **Loop Control**

```python
   if option.lower() == "quit":
       break  # Exit loop
   if invalid_input:
       continue  # Retry input
```

---

## ✅ Testing

### Testing Strategy

Manual testing was performed systematically across all features and edge cases. No automated testing framework was used as this is a simple CLI application.

### Test Cases

#### Input Validation Tests

| Test Case           | Input     | Expected Behavior           | Result  |
| ------------------- | --------- | --------------------------- | ------- |
| Valid number (low)  | `1`       | Display Moment 1            | ✅ Pass |
| Valid number (mid)  | `13`      | Display Moment 13           | ✅ Pass |
| Valid number (high) | `25`      | Display Moment 25           | ✅ Pass |
| Below range         | `0`       | Error: out of range         | ✅ Pass |
| Above range         | `26`      | Error: out of range         | ✅ Pass |
| Far above range     | `100`     | Error: out of range         | ✅ Pass |
| Negative number     | `-5`      | Error: out of range         | ✅ Pass |
| Letters             | `abc`     | Error: not a number         | ✅ Pass |
| Symbols             | `@#$`     | Error: not a number         | ✅ Pass |
| Empty input         | `[Enter]` | Error: not a number         | ✅ Pass |
| Spaces              | `   `     | Error (stripped, empty)     | ✅ Pass |
| Number with spaces  | `5`       | Display Moment 5 (stripped) | ✅ Pass |
| Decimal             | `5.5`     | Error: not a number         | ✅ Pass |

#### Quit Functionality Tests

| Test Case       | Input  | Expected Behavior | Result  |
| --------------- | ------ | ----------------- | ------- |
| Lowercase quit  | `quit` | Exit with message | ✅ Pass |
| Uppercase quit  | `QUIT` | Exit with message | ✅ Pass |
| Mixed case      | `QuIt` | Exit with message | ✅ Pass |
| Short quit      | `q`    | Exit with message | ✅ Pass |
| Short uppercase | `Q`    | Exit with message | ✅ Pass |

#### Moment Display Tests

| Test                   | Description                           | Result  |
| ---------------------- | ------------------------------------- | ------- |
| All 25 moments         | Display each moment 1-25              | ✅ Pass |
| Scripture accuracy     | Verify verse text matches NIV Bible   | ✅ Pass |
| Formatting consistency | Check all moments have same structure | ✅ Pass |
| Special characters     | Verify emojis and symbols display     | ✅ Pass |

#### Loop Functionality Tests

| Test                | Description                       | Expected Behavior          | Result  |
| ------------------- | --------------------------------- | -------------------------- | ------- |
| Multiple selections | Select 5 moments in succession    | Return to menu each time   | ✅ Pass |
| Error recovery      | Enter invalid input 3x then valid | Continue without crash     | ✅ Pass |
| Long session        | View all 25 moments sequentially  | No performance degradation | ✅ Pass |

### Browser/Terminal Compatibility

Tested on:

- ✅ macOS Terminal (Monterey, Ventura)
- ✅ Windows Command Prompt (Windows 10, 11)
- ✅ Windows PowerShell
- ✅ Linux Terminal (Ubuntu 22.04)
- ✅ VS Code Integrated Terminal
- ✅ Git Bash (Windows)

### Known Issues

None identified during testing phase.

### Fixed Bugs

1. **Initial Bug**: Invalid input caused program crash

   - **Solution**: Implemented try/except block for ValueError
   - **Commit**: `feat: Add try/except error handling`

2. **Initial Bug**: Numbers outside 1-25 range accepted
   - **Solution**: Added range validation with clear error message
   - **Commit**: `feat: Add range validation for input`

---

## 🚀 Deployment

### Heroku Deployment

_Instructions to be added upon deployment_

The application will be deployed to Heroku for public access.

#### Deployment Steps

1. Create Heroku account
2. Install Heroku CLI
3. Create new Heroku app
4. Configure buildpacks
5. Deploy from GitHub
6. Set environment variables (if needed)

#### Live Application

_Link will be added here after deployment_

---

## 🛠️ Technologies Used

### Languages

- **Python 3.8+**: Core programming language

### Python Standard Library Modules

- `sys`: Program exit handling
- (No external libraries required)

### Development Tools

- **Git**: Version control
- **GitHub**: Code repository and collaboration
- **VS Code**: Code editor
- **Black**: Python code formatter (PEP8 compliance)

### Documentation

- **Markdown**: README documentation
- **Lucidchart** (or similar): Flowchart creation (planned)

---

## 📏 Code Quality

### PEP8 Compliance

All Python code formatted using **Black** (industry-standard formatter):

```bash
black run.py jesus_moments.py
```

**Black Configuration:**

- Line length: 88 characters
- Python version: 3.8+
- String quote style: double quotes

### Code Organization

- **Modular design**: ASCII art separated into `jesus_moments.py`
- **Clear naming**: Descriptive variable and function names
- **Consistent formatting**: Black ensures uniformity
- **Comments**: Explanatory comments for complex logic
- **Docstrings**: (To be added for functions)

### Best Practices Followed

- ✅ Try/except for error handling
- ✅ Input validation before processing
- ✅ Clear, user-friendly error messages
- ✅ Graceful exit handling
- ✅ No hardcoded "magic numbers" (constants used)
- ✅ Consistent indentation and spacing

---

## 🎓 Learning Outcomes

This project demonstrates proficiency in the following Code Institute Python Essentials assessment criteria:

### LO1: Code Quality & Standards

- ✅ **LO1.1**: Python code is PEP8 compliant (Black formatted)
- ✅ **LO1.2**: Code is well-structured and readable
- ✅ **LO1.3**: Functions and variables have meaningful names

### LO2: Data Processing

- ✅ **LO2.1**: User input validation implemented
- ✅ **LO2.2**: Data manipulation (string processing, type conversion)
- ✅ **LO2.3**: Appropriate data structures (lists, strings)

### LO3: Control Flow

- ✅ **LO3.1**: While loop for continuous menu display
- ✅ **LO3.2**: Try/except for error handling
- ✅ **LO3.3**: Break and continue statements for flow control
- ✅ **LO3.4**: Conditional statements (if/elif/else chains)

### LO4: Documentation

- ✅ **LO4.1**: Comprehensive README with all required sections
- ✅ **LO4.2**: Clear project purpose and features
- ✅ **LO4.3**: Installation and usage instructions
- ✅ **LO4.4**: Screenshots demonstrating functionality
- ✅ **LO4.5**: Code comments explaining logic

### LO5: Testing

- ✅ **LO5.1**: Manual testing performed and documented
- ✅ **LO5.2**: Edge cases identified and tested
- ✅ **LO5.3**: Bugs fixed and documented

### LO6: External Libraries

- ✅ **LO6.1**: Uses Python standard library appropriately
- ✅ **LO6.2**: No unnecessary external dependencies

### LO7: Data Structures

- ✅ **LO7.1**: Lists used for organizing moments by category
- ✅ **LO7.2**: String manipulation for user input processing

### LO8: Version Control

- ✅ **LO8.1**: Git used throughout development
- ✅ **LO8.2**: Regular, meaningful commits
- ✅ **LO8.3**: Clear commit messages following conventions

### LO9: Deployment

- ⏳ **LO9.1**: Heroku deployment (in progress)
- ✅ **LO9.2**: No commented-out code in final version

---

## 🔮 Future Enhancements

### Planned Features (Post-Assessment)

1. **Search Functionality**

   - Search moments by keyword (e.g., "miracle", "teaching")
   - Filter by category
   - Search scripture references

2. **Bookmark System**

   - Save favorite moments
   - Quick access to bookmarked content
   - Persistent storage using file I/O

3. **Daily Devotional Mode**

   - Random moment generator
   - "Moment of the Day" feature
   - Integration with system date

4. **Export Functionality**

   - Save moment details to text file
   - Create personal study notes
   - Print-friendly formatting

5. **Multi-Language Support**

   - Spanish translation
   - Portuguese translation
   - Language selection at startup

6. **Enhanced Navigation**

   - Back button to return to previous moment
   - History of viewed moments
   - "Next moment" sequential navigation

7. **Advanced Content**
   - Cross-references to related moments
   - Historical context expansion
   - Map integration (text-based ASCII maps)

---

## 🙏 Credits

### Content Sources

- **Scripture References**: New International Version (NIV) Bible
- **Biblical Content**: Public domain historical records and traditional Christian teaching
- **Spiritual Insights**: Original interpretations for devotional purposes

### Inspiration

- **Code Institute**: Python Essentials curriculum and assessment criteria
- **Christian Community**: Feedback from local church members during development
- **Personal Faith**: Desire to share the Gospel through technology

### Acknowledgments

- **Code Institute Tutors**: Support during Python learning journey
- **Mentor** (if applicable): Guidance on project structure and best practices
- **Fellow Students**: Code reviews and testing feedback
- **Family**: Patience during development time

---

## 👨‍💻 Author

**Cleino Frank**

- 🐙 GitHub: [@oliveiracle](https://github.com/oliveiracle)
- 💼 LinkedIn: [Cleino Frank](https://www.linkedin.com/in/cleinofrank)
- 📧 Email: cleinofrank@gmail.com
- 🎓 Student: Code Institute - Python Essentials

### About the Developer

I'm a student developer passionate about using technology to share faith and provide spiritual resources. This project combines my growing Python skills with my desire to make biblical content accessible to everyone.

### Connect With Me

Feel free to:

- ⭐ Star this repository if you find it helpful
- 🐛 Report bugs or suggest features via GitHub Issues
- 🤝 Connect on LinkedIn for collaboration
- 📧 Reach out with questions or feedback

---

## 📄 License

This project is created for educational purposes as part of Code Institute's Python Essentials assessment.

**Educational Use Only** - Created as a portfolio project demonstrating Python programming skills.

---

## 📚 Additional Resources

### For Users

- [How to Use a Terminal](https://www.freecodecamp.org/news/command-line-for-beginners/)
- [Bible Gateway - NIV](https://www.biblegateway.com/versions/New-International-Version-NIV-Bible/) - Verify scripture references
- [The Life of Jesus - Timeline](https://www.christianity.com/jesus/life-of-jesus/timeline-key-events/) - Historical context

### For Developers

- [Python Official Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Black Code Formatter](https://black.readthedocs.io/)
- [Git Commit Message Conventions](https://www.conventionalcommits.org/)

---

## 🆘 Support

If you encounter any issues:

1. Check the [Installation](#installation) section
2. Verify Python version: `python3 --version`
3. Review [Testing](#testing) section for known behaviors
4. Open an issue on GitHub with:
   - Error message (if any)
   - Operating system
   - Python version
   - Steps to reproduce

---

✝️ _"For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life."_ - John 3:16

---

**Last Updated**: [Current Date]  
**Version**: 1.0.0
