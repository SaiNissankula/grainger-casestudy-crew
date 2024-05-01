import os
from dotenv import load_dotenv
load_dotenv()

from grainger_casestudy_crew.crew import GraingerCaseStudyCrew

def run():
    inputs = {
    }
    GraingerCaseStudyCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()    