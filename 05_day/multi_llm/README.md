# Multi LLM

This is a project that uses multiple LLMs to solve a problem.

## Installation

```bash
pip install crewai crewai-tools
```

## Create crew and Agents
1. Create a crew
    - `src/multi_llm/crews/nc/nc.py`
2. Create agents
    - Create a agent config file in the crew folder `agents.yaml`
3. Create tasks
    - Create a task config file in the crew folder `tasks.yaml`

## Run Crew

```bash
uv run nc
```

## Contributing

If you have any suggestions or improvements, please feel free to contribute to the project.