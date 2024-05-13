from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def task_1_name(self, agent, var1, expected_output):
        return Task(
            description=dedent(
                f"""
           As a Financial analyst predict the future expenses for the number of days provided by the user.
            
            {self.__tip_section()}
    
            Make sure to use the most recent data as possible.
    
            Use this variable: {var1}
            
        """
            ),
            agent=agent,
            expected_output=expected_output
        )

    
