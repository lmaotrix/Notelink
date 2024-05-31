# NOTELINK
#### Video Demo:  <URL HERE>
#### Description:
- USE CASES:
NoteLink is designed to provide a secure and user-friendly platform for managing personal notes. Users can create an account, log in, and access their notes from any device. The application supports creating, editing, and deleting notes, making it ideal for keeping track of personal thoughts, tasks, or important information. With its session management and user authentication features, Notelink ensures that users' data is kept private and secure. This app is particularly useful for individuals looking for a simple yet effective solution for note-taking and organization.

- FEATURES:
1. **User Authentication**: Users can securely register, login and logout thanks to the efficient password hashing for secure storage.
2. **Session Management**: Users are kept logged in throughout sessions.
3. **Notes Management**: Users can create, view, edit, and delete their own notes.
4. **Database Integration**: The web app uses an SQLite database for storing user information and Flask-Migrate to handle the changes in the table models.
5. **User-Specific-Data**: Notes are linked to user accounts.
6. **Template Rendering**: HTML templates for rendering pages (e.g., login, registration, note list, note editor).


- COMPONENTS:
1. HTML/CSS: Used for frontend development and styling
2. JavaScript: Used for dynamic interactions on the client-side.
3. Python with Flask: Used for backend development and routing.
5. SQLite3: Lightweight database for storing user information and notes.
6. Jinja: Templating engine for rendering dynamic content in HTML

- FILE STRUCTURE:
<pre>
Notelink/
├─ database/
│  ├─ app.db
├─ static/
│  ├─ css/
│  │  ├─ error.css
│  │  ├─ login.css
│  │  ├─ notes.css
│  │  ├─ signup.css
│  │  ├─ styles.css
│  │  ├─ userarea.css
│  ├─ img/
│  │  ├─ abstract_light.png
│  │  ├─ abstract.png
│  │  ├─ favicon.ico
│  ├─ js/
│  │  ├─ editor.js
│  │  ├─ script.js
│  │  ├─ signup.js
├─ templates/
│  ├─ 401.html
│  ├─ about.html
│  ├─ index.html
│  ├─ login.html
│  ├─ notes.html
│  ├─ signup.html
│  ├─ userarea.html
├─ .gitignore
├─ app.py
├─ config.py
├─ README.md
├─ requirements.txt
├─ vercel.json

</pre>

-  ### EXPLANATION:
- **database/**: Contains the SQLite database file.
  - **app.db**: The SQLite database file that stores application data.
  
- **static/**: Holds CSS, images, and JavaScript files.
  - **css/**: Directory for CSS files used for styling the web pages.
    - **error.css**: Styles for error pages.
    - **login.css**: Styles for the login page.
    - **notes.css**: Styles for the notes page.
    - **signup.css**: Styles for the signup page.
    - **styles.css**: General styles for the application.
    - **userarea.css**: Styles for the user area page.
  - **img/**: Directory for image files used in the application.
    - **abstract_light.png**: Light-themed abstract background image.
    - **abstract.png**: Dark-themed abstract background image.
    - **favicon.ico**: Favicon for the application.
  - **js/**: Directory for JavaScript files used in the application.
    - **editor.js**: JavaScript for the note editor functionality.
    - **script.js**: General JavaScript for the application.
    - **signup.js**: JavaScript for the signup page functionality.
    
- **templates/**: Contains HTML templates for rendering web pages.
  - **401.html**: Template for the 401 Unauthorized error page.
  - **about.html**: Template for the About page.
  - **index.html**: Template for the main page.
  - **login.html**: Template for the login page.
  - **notes.html**: Template for the notes listing page.
  - **signup.html**: Template for the signup page.
  - **userarea.html**: Template for the user area page.
  
- **.gitignore**: Specifies which files and directories should be ignored by Git.
- **app.py**: The main application file containing the Flask application instance, routes, and database models.
- **config.py**: Configuration file for environment-specific settings (e.g., secret key, database URI).
- **README.md**: Information about the project, including setup instructions and usage.
- **requirements.txt**: Lists the Python dependencies required by the application.
- **vercel.json**: Configuration file for deploying the application to Vercel, specifying build settings.




