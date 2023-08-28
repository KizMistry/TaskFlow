# Project Deployment Guide

This is the step-by-step process undertaken to deploy my Taskflow API to Heroku.

## ElephantSQL Setup

1. **Log in to ElephantSQL:** Visit [ElephantSQL.com](https://www.elephantsql.com) and log in to access dashboard.

2. **Create a Database Instance:**
   - Click "Create New Instance."
   - Set up plan (Name, Tiny Turtle plan, Select Region).
   - Click "Review," check details, and click "Create instance."

3. **Heroku Setup:**
   - Log in to Heroku and go to the Dashboard.
   - Create a new app, providing a name and selecting the region closest.
   - Open the "Settings" tab and add a Config Var "DATABASE_URL" with ElephantSQL database URL.

## Migrating Data

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

## Preparing for Deployment to Heroku

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

## Heroku Deployment

17. **Heroku Configuration:**
    - In Heroku Dashboard for the app, open the "Settings" tab.
    - Added two Config Vars: `SECRET_KEY` and `CLOUDINARY_URL`.
    - Set up `ALLOWED_HOST` with Heroku app's URL.

18. **Deploy to Heroku:**
    - Open the "Deploy" tab in Heroku.
    - Connect to GitHub and deploy code.
    - Enable automatic deploys for future changes.

## Verification

19. **Check Deployment:**
    - The app should be up and running on Heroku. Click "Open app" to check.

20. **Additional Check:**
    - Verify the JSON welcome message on the home screen.
    - Check the profile for the superuser at `/profiles/` on root URL.

## Bug Fix: dj-rest-auth

21. **Problem Statement:**
    - It turns out that dj-rest-auth has a bug that doesn't allow users to log out.

22. **Proposed Solution (Step 1):**
    - In `views.py`, import JWT_AUTH settings from `settings.py`.
    - Write a logout view to clear cookies properly.

23. **Bug Fix (Step 2):**
    - Include the logout view in `drf_api/urls.py` above the default dj-rest-auth URLs.
    - Push code to GitHub.

## Environment Variables (Optional)

24. **ALLOWED_HOSTS and CLIENT_ORIGIN_DEV:**
    - In `settings.py`, update `ALLOWED_HOSTS` with Heroku's URL.
    - Add `CLIENT_ORIGIN_DEV` if using Gitpod workspace.

25. **Push and Deploy:**
    - Push changes to GitHub.
    - In Heroku, manually deploy code again.


The live link can be found here - https://taskflow-app-734253c0080e.herokuapp.com/
