PROCESS_PARAMETERS = [
    # Frame Parameters
    'AOA',
    'Pitch',
    'Heading',
    'Airspeed',
    'Altitude STD',
    'Altitude Radio',
    'Altitude Radio (A)',
    'Altitude Radio (B)',
    'Altitude Radio (C)',
    'Roll',
    'Acceleration Lateral',
    'Acceleration Normal',
    'Acceleration Longitudinal',
    'Gross Weight',
    'ILS Localizer',
    # 'ILS (L) Localizer',
    # 'ILS (R) Localizer',
    'Eng (1) EGT',
    'Eng (2) EGT',
    'Eng (3) EGT',
    'Eng (4) EGT',
    'Latitude',
    'Longitude',
    'ILS Glideslope',
    # 'ILS (L) Glideslope',
    # 'ILS (R) Glideslope',
    'Drift',
    'ILS Frequency',
    'ILS (L) Frequency',
    'ILS (R) Frequency',
    'Vref',
    'Eng (1) N2',
    'Eng (2) N2',
    'Eng (3) N2',
    'Eng (4) N2',
    'V2',
    'Eng (1) N1',
    'Eng (2) N1',
    'Eng (3) N1',
    'Eng (4) N1',
    'Groundspeed',
    'Speedbrake',
    'Eng (1) Torque',
    'Eng (2) Torque',
    'Eng (3) Torque',
    'Eng (4) Torque',
    'Eng (1) Fuel Flow',
    'Eng (2) Fuel Flow',
    'Eng (3) Fuel Flow',
    'Eng (4) Fuel Flow',
    'Throttle Lever Angle (2)',
    'Throttle Lever Angle (1)',
    'Control Column Position (Capt)',
    'Control Column Position (FO)',
    'Control Column Force (Foreign)',
    'Control Column Force (Local)',
    'TAT',
    'Flight Number',
    'Year',
    'Month',
    'Day',
    'Hour',
    'Minute',
    'Second',
    'Frame Counter',
    # Derived Parameters
    'Pitch Rate',
    'Heading Continuous',
    'Airspeed For Flight Phases',
    'Fast',
    'Altitude AAL For Flight Phases',
    'Takeoff',
    'Pitch Rate During Takeoff Min',
    'Rate Of Climb For Flight Phases',
    'Airborne',
    'Airspeed Below FL100 Max',
    'Altitude Radio',
    'Acceleration Vertical',
    'Rate Of Climb',
    'Landing',
    'Touchdown',
    'Gross Weight At Touchdown',
    'Liftoff',
    'Altitude AAL',
    'Localizer Deviation 1000 To 150 Ft Max',
    'Airspeed Below 3000 Ft Max',
    'Airspeed 50 To 1000 Ft Max',
    'Altitude For Flight Phases',
    'Eng (*) EGT Avg',
    'Climbing',
    'Altitude When Climbing',
    'Climb For Flight Phases',
    'Descent Low Climb',
    'Go Around',
    'Height At Go Around Min',
    'Takeoff Peak Acceleration',
    'Latitude At Takeoff',
    'Longitude At Takeoff',
    'FDR Takeoff Airport',
    'Landing Peak Deceleration',
    'Latitude At Landing',
    'Longitude At Landing',
    'FDR Landing Airport',
    'Altitude QNH',
    'Rate Of Turn',
    'Acceleration Sideways',
    'Acceleration Forwards',
    'Acceleration Along Track',
    'Pitch Rate During Takeoff Max',
    'Rate Of Descent 1000 To 50 Ft Max',
    'Airspeed 500 To 50 Ft Max',
    'Approach And Landing',
    'Approach And Landing Lowest Point',
    'Heading At Lowest Point On Approach',
    'Latitude At Lowest Point On Approach',
    'Start Datetime',
    'Heading At Landing',
    'Approach And Go Around',
    'ILS Localizer Established',
    'ILS Frequency',
    'ILS Frequency On Approach',
    'Longitude At Lowest Point On Approach',
    'Precise Positioning',
    'FDR Approaches',
    'Heading True',
    'Pitch 1000 To 100 Ft Max',
    'Roll Above 1500 Ft Max',
    'Level Flight',
    'Airspeed Level Flight Max',
    'Rate Of Climb High',
    'Airspeed Minus Vref',
    'Airspeed Minus Vref 500 Ft To Touchdown Max',
    'ILS Glideslope Established',
    'Glideslope Deviation 1000 To 150 Ft Max',
    'Initial Climb Start',
    'Eng (*) N2 Avg',
    'Eng N2 Cycles',
    'Airspeed Minus V2',
    'Airspeed Minus V2 At Liftoff',
    'Eng (*) N1 Max',
    'Eng N1 3000 Ft To Touchdown Max',
    'Airspeed 1000 To 500 Ft Max',
    'Roll Above 1000 Ft Max',
    'Airspeed At Liftoff',
    'Glideslope Deviation Above 1000 Ft Max',
    'Descending',
    'Altitude When Descending',
    'Localizer Deviation 1500 To 1000 Ft Max',
    'Height Lost 50 To 1000 Max',
    'Climb Start',
    'ILS Approach',
    'Pitch Rate 35 To 1500 Ft Max',
    'Airspeed 400 To 50 Ft Max',
    'Takeoff Acceleration Start',
    'Altitude Radio For Flight Phases',
    'Final Approach',
    'Pitch During Final Approach Min',
    'Speedbrakes Deployed 1000 To 25 Ft',
    'Bottom Of Descent',
    'Landing Turn Off Runway',
    'Rate Of Descent 2000 To 1000 Ft Max',
    'Eng (*) N2 Min',
    'Airspeed Minus V2 35 To 400 Ft Min',
    'Pitch At Touchdown',
    'Rate Of Descent 500 Ft To Touchdown Max',
    'Altitude At Touchdown',
    'Height Lost 1000 To 2000 Ft Max',
    'FDR Analysis Datetime',
    'Rate Of Descent High',
    'Eng (*) Torque Max',
    'Eng Torque 500 Ft To Touchdown Max',
    'Roll Below 20 Ft Max',
    'FDR Landing Datetime',
    'FDR Takeoff Datetime',
    'FDR Duration',
    'Landing Start',
    'Airspeed 35 To 50 Ft Max',
    'Eng (*) Fuel Flow',
    'Mins To Touchdown',
    'Height Mins To Touchdown',
    'Roll Cycles 1000 Ft To Touchdown Max',
    'Pitch 5 Ft To Touchdown Max',
    'Acceleration Normal Ft To 35 Ft Max',
    'Throttle Lever',
    'Throttle Cycles 1000 Ft To Touchdown Max',
    'Control Column Stiffness Max',
    'Go Around Altitude',
    'Acceleration Normal Airborne Max',
    'Pitch 1000 To 100 Ft Min',
    'Pitch 20 Ft To Touchdown Min',
    'Airspeed 400 To 1500 Ft Min',
    'Acceleration Longitudinal Peak Takeoff',
    'Pitch Rate From 2 Degrees Of Pitch To 35 Ft Min',
    'Airspeed Minus Vref At Touchdown',
    'Landing Deceleration End',
    'Airspeed 2000 To 30 Ft Min',
    'Gross Weight At Liftoff',
    'FDR Takeoff Gross Weight',
    'Deceleration Longitudinal Peak Landing',
    'Eng (*) N1 Avg',
    'Power On With Speedbrakes Deployed Duration',
    'Eng N1 Max',
    'Eng N1 Takeoff Max',
    'Airspeed Max',
    'Altitude For Climb Cruise Descent',
    'Climb Cruise Descent',
    'Top Of Descent',
    'Top Of Climb',
    'Cruise',
    'FDR Landing Runway',
    'Acceleration Normal 20 Ft To Ground Max',
    'FDR Version',
    'Latitude Straighten',
    'Airspeed True',
    'ILS Range',
    'Longitude Straighten',
    'Heading At Takeoff',
    'FDR Takeoff Runway',
    'Latitude Smoothed',
    'Eng (*) Torque Min',
    'Eng Torque 500 Ft To Touchdown Min',
    'Eng (*) EGT Min',
    'Airspeed Minus Vref Between 2 Minutes To Touchdown And Touchdown Min',
    'FDR Flight Number',
    'Glideslope Deviation 1500 To 1000 Ft Max',
    'Longitude Smoothed',
    'Airspeed At Touchdown',
    '500 Ft To 0 Ft',
    'Pitch At Liftoff',
    'Airspeed Below Altitude Max',
    'Altitude Max',
    'Airspeed Minus V2 400 To 1500 Ft Min',
    'Acceleration Across Track',
    'Touch And Go',
    'FDR Flight Type',
    'Acceleration Normal Max',
    'Eng (*) EGT Max',
    'Eng EGT Max',
    'Pitch During Takeoff Max',
    'Takeoff Turn Onto Runway',
    'Eng N1 0 Ft To FL100 Max',
    'Glideslope Deviation Below 1000 Ft Max',
    'Eng EGT Takeoff Max',
    'Rate Of Descent 1000 To 500 Ft Max',
    'FDR Landing Gross Weight',
    'Turning',
    'FDR On Blocks Datetime',
    'Secs To Touchdown',
    'Airspeed Between 90 Sec To Touchdown And Touchdown Max',
    'Acceleration Normal Airborne Min',
    'Flare 20 Ft To Touchdown',
    'Distance Travelled',
    'Distance To Landing',
    'Acceleration Normal During Takeoff Max',
    'Eng Torque 0 Ft To FL100 Max',
    'Eng (*) N1 Min',
    'Eng N1 500 Ft To Touchdown Min',
    'FDR Off Blocks Datetime',
    'Pitch Cycles',
    'Eng (*) N2 Max',
    'Eng N2 Max',
    'Pitch 35 To 400 Ft Max',
    'Roll Between 100 And 500 Ft Max',
    'Pitch 35 To 400 Ft Min',
    'Roll Between 500 And 1500 Ft Max',
]

