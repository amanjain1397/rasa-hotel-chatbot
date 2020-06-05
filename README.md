# rasa-hotel-chatbot
A simple chatbot using Rasa.

# About
The chatbot responds to and handle the following basic functionalities
- Book room
- Request Room Cleaning
- Handle FAQs
- Handle Greetings

# Requirements
`python 3.6.8` is used for this project and use a fresh virtual environment for installing all dependencies.
```bash
(venv)  pip install -r requirements.txt
```

# Usage
Train the chatbot
```bash
rasa train
```
Run actions.py in another terminal and keep it running
```bash
rasa run actions
```
Use the chatbot after training as
```bash
rasa shell
```

# Use-cases

## Book Room

**User**: I want to book a room.

**Bot**: Select the number of rooms you want to book
- Button 1 - 1 
- Button 2 - 2

**User**: (Clicks on Button 2)

**Bot**: Select from one of the room types
- Button 1 - Simple 
- Button 2 - Deluxe

**User**: (Clicks on Button 1)

**Bot**: Your room(s) have been booked. Number of Simple rooms booked : 2

(Clicking on button 2 is handled similarly)

## Clean room

### Schedule cleaning right away -

**User**: I want to have my room cleaned

**Bot**: When do you want to clean your room?

**User**: Could you send someone right now?

**Bot**: Someone is being sent to your room ASAP!

### Schedule cleaning using relative time -

**User**: I want to have my room cleaned

**Bot**: When do you want to clean your room?

**User**: Could you send someone after 2 hours?

**Bot**: Someone will be sent at your required time!

The above two flows are the only multi-step flows. The flows adapt themselves according to the user input. For eg., if the user says "I want to book a room for 2 people", the bot does not ask "How many rooms would you like to book?".

## FAQs

### Check-in timings -
**User**: What are your check-in timings?

**Bot**: Check-in time starts at 4 PM. Minimum check-in age is 21. Please contact the reception for early check-in requests.

### Check-out timings -
**User**: What are your check-out timings?

**Bot**: Check-out time is 11 AM. Please contact the reception for late checkout requests.

### Cancel Reservation -
**User**: How do I cancel a reservation?

**Bot**: To cancel a reservation, select the “Reservations” link from the homepage.

### Cancellation Policy -
**User**: What is your cancellation policy?

**Bot**: The booking deposit is refundable if the cancellation occurs at least 15 days before arrival. For cancellations made after this limit, a penalty will be imposed based on the cancellation policy.

### Restaurant -
**User**: Does the hotel have a restaurant?

**Bot**: Yes, the hotel has a restaurant called the Zephyr Bar. With our menu we strive to reflect the historic art and the spirit of our neighborhood by offering a glimpse into what makes our area unique.

### Breakfast Availability -
**User**: Does the hotel offer breakfast?

**Bot**: The hotel provides its guests with a free made-to-order breakfast each morning.

### Breakfast timings -
**User**: What are the breakfast timings?

**Bot**: Monday through Friday breakfast is 6 am to 9 am. On Saturday and Sunday, we are open from 7 am to 10:30 am.

### Restaurant timings -
**User**: What are the timings of your restaurant?

**Bot**: Our restaurant serves a dazzling 24-hour menu.

## Extra functionality
The flows are divided into two parts - **multi-step pre-defined flows**, and **FAQs**. I have added support to ask any number of FAQs in the middle of pre-defined flows.

For a small example -

**User**: I want to book a room.

**Bot**: Select the number of rooms you want to book
- Button 1 - 1 
- Button 2 - 2

**User**: What are your check-in timings?

**Bot**: Check-in time starts at 4 PM. Minimum check-in age is 21. Please contact the reception for early check-in requests.

**Bot**: Select the number of rooms you want to book
- Button 1 - 1 
- Button 2 - 2

**User**: What are your check-out timings?

**Bot**: Check-out time is 11 AM. Please contact the reception for late checkout requests.

**Bot**: Select the number of rooms you want to book
- Button 1 - 1 
- Button 2 - 2

**User**: (Clicks on Button 1)

**Bot**: Select from one of the room types
- Button 1 - Simple 
- Button 2 - Deluxe

**User**: (Clicks on Button 2)

**Bot**: Your room(s) have been booked. Number of Deluxe rooms booked : 1

# More information
Learn more about Rasa [here](https://rasa.com/docs/rasa/user-guide/rasa-tutorial/).

Watch Rasa Masterclass videos [here](https://www.youtube.com/playlist?list=PL75e0qA87dlHQny7z43NduZHPo6qd-cRc).
