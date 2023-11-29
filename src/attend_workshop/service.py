from src.attend_workshop.domain import (
    Workshop,
    AttendeeWorkshop,
    check_if_workshop_is_open,
    check_if_attendee_has_not_already_attended,
    check_if_workshop_has_not_exceeded_limits,
    assign_attendee_to_workshop)
from src.core.event_handler import evolve


def assign_attendee(attend_workshop: AttendWorkshop, workshopProvider, attendeeWorkshopProvider):
    # Need data
    workshop: Workshop = workshopProvider.getById(attend_workshop.workshop_id)
    attendee_workshop: AttendeeWorkshop = attendeeWorkshopProvider.findByWorkshop()


    event = assign_attendee_to_workshop(
        workshop, attendee_workshop, attend_workshop.discord_id)
    ticket = evolve(event)
