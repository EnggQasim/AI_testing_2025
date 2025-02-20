from crewai.flow.flow import Flow, listen, start
import time

from cu_agent1.crews.cu_crew.cu_crew import CodeCrew

class CustomFlow(Flow):

    @start()
    def start_flow(self):
        print("Step1: User input")
        input_data = input("Your code tasks: ")
        self.state["code_tasks"] = input_data

    @listen(start_flow)
    def listen_flow(self):
        print("Step2: Crew")

        result = CodeCrew().crew().kickoff(
            inputs={
                "code_tasks": self.state["code_tasks"]
            }
        )
        
        self.state["code"] = result.raw
        print("Step4: Crew output Code")
        return self.state["code"]
    
    @listen(listen_flow)
    def listen_flow2(self):
        print("Step5: Print Code")
        with open("code.txt", "w") as f:
            f.write(self.state["code"])

def run_custom_flow():
    obj = CustomFlow()
    final_output = obj.kickoff()
    print(final_output)

