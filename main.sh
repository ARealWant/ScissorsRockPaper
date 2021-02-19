echo -n "Would you like to run a rigged version (if not, normal version)? (y/n)? "

read answer

if [ "$answer" != "${answer#[Yy]}" ] ;then
    python3 riggedScissorsRockPaper.py
else
    python3 ScissorsRockPaper.py
fi