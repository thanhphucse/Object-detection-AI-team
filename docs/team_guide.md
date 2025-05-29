# Team Collaboration Guide

## Getting Started

### 1. Repository Setup
Each team member should:
```bash
# Clone the repository
git clone https://github.com/thanhphucse/Object-detection-AI-team.git
cd Object-detection-AI-team

# Install dependencies
pip install -r requirements.txt

# Run setup script (optional)
python scripts/setup_project.py
```

### 2. Add Yourself to the Team
1. Edit `README.md` and add your name to the team members section
2. Create a pull request with this change
3. This helps practice the workflow!

## Daily Workflow

### 1. Working on Tasks
```bash
# Always start by pulling latest changes
git pull origin main

# Create a new branch for your work
git checkout -b feature/your-task-name

# Do your work (code, notebooks, documentation)

# Commit your changes regularly
git add .
git commit -m "Descriptive message about what you did"

# Push to GitHub when ready
git push origin feature/your-task-name

# Create a pull request on GitHub for team review
```

### 2. Branch Naming Conventions
- `feature/data-exploration` - For new features or major work
- `fix/data-loading-bug` - For bug fixes
- `docs/update-readme` - For documentation updates
- `experiment/new-model` - For experimental work


### 3. Using Pull Requests
- All changes should go through pull requests
- At least one team member should review before merging
- Use pull requests to discuss code and share knowledge
- Include screenshots or results when relevant

### 4. Code Organization
- Keep notebooks in `notebooks/` organized by purpose
- Put reusable code in `src/` modules
- Use scripts in `scripts/` for data processing and training
- Document your code with comments and docstrings

### 5. Data Management
- Never commit large data files to git
- Keep original data in `data/raw/` (add to .gitignore)
- Put processed data in `data/processed/`
- Document data sources and processing steps

### 6. Collaboration
- **Communicate early and often**: Use issues and discussions
- **Share your notebooks**: Even rough exploration is valuable
- **Write clear commit messages**: Help teammates understand changes
- **Review each other's work**: Learn from each other's approaches

### 7. Documentation
- Update README.md with important project information
- Add comments to complex code
- Document data sources and processing steps
- Share interesting findings in issues or discussions


### 8. Common Git Issues
```bash
# If you have merge conflicts
git pull origin main
# Resolve conflicts in files, then:
git add .
git commit -m "Resolve merge conflicts"

# If you need to update your branch with latest main
git checkout main
git pull origin main
git checkout your-branch
git merge main

# If you accidentally committed to main
git checkout -b feature/fix-my-changes
git push origin feature/fix-my-changes
# Then create a pull request
```

### 9. Recommended Tools
- **Jupyter Notebook Extension**: For interactive development
- **VS Code**: For coding and git integration