from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class CodeCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def code_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["code_writer"]
        )
    
    @task
    def write_code(self) -> Task:
        return Task(
            config=self.tasks_config["write_code"]
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )