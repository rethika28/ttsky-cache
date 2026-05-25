import os

print("===================================")
print(" TinyTapeout Cache Memory Test ")
print("===================================")

#-----------------------------------
# Compile Verilog Files
#-----------------------------------

compile_cmd = "iverilog -o cache_sim tt_um_example.v tb.v"

print("\nCompiling Verilog Files...\n")

compile_status = os.system(compile_cmd)

if compile_status != 0:
    print("Compilation Failed!")
    exit()

print("Compilation Successful!")

#-----------------------------------
# Run Simulation
#-----------------------------------

run_cmd = "vvp cache_sim"

print("\nRunning Simulation...\n")

run_status = os.system(run_cmd)

if run_status != 0:
    print("Simulation Failed!")
    exit()

print("\nSimulation Completed Successfully!")

#-----------------------------------
# Open Waveform
#-----------------------------------

print("\nOpening GTKWave...\n")

os.system("gtkwave cache.vcd &")
