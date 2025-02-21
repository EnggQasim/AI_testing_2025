from crewai.tools import tool

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.flow import Flow, start, listen


@tool("add two numbers")
def my_tool(num1: int , num2 : int) -> int:
    """This tool is used to add two numbers"""
    # Function logic here
    return num1 + num2



@CrewBase
class ToolCallerCrew:
   

    # If you would lik to add tools to your crew, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    
    def tool_caller_agent(self) -> Agent:
        return Agent(
            role="You are a helpful assistant",
            goal="Add two numbers 3 and 7",
            backstory="You are a helpful assistant that can add two numbers: pls add 3 and 7",
            tools=[my_tool],
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    
    def tool_caller_task(self) -> Task:
        return Task(
            description="Add two numbers 3 and 7",
            expected_output="The sum of 3 and 7 is 10",
            agent=self.tool_caller_agent(),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=[self.tool_caller_agent()],  # Automatically created by the @agent decorator
            tasks=[self.tool_caller_task()],  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            tools=[my_tool]
        )
    
class CrewRunner(Flow):
    @start()
    def start(self):
        crew = ToolCallerCrew().crew().kickoff()
        return crew.raw

def run_crew():
    runner = CrewRunner()
    result = runner.kickoff()
    print(result)

    
    


