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
        output = "L’Università Politecnica delle Marche ha adottato un sistema per la contribuzione studentesca" \
                     " costituito da una parte fissa (tassa regionale e bollo) e da una parte variabile " \
                     "(contributo onnicomprensivo) determinata in base all’ISEE e al corso di studio dello studente." \
                     "Il pagamento delle tasse è suddiviso in tre rate:\n\n" \
                     "** l’importo della 1a rata è di € 156,00 (di cui € 140,00 di tassa regionale per il diritto allo " \
                     "studio e € 16,00 di imposta di bollo); La 1a rata deve essere corrisposta all’atto " \
                     "dell’immatricolazione (o iscrizione ad anni successivi al primo) entro il termine del 7 novembre " \
                     "2022. Per i corsi ad accesso programmato la 1a rata va corrisposta nei termini indicati nei singoli bandi.\n\n" \
                     "** gli importi della 2a e 3a rata sono definiti sulla base del contributo annuale determinato " \
                     "in base al corso di studio di afferenza e all’ISEE per il diritto allo studio universitario, " \
                     "che viene acquisito esclusivamente tramite il consenso reso online nella propria area riservata " \
                     "di Esse3 Web - Home Dati Anagrafici - Consensi, entro il 7 novembre 2022.\n\n" \
                     "La 2a rata va versata entro il 14 dicembre 2022.\n" \
                     "La 3a rata va versata entro il 31 maggio 2023.\n\n" \
                     "Tutti i pagamenti devono essere effettuati esclusivamente tramite PagoPA (in area riservata studente)." \
                     "I pagamenti effettuati oltre tali termini comportano l’attribuzione della mora di € 25,00" \
                     " (se il pagamento viene fatto entro 60 giorni dalla scadenza) oppure € 50,00 (se il pagamento " \
                     "viene fatto successivamente al 60° giorno).\n\n" \
                     "A questo link trovi il simulatore per calcolare il tuo contributo: http://www.univpm.it/simulatore-tasse.\n" \
                     "Per ulteriori informazioni visita il link: https://www.univpm.it/Entra/Tasse_e_contributi."
        dispatcher.utter_message(text=output)
        return []

class ActionEnrolment(Action):

    def name(self) -> Text:
        return "action_enrolment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output= 'Per immatricolarti ad un corso di studio triennale ad accesso libero prima di tutto devi registrarti al portale:\n' \
                '- https://univpm.esse3.cineca.it/Home.do.\n' \
                'Puoi seguire le indicazioni alla pagina:\n' \
                '- https://www.univpm.it/Entra/Universita_Politecnica_delle_Marche_Home/5_passi_per_iscriverti_a_UNIVPM/Immatricolazioni_Lauree_Triennali_Accesso_Libero.\n' \
                'Per immatricolarti ad un corso di studio magistrale ad accesso libero, segui le indicazioni alla pagina:\n' \
                '- https://www.univpm.it/Entra/Universita_Politecnica_delle_Marche_Home/5_passi_per_iscriverti_a_UNIVPM/Immatricolazione_lauree_magistrali_ad_accesso_libero.\n' \
                'Scadenza della domanda: 7 Novembre . Dall 8 novembre  puoi iscriverti con un contributo aggiuntivo di ' \
                'euro 25,00 entro 60 giorni, oppure di euro 50,00 superati i 60 giorni.\n' \
                'Per i corsi triennali ad accesso libero devi avere un’adeguata preparazione iniziale che è accertata ' \
                'con apposito "test di verifica delle conoscenze".' \
                'Il test serve ad orientarti nella scelta del corso di studio e l esito negativo non ti impedisce di immatricolarti.' \
                'Se non partecipi o non superi il test ti saranno attribuiti gli OFA (Obblighi Formativi Aggiuntivi), ' \
                'che dovrai colmare nei modi e tempi stabiliti dalla tua Facoltà o Dipartimento, altrimenti dovrai ' \
                'ripetere il primo anno (questo significa che non potrai sostenere gli esami previsti al secondo anno).' \
                'Vai alle pagine delle strutture didattiche per conoscere come e quando si svolgono i test:\n' \
                '- Agraria - https://www.d3a.univpm.it/test_verifica_conoscenze.\n' \
                '- Economia - http://www.econ.univpm.it/verifica-conoscenze/.\n' \
                '- Ingegneria - https://www.ingegneria.univpm.it/norme-ammissione-triennali-2022.\n' \
                '- Scienze - http://www.disva.univpm.it/content/test-di-verifica-delle-conoscenze-0.\n' \
                'Per ulteriori informazioni visita i link: \n' \
                '- https://www.univpm.it/Entra/Didattica/5_passi_per_iscriverti_a_UNIVPM.\n' \
                '- https://www.univpm.it/Entra/Servizi_agli_studenti/Segreterie_Studenti/Economia_1/Immatricolazione_Iscrizione_Corsi_di_laurea_triennali.\n' \
                '- https://www.univpm.it/Entra/5_passi_per_iscriverti_a_UNIVPM/Immatricolazione_lauree_magistrali_ad_accesso_libero.'


        dispatcher.utter_message(text=output)
        return []
