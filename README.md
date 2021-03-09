# Dexter the Pokédex Bot
## Setting up a virtual environment

### For Windows:
Use Command Prompt to switch to the directory you want and type in:
```
python -m venv .
cd Scripts
activate
```

### For Mac/Linux:
Use the Terminal to switch to the directory you want and type in:
```
python3 -m venv env
source env/bin/activate
```

## Installing third party libraries
Once you've activated the virtual environments, the following command will install the same version of the third party libraries required to run this code.
```
pip install -r requirements.txt
```

## Future Improvements
- [ ] Add Gen. 7 & Gen. 8 Pokémon to database
- [ ] Add ability to look up Pokémon by name
- [ ] Shut down bot & database properly