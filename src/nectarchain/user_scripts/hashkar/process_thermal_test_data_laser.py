import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from ctapipe.coordinates import EngineeringCameraFrame
from ctapipe.instrument import CameraGeometry
from ctapipe.visualization import CameraDisplay

################################################################
# OPTIONS ARE 2: PED/CHARGE/PEDSTD .... and 1:AVERAGE/STD  -> if 2:PEDSTD change name of files to _ped
name_entity2 = "Charge"
name_entity = "average"
# entity = "PED-INTEGRATION-PED-ALL-AVERAGE-HIGH-GAIN" #what i WANT TO STUDY
entity = "CHARGE-INTEGRATION-PED-ALL-AVERAGE-HIGH-GAIN"  # what i WANT TO STUDY

#          2                           1

intensity = [13, 15, 16.5, 18, 20, 22, 23.5, 25, 30, 35]
temperature = [15, 5, 0, -5]  # should be taken from logs

divide = [58, 58, 58, 58, 58, 58, 58, 58, 58, 58]
divide = np.array(divide)


deg15 = []
deg15std = []
deg5 = []
deg5std = []
deg0 = []
deg0std = []
deg_5 = []
deg_5std = []

temperature = [15, 5, 0, -5]

runs_neg5 = [3798, 3797, 3796, 3795, 3794, 3793, 3792, 3791, 3790, 3789]
runs_0 = [3764, 3763, 3762, 3761, 3760, 3759, 3758, 3757, 3756, 3755]
runs_5 = [3714, 3713, 3712, 3711, 3710, 3709, 3708, 3707, 3706, 3705]
runs_15 = [3630, 3631, 3629, 3628, 3627, 3626, 3625, 3624, 3622, 3623]

path = "./"

################################################


# open the figure
fig = plt.figure(figsize=(10, 10 / 1.61))
axis_font = {"fontname": "Arial", "size": "16"}

# Open the fits file
for i in runs_15:
    with fits.open("%sNectarCAM_Run%s_Results.fits" % (path, i)) as hdulist1:
        table_data1 = hdulist1["Camera"].data
        print(table_data1[entity][21:])
        charge_av = np.mean(table_data1[entity][21:])
        print(charge_av)
        charge_std = np.std(table_data1[entity][21:])
        deg15.append(charge_av)
        print(deg15)
        deg15std.append(charge_std)

plt.errorbar(
    intensity,
    deg15 / divide,
    yerr=np.array(deg15std / np.sqrt(len(table_data1[entity][21:]))),
    label="%s deg" % temperature[0],
)
# plt.errorbar(intensity, deg15/(divide), yerr = deg15std/(divide * np.sqrt(1855)))

for i in runs_5:
    with fits.open("%sNectarCAM_Run%s_Results.fits" % (path, i)) as hdulist1:
        table_data1 = hdulist1["Camera"].data
        charge_av = np.mean(table_data1[entity][21:])
        charge_std = np.std(table_data1[entity][21:])
        deg5.append(charge_av)
        deg5std.append(charge_std)

plt.errorbar(
    intensity,
    deg5 / divide,
    yerr=np.array(deg5std / np.sqrt(len(table_data1[entity][21:]))),
    label="%s deg" % temperature[1],
)
# plt.errorbar(intensity, deg5/(divide), yerr = deg5std/(divide* np.sqrt(1855)))

for i in runs_0:
    with fits.open("%sNectarCAM_Run%s_Results.fits" % (path, i)) as hdulist1:
        table_data1 = hdulist1["Camera"].data
        charge_av = np.mean(table_data1[entity][21:])
        charge_std = np.std(table_data1[entity][21:])
        deg0.append(charge_av)
        deg0std.append(charge_std)

plt.errorbar(
    intensity,
    deg0 / divide,
    yerr=np.array(deg0std / np.sqrt(len(table_data1[entity][21:]))),
    label="%s deg" % temperature[2],
)
# plt.errorbar(intensity, deg0/(divide), yerr = deg0std/(divide* np.sqrt(1855)))

for i in runs_neg5:
    with fits.open("%sNectarCAM_Run%s_Results.fits" % (path, i)) as hdulist1:
        table_data1 = hdulist1["Camera"].data
        charge_av = np.mean(table_data1[entity][21:])
        charge_std = np.std(table_data1[entity][21:])
        deg_5.append(charge_av)
        deg_5std.append(charge_std)

plt.errorbar(
    intensity,
    deg_5 / divide,
    yerr=np.array(deg_5std / np.sqrt(len(table_data1[entity][21:]))),
    label="%s deg" % temperature[3],
)
# plt.errorbar(intensity, deg_5/(divide), yerr = deg_5std/(divide* np.sqrt(1855)))


################################################################
plt.yscale("log")
plt.xlabel("Laser intensity (%)", **axis_font)
plt.ylabel("%s %s (p.e.)" % (name_entity2, name_entity), **axis_font)
plt.legend(prop={"size": 16})
plt.grid()
fig.savefig(
    "temp_%s_%s_all_intensity.png" % (name_entity2, name_entity),
    dpi=300,
    bbox_inches="tight",
)
plt.show()
############################################################################################################