"""
    Create RequestStatus module to keep the 
    track of the request status.
    Steps:
    1. There must be different levels/stages of the request status.
    2. Collect all the error warninings appering within the request cycle.
    3. Generate the report of the error, warrnings appeared in request cycle.
    4. Store the status of each cycle of the request cycle.
"""

from dataclasses import dataclass

@dataclass
class RequestStatus(object):
    pass