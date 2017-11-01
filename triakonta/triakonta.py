#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
import codecs

TRIAKONTA_VERBI = [("ἄγω", "condurre, portare"),
("αἴρω", "sollevare"),
("ἀκούω", "ascoltare, sentire"),
("ἁμαρτάνω", "sbagliare, peccare"),
("ἀμύνω", "difendere; punire"),
("ἀναγκάζω", "costringere"),
("ἀναιρέω", "distruggere; sollevare; dare un responso"),
("ἀνίστημι", "far alzare; alzarsi"),
("ἀξιόω", "ritenere giusto, ritenere degno"),
("ἀπαλλάττω", "cambiare; (al medio) liberarsi di"),
("ἀποβλέπω", "guardare; distogliere lo sguardo"),
("ἀποθνῄσκω", "morire"),
("ἀποκρίνω", "rispondere"),
("ἀποκτείνω", "uccidere"),
("ἀπόλλυμι", "distruggere; (al medio) morire"),
("ἁρπάζω", "rapire, afferrare"),
("ἄρχω", "comandare; (al medio) cominciare"),
("ἀφίημι", "lasciar andare"),
("ἀφικνέομαι", "giungere"),
("βάλλω", "lanciare, scagliare, colpire"),
("βούλομαι", "volere"),
("γαμέω", "sposare, accoppiarsi"),
("γεννάω", "generare"),
("γίγνομαι", "diventare; verificarsi; essere"),
("γιγνώσκω", "conoscere; pensare; decidere"),
("γράφω", "scrivere, disegnare"),
("δεῖ (impers.)", "dovere"),
("δέω", "mancare; dovere; chiedere; legare"),
("δίδωμι", "dare"),
("διώκω", "inseguire; perseguire penalmente"),
("δοκέω", "sembrare; pensare"),
("δράω", "fare"),
("δύναμαι", "potere"),
("ἐθέλω (θέλω)", "volere, desiderare"),
("εἰμί", "essere; esserci"),
("ἐλπίζω", "sperare, aspettarsi"),
("ἐπαινέω", "lodare"),
("ἐργάζομαι", "lavorare, operare"),
("ἔρχομαι", "venire"),
("ἐρωτάω", "domandare"),
("ἐσθίω", "mangiare"),
("εὑρίσκω", "trovare"),
("ἔχω", "avere; stare (con avverbio)"),
("ζάω", "vivere"),
("ἡγέομαι", "guidare; ritenere"),
("ἥκω", "essere giunto"),
("θαυμάζω", "meravigliarsi, ammirare; chiedersi"),
("θύω", "sacrificare"),
("ἵστημι", "collocare; (al medio) stare"),
("καλέω", "chiamare"),
("κελεύω", "ordinare, invitare"),
("κινδυνεύω", "rischiare; essere probabile"),
("κωλύω", "impedire"),
("λαμβάνω", "prendere"),
("λέγω", "dire; parlare"),
("λύω", "sciogliere; assolvere"),
("μανθάνω", "apprendere; capire"),
("μάχομαι", "combattere"),
("μέλλω", "stare per, volere"),
("μισέω", "odiare"),
("νέμω", "distribuire; dividere; pascolare"),
("νικάω", "vincere"),
("νομίζω", "pensare, ritenere"),
("οἶδα", "sapere"),
("οἰκέω", "abitare, insediarsi"),
("οἶμαι (οἴομαι)", "pensare"),
("οἴχομαι", "andare; essersene andato"),
("ὁμολογέω", "accordarsi, essere d'accordo"),
("ὁράω", "vedere"),
("παρασκευάζω", "approntare, preparare"),
("πάρειμι", "essere presenti"),
("παρέχω", "procurare"),
("πάσχω", "subire, soffrire"),
("παύω", "far cessare; (al medio) smettere"),
("πείθω", "persuadere; (al medio) obbedire"),
("πέμπω", "mandare, inviare"),
("ποιέω", "fare; creare"),
("πορεύομαι", "recarsi, andare, viaggiare"),
("πράττω", "fare, eseguire"),
("προΐστημι", "mettere a capo; difendere; essere a capo"),
("προσήκω", "convenire; essere adatto"),
("συνβαίνω", "accadere; convenire"),
("σῴζω", "salvare"),
("τελευτάω", "finire; morire"),
("τολμάω", "osare; sopportare"),
("τρέπω", "volgere"),
("τρέφω", "nutrire"),
("τυγχάνω", "ottenere; avere dalla sorte; trovarsi"),
("ὑβρίζω", "offendere, far violenza"),
("ὑπάρχω", "esserci, esistere"),
("ὑπολαμβάνω", "prendere; rispondere; pensare"),
("φαίνω", "mostrare; (al medio) apparire"),
("φέρω", "portare, produrre"),
("φεύγω", "fuggire; essere imputato"),
("φημί", "affermare"),
("φιλέω", "amare; esser solito"),
("φοβέω", "far paura; temere"),
("φρονέω", "pensare"),
("χράω (χράομαι)", "dare oracoli; (al medio) usare"),
("χρή (impers.)", "essere necessario"),
]


