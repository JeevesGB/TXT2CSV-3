##################################
#### Gran Turismo 3 CSV Tool ####
#################################

import os
import csv
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog

def get_input_for_headers(headers):
    data = {}
    for header in headers:
        value = input(f"Enter {header} (press Enter to skip): ")
        data[header] = value if value else ""
    return data

headers = {
    "ArcadeCar": ["Part","Car","Brake","BrakeController","Steer","Chassis","Lightweight","RacingModify","Engine","PortPolish","EngineBalance","Displacement","Computer","NATune","TurbineKit","Drivetrain","Flywheel","Clutch","PropellerShaft","LSD","Gear","Suspension","Intercooler","Muffler","FrontTire","RearTire","ASCC","TCSC","Unknown","Unknown2","Unknown3","Unknown4","Unknown5","Unknown6","Unknown7","Unknown8","Unknown9","Unknown10","Unknown11","Unknown12","FrontCamber","RearCamber","FrontToe","RearToe","Unknown13","Unknown14","RideHeight","Unknown15","Unknown16","Unknown17","FrontSpringRate","Unknown18","RearSpringRate","Unknown19","Unknown20","Unknown21","PowerMultiplier","FinalGearRatio","Unknown22","Unknown23"
],
    "Brake": ["Part","Car","Stage","FrontBrakeTorque","RearBrakeTorque","HandbrakeTorque","Price"
],
    "BrakeController": ["Part","Car","Stage","FrontSteps","FrontMinValue","FrontMaxValue","FrontDefaultStep","RearSteps","RearMinValue","RearMaxValue","RearDefaultStep","Price"
],
    "Car": ["Car","Brake","BrakeController","Steer","Chassis","Lightweight","RacingModify","Engine","PortPolish","EngineBalance","Displacement","Computer","NATune","TurbineKit","Drivetrain","Flywheel","Clutch","PropellerShaft","LSD","Gear","Suspension","Intercooler","Muffler","FrontTire","RearTire","ASCC","TCSC","WheelsMaybe","TunerIDMaybe","ManufacturerID","NameFirstPartUS","NameSecondPartUS","Label","Year","Price","IsSpecial","CarType","NameFirstPartJP","NameSecondPartJP","RegionFlag","Unknown3","NameFirstPartEU","NameSecondPartEU","ManufacturerName","Unknown4"
],
    "Chassis": ["Part","Car","FrontWeightDistribution","AdjustableDownforce","Unknown","Length","Height","Wheelbase","Weight","Unknown2","Unknown3","Unknown4"
],
    "Clutch": ["Part","Car","Stage","EngineBraking","FlywheelInertia","FrontWheelInertia","RearWheelInertia","ClutchTorque","Price"
],
    "Computer": ["Part","Car","Stage","TorqueModifier","TorqueModifier2","TorqueModifier3","Price"
],
    "Course": ["Course","SurfaceType","Filename","DisplayName","Unknown"
],
    "Displacement": ["Part","Car","Stage","TorqueModifier","TorqueModifier2","TorqueModifier3","Price"
],
    "Drivetrain": ["Part","Car","Stage","TorqueSplitMin","TorqueSplitMax","TorqueSplitDefault","DrivetrainType","AWDBehaviour","EngineBraking","FrontWheelInertia","RearWheelInertia","FrontPropshaftInertia","RearPropshaftInertia","FlywheelInertia","Price"
],
    "EnemyCars": ["Part","Car","Brake","BrakeController","Steer","Chassis","Lightweight","RacingModify","Engine","PortPolish","EngineBalance","Displacement","Computer","NATune","TurbineKit","Drivetrain","Flywheel","Clutch","PropellerShaft","LSD","Gear","Suspension","Intercooler","Muffler","FrontTire","RearTire","ASCC","TCSC","Unknown","Unknown2","Unknown3","Unknown4","Unknown5","Unknown6","Unknown7","Unknown8","Unknown9","Unknown10","Unknown11","Unknown12","FrontCamber","RearCamber","FrontToe","RearToe","Unknown13","Unknown14","RideHeight","Unknown15","Unknown16","Unknown17","FrontSpringRate","Unknown18","RearSpringRate","Unknown19","Unknown20","Unknown21","PowerMultiplier","FinalGearRatio","Unknown22","Unknown23"
],
    "Engine": ["Part","Car","LayoutName","ValvetrainName","Aspiration","SoundFile","TorqueCurve1","TorqueCurve2","TorqueCurve3","TorqueCurve4","TorqueCurve5","TorqueCurve6","TorqueCurve7","TorqueCurve8","TorqueCurve9","TorqueCurve10","TorqueCurve11","TorqueCurve12","TorqueCurve13","TorqueCurve14","TorqueCurve15","TorqueCurve16","Displacement","DisplayedPower","MaxPowerRPM","DisplayedTorque","MaxTorqueRPM","PowerMultiplier","ClutchReleaseRPM","IdleRPM","MaxRPM","RedlineRPM","TorqueCurveRPM1","TorqueCurveRPM2","TorqueCurveRPM3","TorqueCurveRPM4","TorqueCurveRPM5","TorqueCurveRPM6","TorqueCurveRPM7","TorqueCurveRPM8","TorqueCurveRPM9","TorqueCurveRPM10","TorqueCurveRPM11","TorqueCurveRPM12","TorqueCurveRPM13","TorqueCurveRPM14","TorqueCurveRPM15","TorqueCurveRPM16","TorqueCurvePoints"
],
    "EngineBalance": ["Part","Car","Stage","Unknown","RevIncrease","PowerIncreaseMaybe","PowerIncrease","Unknown2","Unknown3","Unknown4","Unknown5","Unknown6","Unknown7","Price"
],
    "Event": ["EventID","CourseID","Opponent1","Opponent2","Opponent3","Opponent4","Opponent5","Opponent6","Opponent7","Opponent8","Opponent9","Opponent10","Opponent11","Opponent12","Opponent13","Opponent14","Opponent15","Opponent16","Opponent17","Opponent18","Opponent19","Opponent20","Opponent21","Opponent22","Opponent23","Opponent24","Opponent25","Opponent26","Opponent27","Opponent28","Opponent29","Opponent30","Opponent31","Opponent32","UnknownOpponentData1","UnknownOpponentData2","UnknownOpponentData3","UnknownOpponentData4","UnknownOpponentData5","UnknownOpponentData6","UnknownOpponentData7","UnknownOpponentData8","UnknownOpponentData9","UnknownOpponentData10","UnknownOpponentData11","UnknownOpponentData12","UnknownOpponentData13","UnknownOpponentData14","UnknownOpponentData15","UnknownOpponentData16","UnknownOpponentData17","UnknownOpponentData18","UnknownOpponentData19","UnknownOpponentData20","UnknownOpponentData21","UnknownOpponentData22","UnknownOpponentData23","UnknownOpponentData24","UnknownOpponentData25","UnknownOpponentData26","UnknownOpponentData27","UnknownOpponentData28","UnknownOpponentData29","UnknownOpponentData30","UnknownOpponentData31","UnknownOpponentData32","EligibleCarsListID","RollingStartSpeed","Laps","SpecialConditionsType","License","AIMaybe1","AIMaybe2","AIMaybe3","AIMaybe4","AIMaybe5","AIMaybe6","AIMaybe7","AIMaybe8","AIMaybe9","AIMaybe10","AIMaybe11","AIMaybe12","AIMaybe13","AIMaybe14","AIMaybe15","AIMaybe16","AIMaybe17","AIMaybe18","AIMaybe19","AIMaybe20","Unknown1","Unknown2","Unknown3","Unknown4","Unknown5","CarsOnTrack","Unknown6","TireWearUnknownMaybe1","TireWearUnknownMaybe2","TireWearUnknownMaybe3","TireWearUnknownMaybe4","TireWearUnknownMaybe5","TireWearUnknownMaybe6","TireWearUnknownMaybe7","TireWearUnknownMaybe8","TireWearUnknownMaybe9","TireWearUnknownMaybe10","TireWearUnknownMaybe11","TireWearUnknownMaybe12","TireWearUnknownMaybe13","GoldTimeMinutes","GoldTimeSeconds","GoldTimeMilliseconds","SilverTimeMinutes","SilverTimeSeconds","SilverTimeMilliseconds","BronzeTimeMinutes","BronzeTimeSeconds","BronzeTimeMilliseconds","Unknown7","TireRestriction","Category","PrizeMoney1st","PrizeMoney2nd","PrizeMoney3rd","PrizeMoney4th","PrizeMoney5th","PrizeMoney6th","TireWearUnknownMaybe14","SeriesChampBonus","TimeLimitMinutes","DifficultyLevel","Unknown8","Unknown9","RaceModeID","Label","MachineTestMaybe","EventTypeRelatedMaybe","CarTypeRestriction","AspirationRestriction","DrivetrainRestriction"
],
    "Flywheel": ["Part","Car","Stage","EngineBraking","FlywheelInertia","FrontWheelInertia","RearWheelInertia","Price"
],
    "FrontTire": ["Part","Car","Stage","Price","Size","Compound1","Compound2","Compound3","Compound4","ForceVol1","ForceVol2","ForceVol3","ForceVol4"
],
    "Gear": ["Part","Car","Stage","NumberOfGears","ReverseGearRatio","FirstGearRatio","SecondGearRatio","ThirdGearRatio","FourthGearRatio","FifthGearRatio","SixthGearRatio","SeventhGearRatio","DefaultFinalDriveRatio","MaxFinalDriveRatio","MinFinalDriveRatio","AllowIndividualRatioAdjustments","DefaultAutoSetting","MinAutoSetting","MaxAutoSetting","Price"
],
    "Intercooler": ["Part","Car","Stage","TorqueModifier","TorqueModifier2","TorqueModifier3","Price"
],
    "Lightweight": ["Part","Car","Stage","YawEffect","WeightEffect","Price"
],
    "LSD": ["Part","Car","Stage","DiffTypeFront","DefaultInitialFront","MinInitialFront","MaxInitialFront","DefaultAccelFront","MinAccelFront","MaxAccelFront","DefaultDecelFront","MinDecelFront","MaxDecelFront","DiffTypeRear","DefaultInitialRear","MinInitialRear","MaxInitialRear","DefaultAccelRear","MinAccelRear","MaxAccelRear","DefaultDecelRear","MinDecelRear","MaxDecelRear","Price"
],
    "Muffler": ["Part","Car","Stage","TorqueModifier","TorqueModifier2","TorqueModifier3","Price"
],
    "NATune": ["Part","Car","Stage","Unknown","RevIncrease","PowerIncreaseMaybe","PowerIncrease","Unknown2","Unknown3","Unknown4","Unknown5","Unknown6","Unknown7","Price"
],
    "PortPolish": ["Part","Car","Stage","TorqueModifier","TorqueModifier2","TorqueModifier3","Price"
],
    "PropellerShaft": ["Part","Car","Stage","EngineBraking","IWheelF","IWheelR","IPropF","IPropR","Unknown1","Unknown2","Price"
],
    "RacingModify": ["Part","Car","Stage","FrontDownforceMin","FrontDownforceMax","FrontDownforceDefault","PriceMaybe","Filename","Unknown1","Unknown2","Unknown3","Unknown4","Unknown5","Unknown6","Unknown7","Unknown8","Unknown9","Unknown10","Unknown11","Unknown12","Unknown13","Unknown14","Unknown15","Unknown16","Unknown17","FrontTrack","RearTrack","Width","Unknown18","RearDownforceMin","RearDownforceMax","RearDownforceDefault","Unknown19","Unknown20","Unknown21","Unknown22","Unknown23","Unknown24","Unknown25","Unknown26","Unknown27","Unknown28","Unknown29","Unknown30"
],
    "RearTire": ["Part","Car","Stage","Price","Size","Compound1","Compound2","Compound3","Compound4","ForceVol1","ForceVol2","ForceVol3","ForceVol4"
],
    "Regulations": ["Regulations","EligibleCars"
],
    "Strings": [],
    "Suspension": ["Part","Car","Stage","MinCamberFront","MaxCamberFront","DefaultCamberFront","MinCamberRear","MaxCamberRear","DefaultCamberRear","MinToeFront","MaxToeFront","DefaultToeFront","MinToeRear","MaxToeRear","DefaultToeRear","Unknown1","Unknown2","Unknown3","Unknown4","MinSpringRateFront","MaxSpringRateFront","DefaultSpringRateFront","MinSpringRateRear","MaxSpringRateRear","DefaultSpringRateRear","FrontLeverRatioDefault","RearLeverRatioDefault","Unknown5","Unknown6","FrontDamperBoundSteps","FrontDamperBoundMinValue","FrontDamperBoundMaxValue","FrontDamperBoundDefaultStep","FrontDamperUnknown1MinValue","FrontDamperUnknown1MaxValue","FrontDamperUnknown1DefaultStep","FrontDamperReboundSteps","FrontDamperReboundMinValue","FrontDamperReboundMaxValue","FrontDamperReboundDefaultStep","FrontDamperUnknown2MinValue","FrontDamperUnknown2MaxValue","FrontDamperUnknown2DefaultStep","RearDamperBoundSteps","RearDamperBoundMinValue","RearDamperBoundMaxValue","RearDamperBoundDefaultStep","RearDamperUnknown1MinValue","RearDamperUnknown1MaxValue","RearDamperUnknown1DefaultStep","RearDamperReboundSteps","RearDamperReboundMinValue","RearDamperReboundMaxValue","RearDamperReboundDefaultStep","RearDamperUnknown2MinValue","RearDamperUnknown2MaxValue","RearDamperUnknown2DefaultStep","FrontStabiliserSteps","FrontStabiliserMinValue","FrontStabiliserMaxValue","FrontStabiliserDefaultStep","RearStabiliserSteps","RearStabiliserMinValue","RearStabiliserMaxValue","RearStabiliserDefaultStep","Unknown7","MinHeightFront","MaxHeightFront","DefaultHeightFront","MinHeightRear","MaxHeightRear","DefaultHeightRear","Unknown8","Unknown9","Unknown10","Unknown11","FrontCamberGripX1","FrontCamberGripX2","FrontCamberGripX3","FrontCamberGripX4","FrontCamberGripY1","FrontCamberGripY2","FrontCamberGripY3","FrontCamberGripY4","RearCamberGripX1","RearCamberGripX2","RearCamberGripX3","RearCamberGripX4","RearCamberGripY1","RearCamberGripY2","RearCamberGripY3","RearCamberGripY4","FrontDamperV1Bound","FrontDamperV2Bound","FrontDamperV1Rebound","FrontDamperV2Rebound","RearDamperV1Bound","RearDamperV2Bound","RearDamperV1Rebound","RearDamperV2Rebound","Unknown12","Unknown13","Unknown14","Unknown15","Price"
],
    "TireSize": ["Part","DiameterInches","Profile","WidthMM"
],
    "TurbineKit": ["Part","Car","Stage","Unknown","TurboLag","Unknown2","Unknown3","TurboLagMaybe","TurboLagMaybe2","TurboLagMaybe3","Unknown4","Unknown5","Unknown6","PowerIncreaseMaybe","PowerIncrease","Unknown7","Unknown8","Unknown9","Unknown10","Unknown11","Unknown12","Price"
],
    "Wheels": ["Wheel","Unknown","Filename"
]
}



class CSVGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TXT-2-CSV 3")
        self.root.geometry("350x450")


        tk.Label(root, text="Select Tab:").pack(pady=5)
        self.tab_var = tk.StringVar()
        self.tab_dropdown = ttk.Combobox(root, textvariable=self.tab_var, values=list(headers.keys()))
        self.tab_dropdown.pack(pady=5)
        self.tab_dropdown.bind("<<ComboboxSelected>>", self.update_input_fields)


        self.input_frame = tk.Frame(root)
        self.input_frame.pack(fill="both", expand=True, padx=5, pady=5)


        self.canvas = tk.Canvas(self.input_frame)
        self.scrollbar = tk.Scrollbar(self.input_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")


        self.entries = {}


        tk.Button(root, text="Generate CSV", command=self.on_generate_csv).pack(pady=10)
        tk.Button(root, text="Import CSV", command=self.import_csv).pack(pady=5)

        self.status_label = tk.Label(root, text="", wraplength=500)
        self.status_label.pack(pady=5)

    from tkinter import filedialog

    def import_csv(self):
        selected_tab = self.tab_var.get()
        if not selected_tab:
            messagebox.showwarning("No Tab Selected", "Please select a tab before importing.")
            return

        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not filepath:
            return  # Cancelled

        try:
            with open(filepath, newline='') as file:
                reader = csv.reader(file)
                rows = list(reader)
                if len(rows) < 2:
                    messagebox.showerror("Invalid CSV", "CSV must have at least two rows (header + data).")
                    return

                # Use second row as data (first row is header)
                data_row = rows[1]
                expected_headers = headers[selected_tab]

                for idx, header in enumerate(expected_headers):
                    if idx < len(data_row):
                        entry_widget = self.entries.get(header)
                        if entry_widget:
                            entry_widget.delete(0, tk.END)
                            value = data_row[idx]
                            #value = value.replace(".csv", "")
                            #value = os.path.basename(value)

                            entry_widget.insert(0, value)

                self.status_label.config(text=f"Data loaded from '{filepath}'")

        except Exception as e:
            messagebox.showerror("Import Failed", f"Failed to import CSV: {e}")

    def update_input_fields(self, event=None):

        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.entries.clear()


        selected_tab = self.tab_var.get()
        if not selected_tab:
            return


        for header in headers[selected_tab]:
            frame = tk.Frame(self.scrollable_frame)
            frame.pack(fill="x", expand=True, pady=2)

            tk.Label(frame, text=header, width=20, anchor="w").pack(side="left")
            entry = tk.Entry(frame, width=40)  # Increase width as needed
            entry.pack(side="left", padx=5)

            self.entries[header] = entry

    def generate_csv(self, selected_tab, expected_headers, data):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Save CSV As"
        )

        if not file_path:
            return False, "Save operation cancelled."

        try:
            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(expected_headers)
                writer.writerow([data.get(header, "") for header in expected_headers])
            return True, f"CSV saved as '{file_path}'"
        except Exception as e:
            return False, f"Error saving CSV: {e}"

    def on_generate_csv(self):
        selected_tab = self.tab_var.get()
        if not selected_tab:
            messagebox.showwarning("No Tab Selected", "Please select a tab.")
            return

        data = {header: entry.get() for header, entry in self.entries.items()}
        success, message = self.generate_csv(selected_tab, headers[selected_tab], data)
        self.status_label.config(text=message)


if __name__ == "__main__":
    root = tk.Tk()
    app = CSVGeneratorApp(root)
    root.mainloop()