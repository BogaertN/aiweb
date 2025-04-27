import os
import json
import time

INSTALL_STATE = "install_state.json"

def setup_environment():
    required_dirs = [
        "../symbolic_capacitor_engine_frozen_v1",
        "../cold_archive_engine_frozen_v1",
        "../loop_resurrection_engine_frozen_v1",
        "../resonance_charge_meter_frozen_v1",
        "../tone_engine_frozen_v1",
        "../peer_communication_engine_frozen_v1",
        "../compute_contribution_engine_frozen_v1",
        "../awh_token_runtime_frozen_v1",
        "../contribution_dashboard_engine_frozen_v1"
    ]

    missing_dirs = []

    for directory in required_dirs:
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
                missing_dirs.append(directory)
            except Exception as e:
                print(f"[!] Failed to create {directory}: {e}")

    install_report = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "missing_directories_created": missing_dirs,
        "status": "completed"
    }

    with open(INSTALL_STATE, "w") as f:
        json.dump(install_report, f, indent=2)

    print(f"✔️ Install check complete. Report: {install_report}")
    return install_report