TRIAKONTA_NOMI = [("ἀγρός, οῦ, ὁ", "campo, campagna"),
("αἰτία, ας, ἡ", "causa; colpa; accusa"),
("ἀλήθεια, ας, ἡ", "verità"),
("ἁμάρτημα, ατος, τό", "errore, colpa; peccato"),
("ἁμαρτία, ας, ἡ", "errore, colpa; peccato"),
("ἀνάγκη, ης, ἡ", "necessità"),
("ἀνήρ, ἀνδρός, ὁ", "uomo; marito"),
("ἄνθρωπος, ου, ὁ", "uomo, persona"),
("ἀρετή, ῆς, ἡ", "virtù"),
("ἄρτος, ου, ὁ", "pane"),
("ἀρχή, ῆς, ἡ", "comando, principio"),
("βασιλεύς, έως, ὁ", "re"),
("βία, ας, ἡ", "violenza"),
("βίος, ου, ὁ", "vita"),
("βουλή, ῆς, ἡ", "consiglio"),
("γῆ, γῆς, ἡ", "terra, territorio"),
("γνώμη, ης, ἡ", "pensiero, sentenza, proverbio"),
("γυνή, γυναικός, ἠ", "donna, moglie"),
("δαίμων, ονος, ὁ", "dio"),
("δεσμός, οῦ, ὁ", "ceppo, legame, vincolo"),
("δένδρον, ου, τό", "albero"),
("δῆμος, ου, ὁ", "popolo"),
("δικαστής, οῦ, ὁ", "giudice"),
("δίκη, ης, ἡ", "giustizia; processo"),
("δύναμις, εως, ἡ", "potenza; esercito"),
("ἐλευθερία, ας, ἡ", "libertà"),
("ἔργον, ου, τό", "opera, impresa, lavoro"),
("ἔρως, ωτος, τό", "eros; amore"),
("ἔτος, ους, τό", "anno"),
("ζῷον, ου, τό", "essere vivente, animale"),
("ἡμέρα, ας, ἡ", "giorno"),
("θάλαττα, ης, ἡ", "mare"),
("θάνατος, ου, ὁ", "morte"),
("θεός, οῦ, ὁ", "dio"),
("θηρίον, ου, τό", "belva, fiera"),
("θυγάτηρ, θυγατρός, ἡ", "figlia"),
("ἱππεύς, έως, ὁ", "cavaliere"),
("ἵππος, ου, ὁ", "cavallo"),
("ἱστορία, ας, ἡ", "ricerca, indagine; storia"),
("ἰχθῦς, ύος, ὁ", "pesce"),
("καρπός, οῦ, ὁ", "frutto"),
("κεφαλή, ῆς, ἡ", "testa"),
("κίνδυνος, ου, ὁ", "pericolo, rischio"),
("λίθος, ου, ὁ", "pietra"),
("λιμήν, ένος, ὁ", "porto"),
("λόγος, ου, ὁ", "parola; discorso; ragionamento"),
("μαθητής, οῦ, ὁ", "studente, discepolo"),
("μάχη, ης, ἡ", "battaglia"),
("μέρος, ους, τό", "parte, porzione"),
("μήτηρ, μητρός, ἡ", "madre"),
("ναῦς, νεώς, ἡ", "nave"),
("νῆσος, ου, ἡ", "isola"),
("νίκη, ης, ἡ", "vittoria"),
("νόμος, ου, ὁ", "legge"),
("νύξ, νυκτός, ἡ", "notte"),
("ξίφος, ους, τό", "spada"),
("ὁδός, οῦ, ἡ", "via, strada"),
("οἰκία, ας, ἡ", "casa"),
("οἰκος, ου, ὁ", "casa"),
("ὄνομα, ατος, ὁ", "nome"),
("οὐρανός, οῦ, ὁ", "cielo"),
("ὄχλος, ου, ὁ", "folla; fastidio"),
("παιδίον, ου, ὁ", "fanciullo; schiavo"),
("παῖς, παιδός, ὁ", "fanciullo, figlio; schiavo"),
("πατήρ, πατρός, ὁ", "padre"),
("πέτρα, ας, ἡ", "roccia, pietra"),
("πίστις, εως, ἡ", "fiducia, fede"),
("πληγή, ῆς, ἡ", "piaga, ferita; colpo"),
("πλῆθος, ους, τό", "quantità, moltitudine, folla"),
("πλοῖον, ου, τό", "nave"),
("πλοῦτος, ου, ὁ", "ricchezza"),
("πόλεμος, ου, ὁ", "guerra"),
("πόλις, εως, ἡ", "città"),
("πολιτεία, ας, ἡ", "costituzione; governo; città"),
("πολίτης, ου, ὁ", "cittadino"),
("ποταμός, ου, ὁ", "fiume"),
("πρᾶγμα, ατος, τό", "fatto, azione, impresa, cosa"),
("στρατηγός, οῦ, ὁ", "comandante, stratego"),
("στρατιά, ᾶς, ἡ", "esercito; spedizione militare"),
("στρατιώτης, ου, ὁ", "soldato"),
("στρατόπεδον, ου, τό", "accampamento; esercito"),
("σύμμαχος (ξύμμαχος), ου, ὁ", "alleato"),
("σῶμα, ατος, τό", "corpo, cadavere"),
("τεῖχος, ους, τό", "muro"),
("τέκνον, ου, τό", "figlio"),
("τέλος, ους, τό", "fine, compimento"),
("τόπος, ου, ὁ", "luogo"),
("τύραννος, ου, ὁ", "tiranno; re"),
("τύχη, ης, ἡ", "sorte"),
("υἱός, οῦ, ὁ", "figlio"),
("φιλία, ας, ἡ", "amore, amicizia"),
("φόβος, ου, ὁ", "paura"),
("φύσις, εως, ἡ", "natura"),
("φωνή, ῆς, ἡ", "voce"),
("χάρις, χάριτος, ἡ", "grazia, gratitudine; (acc.) a causa di, (acc.) al fine di"),
("χεῖρ, χειρός, ἡ", "mano"),
("χρόνος, ου, ὁ", "tempo"),
("χώρα, ας, ἡ", "regione, territorio"),
("ψυχή, ῆς, ἡ", "anima"),
("ὥρα, ας, ἡ", "stagione; ora"),
]

