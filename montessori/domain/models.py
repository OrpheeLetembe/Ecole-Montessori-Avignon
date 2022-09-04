from django.db import models

from student.models import Students


class PracticalLife(models.Model):

    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    date_start = models.CharField(max_length=5)

    """ EXERCICES PRELIMINAIRES """

    title_1 = models.CharField(
        max_length=100, default='EXERCICES PRELIMINAIRES')
    move_mood = models.CharField(
        max_length=255, verbose_name="Se déplacer dans l'ambiance")
    carry_table = models.CharField(
        max_length=255, verbose_name="Porter une table seul, à deux")
    Carry_tray = models.CharField(
        max_length=255, verbose_name="Porter un plateau, un objet fragile")
    Carrying_mat = models.CharField(
        max_length=255, verbose_name="Porter, dérouler et rouler un tapis")
    open_close_door = models.CharField(
        max_length=255, verbose_name="Ouvrir et fermer une porte")
    open_close_window = models.CharField(
        max_length=255, verbose_name="Ouvrir et fermer une fenêtre, un tiroir")

    """ SOIN DU MILEU INTERIEUR """

    title_2 = models.CharField(
        max_length=100, default='SOIN DU MILEU INTERIEUR')
    squeeze_sponge = models.CharField(
        max_length=255, verbose_name="Presser une éponge")
    Screw_bolts = models.CharField(
        max_length=255, verbose_name="Visser, dévisser des boulons")
    screwdriver = models.CharField(
        max_length=255, verbose_name="Utiliser un tournevis")
    open_close_padlock = models.CharField(
        max_length=255, verbose_name="Ouvrir et fermer un cadenas")
    use_clothes_pegs = models.CharField(
        max_length=255, verbose_name="Se servir de pinces à linge")
    open_close_boxes = models.CharField(
        max_length=255, verbose_name="Ouvrir et fermer des boites")
    open_close_bottles = models.CharField(
        max_length=255, verbose_name="Ouvrir et fermer des flacons")
    fold_fabrics = models.CharField(
        max_length=255, verbose_name="Plier des étoffes")
    fold_paper = models.CharField(
        max_length=255, verbose_name="Plier du papier")
    cut_paper_scissors = models.CharField(
        max_length=255, verbose_name="Couper du papier avec des ciseaux")
    paste_paper = models.CharField(
        max_length=255, verbose_name="Coller du papier")
    dust = models.CharField(
        max_length=255, verbose_name="Epousseter avec un chiffon, un plumeau")
    sweep = models.CharField(
        max_length=255, verbose_name="Balayer")
    brush_carpet = models.CharField(
        max_length=255, verbose_name="Brosser un tapis")
    transfer_spoon = models.CharField(
        max_length=255, verbose_name="Transvaser avec une cuillère")
    pour_rice = models.CharField(
        max_length=255, verbose_name="Verser du riz")
    pour_sand = models.CharField(
        max_length=255, verbose_name="Verser du sable")
    pour_water = models.CharField(
        max_length=255, verbose_name="Verser de l'eau")
    pour_water_glasses = models.CharField(
        max_length=255, verbose_name="Verser de l'eau dans des verres")
    clean_mirror = models.CharField(
        max_length=255, verbose_name="Nettoyer un miroir")
    polish_brass = models.CharField(
        max_length=255, verbose_name="Astiquer les cuivres")
    take_care_plants = models.CharField(
        max_length=255, verbose_name="Soigner les plantes")
    chang_flower_water = models.CharField(
        max_length=255, verbose_name="Changer l'eau des fleurs")
    wash_table = models.CharField(
        max_length=255, verbose_name="Laver la table")
    wash_clothes = models.CharField(
        max_length=255, verbose_name="Laver du linge")
    stitching = models.CharField(
        max_length=255, verbose_name="Piquage")

    """ SOIN DE LA PERSONNE"""
    title_3 = models.CharField(
        max_length=100, default='SOIN DE LA PERSONNE')
    frame_press_studs = models.CharField(
        max_length=255, verbose_name="Cadre à boutons pressions")
    frame_big_studs = models.CharField(
        max_length=255, verbose_name="Cadre à gros boutons")
    frame_small_studs = models.CharField(
        max_length=255, verbose_name="Cadre à petits boutons")
    frame_slide = models.CharField(
        max_length=255, verbose_name="Cadre à glissière")
    frame_staple = models.CharField(
        max_length=255, verbose_name="Cadre à agrafes")
    frame_loop = models.CharField(
        max_length=255, verbose_name="Cadre à boucles")
    frame_safety_pin = models.CharField(
        max_length=255, verbose_name="Cadre à épingles à nourrice")
    frame_node = models.CharField(
        max_length=255, verbose_name="Cadre à noeuds")
    frame_lacing = models.CharField(
        max_length=255, verbose_name="Cadre à laçage")
    wash_hands = models.CharField(
        max_length=255, verbose_name="Se laver les mains")
    make_bread = models.CharField(
        max_length=255, verbose_name="Faire le pain")
    fresh_fruit = models.CharField(
        max_length=255, verbose_name="Préparer les fruits frais")
    shine_shoes = models.CharField(
        max_length=255, verbose_name="Cirer ses chaussures")
    sew = models.CharField(
        max_length=255, verbose_name="Coudre")

    """ JEUX COLLECTIFS"""
    title_4 = models.CharField(
        max_length=100, default='JEUX COLLECTIFS')
    walk_line = models.CharField(
        max_length=255, verbose_name="Marcher sur la ligne")
    lesson_silence = models.CharField(
        max_length=255, verbose_name="Leçon de silence")

    title_5 = models.CharField(max_length=100, default='OBSERVATIONS')
    observations_1 = models.TextField(verbose_name="Trimestre 1")
    observations_2 = models.TextField(verbose_name="Trimestre 2")
    observations_3 = models.TextField(verbose_name="Trimestre 3")

    class Meta:
        verbose_name = "Vie Pratique"
        verbose_name_plural = "Vie Pratique"


