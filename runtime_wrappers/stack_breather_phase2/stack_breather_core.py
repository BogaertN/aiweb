# stack_breather_core.py

import json
import os
from datetime import datetime
from core_breather import CoreBreather
from field_breather import FieldBreather

core_breather = CoreBreather()
field_breather = FieldBreather()

def unified_breathe_cycle(stack_loops=2):
    trace_file = "stack_breather_trace.jsonl"
    if os.path.exists(trace_file):
        os.remove(trace_file)

    for loop in range(stack_loops):
        for phase in range(1, 10):
            core_output = core_breather.breathe(phase)
            field_output = field_breather.breathe(phase)

            trace_entry = {
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "loop": loop,
                "phase": phase,
                "core_output": core_output,
                "field_output": field_output
            }

            with open(trace_file, "a") as f:
                f.write(json.dumps(trace_entry) + "\n")

            print(f"Loop {loop} | Phase {phase} | Core Output: {core_output} | Field Output: {field_output}")