class ActionCourses(Action):

    def name(self) -> Text:
        return "action_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output= 'I corsi di laurea disponibili ad UNIVPM sono i seguenti:\n' \
                '- Biologia Marina.\n' \
                '- Biologia Molecolare e Applicata.\n' \
                '- Biomedical Engineering (eng).\n' \
                '- Data Science per l\'Economia e le Imprese.\n' \
                '- Dietistica.\n' \
                '- Digital Economics and Business (eng).\n' \
                '- Economia Aziendale.\n' \
                '- Economia e Commercio.\n' \
                '- Economia e Management.\n' \
                '- Educazione Professionale.\n' \
                '- Environmental Engineering (eng).\n' \
                '- Fisioterapia.\n' \
                '- Food and Beverage Innovation and Management (eng).\n' \
                '- Green Industrial Engineering (eng).\n' \
                '- Igiene Dentale.\n' \
                '- Infermieristica.\n' \
                '- Ingegneria Biomedica.\n' \
                '- Ingegneria Civile.\n' \
                '- Ingegneria Civile e Ambientale.\n' \
                '- Ingegneria dell\'Informazione per Videogame e Realtà Virtuale.\n' \
                '- Ingegneria Edile.\n' \
                '- Ingegneria edile-architettura.\n' \
                '- Ingegneria Elettronica.\n' \
                '- Ingegneria Elettronica e delle Tecnologie Digitali.\n' \
                '- Ingegneria Gestionale.\n' \
                '- Ingegneria Informatica e dell\'Automazione.\n' \
                '- Ingegneria Meccanica.\n' \
                '- Ingegneria per la sostenibilità industriale.\n' \
                '- International Economics and Commerce (eng).\n' \
                '- Logopedia.\n' \
                '- Management della Sostenibilità ed Economia Circolare.\n' \
                '- Management pubblico e dei sistemi socio-sanitari.\n' \
                '- Medicina e Chirurgia.\n' \
                '- Medicine and Surgery (Medicine and Technology) (eng).\n' \
                '- Odontoiatria e Protesi Dentaria.\n' \
                '- Ostetricia.\n' \
                '- Rischio Ambientale e Protezione Civile.\n' \
                '- Scienze Agrarie e del Territorio.\n' \
                '- Scienze Ambientali e Protezione Civile.\n' \
                '- Scienze Biologiche.\n' \
                '- Scienze della Nutrizione e dell\'Alimentazione.\n' \
                '- Scienze e Tecnologie Agrarie.\n' \
                '- Scienze e Tecnologie Alimentari.\n' \
                '- Scienze Economiche e Finanziarie.\n' \
                '- Scienze Forestali e Ambientali.\n' \
                '- Scienze Forestali, dei suoli e del paesaggio.\n' \
                '- Scienze Infermieristiche ed Ostetriche.\n' \
                '- Scienze Riabilitative delle Professioni Sanitarie.\n' \
                '- Sistemi Agricoli Innovativi.\n' \
                '- Sistemi Industriali e dell\'Informazione.\n' \
                '- Tecniche della Costruzione e Gestione del Territorio.\n' \
                '- Tecniche della Prevenzione nell\'Ambiente e nei Luoghi di Lavoro.\n' \
                '- Tecniche di Laboratorio Biomedico.\n' \
                '- Tecniche di Radiologia Medica per Immagini e Radioterapia.\n' \
                '- Terapia della Neuro e Psicomotoricità dell\'Età Evolutiva.\n\n' \
                'Per ulteriori informazioni visitare il link: https://www.univpm.it/Entra/Servizi_agli_studenti/Orientamento/Offerta_formativa_1. \n' \
                'Il piano di studi è il percorso che comprende tutte le attività formative che si devono svolgere per ' \
                'conseguire la laurea. gni corso di laurea prevede un determinato numero di esami: alcuni sono obbligatori' \
                ' e vengono decisi dagli organi istituzionali, altri invece sono scelti dagli studenti “in caso di' \
                ' mancata scelta vengono attribuiti arbitrariamente dalle varie facoltà”. Durante la compilazione lo ' \
                'studente sceglie i corsi a piacere in base a quelli disponibili e offerti nei vari percorsi di laurea.' \
                ' La somma di esami obbligatori ed esami a scelta costituisce il piano di studio del singolo studente.  ' \
                'Il numero totale di crediti “CFU” acquisiti con il superamento degli esami permetterà il ' \
                'conseguimento della laurea. Il proprio piano  può essere cambiato on line secondo le regole stabilite' \
                ' da ogni facoltà e corso di studi accedendo alla propria Area Riservata (https://apps.sia.univpm.it/accesso_area_riservata/).\n' \
                'Per ulteriori informazioni visitare il link: https://www.univpm.it/Entra/Percorsi/Studenti/Piano_di_studi.'

        dispatcher.utter_message(text=output)
        return []

