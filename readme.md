What this changes in the downloader
- Trims file names to 33 characters
  - This is needed because for some reason FANUC programs wont be read if they are longer than this
- removes the AM and PM from the creation and modification date in the attributes section
  - ```ls
  	CREATE          = DATE 23-04-13 TIME 01:16:08 PM;
  ```
  Turns into
  ```ls
  	CREATE          = DATE 23-04-13 TIME 01:16:08;```
- Makes sure all other groups other than GP1 and GP2 always have UTool 1
- E1 doesnt get populated properly if it isnt set for a specific position entry. This sets E1 to the previous position entrys E1 to fix that
  - Example: If you have a position entry with E1 at 1256mm, and your next position doesnt change E1, then E1 will instead be set to 90mm for that position entry
  - ```ls
	 P[10]{
	   GP1:
	  UF : 0, UT : 1, CONFIG : 'N   U   T, 0,0,0',  
	  X = 140.844 mm,  Y = -4855.036 mm,  Z = -612.601 mm,  
	  W = 55.215 deg,  P = 65.206 deg,  R = -73.106 deg,  
	  E1 = 2476.792 mm
	   GP2:
	  UF : 0, UT : 1,
	  J1 = 0.000 mm,  J2 = 0.000 mm,  J3 = 0.000 mm,
	  J4 = 0.000 mm,  J5 = 0.000 mm,  J6 = 0.000 mm
	   GP3:
	  UF : 0, UT : 1,
	  J1 = 301.777 deg
	};
	P[11]{
	   GP1:
	  UF : 0, UT : 1, CONFIG : 'N   U   T, 0,0,0',
	  X = 143.297 mm,  Y = -4863.112 mm,  Z = -630.874 mm,
	  W = 55.215 deg,  P = 65.206 deg,  R = -73.106 deg,
	  E1 = 90.000 mm
	   GP2:
	  UF : 0, UT : 1,
	  J1 = 0.000 mm,  J2 = 0.000 mm,  J3 = 0.000 mm,
	  J4 = 0.000 mm,  J5 = 0.000 mm,  J6 = 0.000 mm
	   GP3:
	  UF : 0, UT : 1,
	  J1 = 301.777 deg
	};
    ```
