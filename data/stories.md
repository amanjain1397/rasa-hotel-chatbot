## book room affirm path --> asks the user for number of rooms and its type (simple or deluxe) 
* greet
  - utter_greet
* book_room{"location":"room"}
  - form_book_room
  - form{"name": "form_book_room"}
  - form{"name": null}
  - action_reset_slots
  - utter_is_that_all
* affirm
  - utter_goodbye

## book room deny path --> asks the user for number of rooms and its type (simple or deluxe)
* greet
  - utter_greet
* book_room{"location":"room"}
  - form_book_room
  - form{"name": "form_book_room"}
  - form{"name": null}
  - action_reset_slots
  - utter_is_that_all
* deny
  - utter_deny_message

## book number room path affirm 1 --> asks the user for type of room given that the number of rooms stated by user = 1
* greet
  - utter_greet
* book_number_room{"location":"room", "number":"1"}
  - slot{"number": "1"}
  - form_book_room_number
  - form{"name": "form_book_room_number"}
  - form{"name": null}
  - action_reset_slots
  - utter_is_that_all
* affirm
  - utter_goodbye

## book number room path deny 1 --> asks the user for type of room given that the number of rooms stated by user = 1
* greet
  - utter_greet
* book_number_room{"location":"room", "number":"1"}
  - slot{"number": "1"}
  - form_book_room_number
  - form{"name": "form_book_room_number"}
  - form{"name": null}
  - action_reset_slots
  - utter_is_that_all
* deny
  - utter_deny_message

## book number room path affirm 2 --> asks the user for type of room given that the number of rooms stated by user = 2
* greet
  - utter_greet
* book_number_room{"location":"room", "number":"2"}
  - slot{"number": "2"}
  - form_book_room_number
  - form{"name": "form_book_room_number"}
  - form{"name": null}
  - action_reset_slots
  - utter_is_that_all
* affirm
  - utter_goodbye

## book number room path deny 2 --> asks the user for type of room given that the number of rooms stated by user = 2
* greet
  - utter_greet
* book_number_room{"location":"room", "number":"2"}
  - slot{"number": "2"}
  - form_book_room_number
  - form{"name": "form_book_room_number"}
  - form{"name": null}
  - action_reset_slots
  - utter_is_that_all
* deny
  - utter_deny_message

## clean room now path affirm
* greet
  - utter_greet
* clean_room{"location":"room"}
  - utter_clean_room
* clean_room_now
  - utter_clean_room_now
  - utter_is_that_all
* affirm
  - utter_goodbye

## clean room now path deny
* greet
  - utter_greet
* clean_room{"location":"room"}
  - utter_clean_room
* clean_room_now
  - utter_clean_room_now
  - utter_is_that_all
* deny
  - utter_deny_message

## clean room relative path affirm
* greet
  - utter_greet
* clean_room{"location":"room"}
  - utter_clean_room
* clean_room_relative
  - utter_clean_room_relative
  - utter_is_that_all
* affirm
  - utter_goodbye

## clean room relative path deny
* greet
  - utter_greet
* clean_room{"location":"room"}
  - utter_clean_room
* clean_room_relative
  - utter_clean_room_relative
  - utter_is_that_all
* deny
  - utter_deny_message

## faq check in time affirm
* greet
  - utter_greet
* faq_check_in_time
  - utter_check_in_time
  - utter_is_that_all
* affirm
  - utter_goodbye

## faq check in time deny
* greet
  - utter_greet
* faq_check_in_time
  - utter_check_in_time
  - utter_is_that_all
* deny
  - utter_deny_message

## faq check out time affirm
* greet
  - utter_greet
* faq_check_out_time
  - utter_check_out_time
  - utter_is_that_all
* affirm
  - utter_goodbye

## faq check out time deny
* greet
  - utter_greet
* faq_check_out_time
  - utter_check_out_time
  - utter_is_that_all
* deny
  - utter_deny_message

## faq cancel reservation affirm
* greet
  - utter_greet
* faq_cancel_reservation
  - utter_cancel_reservation
  - utter_is_that_all
* affirm
  - utter_goodbye

## faq cancel reservation deny
* greet
  - utter_greet
* faq_cancel_reservation
  - utter_cancel_reservation
  - utter_is_that_all
* deny
  - utter_deny_message

## faq cancellation policy affirm
* greet
  - utter_greet
* faq_cancellation_policy
  - utter_cancellation_policy
  - utter_is_that_all
* affirm
  - utter_goodbye

## faq cancellation policy deny
* greet
  - utter_greet
* faq_cancellation_policy
  - utter_cancellation_policy
  - utter_is_that_all
* deny
  - utter_deny_message

## faq have restaurant path affirm
* greet
  - utter_greet
* faq_have_restaurant{"location": "restaurant"} 
  - utter_have_restaurant
  - utter_is_that_all
* affirm
  - utter_goodbye

## faq have restaurant path deny
* greet
  - utter_greet
* faq_have_restaurant{"location": "restaurant"} 
  - utter_have_restaurant
  - utter_is_that_all
* deny
  - utter_deny_message

## faq breakfast availability affirm
* greet
  - utter_greet
* faq_breakfast_avail
  - utter_breakfast_avail
  - utter_is_that_all
* affirm
  - utter_goodbye

## faq breakfast availability deny
* greet
  - utter_greet
* faq_breakfast_avail
  - utter_breakfast_avail
  - utter_is_that_all
* deny
  - utter_deny_message

## faq breakfast time affirm
* greet
  - utter_greet
* faq_breakfast_time
  - utter_breakfast_time
  - utter_is_that_all
* affirm
  - utter_goodbye

## faq breakfast time deny
* greet
  - utter_greet
* faq_breakfast_time
  - utter_breakfast_time
  - utter_is_that_all
* deny
  - utter_deny_message

## faq restaurant time path affirm
* greet
  - utter_greet
* faq_restaurant_time{"location": "restaurant"}
  - utter_restaurant_time
  - utter_is_that_all
* affirm
  - utter_goodbye

## faq restaurant time path deny
* greet
  - utter_greet
* faq_restaurant_time{"location": "restaurant"}
  - utter_restaurant_time
  - utter_is_that_all
* deny
  - utter_deny_message