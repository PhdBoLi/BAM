irun \
-cdslib ../../../cds.lib \
-hdlvar ../../../hdl.var \
-UNBUFFERED -status -errormax 50 -v93 \
-incdir /home/ic/Project \
-modelincdir /home/ic/Project  \
-timescale 1ns/1ns -vtimescale 1ns/1ns \
-discipline logic -delay_mode None -novitalaccl \
-spectre_args +aps +turbo +mt=4 ./amsControlSpectre.scs \
-simcompatible_ams spectre -ncsimargs "+amsrawdir ../psf" \
-input ./inputprobe.tcl \
-run \
./Generated.vams -top Top_Recall_Only \
-amspartinfo ../psf/partition.info \
-amsformat psfxl_all
cd ../psf
#simvision&

