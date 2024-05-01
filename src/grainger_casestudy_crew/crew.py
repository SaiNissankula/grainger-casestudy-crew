from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq

@CrewBase
class GraingerCaseStudyCrew():
	"""GraingerCaseStudyCrew crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self) -> None:
		self.groq_llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")

	@agent
	def company_researcher(self) -> Agent:
		return Agent(
			config = self.agents_config['company_researcher'],
			llm = self.groq_llm
		)

	@agent
	def company_writer(self) -> Agent:
		return Agent(
			config = self.agents_config['company_writer'],
			llm = self.groq_llm
		)

	@task
	def research_company_task(self) -> Task:
		return Task(
			config = self.tasks_config['research_company_task'],
			agent = self.company_researcher()
		)

	@task
	def analyze_company_task(self) -> Task:
		return Task(
			config = self.tasks_config['write_report_task'],
			agent = self.company_writer()
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the GraingerCaseStudyCrew crew"""
		return Crew(
			agents =  self.agents,
			tasks = self.tasks,
			process = Process.sequential,
			verbose = 2
		)