create_project -force -part ${PART} io_plan_for_${PART} io_plan_for_${PART}
set_property design_mode PinPlanning [current_fileset]
open_io_design -name io_design_${PART}
