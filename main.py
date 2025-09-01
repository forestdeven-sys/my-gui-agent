import argparse
from agent_core import get_ai_plan
from action_engine import execute_plan

def main():
    """
    Main entry point for the GUI Agent.
    """
    parser = argparse.ArgumentParser(description="GUI Agent to execute missions in a browser.")
    parser.add_argument("mission", type=str, help="The mission for the agent to accomplish.")
    args = parser.parse_args()

    mission = args.mission
    print(f"Mission: {mission}")

    print("Getting plan from AI...")
    plan = get_ai_plan(mission)

    if plan:
        print("Executing plan:")
        print(plan)
        execute_plan(plan)
    else:
        print("Could not get a plan from the AI.")

if __name__ == "__main__":
    main()
