import streamlit as st
import pandas as pd
import io

st.title("TCB Design Info Generator")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    # Read Excel sheets
    design_info_df = pd.read_excel(uploaded_file, sheet_name="Design Info", header=None, engine="openpyxl")
    tcb_df = pd.read_excel(uploaded_file, sheet_name="TCB Definitions", engine="openpyxl")

    # Extract signal names and slice types
    signals = tcb_df[['TCB signal name', 'Slice type']].copy()
    signals.columns = ['Signal', 'Slice']

    # Generate DESIGN DESCRIPTION section
    design_lines = [
        "#" * 50,
        "DESIGN DESCRIPTION",
        "#" * 50,
        ""
    ]
    for _, row in design_info_df.iterrows():
        key = str(row[0]).strip()
        value = str(row[1]).strip()
        design_lines.append(f"{key:<30}: {value}")
    design_lines.append("")
    design_lines.append("TCB DESCRIPTION")

    # Generate SIGNAL section
    signal_lines = [
        "#" * 90,
        "# Test Signal Slice Type ScanFF",
        "#" * 90,
        "",
        "#General scan control"
    ]
    for idx, row in signals.iterrows():
        signal = str(row['Signal']).strip()
        slice_type = str(row['Slice']).strip()
        if slice_type == '-' or pd.isna(slice_type):
            slice_type = ' -'
        signal_lines.append(f"{signal:<42}{slice_type:<18}- #{idx+1}")

    signal_lines += [
        "",
        "#" * 90,
        "TESTMODE DESCRIPTION",
        "-" * 90,
        "# Test Mode Type Test Signal Values #",
        "-" * 90
    ]

    # Define test mode types
    test_mode_types = {
        'application': 'APPLICATION',
        'initial': 'INIT',
        'capture_tcb': 'USER_TEST'
    }
    default_type = 'USER_TEST'

    # Generate test mode lines
    test_modes = tcb_df.columns[2:]
    for mode in test_modes:
        mode_values = tcb_df[mode].astype(str).str.strip().tolist()
        bitstring = ''.join(mode_values)
        mode_type = test_mode_types.get(mode, default_type)
        signal_lines.append(f"{mode:<40}{mode_type:<15}\\\"{bitstring}\\\"")

    # Combine all sections
    output_lines = design_lines + signal_lines
    output_text = "\n".join(output_lines)

    # Display output
    st.text_area("Generated Output", output_text, height=400)

    # Download button
    st.download_button(
        label="Download Output File",
        data=output_text,
        file_name="generated_timnet_with_design.txt",
        mime="text/plain"
    )
