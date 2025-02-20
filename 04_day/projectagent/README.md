## Step1
```cmd

(base) m.qasim@Muhammads-MacBook-Pro 04_day % pip install crewai crewai-tools -Uq
(base) m.qasim@Muhammads-MacBook-Pro 04_day % crewai version
crewai version: 0.102.0
(base) m.qasim@Muhammads-MacBook-Pro 04_day % crewai create flow projectagent
Creating flow projectagent...
Flow projectagent created successfully!
(base) m.qasim@Muhammads-MacBook-Pro 04_day % cd projectagent 
(base) m.qasim@Muhammads-MacBook-Pro projectagent % cursor .
```

## Step2
1. Open `.env` file and add your API key and Model name
```
GEMINI_API_KEY=Paste your API key here
MODEL=gemini/gemini-1.5-flash
```
## Step3
Run your project
1. open terminal (control+j)
2. run the following command
```cmd
uv run kickoff
```

## Step4 (customize persona of agents)  
1. Open `src/projectagent/crews/poem_crew/config/agents.yaml` file
2. Change the `role` and `goal` of the `poem_writer` agent
```yaml
role: >
    NC Poem Writer
  goal: >
    Generate a artical about Pakistan beautiful places with {sentence_count}
```


![image.png](image.png)


