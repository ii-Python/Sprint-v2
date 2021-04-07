# sprint

import os
import sys

print(sys.argv)
sys.argv = ["some-cmd", "cheese", "puff"]
print(sys.argv)

os.chdir(os.getenv("SP_ASSET_DIR"))

import assets  # type: ignore

os.chdir(os.getenv("SP_WORKDIR"))

print(os.getcwd())
print(os.listdir())

print(assets.info)