class SensoryMaterial(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    date_start = models.CharField(max_length=5)

    """ VISUEL"""

    title_1 = models.CharField(max_length=100, default='VISUEL')
    cylindrical_sockets_1 = models.CharField(
        max_length=250, verbose_name="Emboitements cylindriques 1")
    cylindrical_sockets_2 = models.CharField(
        max_length=250, verbose_name="Emboitements cylindriques 2")
    cylindrical_sockets_3 = models.CharField(
        max_length=250, verbose_name="Emboitements cylindriques 3")
    cylindrical_sockets_4 = models.CharField(
        max_length=250, verbose_name="Emboitements cylindriques 4")
    pink_tower = models.CharField(
        max_length=250, verbose_name="La tour rose")
    brown_staircase = models.CharField(
        max_length=250, verbose_name="L'escalier marron")
    red_bars = models.CharField(
        max_length=250, verbose_name="Les barres rouges")
    color_table_1 = models.CharField(
        max_length=250, verbose_name="Les tables des couleurs 1")
    color_table_2 = models.CharField(
        max_length=250, verbose_name="Les tables des couleurs 2")
    color_table_3 = models.CharField(
        max_length=250, verbose_name="Les tables des couleurs 3")
    geometry_tray = models.CharField(
        max_length=250, verbose_name="Le cabinet de géométrie /plateau")
    geometry_drawers = models.CharField(
        max_length=250, verbose_name="Le cabinet de géométrie /tiroirs")
    geometry_maps = models.CharField(
        max_length=250, verbose_name="Le cabinet de géométrie /cartes")
    constructor_triangles_1 = models.CharField(
        max_length=250, verbose_name="Les triangles constructeurs 1")
    constructor_triangles_2 = models.CharField(
        max_length=250, verbose_name="Les triangles constructeurs 2")
    constructor_triangles_3 = models.CharField(
        max_length=250, verbose_name="Les triangles constructeurs 3")
    constructor_triangles_4 = models.CharField(
        max_length=250, verbose_name="Les triangles constructeurs 4")
    constructor_triangles_5 = models.CharField(
        max_length=250, verbose_name="Les triangles constructeurs 5")
    constructor_triangles_6 = models.CharField(
        max_length=250, verbose_name="Les triangles constructeurs 6")
    superimposed_figures = models.CharField(
        max_length=250, verbose_name="Les figures superposées")
    binomial_cube = models.CharField(
        max_length=250, verbose_name="Le cube du binôme")
    trinomial_cube = models.CharField(
        max_length=250, verbose_name="Le cube du trinôme")
    pythagore_table = models.CharField(
        max_length=250, verbose_name="La table de Pythagore")
    colored_cylinders = models.CharField(
        max_length=250, verbose_name="Les cylindres de couleur")
    botanical_tray = models.CharField(
        max_length=250, verbose_name="Le cabinet de botaniques /plateau")
    botanical_maps = models.CharField(
        max_length=250, verbose_name="Le cabinet de botaniques /cartes")
    roman_arch = models.CharField(
        max_length=250, verbose_name="L'arche romane")

    """ TACTILE"""

    title_2 = models.CharField(


        max_length=100, default='TACTILE')
    smooth_rough = models.CharField(
        max_length=250, verbose_name="Lisse et rugueux")
    smooth_rough_table = models.CharField(
        max_length=250, verbose_name="Lisse et rugueux : les tablettes")
    fabrics = models.CharField(
        max_length=250, verbose_name="Les étoffes")
    baryque_tablets = models.CharField(
        max_length=250, verbose_name="Les tablettes baryques")
    thermal_bottles = models.CharField(
        max_length=250, verbose_name="Les bouteilles thermiques")
    thermal_tablets = models.CharField(
        max_length=250, verbose_name="Les tablettes thermiques")

    """ STEREOGNOSTIQUE"""

    title_3 = models.CharField(

        max_length=100, default='STEREOGNOSTIQUE')
    geometric_solids = models.CharField(
        max_length=250, verbose_name="Les solides géométriques")
    mystery_bag = models.CharField(
        max_length=250, verbose_name="Le sac à mystères")
    stereognostic_bag = models.CharField(
        max_length=250, verbose_name="Les sacs stéréognostiques")
    seed_sorting = models.CharField(
        max_length=250, verbose_name="Le tri des graines")

    """AUDITIF"""

    title_4 = models.CharField(
        max_length=100, default='AUDITIF')
    noise_boxes = models.CharField(
        max_length=250, verbose_name="Les boites à bruits")
    bells = models.CharField(
        max_length=250, verbose_name="Les clochettes")

    """OLFACTIF"""

    title_5 = models.CharField(
        max_length=100, default='OLFACTIF')
    smells = models.CharField(
        max_length=250, verbose_name="Les odeurs")

    """GUSTATIF"""

    title_6 = models.CharField(
        max_length=100, default='GUSTATIF')
    flavours = models.CharField(
        max_length=250, verbose_name="Les saveurs")

    """GEOGRAPHIE"""

    title_7 = models.CharField(
        max_length=100, default='GEOGRAPHIE')
    smooth_rough_globe = models.CharField(
        max_length=250, verbose_name="Le globe lisse et rugueux")
    colorful_globe = models.CharField(
        max_length=250, verbose_name="Le globe coloré")
    planisphere = models.CharField(
        max_length=250, verbose_name="Le planisphère")
    puzzles_continents = models.CharField(
        max_length=250, verbose_name="Les puzzles des continents")
    flags = models.CharField(
        max_length=250, verbose_name="Les drapeaux")
    flags_1 = models.CharField(
        max_length=250, verbose_name="Les drapeaux : nomenclature classifiée")
    land_water = models.CharField(
        max_length=250, verbose_name="Les contrastes de la terre et de l'eau")
    europe = models.CharField(
        max_length=250, verbose_name="La carte de l'Europe")

    """ART"""

    title_8 = models.CharField(
        max_length=100, default='ART')
    art = models.CharField(
        max_length=250, verbose_name="Introduction à l'art")

    """EXPERIENCES SCIENTIFIQUES"""

    title_9 = models.CharField(
        max_length=100, default='EXPERIENCES SCIENTIFIQUES')
    sink_float = models.CharField(
        max_length=250, verbose_name="Les objects qui coulent, qui flottent")
    horizontal_water = models.CharField(
        max_length=250, verbose_name="l'eau qui s'équilibre sur un plan horizontal")
    north = models.CharField(
        max_length=250, verbose_name="La direction du nord")
    water_air_1 = models.CharField(
        max_length=250, verbose_name="L'eau et l'air 1")
    water_air_2 = models.CharField(
        max_length=250, verbose_name="L'eau et l'air 2")
    water_air_3 = models.CharField(
        max_length=250, verbose_name="L'eau et l'air 3")
    electricity = models.CharField(
        max_length=250, verbose_name="L'électricité")
    magnets_1 = models.CharField(
        max_length=250, verbose_name="Les aimants 1")
    magnets_2 = models.CharField(
        max_length=250, verbose_name="Les aimants 2")

    title_10 = models.CharField(
        max_length=100, default='OBSERVATIONS')
    observations_1 = models.TextField(
        verbose_name="Trimestre 1")
    observations_2 = models.TextField(
        verbose_name="Trimestre 2")
    observations_3 = models.TextField(
        verbose_name="Trimestre 3")

    class Meta:
        verbose_name = "Materiel sensoriel"
        verbose_name_plural = "Materiel sensoriel"


class Math(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    date_start = models.CharField(max_length=5)

    """ GROUPE 1 NUMERATION DE 1 A 10"""

    title_1 = models.CharField(
        max_length=100, default='GROUPE 1 NUMERATION DE 1 A 10')
    number_bars = models.CharField(
        max_length=250, verbose_name="Les barres numériques")
    rough_numbers = models.CharField(
        max_length=250, verbose_name="Les chiffres rugueux")
    bars_numbers = models.CharField(
        max_length=250, verbose_name="Association barres et chiffres")
    spindles = models.CharField(
        max_length=250, verbose_name="Les fuseaux")
    token_game = models.CharField(
        max_length=250, verbose_name="Le jeu des jetons")
    memory_game = models.CharField(
        max_length=250, verbose_name="Le jeu de mémoire")

    """ GROUPE 2 INTRODUCTION AU SYSTEME DECIMAL ET AUX OPERATIONS"""

    title_2 = models.CharField(
        max_length=100, default='GROUPE 2 INTRODUCTION AU SYSTEME DECIMAL ET AUX OPERATIONS')
    sd_quantity = models.CharField(
        max_length=250, verbose_name="SD : 1ère présentation, quantités")
    sd_symbol = models.CharField(
        max_length=250, verbose_name="SD : 1ère présentation, symboles")
    sd_number = models.CharField(
        max_length=250, verbose_name="SD : formation des grands nombres")
    add_sd = models.CharField(
        max_length=250, verbose_name="Addition statique / dynamique")
    sous_sd = models.CharField(
        max_length=250, verbose_name="Soustraction statique / dynamique")
    multi_sd = models.CharField(
        max_length=250, verbose_name="Multiplication statique / dynamique")
    div_sd = models.CharField(
        max_length=250, verbose_name="Division statique / dynamique")
    stamps_add = models.CharField(
        max_length=250, verbose_name="Les timbres : addition S/D")
    stamps_sous = models.CharField(
        max_length=250, verbose_name="Les timbres : soustraction S/D")
    stamps_multi = models.CharField(
        max_length=250, verbose_name="Les timbres : multiplication S/D")
    stamps_div = models.CharField(
        max_length=250, verbose_name="Les timbres : division S/D")
    points_tables = models.CharField(
        max_length=250, verbose_name="La table des points")

    """ GROUPE 3 NUMERATION DE 11 A L'INFINI """

    title_3 = models.CharField(
        max_length=100, default="GROUPE 3 NUMERATION DE 11 A L'INFINI")
    quantity_11_19 = models.CharField(
        max_length=250, verbose_name="11 à 19 : les quantités")
    seguin_11_19 = models.CharField(
        max_length=250, verbose_name="11 à 19 : la 1ère table de Seguin")
    quantity_symbol_11_19 = models.CharField(
        max_length=250, verbose_name="11 à 19 : asso quantités symboles")
    seguin_11_99 = models.CharField(
        max_length=250, verbose_name="11 à 99 : la 2ème table de Seguin")
    chain_100 = models.CharField(
        max_length=250, verbose_name="La chaîne de 100")
    chain_1000 = models.CharField(
        max_length=250, verbose_name="La chaîne de 1000")
    chain_square = models.CharField(
        max_length=250, verbose_name="La chaîne du carré")
    chain_cube = models.CharField(
        max_length=250, verbose_name="La chaîne du cube")

    """ GROUPE 4 11 A 19 ASSOCIATION QUANTITES SYMBOLES"""

    title_4 = models.CharField(
        max_length=100, default="GROUPE 4 11 A 19 ASSOCIATION QUANTITES SYMBOLES")
    snake_game_add = models.CharField(
        max_length=250, verbose_name="Le jeu du serpent de l'addition")
    add_table = models.CharField(
        max_length=250, verbose_name="Le tableau de l'addition")
    memo_add_table = models.CharField(
        max_length=250, verbose_name="Tables mémo addition 1, 2, 3, 4")
    snake_game_sous = models.CharField(
        max_length=250, verbose_name="Le jeu du serpent de la soustraction")
    sous_table = models.CharField(
        max_length=250, verbose_name="Le tableau de la soustraction")
    memo_sous_table = models.CharField(
        max_length=250, verbose_name="Tables mémo soustraction 1, 2")
    memo_multi = models.CharField(
        max_length=250, verbose_name="Mémo multiplication : perles couleur")
    multi_table = models.CharField(
        max_length=250, verbose_name="Le tableau de la multiplication")
    memo_multi_table = models.CharField(
        max_length=250, verbose_name="Tables mémo multiplication 1, 2, 3")
    div_table = models.CharField(
        max_length=250, verbose_name="Le tableau de la division")
    memo_div_table = models.CharField(
        max_length=250, verbose_name="Tables mémo division 1, 2")

    """ GROUPE 5 LE PASSAGE A L'ABSTRACTION """

    title_5 = models.CharField(
        max_length=100, default="GROUPE 5 LE PASSAGE A L'ABSTRACTION")
    little_abacus = models.CharField(
        max_length=250, verbose_name="Petit boulier : présentation")
    little_abacus_add_sd = models.CharField(
        max_length=250, verbose_name="Petit boulier : addition S/D")
    little_abacus_sous_sd = models.CharField(
        max_length=250, verbose_name="Petit boulier : SOUSTRACTION S/D")
    little_abacus_multi_sd = models.CharField(
        max_length=250, verbose_name="Petit boulier : MULTIPLICATION S/D")
    hierarchies_quantity_symbol = models.CharField(
        max_length=250, verbose_name="Hiérarchies : quantités, symboles, association")
    large_abacus = models.CharField(
        max_length=250, verbose_name="Grand boulier : présentation")
    large_add_sd = models.CharField(
        max_length=250, verbose_name="Grand boulier : addition S/D")
    large_sous_sd = models.CharField(
        max_length=250, verbose_name="Grand boulier : soustraction S/D")
    large_multi_sd = models.CharField(
        max_length=250, verbose_name="Grand boulier : multiplication S/D")
    div_tube = models.CharField(
        max_length=250, verbose_name="La grande division avec tubes")

    """ GROUPE 6 LES FRACTIONS """
    title_6 = models.CharField(
        max_length=100, default="GROUPE 6 LES FRACTIONS")
    div_name = models.CharField(
        max_length=250, verbose_name="Les nommer")
    div_write = models.CharField(
        max_length=250, verbose_name="Les écrire")
    find_equivalences = models.CharField(
        max_length=250, verbose_name="Rechercher les équivalences")
    make_operations = models.CharField(
        max_length=250, verbose_name="Faire des opérations")

    title_7 = models.CharField(
        max_length=100, default='OBSERVATIONS')
    observations_1 = models.TextField(
        verbose_name="Trimestre 1")
    observations_2 = models.TextField(
        verbose_name="Trimestre 2")
    observations_3 = models.TextField(
        verbose_name="Trimestre 3")

    class Meta:
        verbose_name = "Mathématiques"
        verbose_name_plural = "Mathématiques"


class Langage(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    date_start = models.CharField(max_length=5)

    """ ENRICHISSEMENT DU VOCABULAIRE"""

    title_1 = models.CharField(
        max_length=100, default="ENRICHISSEMENT DU VOCABULAIRE")
    img_before_read = models.CharField(
        max_length=250, verbose_name="Images classifiées avant lecture")
    stories_told = models.CharField(
        max_length=250, verbose_name="Histoires racontées")
    libraries = models.CharField(
        max_length=250, verbose_name="Bibliothèques")
    farm = models.CharField(
        max_length=250, verbose_name="La ferme")
    nomenclature_before_read = models.CharField(
        max_length=250, verbose_name="Nomenclature avant lecture")
    question_game = models.CharField(
        max_length=250, verbose_name="Le jeu des questions")

    """ PREPARATION ECRITURE ET LECTURE """

    title_2 = models.CharField(
        max_length=100, default="PREPARATION ECRITURE ET LECTURE")
    sound_analysis_game = models.CharField(
        max_length=250, verbose_name="Le jeu d'analyse des sons")
    rough_letters_diagrams = models.CharField(
        max_length=250, verbose_name="Les lettres et diagrammes rugUeux")
    design_shapes = models.CharField(
        max_length=250, verbose_name="Les formes à dessins")
    mobile_alphabets_1_2 = models.CharField(
        max_length=250, verbose_name="Les alphabets mobiles 1 & 2")
    slates = models.CharField(

        max_length=250, verbose_name="Les ardoises")
    write_different_media = models.CharField(

        max_length=250, verbose_name="Ecrire : différents supports")
    box_objects_1 = models.CharField(

        max_length=250, verbose_name="La 1ère boite d'objets")
    box_objects_2 = models.CharField(

        max_length=250, verbose_name="La 2ème boite d'objets")
    homophony_covers = models.CharField(

        max_length=250, verbose_name="Les pochettes d'homophonies")
    img_after_read = models.CharField(

        max_length=250, verbose_name="Images classifiées après lecture")
    read_different_media = models.CharField(

        max_length=250, verbose_name="Lire : différents supports")

    """ LA NATURE DES MOTS """

    title_3 = models.CharField(
        max_length=100, default="LA NATURE DES MOTS")
    article = models.CharField(
        max_length=250, verbose_name="L'article")
    adjective = models.CharField(
        max_length=250, verbose_name="L'adjectif")
    logical_adjective_game = models.CharField(
        max_length=250, verbose_name="Le jeu de l'adjectif logique")
    detective_game = models.CharField(
        max_length=250, verbose_name="Le jeu du détective")
    conjunction = models.CharField(
        max_length=250, verbose_name="La conjonction")
    preposition = models.CharField(
        max_length=250, verbose_name="La préposition")
    logical_preposition_game = models.CharField(
        max_length=250, verbose_name="Le jeu de la préposition logique")
    verb = models.CharField(
        max_length=250, verbose_name="Le verbe : différents aspects")
    adverb = models.CharField(
        max_length=250, verbose_name="L'adverbe")
    logical_adverb_game = models.CharField(
        max_length=250, verbose_name="Le jeu de l'adverbe logique")
    orders_123 = models.CharField(
        max_length=250, verbose_name="Les ordres 1, 2, 3")

    """ETUDE DE MOTS"""
    title_4 = models.CharField(
        max_length=100, default="ETUDE DE MOT")
    singular_plural = models.CharField(
        max_length=250, verbose_name="Singulier - pluriel")
    male_female = models.CharField(
        max_length=250, verbose_name="Masculin - féminin")
    compound_words = models.CharField(
        max_length=250, verbose_name="Mots composés")
    family_words = models.CharField(
        max_length=250, verbose_name="Famille de mots")
    prefixes = models.CharField(
        max_length=250, verbose_name="Préfixes")
    suffixes = models.CharField(
        max_length=250, verbose_name="Suffixes")

    """ANALYSE DE LA LECTURE"""

    title_5 = models.CharField(
        max_length=100, default="ANALYSE DE LA LECTURE")
    sentence_analysis_1 = models.CharField(
        max_length=250, verbose_name="Analyse de la phrase, stade 1")
    sentence_analysis_2 = models.CharField(
        max_length=250, verbose_name="Analyse de la phrase, stade 2")

    """ MUSIQUE """

    title_6 = models.CharField(
        max_length=100, default="MUSIQUE")
    name_bells = models.CharField(
        max_length=250, verbose_name="Le nom des clochettes")
    sharp_flat = models.CharField(
        max_length=250, verbose_name="Dièse et bémol")
    read_write_music = models.CharField(
        max_length=250, verbose_name="Lecture et écriture musicale")
    bass_clef = models.CharField(
        max_length=250, verbose_name="La clé de Fa")
    read_sheet_music = models.CharField(
        max_length=250, verbose_name="Lecture de partitions")

    title_7 = models.CharField(
        max_length=100, default='OBSERVATIONS')
    observations_1 = models.TextField(
        verbose_name="Trimestre 1")
    observations_2 = models.TextField(
        verbose_name="Trimestre 2")
    observations_3 = models.TextField(
        verbose_name="Trimestre 3")

    class Meta:
        verbose_name = "Langage"
        verbose_name_plural = "Langage"


class Letter(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    date_start = models.CharField(max_length=5)
    letter_a = models.CharField(
        max_length=250, verbose_name="A")

    letter_b = models.CharField(
        max_length=250, verbose_name="B")
    letter_c = models.CharField(
        max_length=250, verbose_name="C")
    letter_d = models.CharField(
        max_length=250, verbose_name="D")
    letter_e = models.CharField(
        max_length=250, verbose_name="E")
    letter_f = models.CharField(
        max_length=250, verbose_name="F")
    letter_g = models.CharField(
        max_length=250, verbose_name="G")
    letter_h = models.CharField(
        max_length=250, verbose_name="H")
    letter_i = models.CharField(
        max_length=250, verbose_name="I")
    letter_j = models.CharField(
        max_length=250, verbose_name="J")
    letter_k = models.CharField(
        max_length=250, verbose_name="K")
    letter_l = models.CharField(
        max_length=250, verbose_name="L")
    letter_m = models.CharField(
        max_length=250, verbose_name="M")
    letter_n = models.CharField(
        max_length=250, verbose_name="N")
    letter_o = models.CharField(
        max_length=250, verbose_name="O")
    letter_p = models.CharField(
        max_length=250, verbose_name="P")
    letter_q = models.CharField(
        max_length=250, verbose_name="Q")
    letter_r = models.CharField(
        max_length=250, verbose_name="R")
    letter_s = models.CharField(
        max_length=250, verbose_name="S")
    letter_t = models.CharField(
        max_length=250, verbose_name="T")
    letter_u = models.CharField(
        max_length=250, verbose_name="U")
    letter_v = models.CharField(
        max_length=250, verbose_name="V")
    letter_w = models.CharField(
        max_length=250, verbose_name="W")
    letter_x = models.CharField(
        max_length=250, verbose_name="X")
    letter_y = models.CharField(
        max_length=250, verbose_name="Y")
    letter_z = models.CharField(
        max_length=250, verbose_name="Z")

    class Meta:
        verbose_name = "Lettre"
        verbose_name_plural = "Lettres"


