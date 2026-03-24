# RBAC and Authentication Mini-App

## Overview
This is a basic Python script that demonstrates the core concepts of Authentication and Role-Based Access Control (RBAC). 

## How the App Works
1. **Authentication Simulation:** The `login()` function checks a hardcoded dictionary (`USER_DB`) to see if a provided username exists. If it does, it generates a simulated "session" containing the user's name and assigned role. 
2. **Role-Based Access Control (RBAC):** Two separate endpoints are created: `access_admin_settings` and `access_user_dashboard`. 
3. **Enforcement:** Each endpoint inspects the session data. `access_admin_settings` exclusively requires the `"admin"` role, while `access_user_dashboard` exclusively requires the `"user"` role. Any mismatch results in access being denied.

## Connection to the CIA Triad
This application primarily demonstrates **Confidentiality**. 

In the CIA Triad, Confidentiality ensures that sensitive information is only disclosed to authorized individuals. By implementing RBAC, this script ensures that regular users cannot view or interact with administrative settings, and admins cannot improperly access standard user dashboards. The system restricts access based on the principle of least privilege, keeping the data in those specific functions confidential from unauthorized roles.

## How to Run
1. Ensure you have Python installed on your machine.
2. Run the script from your terminal: `python rbac_simulation.py`
3. Observe the console output to see how access is granted or denied based on the hardcoded roles.
