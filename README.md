# TrackMan-Baseball-Data-Analysis
A series of programs written in Python to help visualize baseball TrackMan data in digestible ways to aid in player development. Outputs consist of data tables, figures, and web app interface.

IMPORTANT: Some TrackMan systems use plate_z_cor and plate_x_cor instead of PlateLocHeight and PlateLocSide for pitch locations relative to the strike zone. Additionally, all programs in this repository utilize TaggedPitchType instead of AutoPitchType to distinguish between pitch types.

Data_Cleaner: Streamlined way to acquire overall pitch characteristics. Will output CSV table with average pitch metrics sorted by pitch type. Currently only includes pitch type, release speed, spin rate, horizontal, and vertical break.

Pitch_Graphic: Easy way to visualize pitch command and movmement profile. Will output PNG file with side by side pitch command plot and break plot. Additional legend for distinguishing pitch type.

Pitch_Hub: DASH web app designed to put all data tools in one place. Browser interface includes command plot, movement plot, pitch result chart, spin axis chart, metric histogram, and data table. Each graph includes interactive dropdown menus to filter by pitch type or by metric. The data table includes search bars for each column and max/min filer arrows. Currently set up for 4 pitch mix (FB, CB, SL, CH) but can be adjusted and expanded.