TRIAKONTA_AGGETTIVI = [("ἀγαθός, ή, όν", "buono"),
("ἄδηλος, ον", "oscuro"),
("ἄδικος, ον", "ingiusto"),
("ἀδύνατος, ον", "impotente; impossibile"),
("ἀθάνατος, ον", "immortale"),
("αἰσχρός, ά, όν", "turpe, brutto"),
("αἴτιος, α, ον", "colpevole, responsabile"),
("ἀκούσιος, ον", "involontario"),
("ἄκρος, α, ον", "alto"),
("ἀληθής, ές", "vero, veritiero"),
("ἄλλος, ἄλλη, ἄλλο", "altro"),
("ἀλλότριος, α, ον", "altrui; estraneo"),
("ἀμαθής, ές", "ignorante"),
("ἀναγκαῖος, α, ον", "necessario"),
("ἀνθρώπινος, η, ον", "umano"),
("ἄξιος, α, ον", "degno"),
("ἅπας, ἄπασα, ἄπαν", "tutto quanto"),
("ἄπειρος, ον", "infinito; inesperto"),
("ἄπιστος, ον", "incredibile; incredulo"),
("ἄπορος, ον", "difficile"),
("ἄπρακτος, ον", "inutile, irrealizzabile, senza risultato"),
("ἀπγυροῦς, ᾶ, οῦν", "argenteo, d'argento"),
("ἄρρην, εν", "maschio"),
("ἀρχαῖος, α, ον", "antico"),
("ἀσφαλής, ές", "sicuro"),
("ἀφανής, ές", "nascosto, invisibile"),
("ἄφθονος, ον", "senza invidia, generoso, abbondante"),
("ἄφοβος, ον", "senza paura"),
("βάρβαρος, ον", "barbaro"),
("βραχύς, εῖα, ύ", "corto"),
("γενναῖος, α, ον", "nobile"),
("γυμνός, ή, όν", "nudo"),
("δειλός, ή, όν", "pauroso"),
("δεινός, ή, όν", "terribile; esperto"),
("δεξιός, ά, όν", "destro"),
("δίκαιος, α, ον", "giusto"),
("ἕκαστος, η, ον", "ciascuno"),
("ἐκεῖνος, ἐκείνη, ἐκεῖνο", "quello, quella, quella cosa"),
("ἐλεύθερος, α, ον", "libero"),
("ἐμός, ή, όν", "mio"),
("Ἕλλην, ηνος", "Elleno, Greco"),
("ἐναντίος, α, ον", "opposto, contrario"),
("ἐπιτήδειος, α, ον", "adatto; utile; necessario; amico"),
("ἕτερος, η, ον", "solitario; privo, mancante"),
("ἐχθρός, ά, όν", "nemico, avverso"),
("ἡδὐς, εῖα, ύ", "dolce, soave"),
("θαυμαστός, ή, όν", "meraviglioso"),
("θεῖος, α, ον", "divino"),
("θῆλυς, εια, υ", "femminile"),
("θνητός, ή, ον", "mortale"),
("ἴδιος, α, ον", "proprio, peculiare"),
("ἱερός, ά, όν", "sacro"),
("ἱκανός, ή, όν", "sufficiente"),
("ἰσχυρός, ή, όν", "forte"),
("κακός, ή, όν", "cattivo, vile"),
("καλός, ή, όν", "bello"),
("κενός, ή, όν", "vuoto"),
("κοινός, ή, όν", "comune"),
("λοιπός, ή, όν", "rimanente"),
("μεγαλόψυχος, ον", "magnanimo"),
("μέγας, μεγάλη, μέγα", "grande (m.), grande (f.), grande cosa"),
("μέσος, η, ον", "mezzo, mediano"),
("μικρός, ά, όν", "piccolo"),
("μόνος, η, ον", "solo"),
("νέος, α, ον", "nuovo; giovane"),
("νήπιος, α, ον", "infantile; sciocco"),
("ξένος, η, ον", "straniero, esraneo"),
("ὅδε, ἥδε, τόδε", "questo, questa, questa cosa"),
("ὅλος, η, ον", "tutto quanto, intero"),
("ὀλίγος, η, ον", "piccolo, poco"),
("ὅμοιος, α, ον", "simile, uguale"),
("ὅσος, η, ον", "quanto"),
("οὗτος, αὕτη, τοῦτο", "questo; quello"),
("πραπλήσιος, ον", "simile"),
("πᾶς, πᾶσα, πᾶν", "tutto; ogni"),
("πένης, ητος", "povero"),
("ποιητικός, ή, όν", "creativo, produttivo; poetico"),
("πολέμιος, α, ον", "nemico"),
("πολύς, πολλή, πολύ", "molto, tanto"),
("πονηρός, ά, όν", "malvagio"),
("πρῶτος, η, ον", "primo"),
("ῥᾴδιος, α, ον", "facile"),
("Ῥωμαῖος, α, οω", "Romano"),
("σός, σή, σόν", "tuo"),
("σοφός, ή, όν", "sapiente"),
("συγγενής, ές", "innato; parente; affine"),
("συνεχής, ές", "continuo"),
("ταχύς, εῖα, ύ", "veloce"),
("τοιοῦτος, τοιαύτη, τοιοῦτο", "tale, siffatto"),
("τοσοῦτος, τοσαύτη, τοσοῦτο", "così grande"),
("ὑπεναντίος, α, ον", "opposto, contrastante"),
("ὑποχείριος, ον", "soggetto a, sottoposto al potere di"),
("φανερός, ά, όν", "evidente, manifesto; famoso"),
("φίλος, η, ον", "amico, caro"),
("φυσικός, ή, όν", "naturale"),
("χαλεπός, ή, όν", "difficile; intrattabile"),
("χαλχοῦς, ῆ, οῦν", "bronzeo, di bronzo"),
("χρήσιμος, η, ον", "utile"),
("χρυσοῦς, ῆ, οῦν", "aureo, dorato"),
]

