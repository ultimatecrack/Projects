# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"



import logging
import json
import requests
from datetime import datetime
from typing import Any, Dict, List, Text, Union, Optional
# from rasa_core.policies.fallback import FallbackPolicy
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
)

class ActionCovidReport(Action):

    def __init__(self):
        self.response = requests.get('https://api.covid19india.org/state_district_wise.json').json()


    def name(self) -> Text:
        return "action_covid_report"



    def search_data(self, keyword):
        response = self.response
        for state in response:
            if state.lower() == keyword.lower():
                active = 0
                confirmed = 0
                deceased = 0
                recovered = 0
                for dist in response[state]:
                    for data in response[state][dist]:
                        try:
                            active += int(response[state][dist][data]['active'])
                            confirmed += int(response[state][dist][data]['confirmed'])
                            deceased += int(response[state][dist][data]['deceased'])
                            recovered += int(response[state][dist][data]['recovered'])
                        except:
                            continue
    #             print('Active :', active)
    #             print('Confirmed :', confirmed)
    #             print('Deceased :', deceased)
    #             print('Recovered :', recovered)
                covid_info = {'active': active, 'confirmed':confirmed, 'deceased':deceased, 'recovered':recovered, 'state': state, 'place_type': 'state', 'dist': 'All'}
                return covid_info
        for state in response:
            for dist in response[state]['districtData']:
                if dist.lower() == keyword.lower():
                    response[state]['districtData'][dist]['dist'] = dist
                    response[state]['districtData'][dist]['state'] = state
                    response[state]['districtData'][dist]['place_type'] = 'dist'
                    return response[state]['districtData'][dist]
        return 'No record found !'




    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        covid_info = 'No record found !'
        for e in entities:
            if e['entity'] == 'place':
                place = e['value']
                covid_info = self.search_data(place)
        try:
            if type(covid_info) != str:
                message = '\nState : {},\nDist : {}, \nActive : {}, \nConfirmed: {}, \nDeceased {}, \nRecovered {}'.format(covid_info['state'], covid_info['dist'], covid_info['active'],covid_info['confirmed'],covid_info['deceased'], covid_info['recovered'])
            else:
                message = covid_info
        except:
            message = 'Something went wrong!'

        dispatcher.utter_message(text=message)
        
        return []


class ActionCovidSelfAssessment(FormAction):

    def __init__(self):
        self.most_common_symptoms = ['fever', 'dry cough', 'tiredness']
        self.less_common_symptoms = ['aches and pains', 'sore throat', 'diarrhoea', 'conjunctivitis', 'headache','loss of taste or smell', 'a rash on skin, or discolouration of fingers or toes']
        self.most_common_symptoms = ['difficulty breathing or shortness of breath', 'chest pain or pressure', 'loss of speech or movement']


    def name(self):
        return "self_assessment_form"

    @staticmethod
    def required_slots(tracker):
        return [
            'fever', 
            'dry_cough', 
            'tiredness', 
            'aches_and_pains', 
            'sore_throat', 
            'diarrhoea', 
            'conjunctivitis', 
            'headache',
            'loss_of_taste_or_smell', 
            'rash_or_discolouration', 
            'difficulties', 
            'chest_pain_or_pressure', 
            'loss_of_speech_or_movement'
        ]
    
    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message or a list of them, where a first 
        match will be picked"""
        return {
            "fever": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
                ],
            "dry_cough": 
            [self.from_intent(intent='affirm', value=True),self.from_intent(intent='deny',value=False)],
            "tiredness": 
            [self.from_intent(intent='affirm', value=True),self.from_intent(intent='deny',value=False)],
            "aches_and_pains": 
            [self.from_intent(intent='affirm', value=True),self.from_intent(intent='deny',value=False)],
            "sore_throat": 
            [self.from_intent(intent='affirm', value=True),self.from_intent(intent='deny',value=False)],
            "diarrhoea": 
            [self.from_intent(intent='affirm', value=True),self.from_intent(intent='deny',value=False)],
            "conjunctivitis": 
            [self.from_intent(intent='affirm', value=True),self.from_intent(intent='deny',value=False)],
            "headache": 
            [self.from_intent(intent='affirm', value=True),self.from_intent(intent='deny',value=False)],
            "loss_of_taste_or_smell": 
            [self.from_intent(intent='affirm', value=True),self.from_intent(intent='deny',value=False)],
            "rash_or_discolouration": 
            [self.from_intent(intent='affirm', value=True),self.from_intent(intent='deny',value=False)],
            "difficulties": 
            [self.from_intent(intent='affirm', value=True),self.from_intent(intent='deny',value=False)],
            "chest_pain_or_pressure": 
            [self.from_intent(intent='affirm', value=True),self.from_intent(intent='deny',value=False)],
            "loss_of_speech_or_movement": 
            [self.from_intent(intent='affirm', value=True),self.from_intent(intent='deny',value=False)]
            }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        ) -> List[Dict]:
        severity_measure = 0
        fever = tracker.get_slot("fever")
        dry_cough = tracker.get_slot("dry_cough")
        tiredness = tracker.get_slot("tiredness")
        aches_and_pains = tracker.get_slot("aches_and_pains")
        sore_throat = tracker.get_slot("sore_throat")
        diarrhoea = tracker.get_slot("diarrhoea")
        conjunctivitis = tracker.get_slot("conjunctivitis")
        headache = tracker.get_slot("headache")
        loss_of_taste_or_smell = tracker.get_slot("loss_of_taste_or_smell")
        rash_or_discolouration = tracker.get_slot("rash_or_discolouration")
        difficulties = tracker.get_slot("difficulties")
        chest_pain_or_pressure = tracker.get_slot("chest_pain_or_pressure")
        loss_of_speech_or_movement = tracker.get_slot("loss_of_speech_or_movement")

        if fever:
            severity_measure += 1
        if dry_cough:
            severity_measure += 1
        if tiredness:
            severity_measure += 1
        if aches_and_pains:
            severity_measure += 1
        if sore_throat:
            severity_measure += 1
        if diarrhoea:
            severity_measure += 1
        if conjunctivitis:
            severity_measure += 1
        if headache:
            severity_measure += 1
        if loss_of_taste_or_smell:
            severity_measure += 1
        if rash_or_discolouration:
            severity_measure += 1
        if difficulties:
            severity_measure += 10
        if chest_pain_or_pressure:
            severity_measure += 10
        if loss_of_speech_or_movement:
            severity_measure += 10


        if severity_measure == 0:
            severity = 'None'
            message = 'Great!, You are safe, but still follow the guidelines. Stay home and stay safe!'
        elif severity_measure >= 1 and severity_measure <= 3:
            severity = 'Minor'
            message = 'Do not worry, You can take home medication or visit your doctor to get well soon . Stay home and stay safe!'
        elif severity_measure >3 and severity_measure <=6:
            severity = 'Moderate'
            message = 'Do not worry, Stay separate and visit your doctor to get well soon. Stay home and stay safe!'
        elif severity_measure >6 and severity_measure <10:
            severity = 'Major'
            message = 'Do not worry you will get well soon, visit your doctor as soon as possible, stay under obervation, stay separate and follow doctors instruction'
        elif severity_measure >=10:
            severity = 'Critical'
            message = 'You need to be hospitalised right now. Please contact to hospital on emergency. Do not panic, you will get well soon!'

        final_message = 'Severity: {} \n{} '.format(severity, message)
        print(final_message)
        dispatcher.utter_message(final_message)
        return []


class ActionUtterFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"




    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        dispatcher.utter_message(template='utter_fallback')
        
        return []