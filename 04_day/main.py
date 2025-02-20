from crewai import Agent, Task, Crew
from langchain.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize tools
search_tool = DuckDuckGoSearchRun()

# Define Agents
researcher = Agent(
    role='Research Analyst',
    goal='Conduct thorough research on given topics',
    backstory="""You are an expert research analyst with years of experience in 
    gathering and analyzing information from various sources.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool]
)

writer = Agent(
    role='Content Writer',
    goal='Create well-written, engaging content based on research',
    backstory="""You are a skilled content writer who excels at transforming 
    complex information into clear, engaging content.""",
    verbose=True,
    allow_delegation=False
)

# Define Tasks
research_task = Task(
    description="""Research the latest developments in artificial intelligence 
    and its impact on healthcare. Focus on practical applications and recent 
    breakthroughs.""",
    agent=researcher
)

writing_task = Task(
    description="""Using the research provided, create a comprehensive article 
    about AI in healthcare. Include specific examples and potential future 
    developments.""",
    agent=writer
)

# Create Crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=2
)

# Execute the crew's tasks
result = crew.kickoff()

print("\nFinal Result:")
print(result) 