# test_resurrection_planner_core.py

from resurrection_planner_core import ResurrectionPlanner

def test_resurrection_planner_behavior():
    planner = ResurrectionPlanner()
    record = planner.schedule_recovery("test_loop", 5)
    assert record["loop_id"] == "test_loop", "Loop ID must match."
    assert record["priority_level"] == 5, "Priority level must match."
    print("✅ Resurrection Planner Test Passed.")

if __name__ == "__main__":
    test_resurrection_planner_behavior()
