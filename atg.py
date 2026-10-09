import os
import argparse
from pathlib import Path

BASE = [
  [
    "#include <Arduino.h>",
    "",
    "void setup(){"
  ],
  [
    "",
    "}",
    "",
    "void loop(){",
    "",
    "}"
  ]
]

def get_path() -> str:
  return os.getcwd()

def main() -> None:
  parser = argparse.ArgumentParser(
    prog="atg",
    usage="atg <project_name> [-s|--serial baudrate]",
    formatter_class=argparse.RawTextHelpFormatter,
    description="arduino project template generator",
    epilog="",
    add_help=True
  )
  parser.add_argument
  parser.add_argument("project_name", help="Name of the project to be generated")
  parser.add_argument("-s", "--serial")

  args = parser.parse_args()

  pj_name = args.project_name
  serial_baud = args.serial

  if serial_baud is not None:
    try:
      int_baud = int(serial_baud)
    except ValueError:
      print("ValueError: serial_baud must be of type Integer.")
      return
    file_data = [d for d in BASE[0]] + [f"  Serial.begin({int_baud});"] + ["  while(!Serial);"] + [d for d in BASE[1]]
  else:
    file_data = [d for d in BASE[0]] + [d for d in BASE[1]]

  file_data = [f"{d}\n" for d in file_data]

  pj_root_dir = os.path.join(get_path(), pj_name)
  try:
    Path(pj_root_dir).mkdir()
  except FileExistsError:
    print(f"FileExistsError: {pj_root_dir} already exists.")
    return
  except PermissionError:
    print("PermissionError: Permission denied.")
    return
  except OSError as e:
    print(f"OSError: {e}")
    return

  try:
    Path(os.path.join(pj_root_dir, "src")).mkdir()
  except FileExistsError:
    print(f"FileExistsError: {pj_root_dir} already exists.")
    return
  except PermissionError:
    print("PermissionError: Permission denied.")
    return
  except OSError as e:
    print(f"OSError: {e}")
    return

  try:
    Path(os.path.join(pj_root_dir, f"{pj_name}.ino")).touch()
  except FileExistsError:
    print(f"FileExistsError: {pj_root_dir} already exists.")
    return
  except PermissionError:
    print("PermissionError: Permission denied.")
    return
  except OSError as e:
    print(f"OSError: {e}")
    return

  try:
    with open(os.path.join(pj_root_dir, f"{pj_name}.ino"), "w", encoding="utf-8") as f:
      f.writelines(file_data)
  except FileExistsError:
    print(f"FileExistsError: {pj_root_dir} already exists.")
    return
  except PermissionError:
    print("PermissionError: Permission denied.")
    return
  except OSError as e:
    print(f"OSError: {e}")
    return

if __name__ == "__main__":
  main()