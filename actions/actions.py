# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import html2text
import requests
from bs4 import BeautifulSoup
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import youtubesearchpython as yt


class ActionTaxes(Action):

    def name(self) -> Text:
        return "action_taxes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}
        #r = requests.get(url='https://www.univpm.it/Entra/Tasse_e_contributi', headers= user_agent, verify=False)
        #if r.status_code == 200:
        output = "The Università Politecnica delle Marche has adopted a system for student contribution consisting of a fixed part (regional tax and stamp duty) and a variable part (all-inclusive contribution) determined according to the student's ISEE and course of study. The payment of fees is divided into three installments:\n\n** the amount of the 1st installment is € 156.00 (of which € 140.00 of regional tax for the right to study and € 16.00 of stamp duty); The 1st installment must be paid upon matriculation (or enrollment in years subsequent to the first) by the deadline of November 7, 2022. For courses with programmed access, the 1st installment must be paid by the deadlines indicated in the individual announcements.\n\n ** The amounts of the 2nd and 3rd installments are defined on the basis of the annual contribution determined according to the course of study of afferent and ISEE for the right to university study, which is acquired exclusively through the consent rendered online in one's reserved area of Esse3 Web - Home Personal Data - Consents, by November 7, 2022. \n The 2nd installment is due by December 14, 2022.\n The 3rd installment is due by May 31, 2023.\n All payments must be made exclusively through PagoPA (in the student reserved area). Payments made after these deadlines will incur a late payment fee of € 25.00 (if payment is made within 60 days of the due date) or € 50.00 (if payment is made after the 60th day).\n At this link you will find the simulator to calculate your contribution: http://www.univpm.it/simulatore-tasse.\n For more information visit the link: https://www.univpm.it/Entra/Tasse_e_contributi"
        dispatcher.utter_message(text=output)
        return []

class ActionEnrolment(Action):

    def name(self) -> Text:
        return "action_enrolment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output= "To matriculate in a three-year open-access course of study first of all you have to register on the portal:\n - https://univpm.esse3.cineca.it/Home.do.\n You can follow the directions on the page:\n - https://www.univpm.it/Entra/Universita_Politecnica_delle_Marche_Home/5_passi_per_iscriverti_a_UNIVPM/Immatricolazioni_Lauree_Triennali_Accesso_Libero.\n To matriculate in an open-access master's course of study, follow the directions on the page:\n - https://www. univpm.it/Entra/Universita_Politecnica_delle_Marche_Home/5_steps_to_enroll_at_UNIVPM/Immatricolazione_lauree_magistrali_ad_accesso_libero.\n Application deadline: November 7 . From November 8 you can enroll with an additional contribution of 25.00 euros within 60 days, or 50.00 euros after 60 days.\n For three-year open-access courses, you must have adequate initial preparation, which is ascertained with a special \"knowledge test.\"  The test is used to guide you in choosing a course of study, and a negative result does not prevent you from matriculating.  If you do not participate or fail the test, you will be assigned OFAs (Additional Formative Obligations), which you will have to fill in the manner and timeframe established by your Faculty or Department, otherwise you will have to repeat the first year (this means you will not be able to take the exams scheduled for the second year).  Go to the Teaching Facilities pages to find out how and when the tests take place:\n - Agriculture - https://www.d3a.univpm.it/test_verifica_conoscenze.\n - Economics - http://www.econ.univpm.it/verifica-conoscenze/.\n - Engineering - https://www.ingegneria.univpm.it/norme-ammissione-triennali-2022.\n - Science - http://www.disva.univpm.it/content/test-di-verifica-delle-conoscenze-0.\n For more information visit the links: \n - https://www.univpm.it/Entra/Didattica/5_passi_per_iscriverti_a_UNIVPM.\n - https://www.univpm.it/Entra/Servizi_agli_studenti/Segreterie_Studenti/Economia_1/Immatricolazione_Iscrizione_Corsi_di_laurea_triennali.\n - https://www.univpm.it/Entra/5_passi_per_iscriverti_a_UNIVPM/Immatricolazione_lauree_magistrali_ad_accesso_libero."


        dispatcher.utter_message(text=output)
        return []
