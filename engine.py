import os, csv

def open_patch(in_file):
    """Returns a dict that contains Spot:WYG Patch."""
    # Open the csv and generat a new dict with just the relevant information
    with open(in_file, encoding='utf-16') as read_file:
        csv_reader = csv.DictReader(read_file)
        spot_map = {
            row['Spot']:f"WYG/{row['Patch'].split('.')[0]}/{row['Spot'].rjust(4, '0')}"
            for row in csv_reader
        }

    return spot_map

def generate_patch(old_file, new_file, calibration_file, output_file):
    """Replaces the btcal's file with the new patch information and saves to disk."""

    # Opens the files and creates a dict using spot IDs to easily map patch information back together
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
