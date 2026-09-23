import calc, sys
if calc.add(2, 3) != 5:
    sys.stderr.write("AER_DEFECT_OBSERVED\n")
    sys.exit(101)
sys.exit(0)
