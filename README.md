# Solar Challenge - Week 1

## Environment Setup
Follow these steps to set up and reproduce the development environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/solar-challenge-week1.git
   cd solar-challenge-week1
   ```

2. Create a virtual environment:
   - Using `venv`:
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # Use 'venv\Scripts\activate' on Windows
     ```
   - Using `conda`:
     ```bash
     conda create -n solar_challenge python=3.10 -y
     conda activate solar_challenge
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run CI manually or push changes to the repository to trigger GitHub Actions.

## Folder Structure
```
├── .vscode/

│   └── settings.json

├── .github/

│   └── workflows

│       ├── ci.yml

├── .gitignore

├── requirements.txt

├── README.md

 |------ src/

├── notebooks/

│   ├── __init__.py

│   └── README.md

├── tests/

│   ├── __init__.py

└── scripts/

    ├── __init__.py

    └── README.md
```
# Setup complete