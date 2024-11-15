#!/usr/bin/env python3
import os
import subprocess

result = subprocess.run( ['$1', '$2'], capture_output=True, text=True)

# 输出结果
print("Return code:", result.returncode)
print("Output:\n", result.stdout)
print("Errors:\n", result.stderr)
