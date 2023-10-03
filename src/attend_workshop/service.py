from src.attend_workshop.domain import (
    check_if_attendee_is_signed_up,
    Workshop,
    AttendeeWorkshop,
    check_if_workshop_is_open,
    check_if_attendee_has_already_attended,
    check_if_workshop_has_exceeded_limits,
    assign_attendee_to_workshop)
from src.attend_workshop.router import AttendWorkshop
from src.core.event_handler import event_handler


def assign_attendee(attend_workshop: AttendWorkshop):
    check_if_attendee_is_signed_up(attend_workshop.discord_id)
    workshop = Workshop(attend_workshop.workshop_id)
    attendee_workshop = AttendeeWorkshop()
    check_if_workshop_is_open(workshop)
    check_if_attendee_has_already_attended(attend_workshop.discord_id)
    check_if_workshop_has_exceeded_limits(workshop, attendee_workshop)
    event = assign_attendee_to_workshop(
        attend_workshop.workshop_id, attend_workshop.discord_id)
    ticket = event_handler(event)