class ActionCourses(Action):

    def name(self) -> Text:
        return "action_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output= "The degree programs available at UNIVPM are as follows:\n - Marine Biology.\n - Molecular and Applied Biology.\n - Biomedical Engineering (eng).\n - Data Science for Economics and Business.\n - Dietetics.\n - Digital Economics and Business (eng).\n - Business Administration. \n - Economics and Business.\n - Economics and Management.\n - Professional Education.\n - Environmental Engineering (eng).\n - Physiotherapy.\n - Food and Beverage Innovation and Management (eng).\n - Green Industrial Engineering (eng).\n - Dental Hygiene.\n - Nursing.\n - Biomedical Engineering. \Civil Engineering.\n - Civil and Environmental Engineering.\n - Information Engineering for Videogames and Virtual Reality.\n - Construction Engineering.\n - Construction-Architecture Engineering.\n - Electronic Engineering.\n - Electronic and Digital Technologies Engineering.\n - Management Engineering. \n - Computer and Automation Engineering.\n - Mechanical Engineering.\n - Engineering for Industrial Sustainability.\n - International Economics and Commerce (eng).\n - Speech Therapy.\n - Sustainability Management and Circular Economy.\n - Public and Social-Health Systems Management. \Medicine and Surgery.\n - Medicine and Surgery (Medicine and Technology) (eng).\n - Dentistry and Prosthodontics.\n - Obstetrics.\n - Environmental Risk and Civil Defense.\n - Agricultural and Land Sciences.\n - Environmental Sciences and Civil Defense.\n - Biological Sciences. \n - Nutrition and Food Sciences.\n - Agricultural Sciences and Technology.\n - Food Sciences and Technology.\n - Economic and Financial Sciences.\n - Forestry and Environmental Sciences.\n - Forest, Soil and Landscape Sciences.\n - Nursing and Midwifery Sciences. \n - Rehabilitation Sciences of the Health Professions.\n - Innovative Agricultural Systems.\n - Industrial and Information Systems.\n - Construction and Land Management Techniques.\n - Prevention Techniques in the Environment and Workplaces. \n - Biomedical Laboratory Techniques.\n - Medical Radiology Imaging and Radiotherapy Techniques.\n - Neuro and Psychomotor Therapy in the Age of Development.\n For more information, visit the link: https://www.univpm.it/Entra/Servizi_agli_studenti/Orientamento/Offerta_formativa_1. \n The study plan is the pathway that includes all the educational activities that one has to take in order to obtain a degree.\n Each degree program includes a certain number of exams: some are compulsory and are decided by the institutional bodies, while others are chosen by the students \"in case of non-choice they are assigned arbitrarily by the various faculties. During the compilation process, the student chooses the courses at will based on those available and offered in the various degree tracks.   The sum of compulsory and elective exams constitutes the individual student's study plan.    The total number of credits \"CFUs\" acquired by passing the exams will allow graduation. One's plan can be changed online according to the rules established by each faculty and course of study by accessing one's Reserved Area (https://apps.sia.univpm.it/accesso_area_riservata/).\ For more information visit the link: https://www.univpm.it/Entra/Percorsi/Studenti/Piano_di_studi."

        dispatcher.utter_message(text=output)
        return []

