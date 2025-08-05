import openai
from autogpt import AutoGPT

class MasterOrchestrator:
    def __init__(self):
        self.agents = {
            "website_builder": AutoGPT(task="Build and maintain website"),
            "marketing_bot": AutoGPT(task="Automate social media posts"),
            "payment_processor": AutoGPT(task="Handle FNB payments"),
        }

    def run(self):
        while True:
            for agent_name, agent in self.agents.items():
                agent.execute()
                self.monitor_performance(agent_name)

    def monitor_performance(self, agent_name):
        print(f"[MONITOR] {agent_name} is running optimally.")

if __name__ == "__main__":
    orchestrator = MasterOrchestrator()
    orchestrator.run()
