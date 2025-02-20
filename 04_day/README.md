# CrewAI Flow Example

This project demonstrates a basic CrewAI workflow using Python and uv package manager. It showcases how to create agents, tasks, and execute them in a coordinated manner.

## Project Structure
```
.
├── README.md
├── requirements.txt
└── main.py
```

## Setup Instructions

1. First, ensure you have Python 3.9+ and uv installed. If you don't have uv, install it using:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Create and activate a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Unix/macOS
   # OR
   .venv\Scripts\activate  # On Windows
   ```

3. Install dependencies using uv:
   ```bash
   uv pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Running the Project

To run the project, simply execute:
```bash
python main.py
```

## Project Components

### Agents
- **Research Analyst**: Conducts research using DuckDuckGo search
- **Content Writer**: Creates content based on research findings

### Tasks
- Research task for gathering information
- Writing task for creating content

### Workflow
1. The Research Analyst gathers information about AI in healthcare
2. The Content Writer creates an article based on the research

## Customization

You can modify the agents and tasks in `main.py` to suit your specific needs. Some possibilities include:
- Adding more agents with different roles
- Incorporating additional tools
- Modifying task descriptions
- Changing the research topic

## Requirements
- Python 3.9+
- crewai>=0.14.0
- langchain>=0.1.0
- python-dotenv>=1.0.0
- openai>=1.10.0