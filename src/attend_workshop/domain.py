from typing import Callable
from datetime import datetime
class Declined:
    pass

def pipeIfTrue(results: list[bool]):
    for result in results:
        if not result:
            return False
    return True

class AttendeeAssignedToWorkshop:
    def __init__(self, workshop, attendee_workshop, discord_id):
        self.workshop = workshop
        self.attendee_workshop = attendee_workshop
        self.discord_id = discord_id

def assign_attendee_to_workshop(workshop, attendee_workshop, discord_id):
    limits = workshop.limits
     # This is the domain logic
    verified = pipeIfTrue([
        check_if_workshop_is_open(workshop),
        check_if_workshop_has_not_exceeded_limits(limits, len(attendee_workshop)),
        check_if_attendee_has_not_already_attended(attendee_workshop, discord_id)
        ])
    if not verified:
        return Declined()
    return AttendeeAssignedToWorkshop(workshop, attendee_workshop, discord_id)
    


class Workshop:
    limits: int

class AttendeeWorkshop:
    attendees: list[str]


def check_if_workshop_is_open(workshop): return workshop.open_at < datetime.today()


def check_if_attendee_has_not_already_attended(attendee_workshop, discord_id): return discord_id not in [aw.attendees for aw in attendee_workshop]
    


def check_if_workshop_has_not_exceeded_limits(workshop, attendee_workshop_len): return attendee_workshop_len >= workshop.limits
