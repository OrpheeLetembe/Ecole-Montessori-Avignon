from django import forms


from .models import PracticalLife, SensoryMaterial, Math, Langage, Letter


class PracticalLifeForm(forms.ModelForm):

    """ EXERCICES PRELIMINAIRES """

    title_1 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    move_mood = forms.CharField(
        label="Se déplacer dans l'ambiance",
        required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    carry_table = forms.CharField(
        label="Porter une table seul, à deux",
        required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    Carry_tray = forms.CharField(
        label="Porter un plateau",
        required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    Carrying_mat = forms.CharField(
        label="Porter, dérouler et rouler un tapis",
        required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    open_close_door = forms.CharField(
        label="Ouvrir et fermer une porte",
        required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    open_close_window = forms.CharField(
        label="Ouvrir et fermer une fenêtre, un tiroir",
        required=False, widget=forms.TextInput(attrs={"class": "form-control"}))

    """ SOIN DU MILEU INTERIEUR """

    title_2 = forms.CharField(label="", disabled=True,
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    squeeze_sponge = forms.CharField(
        label="Presser une éponge", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    Screw_bolts = forms.CharField(
        label="Visser, dévisser des boulons", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    screwdriver = forms.CharField(
        label="Utiliser un tournevis", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    open_close_padlock = forms.CharField(
        label="Ouvrir et fermer un cadenas", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    use_clothes_pegs = forms.CharField(
        label="Se servir de pinces à linge", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    open_close_boxes = forms.CharField(
        label="Ouvrir et fermer des boites",
        required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    open_close_bottles = forms.CharField(
        label="Ouvrir et fermer des flacons",
        required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    fold_fabrics = forms.CharField(
        label="Plier des étoffes", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    fold_paper = forms.CharField(
        label="Plier du papier", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    cut_paper_scissors = forms.CharField(
        label="Couper du papier avec des ciseaux",
        required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    paste_paper = forms.CharField(
        label="Coller du papier", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    dust = forms.CharField(
        label="Epousseter avec un chiffon, un plumeau",
        required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    sweep = forms.CharField(
        label="Balayer", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    brush_carpet = forms.CharField(
        label="Brosser un tapis", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    transfer_spoon = forms.CharField(
        label="Transvaser avec une cuillère", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    pour_rice = forms.CharField(
        label="Verser du riz", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    pour_sand = forms.CharField(
        label="Verser du sable", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    pour_water = forms.CharField(
        label="Verser de l'eau", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    pour_water_glasses = forms.CharField(
        label="Verser de l'eau dans des verres", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    clean_mirror = forms.CharField(
        label="Nettoyer un miroir", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    polish_brass = forms.CharField(
        label="Astiquer les cuivres", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    take_care_plants = forms.CharField(
        label="Soigner les plantes", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    chang_flower_water = forms.CharField(
        label="Changer l'eau des fleurs", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    wash_table = forms.CharField(
        label="Laver la table", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    wash_clothes = forms.CharField(
        label="Laver du linge", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    stitching = forms.CharField(
        label="Piquage", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """ SOIN DE LA PERSONNE"""

    title_3 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    frame_press_studs = forms.CharField(
        label="Cadre à boutons pressions", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    frame_big_studs = forms.CharField(
        label="Cadre à gros boutons", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    frame_small_studs = forms.CharField(
        label="Cadre à petits boutons", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    frame_slide = forms.CharField(
        label="Cadre à glissière", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    frame_staple = forms.CharField(
        label="Cadre à agrafes", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    frame_loop = forms.CharField(
        label="Cadre à boucles", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    frame_safety_pin = forms.CharField(
        label="Cadre à épingles à nourrice", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    frame_node = forms.CharField(
        label="Cadre à noeuds", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    frame_lacing = forms.CharField(
        label="Cadre à laçage", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    wash_hands = forms.CharField(
        label="Se laver les mains", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    make_bread = forms.CharField(
        label="Faire le pain", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    fresh_fruit = forms.CharField(
        label="Préparer les fruits frais", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    shine_shoes = forms.CharField(
        label="Cirer ses chaussures", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    sew = forms.CharField(
        label="Coudre", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """ JEUX COLLECTIFS"""
    title_4 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    walk_line = forms.CharField(
        label="Marcher sur la ligne", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    lesson_silence = forms.CharField(
        label="Leçon de silence", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    title_5 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    observations_1 = forms.CharField(
        label="Trimestre 1", required=False,
        widget=forms.Textarea(attrs={"rows": 8, "cols": 81}))
    observations_2 = forms.CharField(
        label="Trimestre 2", required=False,
        widget=forms.Textarea(attrs={"rows": 8, "cols": 81}))
    observations_3 = forms.CharField(
        label="Trimestre 2", required=False,
        widget=forms.Textarea(attrs={"rows": 8, "cols": 81}))

    class Meta:
        model = PracticalLife
        exclude = ('student', 'date_start')


class SensoryMaterialForm(forms.ModelForm):

    """ VISUEL"""

    title_1 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    cylindrical_sockets_1 = forms.CharField(
        label="Emboitements cylindriques 1", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    cylindrical_sockets_2 = forms.CharField(
        label="Emboitements cylindriques 2", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    cylindrical_sockets_3 = forms.CharField(
        label="Emboitements cylindriques 3", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    cylindrical_sockets_4 = forms.CharField(
        label="Emboitements cylindriques 4", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    pink_tower = forms.CharField(
        label="La tour rose", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    brown_staircase = forms.CharField(
        label="L'escalier marron", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    red_bars = forms.CharField(
        label="Les barres rouges", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    color_table_1 = forms.CharField(
        label="Les tables des couleurs 1", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    color_table_2 = forms.CharField(
        label="Les tables des couleurs 2", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    color_table_3 = forms.CharField(
        label="Les tables des couleurs 3", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    geometry_tray = forms.CharField(
        label="Le cabinet de géométrie/plateau", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    geometry_drawers = forms.CharField(
        label="Le cabinet de géométrie/tiroirs", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    geometry_maps = forms.CharField(
        label="Le cabinet de géométrie/cartes", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    constructor_triangles_1 = forms.CharField(
        label="Les triangles constructeurs 1", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    constructor_triangles_2 = forms.CharField(
        label="Les triangles constructeurs 2", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    constructor_triangles_3 = forms.CharField(
        label="Les triangles constructeurs 3", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    constructor_triangles_4 = forms.CharField(
        label="Les triangles constructeurs 4", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    constructor_triangles_5 = forms.CharField(
        label="Les triangles constructeurs 5", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    constructor_triangles_6 = forms.CharField(
        label="Les triangles constructeurs 6", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    superimposed_figures = forms.CharField(
        label="Les figures superposées", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    binomial_cube = forms.CharField(
        label="Le cube du binôme", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    trinomial_cube = forms.CharField(
        label="Le cube du trinôme", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    pythagore_table = forms.CharField(
        label="La table de Pythagore", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    colored_cylinders = forms.CharField(
        label="Les cylindres de couleur", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    botanical_tray = forms.CharField(
        label="Le cabinet de botaniques/plateau", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    botanical_maps = forms.CharField(
        label="Le cabinet de botaniques/cartes", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    roman_arch = forms.CharField(
        label="L'arche romane", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """ TACTILE"""

    title_2 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    smooth_rough = forms.CharField(
        label="Lisse et rugueux", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    smooth_rough_table = forms.CharField(
        label="Lisse et rugueux : les tablettes", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    fabrics = forms.CharField(
        label="Les étoffes", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    baryque_tablets = forms.CharField(
        label="Les tablettes baryques", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    thermal_bottles = forms.CharField(
        label="Les bouteilles thermiques", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    thermal_tablets = forms.CharField(
        label="Les tablettes thermiques", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """ STEREOGNOSTIQUE"""

    title_3 = forms.CharField(label="", disabled=True,
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    geometric_solids = forms.CharField(
        label="Les solides géométriques", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    mystery_bag = forms.CharField(
        label="Le sac à mystères", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    stereognostic_bag = forms.CharField(
        label="Les sacs stéréognostiques", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    seed_sorting = forms.CharField(
        label="Le tri des graines", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """AUDITIF"""

    title_4 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    noise_boxes = forms.CharField(
        label="Les boites à bruits", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    bells = forms.CharField(
        label="Les clochettes", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """OLFACTIF"""
    title_5 = forms.CharField(label="", disabled=True,
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    smells = forms.CharField(
        label="Les odeurs", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """GUSTATIF"""
    title_6 = forms.CharField(label="", disabled=True,
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    flavours = forms.CharField(
        label="Les saveurs", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """GEOGRAPHIE"""
    title_7 = forms.CharField(label="", disabled=True,
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    smooth_rough_globe = forms.CharField(
        label="Le globe lisse et rugueux", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    colorful_globe = forms.CharField(
        label="Le globe coloré", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    planisphere = forms.CharField(
        label="Le planisphère", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    puzzles_continents = forms.CharField(
        label="Les puzzles des continents", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    flags = forms.CharField(
        label="Les drapeaux", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    flags_1 = forms.CharField(
        label="Les drapeaux : nomenclature classifiée", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    land_water = forms.CharField(
        label="Les contrastes de la terre et de l'eau",  required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    europe = forms.CharField(
        label="La carte de l'Europe", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """ART"""
    title_8 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    art = forms.CharField(
        label="Introduction à l'art", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """EXPERIENCES SCIENTIFIQUES"""
    title_9 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    sink_float = forms.CharField(
        label="Les objets qui coulent, qui flottent", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    horizontal_water = forms.CharField(
        label="l'eau qui s'équilibre sur un plan horizontal", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    north = forms.CharField(
        label="La direction du nord", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    water_air_1 = forms.CharField(
        label="L'eau et l'air 1", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    water_air_2 = forms.CharField(
        label="L'eau et l'air 3", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    water_air_3 = forms.CharField(
        label="L'eau et l'air 3", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    electricity = forms.CharField(
        label="L'électricité", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    magnets_1 = forms.CharField(
        label="Les aimants 1", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    magnets_2 = forms.CharField(
        label="Les aimants 2", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    title_10 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    observations_1 = forms.CharField(
        label="Trimestre 1", required=False,
        widget=forms.Textarea(attrs={"rows": 8, "cols": 81}))
    observations_2 = forms.CharField(
        label="Trimestre 2", required=False,
        widget=forms.Textarea(attrs={"rows": 8, "cols": 81}))
    observations_3 = forms.CharField(
        label="Trimestre 3", required=False,
        widget=forms.Textarea(attrs={"rows": 8, "cols": 81}))

    class Meta:
        model = SensoryMaterial
        exclude = ('student', 'date_start')


class MathForm(forms.ModelForm):

    """ GROUPE 1 NUMERATION DE 1 A 10"""
    title_1 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    number_bars = forms.CharField(
        label="Les barres numériques", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    rough_numbers = forms.CharField(
        label="Les chiffres rugueux", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    bars_numbers = forms.CharField(
        label="Association barres et chiffres", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    spindles = forms.CharField(
        label="Les fuseaux", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    token_game = forms.CharField(
        label="Le jeu des jetons", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    memory_game = forms.CharField(
        label="Le jeu de mémoire", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """ GROUPE 2 INTRODUCTION AU SYSTEME DECIMAL ET AUX OPERATIONS"""
    title_2 = forms.CharField(label="", disabled=True,
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    sd_quantity = forms.CharField(
        label="SD : 1ère présentation, quantités", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    sd_symbol = forms.CharField(
        label="SD : 1ère présentation, symboles", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    sd_number = forms.CharField(
        label="SD : formation des grands nombres", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    add_sd = forms.CharField(
        label="Addition statique / dynamique", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    sous_sd = forms.CharField(
        label="Soustraction statique / dynamique", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    multi_sd = forms.CharField(
        label="Multiplication statique / dynamique", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    div_sd = forms.CharField(
        label="Division statique / dynamique", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    stamps_add = forms.CharField(
        label="Les timbres : addition S/D", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    stamps_sous = forms.CharField(
        label="Les timbres : soustraction S/D", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    stamps_multi = forms.CharField(
        label="Les timbres : multiplication S/D", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    stamps_div = forms.CharField(
        label="Les timbres : division S/D", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    points_tables = forms.CharField(
        label="La table des points", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """ GROUPE 3 NUMERATION DE 11 A L'INFINI """

    title_3 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    quantity_11_19 = forms.CharField(
        label="11 à 19 : les quantités", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    seguin_11_19 = forms.CharField(
        label="11 à 19 : la 1ère table de Seguin", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    quantity_symbol_11_19 = forms.CharField(
        label="11 à 19 : asso quantités symboles", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    seguin_11_99 = forms.CharField(
        label="11 à 99 : la 2ème table de Seguin", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    chain_100 = forms.CharField(
        label="La chaîne de 100", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    chain_1000 = forms.CharField(
        label="La chaîne de 1000", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    chain_square = forms.CharField(
        label="La chaîne du carré", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    chain_cube = forms.CharField(
        label="La chaîne du cube", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """ GROUPE 4 11 A 19 ASSOCIATION QUANTITES SYMBOLES"""

    title_4 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    snake_game_add = forms.CharField(
        label="Le jeu du serpent de l'addition", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    add_table = forms.CharField(
        label="Le tableau de l'addition", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    memo_add_table = forms.CharField(
        label="Tables mémo addition 1, 2, 3, 4", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    snake_game_sous = forms.CharField(
        label="Le jeu du serpent de la soustraction", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    sous_table = forms.CharField(
        label="Le tableau de la soustraction", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    memo_sous_table = forms.CharField(
        label="Tables mémo soustraction 1, 2", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    memo_multi = forms.CharField(
        label="Mémo multiplication : perles couleur", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    multi_table = forms.CharField(
        label="Le tableau de la multiplication", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    memo_multi_table = forms.CharField(
        label="Tables mémo multiplication 1, 2, 3", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    div_table = forms.CharField(
        label="Le tableau de la division", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    memo_div_table = forms.CharField(
        label="Tables mémo division 1, 2", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """ GROUPE 5 LE PASSAGE A L'ABSTRACTION """

    title_5 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    little_abacus = forms.CharField(
        label="Petit boulier : présentation", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    little_abacus_add_sd = forms.CharField(
        label="Petit boulier : addition S/D", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    little_abacus_sous_sd = forms.CharField(
        label="Petit boulier : soustraction S/D", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    little_abacus_multi_sd = forms.CharField(
        label="Petit boulier : multiplication S/D", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    hierarchies_quantity_symbol = forms.CharField(
        label="Hiérarchies : quantités, symboles, association", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    large_abacus = forms.CharField(
        label="Grand boulier : présentation", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    large_add_sd = forms.CharField(
        label="Grand boulier : addition S/D", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    large_sous_sd = forms.CharField(
        label="Grand boulier : soustraction S/D", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    large_multi_sd = forms.CharField(
        label="Grand boulier : multiplication S/D", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    div_tube = forms.CharField(
        label="La grande division avec tubes", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """ GROUPE 6 LES FRACTIONS """

    title_6 = forms.CharField(label="", disabled=True,
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    div_name = forms.CharField(
        label="Les nommer", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    div_write = forms.CharField(
        label="Les écrire", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    find_equivalences = forms.CharField(
        label="Rechercher les équivalences", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    make_operations = forms.CharField(
        label="Faire des opérations", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    title_7 = forms.CharField(label="", disabled=True,
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    observations_1 = forms.CharField(
        label="Trimestre 1", required=False,
        widget=forms.Textarea(attrs={"rows": 8, "cols": 81}))
    observations_2 = forms.CharField(
        label="Trimestre 2", required=False,
        widget=forms.Textarea(attrs={"rows": 8, "cols": 81}))
    observations_3 = forms.CharField(
        label="Trimestre 3", required=False,
        widget=forms.Textarea(attrs={"rows": 8, "cols": 81}))

    class Meta:
        model = Math
        exclude = ('student', 'date_start')


class LangageForm(forms.ModelForm):

    """ ENRICHISSEMENT DU VOCABULAIRE"""

    title_1 = forms.CharField(label="", disabled=True,
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    img_before_read = forms.CharField(
        label="Images classifiées avant lecture", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    stories_told = forms.CharField(
        label="Histoires racontées", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    libraries = forms.CharField(
        label="Bibliothèques", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    farm = forms.CharField(
        label="La ferme", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    nomenclature_before_read = forms.CharField(
        label="Nomenclature avant lecture", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    question_game = forms.CharField(
        label="Le jeu des questions", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """ PREPARATION ECRITURE ET LECTURE """

    title_2 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    sound_analysis_game = forms.CharField(
        label="Le jeu d'analyse des sons", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    rough_letters_diagrams = forms.CharField(
        label="Les lettres et diagrammes rugueux", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    design_shapes = forms.CharField(
        label="Les formes à dessins", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    mobile_alphabets_1_2 = forms.CharField(
        label="Les alphabets mobiles 1 & 2", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    slates = forms.CharField(
        label="Les ardoises", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    write_different_media = forms.CharField(
        label="Ecrire : différents supports", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    box_objects_1 = forms.CharField(
        label="La 1ère boite d'objets", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    box_objects_2 = forms.CharField(
        label="La 2ème boite d'objets", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    homophony_covers = forms.CharField(
        label="Les pochettes d'homophonies", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    img_after_read = forms.CharField(
        label="Images classifiées après lecture", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    read_different_media = forms.CharField(
        label="Lire : différents supports", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """ LA NATURE DES MOTS """

    title_3 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    article = forms.CharField(
        label="L'article", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    adjective = forms.CharField(
        label="L'adjectif", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    logical_adjective_game = forms.CharField(
        label="Le jeu de l'adjectif logique", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    detective_game = forms.CharField(
        label="Le jeu du détective", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    conjunction = forms.CharField(
        label="La conjonction", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    preposition = forms.CharField(
        label="La préposition", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    logical_preposition_game = forms.CharField(
        label="Le jeu de la préposition logique", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    verb = forms.CharField(
        label="Le verbe : différents aspects", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    adverb = forms.CharField(
        label="L'adverbe", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    logical_adverb_game = forms.CharField(
        label="Le jeu de l'adverbe logique", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    orders_123 = forms.CharField(
        label="Les ordres 1, 2, 3", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """ETUDE DE MOTS"""
    title_4 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    singular_plural = forms.CharField(
        label="Singulier - pluriel", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    male_female = forms.CharField(
        label="Masculin - féminin", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    compound_words = forms.CharField(
        label="Mots composés", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    family_words = forms.CharField(
        label="Famille de mots", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    prefixes = forms.CharField(
        label="Préfixes", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    suffixes = forms.CharField(
        label="Suffixes", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """ANALYSE DE LA LECTURE"""

    title_5 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    sentence_analysis_1 = forms.CharField(
        label="Analyse de la phrase, stade 1", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    sentence_analysis_2 = forms.CharField(
        label="Analyse de la phrase, stade 2", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    """ MUSIQUE """

    title_6 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    name_bells = forms.CharField(
        label="Le nom des clochettes", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    sharp_flat = forms.CharField(
        label="Dièse et bémol", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    read_write_music = forms.CharField(
        label="Lecture et écriture musicale", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    bass_clef = forms.CharField(
        label="La clé de Fa", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    read_sheet_music = forms.CharField(
        label="Lecture de partitions", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    title_7 = forms.CharField(
        label="", disabled=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    observations_1 = forms.CharField(
        label="Trimestre 1", required=False,
        widget=forms.Textarea(attrs={"rows": 8, "cols": 81}))
    observations_2 = forms.CharField(
        label="Trimestre 2", required=False,
        widget=forms.Textarea(attrs={"rows": 8, "cols": 81}))
    observations_3 = forms.CharField(
        label="Trimestre 3", required=False,
        widget=forms.Textarea(attrs={"rows": 8, "cols": 81}))

    class Meta:
        model = Langage
        exclude = ('student', 'date_start')


class LetterForm(forms.ModelForm):
    CHOICES = (
        ('presented', 'Présentée'),
        ('traced', 'tracée'),
        ('heard', "Entendue"),
        ('read', 'Lue'),
        ('written', 'Ecrite')

    )
    letter_a = forms.CharField(
        label="A", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_b = forms.CharField(
        label="B", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_c = forms.CharField(
        label="C", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_d = forms.CharField(
        label="D", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_e = forms.CharField(
        label="E", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_f = forms.CharField(
        label="F", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_g = forms.CharField(
        label="G", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_h = forms.CharField(
        label="H", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_i = forms.CharField(
        label="I", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_j = forms.CharField(
        label="J", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_k = forms.CharField(
        label="K", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_l = forms.CharField(
        label="L", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_m = forms.CharField(
        label="M", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_n = forms.CharField(
        label="N", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_o = forms.CharField(
        label="O", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_p = forms.CharField(
        label="P", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_q = forms.CharField(
        label="Q", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_r = forms.CharField(
        label="R", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_s = forms.CharField(
        label="S", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_t = forms.CharField(
        label="T", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_u = forms.CharField(
        label="U", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_v = forms.CharField(
        label="V", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_w = forms.CharField(
        label="W", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_x = forms.CharField(
        label="X", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_y = forms.CharField(
        label="Y", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    letter_z = forms.CharField(
        label="Z", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Letter
        exclude = ('student', 'date_start')


class PrintFrom(forms.Form):
    CHOICES = (
        ('observations_1', 'Trimestre 1'),
        ('observations_2', 'Trimestre 2'),
        ('observations_3', 'Trimestre 3')
    )

    pratique_life = forms.ChoiceField(
        label="Vie Pratique", required=False,
        choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'inline'}))
    sensorial_material = forms.ChoiceField(
        label="Matériel Sensoriel", required=False,
        choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'inline'}))
    mathe = forms.ChoiceField(
        label="Mathématiques", required=False,
        choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'inline'}))
    langage = forms.ChoiceField(
        label="Langage", required=False,
        choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'inline'}))
