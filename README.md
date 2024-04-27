# NOTELINK
#### Video Demo:  <URL HERE>
#### Description:
- USE CASES:
NoteLink serves as a versatile tool for users to organize their thoughts, ideas, and information effectively. With the ability to register and log in, users gain access to personalized features, such as creating, editing, and deleting their own notes. The sidebar navigation enhances user experience by allowing seamless movement between different sections, including the user's private notes and the community page. On the community page, users can share their knowledge by uploading notes for others to benefit from, fostering a collaborative learning environment. Moreover, the functionality to copy notes to their codespace empowers users to integrate their notes directly into their coding workflow, facilitating efficient referencing and utilization of information. Overall, NoteLink caters to diverse user needs, from individual organization to community knowledge-sharing, while promoting productivity and collaboration.

- FEATURES:
1. Register/Login/Logout: Users can create an account, log in, and log out.
2. Sidebar Navigation: Allows users to navigate between different sections of the app.
3. Notes Management: Users can create, view, edit, and delete their own notes.
4. Community Page: Users can upload their notes for others to view and use.
5. Copy Note to Codespace: Provides a button to copy a note to the user's codespace as a new note.

- COMPONENTS:
1. HTML/CSS/Bootstrap: Used for frontend development and styling
2. JavaScript: Used for dynamic interactions on the client-side.
3. Python with Flask: Used for backend development and routing.
4. Python with Eel: Facilitates integration of Python backend with frontend using web technologies
5. SQLite3: Lightweight database for storing user information and notes.
6. Jinja: Templating engine for rendering dynamic content in HTML

- FILE STRUCTURE:
notelink/
│
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── script.js
│   ├── templates/
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── notes.html
│   │   ├── community.html
│   │   └── note_detail.html
│   ├── controllers.py
│   ├── models.py
│   └── __init__.py
│
├── database/
│   └── app.db
│
├── scripts/
│   └── seed.py
│
├── requirements.txt
│
└── run.py

- EXPLANATION:
app/: This directory contains all the application code.
    static/: Holds CSS and JavaScript files.
    templates/: Contains HTML templates.
    controllers.py: Handles the application logic.
    models.py: Defines the database models.
    _init_.py: Initializes the Flask application.
database/: Contains the SQLite database file.
scripts/: Scripts for database seeding or other utilities.
requirements.txt: Lists all Python dependencies.
run.py: Entry point to run the Flask application.
