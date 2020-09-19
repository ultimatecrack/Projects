## Greet
* greet
  - utter_greet

## Thanks
* thanks
    - utter_noworries

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## covid report
* covid_report
  - action_covid_report

## Some question from FAQ
* faq
  - respond_faq

## Corona self assessment
* self_assessment
    - self_assessment_form
    - form{"name": "self_assessment_form"}
    - form{"name": null}

## New Story

    - utter_greet
* greet
* faq
    - action_default_fallback
* out_of_scope
* thanks
    - utter_noworries
* faq
    - respond_faq
* greet
    - utter_greet
* faq
    - respond_faq
* covid_report{"place":"pune"}
    - action_covid_report
* covid_report{"place":"pune"}
    - action_covid_report
* covid_report{"place":"new delhi"}
    - action_covid_report
* faq
    - respond_faq
* faq
    - respond_faq
* self_assessment
    - self_assessment_form
    - form{"name":"self_assessment_form"}
    - slot{"requested_slot":"fever"}
* deny
    - self_assessment_form
    - slot{"fever":false}
* deny
    - self_assessment_form
    - slot{"dry_cough":false}
* affirm
    - self_assessment_form
    - slot{"tiredness":true}
* affirm
    - self_assessment_form
    - slot{"aches_and_pains":true}
* deny
    - self_assessment_form
    - slot{"sore_throat":false}
* deny
    - self_assessment_form
    - slot{"diarrhoea":false}
* deny
    - self_assessment_form
    - slot{"conjunctivitis":false}
* deny
    - self_assessment_form
    - slot{"headache":false}
* affirm
    - self_assessment_form
    - slot{"loss_of_taste_or_smell":true}
* deny
    - self_assessment_form
    - slot{"rash_or_discolouration":false}
* deny
    - self_assessment_form
    - slot{"difficulties":false}
* deny
    - self_assessment_form
    - slot{"chest_pain_or_pressure":false}

## New Story

* greet
    - utter_greet
* covid_report{"place":"uttarakhand"}
    - action_covid_report
* covid_report{"place":"uttarakhand"}
    - action_covid_report
* covid_report{"place":"uttarakhand"}
    - action_covid_report
* covid_report{"place":"dehradun"}
    - action_covid_report

## New Story

* covid_report
    - action_covid_report
* covid_report
    - action_covid_report

## New Story

* greet
    - utter_greet
* covid_report{"place":"jaunpur"}
    - action_covid_report
* covid_report{"place":"jaunpur"}
    - action_covid_report
* faq
    - respond_faq
* bot_challenge
    - utter_iamabot
* faq
    - respond_faq
* faq
    - respond_faq
* faq
    - respond_faq
* self_assessment
    - self_assessment_form
    - form{"name":"self_assessment_form"}
    - slot{"requested_slot":"fever"}
* affirm
    - self_assessment_form
    - slot{"fever":true}
* affirm
    - self_assessment_form
    - slot{"dry_cough":true}
* deny
    - self_assessment_form
    - slot{"tiredness":false}
* deny
    - self_assessment_form
    - slot{"aches_and_pains":false}
* affirm
    - self_assessment_form
* affirm
    - self_assessment_form
    - slot{"diarrhoea":true}
* affirm
    - self_assessment_form
    - slot{"conjunctivitis":true}
* deny
    - self_assessment_form
    - slot{"headache":false}
* affirm
    - self_assessment_form
* deny
    - self_assessment_form
    - slot{"rash_or_discolouration":false}
* deny
    - self_assessment_form
    - slot{"difficulties":false}
* affirm
    - self_assessment_form
    - slot{"chest_pain_or_pressure":true}
* deny
    - self_assessment_form
    - form{"name":null}
    - slot{"loss_of_speech_or_movement":false}
* thanks
    - utter_noworries

## New Story

* greet
    - utter_greet
* greet
    - utter_greet
* faq
    - respond_faq
* covid_report
    - action_covid_report
* covid_report{"GPE":"hyderabad"}
    - action_covid_report
* covid_report{"GPE":"hyderabad"}
    - action_covid_report
* covid_report{"GPE":"hyderabad"}
    - action_covid_report
* covid_report{"GPE":"hyderabad"}
    - action_covid_report
* covid_report{"GPE":"mumbai","place":"mumbai"}
    - action_covid_report
* covid_report{"place":"andhra pradesh"}
    - action_covid_report
* covid_report
    - action_covid_report
* covid_report{"GPE":"mumbai","place":"mumbai"}
    - action_covid_report
* faq{"DATE":"many 5 to 15 years"}
    - respond_faq
* faq
    - respond_faq
* self_assessment
    - self_assessment_form
* affirm
    - self_assessment_form
    - slot{"fever":true}
* affirm
    - self_assessment_form
    - slot{"dry_cough":true}
* affirm
    - self_assessment_form
    - slot{"tiredness":true}
* affirm
    - self_assessment_form
    - slot{"aches_and_pains":true}
* affirm
    - self_assessment_form
    - slot{"sore_throat":true}
* deny
    - self_assessment_form
    - slot{"diarrhoea":false}
* deny
    - self_assessment_form
    - slot{"conjunctivitis":false}
* affirm
    - self_assessment_form
    - slot{"headache":true}
* deny
    - self_assessment_form
* deny
    - self_assessment_form
    - slot{"rash_or_discolouration":false}
* affirm
    - self_assessment_form
    - slot{"difficulties":true}
* affirm
    - self_assessment_form
    - slot{"chest_pain_or_pressure":true}
* deny
    - self_assessment_form
    - form{"name":null}
    - slot{"loss_of_speech_or_movement":false}
* faq
    - respond_faq
* faq
    - respond_faq
* faq
    - respond_faq

## New Story

* greet
    - utter_greet
* faq
    - respond_faq
* faq
    - respond_faq
* faq
    - respond_faq
* faq
    - respond_faq
* faq
    - respond_faq
* faq
    - respond_faq
* faq
    - respond_faq
* out_of_scope
    - action_default_fallback
* covid_report{"GPE":"india"}
    - action_covid_report
* covid_report{"place":"maharashtra"}
    - action_covid_report
* covid_report{"place":"thane"}
    - action_covid_report
* faq
    - respond_faq
* faq{"ORDINAL":"first"}
    - respond_faq
