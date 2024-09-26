
# venv and python-dotenv

># Initializing this project with a .env file and a virtual environment
1. Create a virtual environment: `python -m venv project_env`
2. Activate the environment: `.\project_env\Scripts\activate` (for VS Code)
3. Install libraries for this environment: `pip install - r requirement.txt`
4. Create a `.env` file
5. Fill it up based on what is described in the `env-template` file
6. Edit your `.env` file to enter your Open AI key

># venv
## Tutorials
- **windows**: https://www.youtube.com/watch?v=APOPm01BVrk
- **mac & linux**: https://www.youtube.com/watch?v=Kg1Yvry_Ydk&t=0s
- **Integration with vscode**: https://app.pluralsight.com/ilx/video-courses/ca7b7610-2aab-4aa2-996c-f2a87db870c5/40f2adaa-9efb-4b91-abe0-1f1202be6a17/6269b315-4f03-4fe9-be63-bf67806812b1
## Commands
- `pip list` list all the packages installed
where python >>> lists all environments
  - `pip list --local` gives you the list of the packages in the active environment only (venv) 
- `python -m venv project_env` >>> create virtual environments
- project_env\Scripts\activate.bat >>> activate that environment
    - `deactivate`  >>> to deactivate the venv
    - in VSCode, use `.\project_env\Scripts\activate`
    - `rm - rf project_env` >>> to delete the virtual environment

- `requirement.txt` >>> file used to share the pip install requirement between different virtual environments (so you don't have to run multiple pip install for every environments)
    - run `pip freeze` to get the input of the requirement.txt file in the right format
    - `pip install - r requirement.txt` >>> to install the libraries in the requirement.txt file
    - `python -m venv project_env --system-site-packages` >>> inherits the packages installed at the system level


># dot-env
## Tutorials
https://www.youtube.com/watch?v=V_2sbyFMrUA

## Commands
### See code in main.py

### For production
Use export function to set environment variables instead of .env
`export OPENAI_KEY=123456` >>> that will overwrite the values set in .env

### Alternative
Set environment variable when executing the script:
- `OPENAI_KEY=xxx URL_VARIABLE_1=https://xxx main.py` >>> that will overwrite any value in the session or .env


># Writing a README.md file 

- Basic syntax: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
- VSCode specifics: https://www.youtube.com/watch?v=DLLrcr9u_XI
