# test_aiweb_os_engine.py

from run import execute_command

print(">>> ping")
print(execute_command("ping"))

print("\n>>> init")
print(execute_command("init"))

print("\n>>> get_status")
print(execute_command("get_status"))

print("\n>>> invalid")
print(execute_command("launch_nuke"))

