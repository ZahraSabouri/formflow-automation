# FormFlow Automation Setup Guide

## Project Setup

### 1. Environment Setup
```bash
# Create and activate virtual environment
python -m venv formflow-automation/venv
formflow-automation/venv/Scripts/activate  # Windows
source formflow-automation/venv/bin/activate  # Linux/Mac

# Upgrade pip and install poetry
python -m pip install --upgrade pip
python -m pip install poetry
```

### 2. Project Structure
```
formflow-automation/
├── .github/
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── form_handler.py
│   │   └── webdriver.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   └── config.py
│   └── tests/
├── logs/
├── config/
├── .gitignore
├── poetry.toml
├── pyproject.toml
└── README.md
```

### 3. Dependencies Setup
```bash
cd formflow-automation
poetry init

# Core dependencies to be added:
poetry add selenium
poetry add webdriver-manager
poetry add python-dotenv
poetry add loguru
poetry add pytest  --group dev
poetry add black --group dev
poetry add flake8 --group dev
```

### 4. WebDriver Setup
- Chrome WebDriver will be managed automatically through `webdriver-manager`
- No manual driver download required

### 5. Configuration
Create `.env` file in the root directory:
```
CHROME_DRIVER_PATH=auto
FORM_URL=your_google_form_url
SUBMISSION_DELAY=2
MAX_RETRIES=3
LOG_LEVEL=INFO
```

### 6. Git Setup
```bash
# Initialize git repository
git init

# Configure line endings
git config --global core.autocrlf false

# Create initial branch
git checkout -b main

# Add .gitignore
# Include common Python patterns, logs, and environment files
cat > .gitignore << EOL
# Virtual Environment
venv/
env/

# Python
__pycache__/
*.py[cod]
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Logs
logs/
*.log

# Environment variables
.env
.env.local

# IDE specific files
.idea/
.vscode/
*.swp
*.swo

# Operating System
.DS_Store
Thumbs.db
EOL

# Initial commit
git add .
git commit -m "Initial project setup with core structure"

# Add remote repository
git remote add origin [your-repo-url]
git push -u origin main
```

### 7. Running Tests
```bash
poetry run pytest
```

### 8. Code Formatting
```bash
poetry run black src/
poetry run flake8 src/
```

### 9. Troubleshooting

Common issues and solutions:
- If WebDriver fails to initialize, check Chrome browser version compatibility
- For SSL certificate errors, ensure proper system certificates
- For permission issues on Linux/Mac, ensure proper execute permissions on venv

### 10. Development Guidelines
- Always activate virtual environment before development
- Run tests before committing changes
- Follow PEP 8 style guide
- Use meaningful commit messages