TRIAKONTA_VERBI_BL = [("ἄγω", "condurre, portare"),
("λέγω", "dire; parlare"),
("λύω", "sciogliere; assolvere"),
("εἰμί", "essere; esserci"),
("μανθάνω", "apprendere; capire"),
("πέμπω", "mandare, inviare"),
("φέρω", "portare, produrre"),
("φημί", "affermare"),
]

WORDS = (TRIAKONTA_VERBI, TRIAKONTA_NOMI, TRIAKONTA_AGGETTIVI)

ITEMS = (TRIAKONTA_VERBI, 
         TRIAKONTA_NOMI, 
         TRIAKONTA_AGGETTIVI, 
         TRIAKONTA_VERBI + TRIAKONTA_NOMI,
         TRIAKONTA_NOMI + TRIAKONTA_AGGETTIVI,
         TRIAKONTA_VERBI + TRIAKONTA_AGGETTIVI,
         TRIAKONTA_VERBI + TRIAKONTA_NOMI + TRIAKONTA_AGGETTIVI)

MAXQUESTION = 33
MAXSINTAGMI = 300
EXTRA=400

if __name__ == "__main__":
  random.seed()
  with codecs.open('TRIAKONTA_LATEST','w', encoding='utf8') as outf:
    
    for set in WORDS:
        print(">>>>START WORDSET>>>>>", file=outf)
        for item in set:
            print("%s\t%s" % item, file=outf)
        print(">>>>>>>>END WORDSET>>>>>>>>\n\n", file=outf)
     
    exnum = 1     
    for set in ITEMS:
        # shuffle the list
        random.shuffle(set)
        print(">>>>START EXERCISE %d >>>>>" % (exnum,), file=outf)
        for item in set[:MAXQUESTION]:
            print("%s" % (item[0],), file=outf)
        print(">>>>>>>>END RUN ONE>>>>>>>>\n", file=outf)
        for item in set[MAXQUESTION:2*MAXQUESTION]:
            print("%s" % (item[0],), file=outf)
        print(">>>>>>>>END RUN TWO>>>>>>>>\n\n", file=outf)
        for item in set[2*MAXQUESTION:3*MAXQUESTION]:
            print("%s" % (item[0],), file=outf)
        print(">>>>>>>>END RUN THREE>>>>>>>>\n\n", file=outf)
        
        exnum += 1
        
    # ora il generatore di sintagmi per i participi
    TEMPI_PARTICIPIO = ['PRESENTE.PARTICIPIO.ATTIVO',
        'FUTURO.PARTICIPIO.ATTIVO',
        'AORISTO.PARTICIPIO.ATTIVO',
        'PERFETTO.PARTICIPIO.ATTIVO',
        'PRESENTE.PARTICIPIO.MEDIO',
        'FUTURO.PARTICIPIO.MEDIO',
        'AORISTO.PARTICIPIO.MEDIO',
        'PERFETTO.PARTICIPIO.MEDIO',
        'FUTUROPERFETTO.PARTICIPIO.PASSIVO',
        'FUTURO.PARTICIPIO.PASSIVO',
        'AORISTO.PARTICIPIO.PASSIVO',
        ]
    
    GENERE = ['MASCHILE', 'FEMMINILE', 'NEUTRO']
    NUMERO = ['SINGOLARE', 'PLURALE', 'DUALE']
    CASO = ['NOMINATIVO', 'GENITIVO', 'DATIVO', 'ACCUSATIVO']
    FUNZIONE = ['TEMPORALE', 
                'CAUSALE', 
                'MODALE O STRUMENTALE', 
                'FINALE', 
                'CONDIZIONALE (PROTASI)', 
                'CONCESSIVA', ]

    print(">>>>START EXERCISE PARTICIPLE >>>>>\n", file=outf)
    exnum = 1
    print("ESERCIZIO_NUMERO\tPARTICIPIO_GRECO\tTRADUZIONE_ITALIANA\tVERBO_DA_CONIUGARE\tVOCE_DI_CONIUGAZIONE_RICHIESTA\tIN_FUNZIONE", file=outf)
       
    for counter in range(MAXSINTAGMI):
        verb = random.choice(TRIAKONTA_VERBI)
        time = random.choice(TEMPI_PARTICIPIO)
        gender = random.choice(GENERE)
        number = random.choice(NUMERO)
        case = random.choice(CASO)
        func = random.choice(FUNZIONE)
        
        print("P%03d\t%s+++\tIN FUNZIONE: %s\t%s (%s)\t%s\t%s" % (exnum, verb[0], func, verb[0], verb[1], time + ' ' + case + '.' + gender + '.' + number, func), file=outf)
        exnum += 1
    print(">>>>>>>>END EXERCISE PARTICIPLE >>>>>>>>>\n\n", file=outf)   

    # ora il generatore di sintagmi per i verbi
    TEMPI = ['PRESENTE.INDICATIVO.ATTIVO',
        'IMPERFETTO.INDICATIVO.ATTIVO',
        'FUTURO.INDICATIVO.ATTIVO',
        'AORISTO.INDICATIVO.ATTIVO',
        'PERFETTO.INDICATIVO.ATTIVO',
        'PIUCCHEPERFETTO.INDICATIVO.ATTIVO',
        'PRESENTE.CONGIUNTIVO.ATTIVO',
        'AORISTO.CONGIUNTIVO.ATTIVO',
        'PERFETTO.CONGIUNTIVO.ATTIVO',
        'PRESENTE.OTTATIVO.ATTIVO',
        'FUTURO.OTTATIVO.ATTIVO',
        'AORISTO.OTTATIVO.ATTIVO',
        'PERFETTO.OTTATIVO.ATTIVO',
        'PRESENTE.IMPERATIVO.ATTIVO',
        'AORISTO.IMPERATIVO.ATTIVO',
        'PRESENTE.INFINITO.ATTIVO',
        'FUTURO.INFINITO.ATTIVO',
        'AORISTO.INFINITO.ATTIVO',
        'PERFETTO.INFINITO.ATTIVO',
        'PRESENTE.INDICATIVO.MEDIO',
        'IMPERFETTO.INDICATIVO.MEDIO',
        'FUTURO.INDICATIVO.MEDIO',
        'AORISTO.INDICATIVO.MEDIO',
        'PERFETTO.INDICATIVO.MEDIO',
        'PIUCCHEPERFETTO.INDICATIVO.MEDIO',
        'PRESENTE.CONGIUNTIVO.MEDIO',
        'AORISTO.CONGIUNTIVO.MEDIO',
        'PERFETTO.CONGIUNTIVO.MEDIO',
        'PRESENTE.OTTATIVO.MEDIO',
        'FUTURO.OTTATIVO.MEDIO',
        'AORISTO.OTTATIVO.MEDIO',
        'PERFETTO.OTTATIVO.MEDIO',
        'PRESENTE.IMPERATIVO.MEDIO',
        'AORISTO.IMPERATIVO.MEDIO',
        'PERFETTO.IMPERATIVO.MEDIO',
        'PRESENTE.INFINITO.MEDIO',
        'FUTURO.INFINITO.MEDIO',
        'AORISTO.INFINITO.MEDIO',
        'PERFETTO.INFINITO.MEDIO',
        'FUTURO.INDICATIVO.PASSIVO',
        'AORISTO.INDICATIVO.PASSIVO',
        'FUTUROPERFETTO.INDICATIVO.PASSIVO',
        'AORISTO.CONGIUNTIVO.PASSIVO',
        'FUTURO.OTTATIVO.PASSIVO',
        'AORISTO.OTTATIVO.PASSIVO',
        'FUTUROPERFETTO.OTTATIVO.PASSIVO',
        'AORISTO.IMPERATIVO.PASSIVO',
        'FUTURO.INFINITO.PASSIVO',
        'AORISTO.INFINITO.PASSIVO',
        'FUTUROPERFETTO.INFINITO.PASSIVO',
        ]
    PERSONA = ['PRIMA', 'SECONDA', 'TERZA']
    
    print(">>>>START EXERCISE VERB >>>>>\n", file=outf)
    exnum = 1
    print("ESERCIZIO_NUMERO\tVERBO_GRECO\tTRADUZIONE_ITALIANA\tVERBO_DA_CONIUGARE\tVOCE_DI_CONIUGAZIONE_RICHIESTA", file=outf)
       
    for counter in range(MAXSINTAGMI+EXTRA):
        if exnum > MAXSINTAGMI:
            break
        verb = random.choice(TRIAKONTA_VERBI)
        time = random.choice(TEMPI+TEMPI_PARTICIPIO)
        person = random.choice(PERSONA)
        number = random.choice(NUMERO)

        if (person == "PRIMA" and number == "DUALE"):
            continue
        elif ('IMPERATIVO' in time and person in ['PRIMA',]):
            continue
        elif ('INFINITO' in time and (person in ['SECONDA', 'TERZA'] or number in ['PLURALE', 'DUALE'])):
            continue
        elif ('PARTICIPIO' in time and (person in ['SECONDA', 'TERZA'] or number in ['PLURALE', 'DUALE'])):
            continue    
        else:
            print("V%03d\t%s+++\t<TRADUZIONE>\t%s (%s)\t%s" % (exnum, verb[0], verb[0], verb[1], time + ' ' + person + '_PERSONA.' + number), file=outf)
            exnum += 1
    print(">>>>>>>>END EXERCISE VERB >>>>>>>>>\n\n", file=outf)   
        
        
             
             
