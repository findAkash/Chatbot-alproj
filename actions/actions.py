# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted

from openai import OpenAI
import os


# profile picture sample
thoma: str = "https://rb.gy/9lhbl4"
bill: str = "https://rb.gy/ojbfte"
raisa: str = "https://rb.gy/oys1bg"

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)
def gpt3(text):
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )
    return completion.choices[0].message

class GetUserDetail(Action):
    def name(self) -> Text:
        return 'action_get_user_details'
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            person = tracker.get_slot('PERSON')
            name = person.lower().split(' ')
            if 'thoma' in name:
                dispatcher.utter_message(text=f"Thoma is a HOD of EPITA International. He teaches courses in 10 different courses aligned with computer science. He is a renowned expert in the field.")
                dispatcher.utter_message(image=thoma)
            elif 'bill' in name:
                dispatcher.utter_message(text=f"Bill is a professor at EPITA International. He teaches courses in Action Learning. He is a renowned expert in the field.")
                dispatcher.utter_message(image=bill)
            elif 'raisa' in name:
                dispatcher.utter_message(text=f"Raisa is a staff member at EPITA International. She works in the admissions office and helps students with their enrollment process. She is friendly and helpful.")
                dispatcher.utter_message(image=raisa)
            else:
                dispatcher.utter_message(text=f"I am sorry, I do not have information about {person}.")
            
            # dispatcher.utter_message(image=img)
            # dispatcher.utter_message(text=f"{fullname}, the {(d['type']).lower()} of our institution, can be reached via email at {d['email']}")
            # else:
            #     dispatcher.utter_message(text=f'I am not able to find {fullname}')
            return []
      


# def get_custom_data(tracker):
#     events = tracker.current_state()['events']
#     user_events = []
#     for e in events:
#         if e['event'] == 'user':
#             user_events.append(e)
#     custom_data = user_events[-1]['metadata']
#     return custom_data


class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""
    def init(self):
        super()._init_()
    def name(self) -> Text:
        return "action_default_fallback"
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        query = tracker.latest_message['text']
        # print(query)
        # custom_action=check_user(tracker)
        # if not custom_action:
        #     dispatcher.utter_message(text="Unauthorized user!")
        #     return []
        # if custom_action['institution']==''
        # dispatcher.utter_message(text=f"I apologize {custom_action['firstname']}, I am not designed for this kind of question and answer.")
        dispatcher.utter_message(text=gpt3(query))
        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]

class Greet(Action):
    def name(self) -> Text:
        return "action_greet"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # custom_data = get_custom_data(tracker)
        dispatcher.utter_message(text=f"Hi, I am a bot designed to assist students with information related to EPITA international.", 
                                 buttons=[{"title": "Administrative Process", "payload":"/admin_process"},
                                          {"title":"Assignments", "payload":"/check_assignment"},
                                          {"title":"Result", "payload":"/check_result"},
                                          {"title":"Routine", "payload":"/check_routine"}])
        
class AdminProcess(Action):
    def name(self) -> Text:
        return "action_admin_process"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # custom_data = get_custom_data(tracker)
        dispatcher.utter_message(text=f"Here are some administrative processes you may need to know..", 
                                 buttons=[{"title": "Visa Renewal", "payload":"/visa_renewal"},
                                          {"title":"CAF", "payload":"/caf"},
                                          {"title":"NAVIGO", "payload":"/navigo"},
                                          {"title":"Health Insurance", "payload":"/health_insurance"}])
        
class VisaRenewal(Action):
    def name(self) -> Text:
        return "action_visa_renewal"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # custom_data = get_custom_data(tracker)
        
        visa_info = (
            "Here is some information about visa renewal:<br>\
            \n<br>1. Check Eligibility: Ensure you meet all the eligibility criteria for visa renewal.\
            \n<br>2. Gather Documents: Collect all required documents including your current visa, passport, and any supporting documents.\
            \n<br>3. Complete Application: Fill out the visa renewal application form. Make sure all information is accurate and up-to-date.\
            \n<br> 4. Pay Fees: Pay the necessary visa renewal fees. The amount will vary depending on your visa type and duration.\
            \n<br> 5. Submit Application: Submit your completed application and supporting documents either online or at the visa office.\
            \n<br> 6. Schedule Appointment: If required, schedule and attend a visa renewal appointment.\
            \n<br> 7. Await Decision: Wait for the decision on your visa renewal application. Processing times can vary.\
         ")
        dispatcher.utter_message(text=visa_info)
        dispatcher.utter_message(text="For more detailed information and to apply online, visit the official visa renewal website:", buttons=[{"title": "Visa Renewal Website", "url": "https://administration-etrangers-en-france.interieur.gouv.fr/particuliers/#/"}])
        
        return []

