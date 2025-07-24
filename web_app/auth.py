# auth.py

# --- Admin Username ---
# !!! IMPORTANT: Replace with your actual admin username !!!
# This username should also be included in the APPROVED_USERS set below.
ADMIN_USERNAME = "your_admin_username"

# --- List of Approved/VIP Users ---
# Add the usernames of users who should have access to this set.
# To add a new user later, just edit this file and add their username here.
# The ADMIN_USERNAME MUST also be in this set to log in.
APPROVED_USERS = {
    ADMIN_USERNAME, # Make sure the admin username is in the approved list
    "user1",
    "vip_user_2",
    "another_approved_user"
    # Example: "ali_vip", "reza_approved"
}

# --- Authentication Check Function (Username Only) ---
def check_credentials(username):
    """
    Checks if the provided username is valid (exists in the APPROVED_USERS list).
    Password is NOT checked in this simplified version.
    Returns True if the username is in the APPROVED_USERS list.
    Returns False otherwise.
    """
    return username in APPROVED_USERS

# --- Helper function to check if a user is admin ---
def is_admin(username):
    """Checks if the given username is the admin username."""
    # Note: In this setup, the admin user logs in just like any other approved user,
    # but this function can still be used to grant admin-specific features if needed.
    return username == ADMIN_USERNAME

# Note: In this simple approach, the APPROVED_USERS list and admin username
# are stored in the application's memory. They will reset to the values defined
# in the code every time the application restarts. For persistent storage,
# you would need to save this data to a file or database, which adds complexity.