#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from multi_llm.crews.nc.nc import NcCrew


class NcState(BaseModel):
    problem: str = ""
    code : str = ""
    review : str = ""


class NcFlow(Flow[NcState]):

    @start()
    def generate_problem(self):
        print("Step 1 : Generate problem")
        self.state.problem = "write python addition function code that will add 2 numbers"

    @listen(generate_problem)
    def generate_code(self):
        print("Step 2 : Generating code")
        result = (
            NcCrew()
            .crew()
            .kickoff(inputs={"problem": self.state.problem})
        )

        print("Code generated", result.raw)
        self.state.code = result.raw

    @listen(generate_code)
    def save_code(self):
        print("Step 3 : Saving code")
        with open("code.py", "w") as f:
            f.write(self.state.code)


def kickoff():
    nc_flow = NcFlow()
    nc_flow.kickoff()



