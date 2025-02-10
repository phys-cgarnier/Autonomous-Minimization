from checks.system_checks import SystemChecks
from pathlib import Path
import os
print(os.getcwd())
yaml = Path('yaml/checks_config.yaml')
checks_obj = SystemChecks.from_yaml(yaml)