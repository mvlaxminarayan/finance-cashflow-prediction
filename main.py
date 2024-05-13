import os
from crewai import Agent, Task, Crew, Process
# from langchain_openai import ChatOpenAI
# from decouple import config

from textwrap import dedent
from src.agents import CustomAgents
from src.tasks import CustomTasks

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

from langchain.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

# os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
# os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")

from dotenv import load_dotenv
load_dotenv()

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
    def __init__(self, var1):
        self.var1 = str(var1)

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        custom_agent_1 = agents.agent_1_name()

        # Custom tasks include agent name and variables as input
        expected_output = "description : provide the forecast for future number of days"
        custom_task_1 = tasks.task_1_name(
            custom_agent_1,
            self.var1,
            expected_output
        )

        

        # Define your custom crew here
        crew = Crew(
            agents=[custom_agent_1],
            tasks=[custom_task_1],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    var1 = input(dedent("""Enter variable 1: """))
    

    custom_crew = CustomCrew(var1)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