class ActionStage(Action):

    def name(self) -> Text:
        return "action_stage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output= 'Il  tirocinio formativo e di orientamento ha lo scopo di realizzare momenti di alternanza tra studio ' \
                'e lavoro nell\'ambito di processi formativi e di agevolare le scelte professionali mediante la ' \
                'conoscenza diretta del mondo del lavoro.\n' \
                'Può avere dunque due finalità:\n' \
                '** formativa, che permette di approfondire, verificare ed ampliare l\'apprendimento ricevuto nel ' \
                'percorso degli studi;\n' \
                '** orientativa, che mira prevalentemente a far conoscere la realtà del mondo del lavoro.\n\n' \
                'I tirocini possono essere avviati per:\n' \
                '** studenti,\n ' \
                'si tratta di tirocini curriculari, svolti cioé durante il corso di studi o di formazione, ' \
                'possono essere finalizzati al conseguimento di CFU. La normativa di riferimento è il DM 142/98; ' \
                'https://www.univpm.it/Entra/Servizi_agli_studenti/Tirocini_-_Stage_e_Placement/Tirocini_o_Stage/Tirocini_curriculari.\n' \
                '** neolaureati,\n' \
                'entro i 12 mesi dal conseguimento di un diploma di laurea, laurea magistrale, dottorato di ricerca, ' \
                'master ecc. Si tratta di tirocini extracurriculari per i quali deve essere previsto un rimborso ' \
                'obbligatorio. La normativa di riferimento è quella regionale, varia quindi in base alla regione in' \
                ' cui si svolge il tirocinio. https://www.univpm.it/Entra/Servizi_agli_studenti/Tirocini_-_Stage_e_Placement/Tirocini_o_Stage/Tirocini_extracurriculari.\n' \
                'In tutti i casi il rapporto che si instaura tra il datore di lavoro e il tirocinante non costituisce rapporto di lavoro.\n' \
                'Per ulteriori informazioni visita il link: https://www.univpm.it/Entra/Servizi_agli_studenti/Tirocini_-_Stage_e_Placement/Tirocini_o_Stage.'

        dispatcher.utter_message(text=output)
        return []

