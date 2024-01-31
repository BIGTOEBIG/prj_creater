# set PART "xcku035-ffva1156-3-e"
# set PART "xcku15p-ffve1760-3-e"
# set PART "xcvu9p-fsgd2104-2L-e"
# set PART "xcvu19p-fsva3824-2-e"
set PART "xcvu37p-fsvh2892-2L-e"
create_project -force -part ${PART} io_plan_for_${PART} io_plan_for_${PART}
set_property design_mode PinPlanning [current_fileset]
open_io_design -name io_1
