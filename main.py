import os, csv

old_file = "Sample Files\\Old.csv"
new_file = "Sample Files\\New.csv"
calibration_file = "Sample Files\\Old.btcal"
output_file = "updated_cal.btcal"

def open_patch(in_file):
    """Returns a dict that contains Spot:Patch."""
    with open(in_file, encoding='utf-16') as read_file:
        csv_reader = csv.DictReader(read_file)
        spot_map = {
            row['Spot']:f"WYG/{row['Patch'].split('.')[0]}/{row['Spot'].rjust(4, '0')}"
            for row in csv_reader
        }

    return spot_map

old_map = open_patch(old_file)
new_map = open_patch(new_file)
keywords = {new_map[key]:old_map[key] for key in old_map}

with open(calibration_file) as read_file:
    calibration_content = read_file.read()

for key in keywords:
    calibration_content = calibration_content.replace(keywords[key], key)

try:
    os.remove(output_file)
except FileNotFoundError:
    pass

with open(output_file, 'x') as write_file:
    write_file.write(calibration_content)