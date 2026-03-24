"""
rbac_simulation.py
A simple script demonstrating Authentication and Role-Based Access Control (RBAC).
"""

# Simulated database linking usernames to their specific roles
USER_DB = {
    "alice_admin": "admin",
    "bob_regular": "user"
}

def login(username):
    """
    Simulates a login process.
    Returns a 'session' dictionary if the user exists, or None if they don't.
    """
    print(f"\nAttempting to log in as: '{username}'...")
    if username in USER_DB:
        print(f"[*] Login successful!")
        return {"username": username, "role": USER_DB[username]}
    else:
        print(f"[!] Login failed: User '{username}' does not exist.")
        return None

def access_admin_settings(session):
    """
    Protected endpoint #1: Strictly for 'admin' roles.
    """
    if not session:
        print("[!] Access Denied: No active session.")
        return

    # Check if the user has the required 'admin' role
    if session.get("role") == "admin":
        print(f"[+] ACCESS GRANTED: Welcome to Admin Settings, {session['username']}.")
    else:
        print(f"[-] ACCESS DENIED: {session['username']} lacks 'admin' privileges.")

def access_user_dashboard(session):
    """
    Protected endpoint #2: Strictly for 'user' roles.
    """
    if not session:
        print("[!] Access Denied: No active session.")
        return

    # Check if the user has the required 'user' role
    if session.get("role") == "user":
        print(f"[+] ACCESS GRANTED: Welcome to your Personal Dashboard, {session['username']}.")
    else:
        print(f"[-] ACCESS DENIED: {session['username']} is not a standard user.")

def main():
    print("=== Starting RBAC Simulation ===")

    # 1. Test the Admin User
    admin_session = login("alice_admin")
    access_admin_settings(admin_session)   # Should Succeed
    access_user_dashboard(admin_session)   # Should Fail (only 'user' role allowed here)

    # 2. Test the Standard User
    user_session = login("bob_regular")
    access_admin_settings(user_session)    # Should Fail (only 'admin' role allowed here)
    access_user_dashboard(user_session)    # Should Succeed

    # 3. Test an Invalid/Unauthenticated User
    hacker_session = login("eve_hacker")
    access_admin_settings(hacker_session)  # Should Fail (no session)

if __name__ == "__main__":
    main()