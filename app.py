{
    "chunks": [
        {
            "type": "txt",
            "chunk_number": 1,
            "lines": [
                {
                    "line_number": 1,
                    "text": "import pandas as pd"
                },
                {
                    "line_number": 2,
                    "text": ""
                },
                {
                    "line_number": 3,
                    "text": "# Load the Excel file"
                },
                {
                    "line_number": 4,
                    "text": "excel_file = \"Example_input_TCB 4.xlsx\""
                },
                {
                    "line_number": 5,
                    "text": ""
                },
                {
                    "line_number": 6,
                    "text": "# Read the Design Info sheet"
                },
                {
                    "line_number": 7,
                    "text": "design_info_df = pd.read_excel(excel_file, sheet_name=\"Design Info\", header=None, engine=\"openpyxl\")"
                },
                {
                    "line_number": 8,
                    "text": ""
                },
                {
                    "line_number": 9,
                    "text": "# Read the TCB Definitions sheet"
                },
                {
                    "line_number": 10,
                    "text": "tcb_df = pd.read_excel(excel_file, sheet_name=\"TCB Definitions\", engine=\"openpyxl\")"
                },
                {
                    "line_number": 11,
                    "text": ""
                },
                {
                    "line_number": 12,
                    "text": "# Extract signal names and slice types"
                },
                {
                    "line_number": 13,
                    "text": "signals = tcb_df[['TCB signal name', 'Slice type']].copy()"
                },
                {
                    "line_number": 14,
                    "text": "signals.columns = ['Signal', 'Slice']"
                },
                {
                    "line_number": 15,
                    "text": ""
                },
                {
                    "line_number": 16,
                    "text": "# Generate the Design Info section"
                },
                {
                    "line_number": 17,
                    "text": "design_lines = []"
                },
                {
                    "line_number": 18,
                    "text": "design_lines.append(\"#################################################\")"
                },
                {
                    "line_number": 19,
                    "text": "design_lines.append(\"DESIGN DESCRIPTION\")"
                },
                {
                    "line_number": 20,
                    "text": "design_lines.append(\"#################################################\")"
                },
                {
                    "line_number": 21,
                    "text": "design_lines.append(\"\")"
                },
                {
                    "line_number": 22,
                    "text": ""
                },
                {
                    "line_number": 23,
                    "text": "for _, row in design_info_df.iterrows():"
                },
                {
                    "line_number": 24,
                    "text": "key = str(row[0]).strip()"
                },
                {
                    "line_number": 25,
                    "text": "value = str(row[1]).strip()"
                },
                {
                    "line_number": 26,
                    "text": "line = f\"{key:<30}: {value}\""
                },
                {
                    "line_number": 27,
                    "text": "design_lines.append(line)"
                },
                {
                    "line_number": 28,
                    "text": ""
                },
                {
                    "line_number": 29,
                    "text": "design_lines.append(\"\")"
                },
                {
                    "line_number": 30,
                    "text": "design_lines.append(\"\")"
                },
                {
                    "line_number": 31,
                    "text": "design_lines.append(\"TCB                             DESCRIPTION\")"
                },
                {
                    "line_number": 32,
                    "text": ""
                },
                {
                    "line_number": 33,
                    "text": "# Generate the signal section"
                },
                {
                    "line_number": 34,
                    "text": "signal_lines = []"
                },
                {
                    "line_number": 35,
                    "text": "signal_lines.append(\"####################################################################################################\")"
                },
                {
                    "line_number": 36,
                    "text": "signal_lines.append(\"# Test Signal                              Slice Type        ScanFF\")"
                },
                {
                    "line_number": 37,
                    "text": "signal_lines.append(\"####################################################################################################\")"
                },
                {
                    "line_number": 38,
                    "text": "signal_lines.append(\"\")"
                },
                {
                    "line_number": 39,
                    "text": "signal_lines.append(\"#General scan control\")"
                },
                {
                    "line_number": 40,
                    "text": ""
                },
                {
                    "line_number": 41,
                    "text": "for idx, row in signals.iterrows():"
                },
                {
                    "line_number": 42,
                    "text": "signal = str(row['Signal']).strip()"
                },
                {
                    "line_number": 43,
                    "text": "slice_type = str(row['Slice']).strip()"
                },
                {
                    "line_number": 44,
                    "text": "if slice_type == '-' or pd.isna(slice_type):"
                },
                {
                    "line_number": 45,
                    "text": "slice_type = '    -'"
                },
                {
                    "line_number": 46,
                    "text": "line = f\"{signal:<42}{slice_type:<18}-  #{idx+1}\""
                },
                {
                    "line_number": 47,
                    "text": "signal_lines.append(line)"
                },
                {
                    "line_number": 48,
                    "text": ""
                },
                {
                    "line_number": 49,
                    "text": "signal_lines.append(\"\")"
                },
                {
                    "line_number": 50,
                    "text": "signal_lines.append(\"####################################################################################################\")"
                },
                {
                    "line_number": 51,
                    "text": "signal_lines.append(\"TESTMODE                        DESCRIPTION\")"
                },
                {
                    "line_number": 52,
                    "text": "signal_lines.append(\"#----------------------------------------------------------------------------------------------------------\")"
                },
                {
                    "line_number": 53,
                    "text": "signal_lines.append(\"# Test Mode                                Type            Test Signal Values                             #\")"
                },
                {
                    "line_number": 54,
                    "text": "signal_lines.append(\"#----------------------------------------------------------------------------------------------------------\")"
                },
                {
                    "line_number": 55,
                    "text": ""
                },
                {
                    "line_number": 56,
                    "text": "# Define test mode types"
                },
                {
                    "line_number": 57,
                    "text": "test_mode_types = {"
                },
                {
                    "line_number": 58,
                    "text": "'application': 'APPLICATION',"
                },
                {
                    "line_number": 59,
                    "text": "'initial': 'INIT',"
                },
                {
                    "line_number": 60,
                    "text": "'capture_tcb': 'USER_TEST'"
                },
                {
                    "line_number": 61,
                    "text": "}"
                },
                {
                    "line_number": 62,
                    "text": "default_type = 'USER_TEST'"
                },
                {
                    "line_number": 63,
                    "text": ""
                },
                {
                    "line_number": 64,
                    "text": "# Generate test mode lines"
                },
                {
                    "line_number": 65,
                    "text": "test_modes = tcb_df.columns[2:]"
                },
                {
                    "line_number": 66,
                    "text": "for mode in test_modes:"
                },
                {
                    "line_number": 67,
                    "text": "mode_values = tcb_df[mode].astype(str).str.strip().tolist()"
                },
                {
                    "line_number": 68,
                    "text": "bitstring = ''.join(mode_values)"
                },
                {
                    "line_number": 69,
                    "text": "mode_type = test_mode_types.get(mode, default_type)"
                },
                {
                    "line_number": 70,
                    "text": "line = f\"{mode:<40}{mode_type:<15}\\\"{bitstring}\\\"\""
                },
                {
                    "line_number": 71,
                    "text": "signal_lines.append(line)"
                },
                {
                    "line_number": 72,
                    "text": ""
                },
                {
                    "line_number": 73,
                    "text": "# Combine all sections"
                },
                {
                    "line_number": 74,
                    "text": "output_lines = design_lines + signal_lines"
                },
                {
                    "line_number": 75,
                    "text": ""
                },
                {
                    "line_number": 76,
                    "text": "# Write to output file"
                },
                {
                    "line_number": 77,
                    "text": "with open(\"generated_timnet_with_design.txt\", \"w\") as f:"
                },
                {
                    "line_number": 78,
                    "text": "for line in output_lines:"
                },
                {
                    "line_number": 79,
                    "text": "f.write(line + \"\\n\")"
                }
            ],
            "token_count": 321
        }
    ]
}