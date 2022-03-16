from osparc_control import (
    ControlInterface,
    CommandManifest,
    CommandParameter,
    CommnadType,
)


command_add = CommandManifest(
    action="add_internal_time",
    description="adds internal time to a provided paramter",
    params=[
        CommandParameter(name="a", description="param to add to internal time"),
    ],
    command_type=CommnadType.WITH_DELAYED_REPLY,
)

command_get_time = CommandManifest(
    action="get_time",
    description="gets the time",
    params=[],
    command_type=CommnadType.WITH_IMMEDIATE_REPLY,
)

command_print_solver_status = CommandManifest(
    action="print_status",
    description="prints the status of the solver",
    params=[],
    command_type=CommnadType.WITHOUT_REPLY,
)


control_interface = ControlInterface(
    remote_host="localhost",
    exposed_interface=[command_add, command_get_time, command_print_solver_status],
    remote_port=1235,
    listen_port=1234,
)