class ActionErasmus(Action):

    def name(self) -> Text:
        return "action_erasmus"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output= 'L\'Università Politecnica delle Marche offre ai propri studenti l\'opportunità di svolgere periodi di' \
                ' studio all\'estero attraverso numerosi programmi di mobilità:\n' \
                '** Erasmus+. \n'\
                'https://www.univpm.it/Entra/Mobilita_per_Studio/Erasmus_outgoing_student.\n' \
                'Bando: https://www.univpm.it/Entra/Offerta_formativa_1/Diplome_en_Biologie_Marine/Studio/' \
                'Erasmus_bando_di_selezione_per_studenti_5_scuole_superiori.\n' \
                '**ANC_HIO.\n' \
                'https://www.univpm.it/Entra/Offerta_formativa_1/Diplome_en_Biologie_Marine/Studio/Selezione_mobilita_internazionale_per_studenti_universitari.\n' \
                '**Titoli Congiunti/Doppi titoli.\n' \
                'https://www.univpm.it/Entra/Offerta_formativa_1/Diplome_en_Biologie_Marine/Studio/Titoli_congiunti_Double_Degree.\n' \
                'Per ulteriori informazioni visita il link: https://www.univpm.it/Entra/Internazionale/Opportunita_allestero/Studio.'
        dispatcher.utter_message(text=output)
        return []

class ActionSecretary(Action):

    def name(self) -> Text:
        return "action_secretary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output= '** AGRARIA **\n' \
                'Da Gennaio ad Agosto:\n ' \
                '11.00 - 13.00 Lunedì e Giovedì.\n' \
                '15.00 -16.30 Mercoledì.\n' \
                'Da Settembre a Dicembre:\n' \
                '10.00 - 13.00 Lunedì, Martedì, Giovedì, Venerdì.\n' \
                '15.00 - 16.30 Mercoledì.\n\n' \
                '** ECONOMIA **\n' \
                'Da Gennaio ad Agosto:\n ' \
                '11.00 - 13.00 Lunedì e Giovedì.\n' \
                '15.00 -16.30 Mercoledì.\n' \
                'Da Settembre a Dicembre:\n' \
                '10.00 - 13.00 Lunedì, Martedì, Giovedì, Venerdì.\n' \
                '15.00 - 16.30 Mercoledì.\n\n' \
                '** INGEGNERIA **\n' \
                'Da Gennaio ad Agosto:\n ' \
                '11.00 - 13.00 Lunedì e Giovedì.\n' \
                '15.00 -16.30 Mercoledì.\n' \
                'Da Settembre a Dicembre:\n' \
                '10.00 - 13.00 Lunedì, Martedì, Giovedì, Venerdì.\n' \
                '15.00 - 16.30 Mercoledì.\n\n' \
                '** MEDICINA **\n' \
                'Da Gennaio ad Agosto:\n ' \
                '11.00 - 13.00 Lunedì e Giovedì.\n' \
                '15.00 -16.30 Mercoledì.\n' \
                'Da Settembre a Dicembre:\n' \
                '10.00 - 13.00 Lunedì, Martedì, Giovedì, Venerdì.\n' \
                '15.00 - 16.30 Mercoledì.\n\n' \
                '** SCIENZE **\n' \
                'Da Gennaio ad Agosto:\n ' \
                '11.00 - 13.00 Lunedì e Giovedì.\n' \
                '15.00 -16.30 Mercoledì.\n' \
                'Da Settembre a Dicembre:\n' \
                '10.00 - 13.00 Lunedì, Martedì, Giovedì, Venerdì.\n' \
                '15.00 - 16.30 Mercoledì.\n\n'
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

