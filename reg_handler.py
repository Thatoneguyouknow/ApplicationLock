import os
import winreg


# The steps for this are detailed in the following website:
    # https://www.technipages.com/prevent-users-from-running-certain-programs
blocked_apps = {}
def main():
    ### This sets up the registry for addition of new keys ###
    # Registry values are located in:
    # Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer
    # winreg.HKEY_CURRENT_USER is a winreg constant
    global blocked_apps
    hkey = winreg.HKEY_CURRENT_USER
    try: 
        subKeyExplorer = winreg.openKey(hkey, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer")
        subKeyDisallow = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\DisallowRun")
        # Creating DWORD Value called DisallowRun with value of 1
        winreg.SetValueEx( subKeyExplorer, "DisallowRun", 0, winreg.REG_DWORD, 1 )
        # Creating a key called DisallowRun
        mainKey = winreg.CreateKey( hKey, subKeyDisallow )
    except WindowsError:
        print("Could not create keys")
    # Creating a dictionary to hold each key and the number name associated with it
    add_new_app( "chrome.exe", "1")
    blocked_apps["1"] = "chrome.exe"
    delete_app( "chrome.exe" )



# This method will add a new app to block
# Param:
#   app_to_add: String name of format app.exe
#   registry_num: String number to order blocked apps
def add_new_app( app_to_add, registry_num ):
    # Within the new folder DisallowRun, create a new DWORD (32-bit) Value named '1'
    # Give '1' a value of "app_to_add".exe
    # Repeat with new apps under the values named 2-n
        # Create a new DWORD with a number name and app.exe value
    try:
        winreg.SetValueEX( mainKey, registry_num, 0, winreg.REG_DWORD, app_to_add )
    except WindowsError:
        print("Unable to add new value")



def delete_app( app_to_del ):
    # This will delete values that correspond with a specific app within the Key DisallowRun
    # Search dictionary for the access key of the app_to_del
    global blocked_apps
    for num_val in blocked_apps:
        if blocked_apps[num_val] == app_to_del:
            registry_num = num_val
    try:
        DeleteValue( mainKey, registry_num )
    except WindowsError:
        print("Unable to delete new value")

    

def block_pop_up():
    # When an application is blocked via the registry, and it is clicked to be opened a
    # dialogue pops up to tell the user that the user doesn't have the permission to open the app
    # We need a way to either edit or block this popup to replace it with our own.


    
main()
