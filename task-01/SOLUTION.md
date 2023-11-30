

# SETUP

First of all I cloned the TerminalWizard repo using the git clone command:
```bash
git clone https://github.com/KshitijThareja/TerminalWizard.git
```

Since I was facing some 'Unknown error' when trying to execute the spell files, I reinstalled gh using the following commands:

```bash
sudo apt remove gh
```

```bash
sudo apt install gh
```
Then I basically followed all the steps as mentioned in the Steps.md file.
```bash
gh auth login
```

# PART 1
First, I created a directory called codes using the following: 

```bash
mkdir codes
```

For part one or the first challenge solving for x and y, I found the spell to be Impedimenta.py which I executed using the following:

```bash
cd spellbook
```

```bash
python3 Impedimenta.py
```

Then I copied the spell file to the codes directory
```bash
cp Impedimenta.py ../codes
```
I used the cat command to create and write the code that was printed out when I executed the Impedimenta.py to a Part_1.txt file:

```bash
cat > Part_1.txt
```

# PART 2

Solving for x and y, I executed the Stupefy.py file to find the code...
Using the exact commands mentioned above I was able to copy the spell file and write the code from the executed spell file to a Part_2.txt file

# PART 3

For the next part I solved the riddles by Googling for the answer since I was not interested in Harry Potter and the series.
I used the following commands to find the branch associated with the spell file:

```bash
git branch -a
ls
```
To find where the spell file was stored in, which according to the riddle was named after the spell Riddikulus I switched to the branch defenseAgainstTheDarkArts named after the subject taught by Professor Lupin...


```bash
git checkout defenseAgainstTheDarkArts
ls
cd spellbook
ls
```
Then I switched to main branch to copy the Riddikulus.py file from the defenseAgainstTheDarkArts branch to the main branch:

```bash
git checkout defenseAgainstTheDarkArts ../spellbook/Riddikulus.py
```

Then I executed the spell file to obtain the code:
```bash
git branch
cd spellbook
ls
python3 Riddikulus.py
```

Then I copied the file to the codes folder and made the Part_3.txt file to store the code:

```bash
cp Riddikulus.py ../codes/
cat > Part_3.txt
```
# PART 4

To obtain the last part of the code I cd'ed into the main repo TerminalWizard and executed:
```bash
git log
Hey there! The last spell is in path 0x/Spell_0y" of thegraveyard...
where x is the number of horcruxes made by Voldemort and y is the number that has same alphabets as the number
```
To find the spell I cd'ed to the spellbook directory in the corresponding branch:
```bash
git branch -a
git checkout thegraveyard
ls
cd spellbook
ls
```
Then I switched to main branch to copy the spell file from the thegraveyard branch to the main branch:

```bash
git checkout main
git checkout thegraveyard ../spellbook/Priori\ Incantatem.py
cd spellbook
python3 Priori\ Incantatem.py 
```
Then I copied the file to the codes folder and stored the code from executing the spell to the Part_4.txt file:
```bash
cp Priori\ Incantatem.py ../codes/
cd ..
cd codes
cat > Part_4.txt
```
# The End

For the final part to obtain the final code I concatenated all the files containing each separate code to one finalcode.txt file...
Then I deleted the files containing the individual codes:

```bash
cat Part_1.txt Part_2.txt Part_3.txt Part_4.txt > finalcode.txt
rm Part_1.txt Part_2.txt Part_3.txt Part_4.txt
```
To decode the base64 code I executed the following:

```bash
cat finalcode.txt
echo aHR0cHM6Ly9naXRodWIuY29tL1RoZUh1bnRzbWFuNC9UaGVGaW5hbFNwZWxs | base64 --decode
```
The code was decoded into a repo link which I cloned and :

```bash
git clone https://github.com/TheHuntsman4/TheFinalSpell.git
ls
cd TheFinalSpell
ls
cat TheOneThatEndsItAll.txt
```