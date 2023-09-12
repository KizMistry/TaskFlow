# TaskFlow API

Welcome to back-end of my TaskFlow app. This back-end hosts the Data Models and Endpoints for the TaskFlow API.
TaskFlow is a task management application that enables users to organize and track their projects and tasks.

The Front-End React TaskFlow app can be found here: https://taskflow-2023-b9a3557ae482.herokuapp.com/

## Installation

These are the installation steps taken:

1. **Install Django:** 
   - Open terminal and run the following command to install Django (version 4):
     ```
     pip3 install 'django<4'
     ```

2. **Start the Project:**
   - Create a new Django project and initialize it in the current directory using the following command:
     ```
     django-admin startproject TaskFlow .
     ```

3. **Connect to Cloudinary:**
   - Install the Django Cloudinary Storage library to connect project to Cloudinary:
     ```
     pip install django-cloudinary-storage
     ```

4. **Install Pillow:**
   - Install the Pillow library, which provides image processing capabilities required for the project:
     ```
     pip install Pillow
     ```


## API Deployment

This is the step-by-step process undertaken to deploy my Taskflow API to Heroku.

### ElephantSQL Setup

1. **Log in to ElephantSQL:** Visit [ElephantSQL.com](https://www.elephantsql.com) and log in to access dashboard.

2. **Create a Database Instance:**
   - Click "Create New Instance."
   - Set up plan (Name, Tiny Turtle plan, Select Region).
   - Click "Review," check details, and click "Create instance."

3. **Heroku Setup:**
   - Log in to Heroku and go to the Dashboard.
   - Create a new app, providing a name and selecting the region closest.
   - Open the "Settings" tab and add a Config Var "DATABASE_URL" with ElephantSQL database URL.

### Migrating Data

4. **Install Dependencies:**
   - Run `pip3 install dj_database_url==0.5.0 psycopg2` in your terminal.

5. **Update Settings:**
   - In your `settings.py` file, import `dj_database_url`.
   - Update the `DATABASES` section to use the `DATABASE_URL` environment variable.

6. **Environment Variable:**
   - In `env.py` file, add a new environment variable with the key set to `DATABASE_URL` and the value as ElephantSQL database URL.

7. **Check Connection:**
   - Temporarily comment out the `DEV` environment variable.
   - Add a print statement to confirm the connection to the external database.
   - Run `python3 manage.py makemigrations --dry-run` to check the connection.
   - If connected, remove the print statement.

8. **Migrate and Create Superuser:**
   - Migrate database models: `python3 manage.py migrate`.
   - Create a superuser: `python3 manage.py createsuperuser`.
   - Follow the prompts to create the superuser.

9. **Confirm Database Creation:**
   - On the ElephantSQL page for the database, select "BROWSER."
   - Click the "Table queries" button and select "auth_user."
   - Click "Execute" to confirm that superuser details are displayed.

### Preparing for Deployment to Heroku

10. **Install Gunicorn and Update Requirements:**
    - Install Gunicorn: `pip3 install gunicorn django-cors-headers`.
    - Update `requirements.txt`: `pip freeze --local > requirements.txt`.

11. **Create a Procfile:**
    - Create a file named `Procfile` with these two commands:
      ```
      release: python manage.py makemigrations && python manage.py migrate
      web: gunicorn drf_api.wsgi
      ```

12. **Update Settings:**
    - In `settings.py`, update the `ALLOWED_HOSTS` variable.
    - Add `corsheaders` to `INSTALLED_APPS`.
    - Add `corsheaders` middleware to the top of the `MIDDLEWARE` list.
    - Set `ALLOWED_ORIGINS` for network requests.

13. **Cookie Settings:**
    - Set `JWT_AUTH_SAMESITE` to `'None'` for cross-origin requests.
    - Replace `SECRET_KEY` with an environment variable.

14. **Debug Settings:**
    - Set `DEBUG` to `True` only if the `DEV` environment variable exists.
    - Uncomment `DEV` in `env.py`.

15. **Update Requirements:**
    - Ensure `requirements.txt` is up to date: `pip freeze --local > requirements.txt`.

16. **Commit to GitHub:**
    - Add, commit, and push code to GitHub.

### Heroku Deployment

17. **Heroku Configuration:**
    - In Heroku Dashboard for the app, open the "Settings" tab.
    - Added two Config Vars: `SECRET_KEY` and `CLOUDINARY_URL`.
    - Set up `ALLOWED_HOST` with Heroku app's URL.

18. **Deploy to Heroku:**
    - Open the "Deploy" tab in Heroku.
    - Connect to GitHub and deploy code.
    - Enable automatic deploys for future changes.

### Verification

19. **Check Deployment:**
    - Click "Open app" to check the app is running on Heroku.

20. **Additional Check:**
    - Verify the JSON welcome message on the home screen.
    - Check the profile for the superuser at `/profiles/` on root URL.

### Bug Fix: dj-rest-auth

21. **Problem Statement:**
    - dj-rest-auth has a bug that doesn't allow users to log out.

22. **Solution (Step 1):**
    - In `views.py`, import JWT_AUTH settings from `settings.py`.
    - Write a logout view to clear cookies properly.

23. **Bug Fix (Step 2):**
    - Include the logout view in `drf_api/urls.py` above the default dj-rest-auth URLs.
    - Push code to GitHub.

### Environment Variables (Optional)

24. **ALLOWED_HOSTS and CLIENT_ORIGIN_DEV:**
    - In `settings.py`, update `ALLOWED_HOSTS` with Heroku's URL.
    - Add `CLIENT_ORIGIN_DEV` if using Gitpod workspace.

25. **Push and Deploy:**
    - Push changes to GitHub.
    - In Heroku, manually deploy code again.
   
The live link can be found here - https://taskflow-app-734253c0080e.herokuapp.com/

## Libraries Used for Back-End

1. **Django REST Framework:** This Python library served as the core framework for building the API, providing essential tools for API development.

2. **Django Forms:** Django Forms played a pivotal role in handling HTML forms within the TaskFlow web application. It was employed for tasks such as creating projects and tasks, making the application interactive.

3. **Django REST Auth:** Django REST Auth was instrumental in user registration and authentication management. It allowed users on the front end to create and manage their accounts by making requests to the API endpoints. Its compatibility with Django REST Framework ensured seamless integration.

## Testing 

All sections of Taskflow were tested End to End; Some of the main testing points included:

| Test       | Expected           | Passed  |
| :------------- |:-------------:| :-----:|
| Non-authenticated user tries accessing URL endpoints '/projects' | Displays Welcome message requesting user to sign in/up  | ✅ |
| Non-authenticated user tries accessing URL endpoints '/projects/:id' | Redirected to Sign In page  | ✅ |
| Non-authenticated user tries accessing URL endpoints '/projects/create' | Redirected to Sign In page | ✅ |
| Non-authenticated user tries accessing URL endpoints '/projects/:id/edit' | Redirected to Sign In page | ✅ |
| Non-authenticated user tries accessing URL endpoints '/projects/:id/tasks/create' | Redirected to Sign In page | ✅ |
| Non-authenticated user tries accessing URL endpoints '/tasks' | Redirected to Sign In page | ✅ |
| Non-authenticated user tries accessing URL endpoints '/tasks/:id' | Redirected to Sign In page | ✅ |
| Non-authenticated user tries accessing URL endpoints '/tasks/:id/edit' | Redirected to Sign In page | ✅ |
| Authenticated user tries accessing projects they don't own via URL endpoints '/projects/:id' | Redirected to Home/Projects Page | ✅ |
| Authenticated user tries editing projects they don't own via URL endpoints '/projects/:id/edit' | Redirected to Home/Projects Page | ✅ |
| Authenticated user tries creating tasks for projects they don't own via URL endpoints '/projects/:id/tasks/create' | Redirected to Home/Projects Page | ✅ |
| Authenticated user tries accessing tasks they don't own via URL endpoints '/tasks/:id' | Redirected to Home/Projects Page | ✅ |
| Authenticated user tries editing task they don't own via URL endpoints '/tasks/:id/edit' | Redirected to Home/Projects Page | ✅ |
| User clicks all navigation links on home page     | Taken to corresponding page | ✅ |
| User logs in / registers | Nav links change and access to projects/tasks becomes available | ✅ |
| User clicks 'Create Project'| Directed to create project page | ✅ |
| User completes create project form and submits (valid data) | Project created and redirected to Project page with project info | ✅ |
| User completes project form and submits (invalid data)| Error / Invalid messages | ✅ |
| User clicks edit project button | Directed to edit project page with prepopulated form | ✅ |
| User updates project (valid data) | Project details updated successfully and redirected to previous page | ✅ |
| User updates project (invalid data) | Error / Invalid messages | ✅ |
| User clicks delete icon on project page | Project is deleted and redirected to landing page | ✅ |
| User clicks 'Add Task'| Directed to create task page | ✅ |
| User completes create task form and submits (valid data) | Task created and redirected to previous page | ✅ |
| User completes task form and submits (invalid data)| Error / Invalid messages | ✅ |
| User clicks edit task button | Directed to edit task page with prepopulated form | ✅ |
| User updates task (valid data) | Task details updated successfully and redirected to related project page | ✅ |
| User updates task (invalid data) | Error / Invalid messages | ✅ |
| User clicks delete icon on task page | Task is deleted and redirected to landing page | ✅ |
| User clicks project card | Directed to the Project page | ✅ |
| User clicks task card | Directed to the Task page | ✅ |
| User types in the search bar on landing page | Project cards are filtered to match search | ✅ |
| User clicks sign out | User is signed out and directed to the logged-out home page | ✅ |