class ActionStage(Action):

    def name(self) -> Text:
        return "action_stage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output= "The purpose of the training and orientation internship is to realize moments of alternation between study and work within training processes and to facilitate professional choices through direct knowledge of the world of work. \n It can therefore have two purposes:\n** formative, which allows to deepen, verify and broaden the learning received in the course of studies;\n** orientative, which aims mainly to get to know the reality of the world of work.\n Internships can be initiated for:\n** students,\n they are curricular internships, that is, carried out during the course of studies or training, they can be aimed at obtaining CFUs. The reference legislation is DM 142/98; https://www.univpm.it/Entra/Servizi_agli_studenti/Tirocini_-_Stage_e_Placement/Tirocini_o_Stage/Tirocini_curriculari.\n ** recent graduates,\n within 12 months of obtaining a bachelor's degree, master's degree, PhD, master's degree, etc. These are extracurricular internships for which there must be mandatory reimbursement. The reference legislation is regional, so it varies according to the region in which the internship takes place. https://www.univpm.it/Entra/Servizi_agli_studenti/Tirocini_-_Stage_e_Placement/Tirocini_o_Stage/Tirocini_extracurriculari.\n In all cases, the relationship that is established between the employer and the intern does not constitute an employment relationship.\n For more information visit the link: https://www.univpm.it/Entra/Servizi_agli_studenti/Tirocini_-_Stage_e_Placement/Tirocini_o_Stage."

        dispatcher.utter_message(text=output)
        return []

class ActionErasmus(Action):

    def name(self) -> Text:
        return "action_erasmus"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output= "The Università Politecnica delle Marche offers its students the opportunity to carry out periods of study abroad through several mobility programs:\n ** Erasmus+. \n'\
                'https://www.univpm.it/Entra/Mobilita_per_Studio/Erasmus_outgoing_student.\n Announcement: https://www.univpm.it/Entra/Offerta_formativa_1/Diplome_en_Biologie_Marine/Studio/ Erasmus_bando_di_selection_for_students_5_high_schools.\n **ANC_HIO.\n https://www.univpm.it/Entra/Offerta_formativa_1/Diplome_en_Biologie_Marine/Studio/Selezione_mobilita_internazionale_per_studenti_universitari.\n **Joint/Double Degrees.\n https://www.univpm.it/Entra/Offerta_formativa_1/Diplome_en_Biologie_Marine/Studio/Titoli_congiunti_Double_Degree.\n For more information visit the link: https://www.univpm.it/Entra/Internazionale/Opportunita_allestero/Studio."
        dispatcher.utter_message(text=output)
        return []

class ActionSecretary(Action):

    def name(self) -> Text:
        return "action_secretary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output= "** AGRICULTURE ** January to August:\n 11 a.m. - 1 p.m. Monday and Thursday.\n 3 p.m. - 4:30 p.m. Wednesday.\n September to December:\n 10 a.m. - 1 p.m. Monday, Tuesday, Thursday, Friday.\n 3 p.m. - 4:30 p.m. Wednesday.\n ** ECONOMICS ** January to August:\n 11 a.m. - 1 p.m. 00 Monday and Thursday.\n 15.00 -16.30 Wednesday.\n From September to December:\n 10.00 - 13.00 Monday, Tuesday, Thursday, Friday.\n 15.00 - 16.30 Wednesday.\n ** ENGINEERING **n From January to August:\n 11.00 - 13.00 Monday and Thursday.\n 15.00 -16.30 Wednesday. \n September to December:\n 10 a.m. - 1 p.m. Monday, Tuesday, Thursday, Friday.\n 3 p.m. - 4:30 p.m. Wednesday.\n ** MEDICINE **\n January to August:\n 11 a.m. - 1 p.m. Monday and Thursday.\n 3 p.m. - 4:30 p.m. Wednesday.\n September to December:\n 10 a.m. - 1 p.m. 00 Mondays, Tuesdays, Thursdays, Fridays.\n 15.00 - 16.30 Wednesdays.\n ** SCIENCES ** From January to August:\n 11.00 - 13.00 Mondays and Thursdays.\n 15.00 -16.30 Wednesdays.\n From September to December:\n 10.00 - 13.00 Mondays, Tuesdays, Thursdays, Fridays.\n 15.00 - 16.30 Wednesdays.\n"
        dispatcher.utter_message(text=output)
        return []

class ActionSearch(Action):

    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        title = str(tracker.latest_message['text'])
        splits = title.split()
        to_seek = ''
        for item in splits:
            if item != 'search' and item != 'video':
                to_seek += (item + ' ')
        search = yt.VideosSearch(to_seek, limit = 1)
        splits = str(search.result()).split()
        for word in splits:
            if 'watch?' in word:
                dispatcher.utter_message(text=str(word))
        return []

