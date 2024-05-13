from crewai import Agent
from textwrap import dedent
# from langchain.llms import OpenAI, Ollama
# from langchain_openai import ChatOpenAI
# from .cashflow_prediction import CashFlowPrediction
from .tools.cashflow_prediction import CashFlowPrediction


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        # self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        # self.Ollama = Ollama(model="openhermes")
        pass

    

    def agent_1_name(self):
        return Agent(
            role="you are an expert financial analyst",
            backstory=dedent(f"""as a financial analyst you predict cashflow of expenses for future number of dates provided by the customer"""),
            goal=dedent(f"""Forecasting the cashflow prediction"""),
            tools=[CashFlowPrediction.forecast_cashflow],
            allow_delegation=False,
            verbose=True,
            # llm=self.OpenAIGPT35,
        )
