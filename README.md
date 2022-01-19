# TrackMan-Baseball-Data-Analysis
A series of programs written in Python to help visualize baseball TrackMan data in digestible ways to aid in player development. Outputs consist of data tables, figures, and web app interface.

**IMPORTANT:** Some TrackMan systems use plate_z_cor and plate_x_cor instead of PlateLocHeight and PlateLocSide for pitch locations relative to the strike zone. Additionally, all programs in this repository utilize TaggedPitchType instead of AutoPitchType to distinguish between pitch types.

**Data_Cleaner:** Streamlined way to acquire overall pitch characteristics. Will output CSV table with average pitch metrics sorted by pitch type. Currently includes pitch type, release speed, spin rate, horizontal, and vertical break.
![image](https://user-images.githubusercontent.com/96801448/150199437-82d5a4c4-e4b9-4d5c-aec8-043b0933b7d8.png)

**Pitch_Graphic:** Easy way to visualize pitch command and movmement profile. Will output PNG file with side by side pitch command plot and break plot. Additional legend for distinguishing pitch type.
![image](https://user-images.githubusercontent.com/96801448/150199517-9f71d856-4589-4f2b-a850-77ea271a0a45.png)

**Pitch_Hub:** DASH web app designed to put all data tools in one place. Browser interface includes command plot, movement plot, pitch result chart, spin axis chart, metric histogram, and data table. Each graph includes interactive dropdown menus to filter by pitch type or by metric. The data table includes search bars for each column and max/min filer arrows. Currently set up for 4 pitch mix (FB, CB, SL, CH) but can be adjusted and expanded.
![image](https://user-images.githubusercontent.com/96801448/150199724-67728a67-46ab-48e2-b9eb-82e97a3457f6.png)
![image](https://user-images.githubusercontent.com/96801448/150199871-5da1e350-39d2-4b58-9da9-f0b274d9cf8a.png)
![image](https://user-images.githubusercontent.com/96801448/150200027-cb2a734c-3119-4793-ba0b-f534f1562723.png)
![image](https://user-images.githubusercontent.com/96801448/150200211-e023c9ad-c09f-4043-b98f-e529c2b8a48f.png)
