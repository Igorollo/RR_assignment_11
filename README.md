# RR Assignment 11

Reproducible Python project using `uv`.

## Setup

Install `uv` if it is not already available:

```bash
brew install uv
```

Clone the repository and reproduce the environment:

```bash
git clone https://github.com/Igorollo/RR_assignment_11.git
cd RR_assignment_11
uv sync --frozen
uv run python main.py
```

The script loads a small CSV dataset, prints the installed `numpy` and `pandas`
versions, and shows a short summary of the scores.
