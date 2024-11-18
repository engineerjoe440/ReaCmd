################################################################################
"""
ReaCmd - Reaper Command-Line Utilities.
"""
################################################################################

import reapy


def entrypoint():
    """Start the Recording Operation for the Active Project."""
    project = reapy.Project()
    project.record()