class Caf(Action):
    def name(self) -> Text:
        return "action_caf"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # custom_data = get_custom_data(tracker)
        
        caf_info = (
            "Here is some information about the CAF process:\n\n"
            "1. **Eligibility Check:** Verify that you meet all the eligibility criteria for applying for CAF.\n"
            "2. **Document Preparation:** Gather all necessary documents such as proof of income, residency, and any other required forms.\n"
            "3. **Application Form:** Complete the CAF application form accurately and thoroughly.\n"
            "4. **Submission:** Submit your completed application form and all supporting documents online or at a designated office.\n"
            "5. **Follow-Up:** Keep track of your application status and provide any additional information if requested.\n"
            "6. **Decision Notification:** Wait for the decision on your application. Processing times can vary.\n"
        )
        
        dispatcher.utter_message(text=caf_info)
        dispatcher.utter_message(text="For more detailed information and to apply online, visit the official CAF website:", buttons=[{"title": "CAF Website", "url": "https://www.examplecafwebsite.com"}])
        
        return []


class Navigo(Action):
    def name(self) -> Text:
        return "action_navigo"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # custom_data = get_custom_data(tracker)
        
        navigo_info = (
            "Here is some information about the NAVIGO pass process:\n\n"
            "1. **Eligibility Check:** Ensure you meet the eligibility criteria for obtaining a NAVIGO pass.\n"
            "2. **Document Preparation:** Collect the necessary documents such as proof of identity, address, and a recent photo.\n"
            "3. **Application Form:** Fill out the NAVIGO pass application form accurately.\n"
            "4. **Submission:** Submit your application form and supporting documents at a NAVIGO office or online.\n"
            "5. **Payment:** Pay the applicable fees for the NAVIGO pass. Fees may vary based on the type of pass and duration.\n"
            "6. **Receive Pass:** Once approved, you will receive your NAVIGO pass. Make sure to validate it before use.\n"
            "7. **Renewal:** Keep track of the expiration date and renew your pass as necessary to continue enjoying the benefits.\n"
        )
        
        dispatcher.utter_message(text=navigo_info)
        dispatcher.utter_message(text="For more detailed information and to apply online, visit the official NAVIGO website:", buttons=[{"title": "NAVIGO Website", "url": "https://www.navigo.com"}])
        
        return []


class HealthInsurance(Action):
    def name(self) -> Text:
        return "action_health_insurance"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # custom_data = get_custom_data(tracker)
        
        health_insurance_info = (
            "Here is some information about the Health Insurance process:\n\n"
            "1. **Eligibility Check:** Determine if you meet the eligibility criteria for the health insurance plan.\n"
            "2. **Plan Comparison:** Compare different health insurance plans to find one that best suits your needs.\n"
            "3. **Document Preparation:** Gather all required documents such as proof of identity, residence, and income.\n"
            "4. **Application Form:** Fill out the health insurance application form with accurate information.\n"
            "5. **Submission:** Submit your completed application form and supporting documents online or at the health insurance office.\n"
            "6. **Payment:** Pay the necessary premiums for the chosen health insurance plan.\n"
            "7. **Receive Confirmation:** Once your application is processed, you will receive confirmation of your health insurance coverage.\n"
            "8. **Utilize Benefits:** Use your health insurance card to access healthcare services covered under your plan.\n"
        )
        
        dispatcher.utter_message(text=health_insurance_info)
        dispatcher.utter_message(text="For more detailed information and to apply online, visit the official Health Insurance website:", buttons=[{"title": "Health Insurance Website", "url": "https://www.examplehealthinsurance.com"}])
        
        return []



class CheckAssignment(Action):
    def name(self) -> Text:
        return "action_check_assignment"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # custom_data = get_custom_data(tracker)
        dispatcher.utter_message(text=f"Your assignment details are as follows..", 
                                 buttons=[{"title": "3 - Pendind Assignments", "payload":"/check_pending_assignment"},
                                          {"title":"0 - Due Assignments", "payload":"/check_due_assignment"},
                                          {"title":"10 - Completed Assignments", "payload":"/check_completed_assignment"}])
        


