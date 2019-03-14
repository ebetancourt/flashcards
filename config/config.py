import os

DEBUG = True
SECRET_KEY = 'REPLACE ME - this value is here as a placeholder.'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-Mail SMTP server settings
MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_DEFAULT_SENDER = '"Flash Cards" <flashcardsapp@gmail.com>'
MAIL_SERVER = os.environ['MAIL_SERVER']
MAIL_PORT = os.environ['MAIL_PORT']
MAIL_USERNAME = os.environ['MAIL_USERNAME']
MAIL_PASSWORD = os.environ['MAIL_PASSWORD']

# Flask-User settings
# Shown in and email templates and page footers
USER_APP_NAME = "Flash Cards"
USER_ENABLE_EMAIL = False        # Enable email authentication
USER_ENABLE_USERNAME = True    # Disable username authentication
USER_EMAIL_SENDER_NAME = USER_APP_NAME
USER_EMAIL_SENDER_EMAIL = "noreply@example.com"
