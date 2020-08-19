initialize()
{
cp .env ~/bin/
cp create.py ~/bin/create
chmod a+x ~/bin/.env
chmod a+x ~/bin/create
echo "Created files. Installing Requirements"
sudo pip install -r requirements.txt
}

notexist()
{
echo "bin folder does not exist. Creating.."
mkdir ~/bin
initialize
}
test -d "/home/$USER/bin" && initialize ||  notexist