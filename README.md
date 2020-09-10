# BlackTrax Auto Patcher
Takes an export from BTWYG for new and old patches and updates a .btcal file for easy re-importing.

## Instructions
1. Using the old WYG file with the old patch, go to `Data -> Spreadsheet`
2. Export the current table from `File - Export`
3. Select `csv` as the export option
4. Repeat for the new WYG file and the new patch
5. In BlackTrax, with the old patch and calibrated fixtures go to `File - Export - Fixture Calibration`
6. Open the Auto Patcher and browse for each file (the two csv files and the btcal export)
7. Press Re-Patch (when successful a message will appear)
8. Open the new BlackTrax file with the new patch and go to `File - Import - Fixture Calibration`
9. Verify import was successful

**NOTE:** This will only work if the spot IDs haven't changed. Spot IDs must be consistent between patches. 