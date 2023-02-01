"""
A small list of molecules used to validate and tests computation.
"""

import copy

from qcelemental.models import Molecule

_test_mols = {
    "hydrogen": {
        "symbols": ["H", "H"],
        "geometry": [[0, 0, -0.65], [0.0, 0.0, 0.65]],
        "molecular_multiplicity": 1,
        "connectivity": [[0, 1, 1]],
    },
    "lithium": {"symbols": ["Li"], "geometry": [0, 0, 0], "molecular_multiplicity": 2, "connectivity": None},
    "water": {
        "geometry": [
            [0.0, 0.0, -0.1294769411935893],
            [0.0, -1.494187339479985, 1.0274465079245698],
            [0.0, 1.494187339479985, 1.0274465079245698],
        ],
        "symbols": ["O", "H", "H"],
        "connectivity": [[0, 1, 1], [0, 2, 1]],
    },
    "eneyne": {
        "symbols": ["C", "C", "H", "H", "H", "H", "C", "C", "H", "H"],
        "fragments": [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9]],
        "geometry": [
            [0.000000, -0.667578, -2.124659],
            [0.000000, 0.667578, -2.124659],
            [0.923621, -1.232253, -2.126185],
            [-0.923621, -1.232253, -2.126185],
            [-0.923621, 1.232253, -2.126185],
            [0.923621, 1.232253, -2.126185],
            [0.000000, 0.000000, 2.900503],
            [0.000000, 0.000000, 1.693240],
            [0.000000, 0.000000, 0.627352],
            [0.000000, 0.000000, 3.963929],
        ],
    },
    "ethane": {
        "geometry": [
            [+1.54034068369141, -1.01730823913235, +0.93128102073425],
            [+4.07197633001232, -0.09756825926424, -0.02203578938791],
            [+0.00025636057017, +0.00139534039687, +0.00111211603233],
            [+1.30983130616505, -3.03614919350581, +0.54918567185649],
            [+1.38003941036405, -0.71812565437083, +2.97078783593882],
            [+5.61209917480096, -1.11612498901607, +0.90799157528946],
            [+4.30241880148479, +1.92102238874847, +0.36057345099335],
            [+4.23222331256867, -0.39619160402976, -2.06158817835790],
        ],
        "symbols": ["C", "C", "H", "H", "H", "H", "H", "H"],
        "connectivity": [[0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [1, 5, 1], [1, 6, 1], [1, 7, 1]],
    },
    "mindless-01": {
        "symbols": ["Na", "H", "O", "H", "F", "H", "H", "O", "N", "H", "H", "Cl", "B", "B", "N", "Al"],
        "geometry": [
            [-1.85528263484662, +3.58670515364616, -2.41763729306344],
            [+4.40178023537845, +0.02338844412653, -4.95457749372945],
            [-2.98706033463438, +4.76252065456814, +1.27043301573532],
            [+0.79980886075526, +1.41103455609189, -5.04655321620119],
            [-4.20647469409936, +1.84275767548460, +4.55038084858449],
            [-3.54356121843970, -3.18835665176557, +1.46240021785588],
            [+2.70032160109941, +1.06818452504054, -1.73234650374438],
            [+3.73114088824361, -2.07001543363453, +2.23160937604731],
            [-1.75306819230397, +0.35951417150421, +1.05323406177129],
            [+5.41755788583825, -1.57881830078929, +1.75394002750038],
            [-2.23462868255966, -2.13856505054269, +4.10922285746451],
            [+1.01565866207568, -3.21952154552768, -3.36050963020778],
            [+2.42119255723593, +0.26626435093114, -3.91862474360560],
            [-3.02526098819107, +2.53667889095925, +2.31664984740423],
            [-2.00438948664892, -2.29235136977220, +2.19782807357059],
            [+1.12226554109716, -1.36942007032045, +0.48455055461782],
        ],
    },
    "mindless-02": {
        "symbols": ["H", "S", "B", "O", "Mg", "H", "H", "H", "Si", "H", "B", "Li", "F", "H", "H", "S"],
        "geometry": [
            [-1.79537625851198, -3.77866422935275, -1.07883558363403],
            [-2.68278833302782, +0.38892666265890, +1.66214865238427],
            [+0.11484649791305, +1.48857933226955, +3.65660396510375],
            [-1.07998879593946, -0.16259121615748, -4.55703065871422],
            [+0.60302832999383, +4.08816149622342, -0.02589373148029],
            [-1.22534089315880, -1.79981382478068, -3.70773173318592],
            [-1.33460982049866, -4.24819082475503, +2.72791902701083],
            [-0.16278082578516, +2.41267994179303, +5.69030695190570],
            [+2.87802444057103, -0.33120525058830, +1.88311373530297],
            [+0.68489327931487, +0.32790204044961, -4.20547693710673],
            [-1.20919773588330, -2.87253762561437, +0.94064204223101],
            [-3.25572604597922, +2.21241092990940, -2.86715549314771],
            [-1.83147468262373, +5.20527293771933, -2.26976270603341],
            [+4.90885865772880, -1.92576561961811, +2.99069919443735],
            [+1.26806242248758, -2.60409341782411, +0.55162805282247],
            [+4.11956976339902, +1.59892866766766, -1.39117477789609],
        ],
        "molecular_multiplicity": 2,
    },
    "mindless-03": {
        "symbols": ["C", "O", "H", "Li", "Mg", "Al", "C", "H", "H", "H", "F", "S", "C", "H", "Na", "H"],
        "geometry": [
            [-0.02148551327524, -0.67161751504297, -4.75078512817560],
            [+1.37792545875526, -3.24818416423144, +3.83896600631495],
            [-2.23986953822894, +1.64550402751694, +3.42773272178522],
            [-0.87622711432790, -2.74068400827752, +1.43723692979592],
            [+1.29492470653815, +1.86470311043681, -1.04536500695239],
            [-3.65768365013010, +0.45437052179208, -1.41566056087159],
            [-0.23245910487384, -1.83274112101585, -2.43395808606122],
            [+0.30373451850419, -3.84228931776777, -2.44882782867802],
            [-3.36159503902161, +4.20056392581975, +1.63352684198071],
            [+0.49372989648081, -1.56245253044952, -6.53610501083288],
            [+4.38566058812996, +1.86127331114460, +0.56178822055152],
            [-1.17545963764009, +2.49456345795141, -4.90195191215762],
            [-1.86623614216854, +2.76329843590746, +1.71572598870213],
            [+1.02361259176985, -4.24377370348987, +5.32418288889440],
            [+4.71194535010347, -1.03648125005561, +3.35573062118779],
            [-0.16051737061546, +3.89394681976155, +2.23776331451663],
        ],
    },
    "mindless-04": {
        "symbols": ["H", "B", "H", "F", "B", "H", "H", "Si", "H", "H", "C", "Al", "Si", "O", "H", "B"],
        "geometry": [
            [-1.34544890768411, +2.85946545334720, +3.11183388215396],
            [-0.36293929605305, +4.15983774640545, +1.36413101934678],
            [-3.36268280924844, +4.92951597114402, -3.59085684882314],
            [+3.78143178536443, -4.97181356229699, +1.59003443639387],
            [+3.44227417874042, -3.46504338606415, +3.62082644591507],
            [+1.88917586252014, +3.42088101960529, +1.28872629783483],
            [-0.32747529934233, -4.29711514977711, -3.55330460209973],
            [-3.58768360829779, -1.39509759062952, -1.10396714572410],
            [-0.39440896193088, +6.31837673143592, +1.99105318714945],
            [+4.34376903295874, -4.12502353873667, +5.57829602371555],
            [-1.39570266622309, -2.60410756418652, -4.03149806979915],
            [+0.21788515354592, +0.28610741675369, +1.29731097788136],
            [-2.00000183598828, +3.04473467156937, -2.00578147078785],
            [+2.12833842504876, -1.30141517432227, +3.38069910888504],
            [-2.48411958079522, -2.81581487156584, -5.76829803496286],
            [-0.54241147261516, -0.04348817268188, -3.16920520707912],
        ],
    },
    "mindless-05": {
        "symbols": ["B", "P", "H", "H", "B", "P", "H", "Cl", "N", "H", "P", "Si", "H", "H", "P", "N"],
        "geometry": [
            [+0.68391902268453, +0.21679405065309, -2.81441127558071],
            [-2.67199537993843, -3.97743927106200, +0.03497540139192],
            [+2.02325266152397, -0.16048070975416, -0.41980608052722],
            [+4.26224346168617, +3.65384961705338, -2.81836810458488],
            [-2.80378310343644, +1.84796600006216, +0.15107304476153],
            [+1.58317082705122, +3.77079801391042, -2.86230158107979],
            [+2.63670178694113, +3.13142099211650, +2.24139937019049],
            [-6.27112533979613, -3.92471014080274, +1.62562669834852],
            [-0.92594349239390, -2.94451283088352, +2.60616476876177],
            [-1.79532342290201, -1.56841672860834, +3.65515689388732],
            [-3.01460634915379, -0.47748181717446, -2.44834110183776],
            [+2.18249449208515, -2.23505035804805, +1.77725119258081],
            [+3.26068149442689, -4.54078259646428, +0.57204329987377],
            [+1.73744972267909, -1.18654391698320, -4.24063427353503],
            [+0.94405328902426, +4.99525793054843, +1.18501287451328],
            [-1.83118967048165, +3.39933176543682, +1.75515887283605],
        ],
        "molecular_multiplicity": 2,
    },
    "L-alanine": {
        "symbols": ["C", "N", "C", "O", "O", "H", "H", "H", "H", "C", "H", "H", "H"],
        "geometry": [
            [-0.67019300, 0.14070600, -0.40132000],
            [-1.55028000, -1.02241500, -0.33971900],
            [0.77902000, -0.16783400, -0.00263000],
            [1.14641500, -1.13427800, 0.64248600],
            [1.64699000, 0.78741600, -0.44500800],
            [2.53138800, 0.52936000, -0.12771500],
            [-1.21914400, -1.74668300, -0.97336400],
            [-0.64576800, 0.50574300, -1.43351600],
            [-1.50838700, -1.42717100, 0.59430400],
            [-1.20949300, 1.26879500, 0.49961500],
            [-0.57946200, 2.15935800, 0.43742200],
            [-2.22420300, 1.52057100, 0.18314600],
            [-1.24570800, 0.94061700, 1.54394000],
        ],
        "connectivity": [
            [0, 1, 1],
            [0, 2, 1],
            [0, 7, 1],
            [0, 9, 1],
            [1, 6, 1],
            [1, 8, 1],
            [2, 3, 2],
            [2, 4, 1],
            [4, 5, 1],
            [9, 10, 1],
            [9, 11, 1],
            [9, 12, 1],
        ],
    },
}


def get_molecule(name):
    """
    Returns a QC JSON representation of a test molecule.
    """
    if name not in _test_mols:
        raise KeyError("Molecule name '{}' not found".format(name))

    return Molecule(**copy.deepcopy(_test_mols[name]))
