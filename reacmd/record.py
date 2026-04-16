################################################################################
"""
ReaCmd - Reaper Command-Line Utilities.
"""
################################################################################

import reapy


def entrypoint():
    """Start the Recording Operation for the Active Project."""
    project = reapy.Project()
    if project.is_recording:
        project.current_surface_stop()
    else:
        project.current_surface_record()
