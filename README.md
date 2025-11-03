# HalloweenHackathon
Team 5's Halloween hackathon with Code Institute

deployment link: https://halloweenhackathon-aaa7ba8be0f6.herokuapp.com/

To install/ set up:


# 2. Create the virtual environment
python3 -m venv venv

# 3. ACTIVATE the virtual environment (This is the critical step)
# This command is correct for macOS/Linux:
source venv/bin/activate



# 4. Install dependencies using your requirements.txt file
# This assumes your requirements.txt file is already saved in this folder.
pip install -r requirements.txt

# 7. Run initial database migrations
# This sets up the default tables for authentication, admin, etc.
python manage.py migrate


# 8. Run the server to verify the setup
echo "Starting server on http://127.0.0.1:8000/"
python manage.py runserver

# 9. Presentation Video Team 5 Halloween Hackaton

Link:- https://drive.google.com/file/d/1cz2zbY7u7Yjytu5XAXP38Rm44LT2ENRF/view?usp=sharing