class CheckPendingAssignment(Action):
    def name(self) -> Text:
        return "action_check_pending_assignment"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # custom_data = get_custom_data(tracker)
        dispatcher.utter_message(text=f"Your pending assignments are as follows..", 
                                 buttons=[{"title": "Assignment 1", "payload":"/check_assignment_1"},
                                          {"title":"Assignment 2", "payload":"/check_assignment_2"},
                                          {"title":"Assignment 3", "payload":"/check_assignment_3"}])

class CheckAssignment1(Action):
    def name(self) -> Text:
        return "action_check_assignment_1"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        assignment_description = (
            "Assignment Title: Development of a Conversational AI Chatbot Using Rasa\n"
            "Course: MSc in Computer Science\n"
            "Course Code: CS530\n"
            "Semester: 3\n"
            "Instructor: Dr. Jane Doe\n\n"
            "Overview:\n"
            "In this assignment, you will develop a conversational AI chatbot using the Rasa framework. "
            "The chatbot should be capable of handling a set of predefined tasks and provide a seamless user experience. "
            "This assignment aims to enhance your understanding of natural language processing, machine learning, "
            "and the practical application of these concepts in developing a functional chatbot.\n\n"
            "Objectives:\n"
            "1. To understand the core components and workflow of the Rasa framework.\n"
            "2. To design and implement a conversational AI chatbot.\n"
            "3. To integrate natural language understanding (NLU) and dialogue management in the chatbot.\n"
            "4. To test and evaluate the performance of the chatbot.\n\n"
            "Requirements:\n"
            "1. Environment Setup:\n"
            "   - Set up a Python virtual environment and install the necessary packages.\n"
            "2. Data Preparation:\n"
            "   - Collect and annotate training data for NLU.\n"
            "3. Model Training:\n"
            "   - Train the NLU and dialogue models using Rasa.\n"
            "4. Implementation:\n"
            "   - Implement custom actions if necessary.\n"
            "5. Testing and Evaluation:\n"
            "   - Test the chatbot and evaluate its performance using predefined metrics.\n"
        )

        dispatcher.utter_message(text=assignment_description)
        return []

        


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionProvideVisaRenewalInfo(Action):

    def name(self) -> str:
        return "action_provide_visa_renewal_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        visa_renewal_info = (
            "To renew your visa, you need to follow these steps:\n"
            "1. Gather all necessary documents (passport, previous visa, proof of enrollment).\n"
            "2. Fill out the visa renewal application form.\n"
            "3. Pay the renewal fee.\n"
            "4. Submit your application to the appropriate visa office.\n"
            "5. Wait for the confirmation and further instructions.\n"
            "If you need more detailed information, please visit the university's international office or their website."
        )
        dispatcher.utter_message(text=visa_renewal_info)
        return []
    
class ActionProvideCafInfo(Action):

    def name(self) -> str:
        return "action_provide_caf_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        caf_info = (
            "To apply for CAF (Caisse des Allocations Familiales), you need to follow these steps:\n"
            "1. Gather necessary documents: proof of identity, proof of residence, income statements, etc.\n"
            "2. Create an account on the CAF website or visit a local CAF office.\n"
            "3. Fill out the application form and provide the required documents.\n"
            "4. Submit your application online or at a local CAF office.\n"
            "5. Wait for a response from CAF, which may include a request for additional information or documents.\n"
            "For more detailed information, you can visit the official CAF website or contact their customer service."
        )
        dispatcher.utter_message(text=caf_info)
        return []
    
class ActionProvideNavigoInfo(Action):

    def name(self) -> str:
        return "action_provide_navigo_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        navigo_info = (
            "To apply for a NAVIGO card, follow these steps:\n"
            "1. Gather the necessary documents: a passport photo, proof of identity, and proof of residence.\n"
            "2. Visit the official NAVIGO website or go to a local NAVIGO office.\n"
            "3. Fill out the application form and upload or submit the required documents.\n"
            "4. Pay the applicable fee for the card.\n"
            "5. Wait for the confirmation and receive your NAVIGO card in the mail or collect it from the office.\n"
            "For more detailed information, you can visit the official NAVIGO website or contact their customer service."
        )
        dispatcher.utter_message(text=navigo_info)
        return []