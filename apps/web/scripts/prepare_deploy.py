import os
import glob

frontend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web\src"

# We will replace 'http://localhost:5000' with a base URL constant or env variable.
# To keep it simple without breaking things, we'll replace:
# 'http://localhost:5000/api
# with
# `${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api

files = glob.glob(os.path.join(frontend_dir, "**/*.tsx"), recursive=True) + glob.glob(os.path.join(frontend_dir, "**/*.ts"), recursive=True)

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "'http://localhost:5000" in content or "`http://localhost:5000" in content:
        # For strings with backticks: `http://localhost:5000/api/...`
        content = content.replace("`http://localhost:5000/api", "`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api")
        # For regular strings: 'http://localhost:5000/api/...' -> we need to convert them to template literals
        content = content.replace("'http://localhost:5000/api", "`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api")
        # Fix any ending quotes if it was a standard string
        content = content.replace("'/api", "`/api").replace("', {", "`, {") 
        # Actually a safer regex replacement:
        pass

# Let's do a more robust string replace using python regex
import re

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = content
    # Replace 'http://localhost:5000/api...' with `${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api...`
    new_content = re.sub(r"'http://localhost:5000([^']*)'", r"`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}\1`", new_content)
    new_content = re.sub(r"`http://localhost:5000([^`]*)`", r"`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}\1`", new_content)
    
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file}")

print("Frontend API URLs updated for deployment!")
