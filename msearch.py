import os
import urllib.parse
import webbrowser
from colorama import init, Fore, Style

# Funzione per pulire il terminale
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Inizializza colorama per consentire la stampa colorata su terminale
init(autoreset=True)

def generate_google_dork(search_element, detail1, detail2):
    site_list = ['site:kijiji.*', 'site:subito.*', 'site:bakeca.it', 'site:shpock.com/en-gb', 'site:prezzishock.it', 'site:etsy.com/it/.*', 'site:it.wallapop.com', 'site:vinted.*', 'site:facebook.com/marketplace/', 'site:autoscout24.*', 'site:ebay.*']  # Possiamo aggiungere altri siti qui
    dorks = []

    if search_element:
        for site in site_list:
            dork_parts = [search_element]

            if detail1:
                dork_parts.append(urllib.parse.quote(detail1))
            if detail2:
                dork_parts.append(urllib.parse.quote(detail2))

            dork = f"{site} {' AND '.join(dork_parts)}"
            dorks.append(dork)

    return dorks

# Pulisce il terminale
clear_terminal()

print(f"{Fore.GREEN}Benvenuti su UNAMMED Market Search\n")
search_element = input("Inserisci l'elemento da cercare: ")
detail1 = input("Inserisci il dettaglio 1 (opzionale): ")
detail2 = input("Inserisci il dettaglio 2 (opzionale): ")
google_dorks = generate_google_dork(search_element, detail1, detail2)

if not google_dorks:
    print(f"{Fore.RED}Nessuna Dork generata. Assicurati di inserire almeno l'elemento da cercare.")
else:
    # Stampa le Google Dorks generate
    print(f"\n{Fore.CYAN}Google Dorks:")
    for dork in google_dorks:
        print(f"{Fore.YELLOW}{dork}")

    # Apri le Google Dorks nel browser predefinito solo se ci sono risultati
    open_search = input(f"\n{Fore.GREEN}Vuoi aprire la ricerca nel browser? (y/n): ")
    if open_search.lower() == 'y':
        for dork in google_dorks:
            webbrowser.open('https://www.google.com/search?q=' + urllib.parse.quote(dork))
    else:
        print(f"{Fore.GREEN}Ricerca nel browser non eseguita.")