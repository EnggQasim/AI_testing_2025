# LLM Tool Call Example

This project demonstrates how to use CrewAI to create an agent that can perform tool calls using Large Language Models (LLMs).

## Overview

The code implements a simple example where an AI agent uses a tool to add two numbers (3 and 7). This showcases the basic structure of tool calling in CrewAI.

## Code Structure

The implementation is divided into several key components:

### 1. Tool Definition
```python
@tool("add two numbers")
def my_tool(num1: int, num2: int) -> int:
    """This tool is used to add two numbers"""
    return num1 + num2
```
- Defines a simple tool that adds two numbers
- Uses the `@tool` decorator to register it with CrewAI
- Takes two integers as input and returns their sum

### 2. ToolCallerCrew Class
```python
@CrewBase
class ToolCallerCrew:
    def tool_caller_agent(self) -> Agent:
        # Defines the agent with its role and tools
    
    def tool_caller_task(self) -> Task:
        # Defines the task for the agent
    
    @crew
    def crew(self) -> Crew:
        # Creates and configures the crew
```
- Main class that orchestrates the tool calling process
- Uses `@CrewBase` decorator for CrewAI integration
- Contains methods for agent, task, and crew configuration

### 3. CrewRunner Class
```python
class CrewRunner(Flow):
    @start()
    def start(self):
        crew = ToolCallerCrew().crew().kickoff()
        return crew.raw
```
- Handles the execution flow of the crew
- Uses CrewAI's Flow system for orchestration
- Returns the raw results from the crew execution

### 4. Run Function
```python
def run_crew():
    runner = CrewRunner()
    result = runner.kickoff()
    print(result)
```
- Entry point for executing the tool call
- Creates a CrewRunner instance and starts the process
- Prints the final result

## How to Run

1. Make sure you have the required dependencies installed:
   ```bash
   pip install crewai
   ```

2. Run the script using:
   ```bash
   uv run run_crew
   ```
   Where `run_crew = "llm_tool_call.main1:run_crew"`

## Expected Output

The script will output:
```
The sum of 3 and 7 is 10
```

## Note

- The code uses CrewAI's decorators (`@CrewBase`, `@crew`, `@start`) for proper integration
- The agent is configured to be a helpful assistant focused on adding numbers
- The process runs sequentially as specified by `Process.sequential`
- Warning messages about missing config files are normal and don't affect functionality
