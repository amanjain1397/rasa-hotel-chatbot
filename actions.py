from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

def repeat(tracker, dispatcher):
    user_ignore_count = 2
    count = 0
    tracker_list = []

    while user_ignore_count > 0:
        event = tracker.events[count].get('event')
        if event == 'user':
            user_ignore_count = user_ignore_count - 1
        if event == 'bot':
            tracker_list.append(tracker.events[count])
        count = count - 1

    tracker_list.reverse()
    i = len(tracker_list) - 1

    while i >= 0:
        data = tracker_list[i].get('data')
        if data:
            if "buttons" in data:
                dispatcher.utter_message(text=tracker_list[i].get('text'), buttons=data["buttons"])
            else:
                dispatcher.utter_message(text=tracker_list[i].get('text'))
            break
        i -= 1

class BookRoomInfo(FormAction):
    def name(self) -> Text:
        return "form_book_room"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["number", "room_type"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        # utter submit template
        dispatcher.utter_message(template="utter_submit", number=tracker.get_slot('number'),
                                 room_type=tracker.get_slot('room_type'))
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "number": self.from_entity(entity="number", intent='num_rooms'),
            "room_type": self.from_entity(entity="room_type", intent="type_rooms")
        }

class BookRoomNumberInfo(FormAction):
    def name(self) -> Text:
        return "form_book_room_number"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["room_type"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        # utter submit template
        dispatcher.utter_message(template="utter_submit", 
                                room_type=tracker.get_slot('room_type'))
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "room_type": self.from_entity(entity="room_type", intent="type_rooms")
        }

class ResetSlots(Action):

    def name(self):
        return "action_reset_slots"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("number", None), SlotSet("room_type", None)]

class MyFallbackAction(Action):
    def name(self):
        return "action_my_fallback"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_fallback_message", tracker)
        # repeat(tracker, dispatcher)        
        return [UserUtteranceReverted()]

class ActionCheckInTime(Action):

    def name(self):
        return "action_check_in_time"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_check_in_time", tracker)
        repeat(tracker, dispatcher)        
        return [UserUtteranceReverted()]

class ActionCheckOutTime(Action):
    
    def name(self):
        return "action_check_out_time"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_check_out_time", tracker)
        repeat(tracker, dispatcher)
        return [UserUtteranceReverted()]
    
class ActionCancelReservation(Action):
    
    def name(self):
        return "action_cancel_reservation"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_cancel_reservation", tracker)
        repeat(tracker, dispatcher)
        return [UserUtteranceReverted()]

class ActionCancellationPolicy(Action):
    
    def name(self):
        return "action_cancellation_policy"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_cancellation_policy", tracker)
        repeat(tracker, dispatcher)
        return [UserUtteranceReverted()]

class ActionHaveRestaurant(Action):
    
    def name(self):
        return "action_have_restaurant"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_have_restaurant", tracker)
        repeat(tracker, dispatcher)
        return [UserUtteranceReverted()]

class ActionBreakfastAvail(Action):
    
    def name(self):
        return "action_breakfast_avail"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_breakfast_avail", tracker)
        repeat(tracker, dispatcher)
        return [UserUtteranceReverted()]
    
class ActionBreakfastTime(Action):
    
    def name(self):
        return "action_breakfast_time"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_breakfast_time", tracker)
        repeat(tracker, dispatcher)
        return [UserUtteranceReverted()]

class ActionRestaurantTime(Action):
    
    def name(self):
        return "action_restaurant_time"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_restaurant_time", tracker)
        repeat(tracker, dispatcher)
        return [UserUtteranceReverted()]