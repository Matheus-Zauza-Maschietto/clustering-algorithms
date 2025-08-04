from knn import knn
from genericItem import generic_item
import random

def generate_daisy():
    return generic_item({
        "petal_length": random.uniform(1.0, 3.0),
        "petal_width": random.uniform(0.1, 1.0),
        "sepal_length": random.uniform(3.5, 5.0),
        "sepal_width": random.uniform(1.0, 2.5)    
    }, 'daisy')

def generate_rose():
    return generic_item({
        "petal_length": random.uniform(4.5, 6.5),
        "petal_width": random.uniform(1.2, 2.5),
        "sepal_length": random.uniform(5.0, 7.0),
        "sepal_width": random.uniform(2.5, 3.5)
    }, 'rose')

knn_cluster = knn(k=2, items=[
    generic_item({'petal_length': 6.008022958191159, 'petal_width': 1.6967628509253159, 'sepal_length': 6.639974058154039, 'sepal_width': 2.780757164523594    }, 'daisy'),
    generic_item({'petal_length': 5.683978508179214, 'petal_width': 1.8805044874097696, 'sepal_length': 6.055358583785008, 'sepal_width': 2.6294722681955136    }, 'daisy'),
    generic_item({'petal_length': 4.711343640415009, 'petal_width': 1.6502506023382888, 'sepal_length': 5.670988236575413, 'sepal_width': 3.381688817089133    }, 'daisy'),
    generic_item({'petal_length': 6.1408042558078595, 'petal_width': 2.376800534065223, 'sepal_length': 6.157819872938919, 'sepal_width': 3.0139623057720155    }, 'daisy'),
    generic_item({'petal_length': 6.274006246585923, 'petal_width': 1.89684479085245, 'sepal_length': 6.437260969609133, 'sepal_width': 2.8390355865161205    }, 'daisy'),
    generic_item({'petal_length': 4.943884902959423, 'petal_width': 2.274992653076232, 'sepal_length': 5.066742660382031, 'sepal_width': 3.289569225640888    }, 'daisy'),
    generic_item({'petal_length': 6.471184051893343, 'petal_width': 1.7631638742151183, 'sepal_length': 5.333778165261574, 'sepal_width': 2.54381448105441    }, 'daisy'),
    generic_item({'petal_length': 5.285703428152682, 'petal_width': 1.4296826299170735, 'sepal_length': 5.567946600948419, 'sepal_width': 3.1777059949316637    }, 'daisy'),
    generic_item({'petal_length': 4.760641279344541, 'petal_width': 2.068185516107534, 'sepal_length': 5.3150826679961884, 'sepal_width': 2.885283110892889    }, 'daisy'),
    generic_item({'petal_length': 4.898231929043693, 'petal_width': 1.7321198703191882, 'sepal_length': 5.634866511084516, 'sepal_width': 3.273409084336462    }, 'daisy'),
    generic_item({'petal_length': 5.44372847636336, 'petal_width': 1.2405480178159694, 'sepal_length': 5.251579559464342, 'sepal_width': 3.4329819181533066    }, 'daisy'),
    generic_item({'petal_length': 5.355206804345113, 'petal_width': 1.321051590315223, 'sepal_length': 5.736413068945394, 'sepal_width': 2.9635460056158154    }, 'daisy'),
    generic_item({'petal_length': 5.630054864041881, 'petal_width': 1.7776452264414355, 'sepal_length': 5.550045975919267, 'sepal_width': 3.019664726520571    }, 'daisy'),
    generic_item({'petal_length': 6.27629338501684, 'petal_width': 1.872500574746741, 'sepal_length': 5.449040339112359, 'sepal_width': 3.2878303248522998    }, 'daisy'),
    generic_item({'petal_length': 6.058440302992581, 'petal_width': 2.336731797033948, 'sepal_length': 5.61230734362883, 'sepal_width': 2.689128673574817    }, 'daisy'),
    generic_item({'petal_length': 5.889238265009743, 'petal_width': 1.4644134156434323, 'sepal_length': 6.885443549319461, 'sepal_width': 3.3980959649351155    }, 'daisy'),
    generic_item({'petal_length': 5.637061878593651, 'petal_width': 1.972308198184148, 'sepal_length': 5.3753915062314865, 'sepal_width': 2.5233425393006286    }, 'daisy'),
    generic_item({'petal_length': 4.613735949766003, 'petal_width': 1.3993400520504302, 'sepal_length': 5.179520348004537, 'sepal_width': 3.313334769261048    }, 'daisy'),
    generic_item({'petal_length': 6.0941390728561124, 'petal_width': 1.7644789655237239, 'sepal_length': 5.6792927124030665, 'sepal_width': 3.229503157257772    }, 'daisy'),
    generic_item({'petal_length': 5.455660705178829, 'petal_width': 1.2935242744472828, 'sepal_length': 5.985499869837189, 'sepal_width': 3.0148028674008187    }, 'daisy'),
    generic_item({'petal_length': 5.244559912380612, 'petal_width': 1.6448326066231889, 'sepal_length': 5.249483427347447, 'sepal_width': 3.2018247645596385    }, 'daisy'),
    generic_item({'petal_length': 5.055256623397061, 'petal_width': 1.5744676132530762, 'sepal_length': 5.8212792724065, 'sepal_width': 3.1965497420306983    }, 'daisy'),
    generic_item({'petal_length': 4.50488427676107, 'petal_width': 1.7023370657606332, 'sepal_length': 5.3014600111700965, 'sepal_width': 3.0061651421997793    }, 'daisy'),
    generic_item({'petal_length': 6.309443486825908, 'petal_width': 1.9909978619196742, 'sepal_length': 6.139466431993298, 'sepal_width': 3.440094748971134    }, 'daisy'),
    generic_item({'petal_length': 6.191926067853451, 'petal_width': 2.2031461856634817, 'sepal_length': 6.378785559423452, 'sepal_width': 3.272345652306087    }, 'daisy'),

    generic_item({'petal_length': 1.9667078135793794, 'petal_width': 0.18507653363790896, 'sepal_length': 3.534977343028928, 'sepal_width': 2.4319633559714795    }, 'rose'),
    generic_item({'petal_length': 1.9979488001918932, 'petal_width': 0.4238731596770363, 'sepal_length': 3.894979633544268, 'sepal_width': 2.3946423837148063    }, 'rose'),
    generic_item({'petal_length': 1.8154562641274565, 'petal_width': 0.639921373206554, 'sepal_length': 4.648738024446703, 'sepal_width': 1.0780645785991756    }, 'rose'),
    generic_item({'petal_length': 1.6433684613914592, 'petal_width': 0.9756196691359998, 'sepal_length': 4.5046666488292555, 'sepal_width': 1.8398074454972815    }, 'rose'),
    generic_item({'petal_length': 2.0805955317778357, 'petal_width': 0.9864579095735282, 'sepal_length': 4.808934849913925, 'sepal_width': 1.3468589918476317    }, 'rose'),
    generic_item({'petal_length': 2.6735763691707026, 'petal_width': 0.7818487182734172, 'sepal_length': 4.277877883358537, 'sepal_width': 1.6575319981745027    }, 'rose'),
    generic_item({'petal_length': 2.988874003552374, 'petal_width': 0.47316378844256823, 'sepal_length': 4.53784851452718, 'sepal_width': 2.2496630818046386    }, 'rose'),
    generic_item({'petal_length': 1.415697729020027, 'petal_width': 0.5440917666293402, 'sepal_length': 4.385753984686733, 'sepal_width': 1.6965782625032428    }, 'rose'),
    generic_item({'petal_length': 2.2471268441617758, 'petal_width': 0.2888897868243751, 'sepal_length': 4.748321491601833, 'sepal_width': 1.0523582574321617    }, 'rose'),
    generic_item({'petal_length': 2.456367350314718, 'petal_width': 0.4039919130855576, 'sepal_length': 3.8019183166160824, 'sepal_width': 2.0336141815637196    }, 'rose'),
    generic_item({'petal_length': 1.8694679018888283, 'petal_width': 0.7046556532474297, 'sepal_length': 3.6815709981097333, 'sepal_width': 2.2735935091128834    }, 'rose'),
    generic_item({'petal_length': 2.3870142806459023, 'petal_width': 0.2852958439303123, 'sepal_length': 4.8394518867005125, 'sepal_width': 1.1231165297382004    }, 'rose'),
    generic_item({'petal_length': 2.906393339041937, 'petal_width': 0.15831819095602745, 'sepal_length': 3.8512678678439243, 'sepal_width': 1.6916034354680771    }, 'rose'),
    generic_item({'petal_length': 2.8702984146644006, 'petal_width': 0.21759053919658145, 'sepal_length': 4.727860432032157, 'sepal_width': 2.2380401713180644    }, 'rose'),
    generic_item({'petal_length': 1.2124725037981559, 'petal_width': 0.25332149922515057, 'sepal_length': 3.579788861999143, 'sepal_width': 1.2601849180938536    }, 'rose'),
    generic_item({'petal_length': 1.3933438574935766, 'petal_width': 0.4352944108443766, 'sepal_length': 4.785733824905574, 'sepal_width': 2.412984611503805    }, 'rose'),
    generic_item({'petal_length': 2.1556819496051043, 'petal_width': 0.7977951621512834, 'sepal_length': 3.609344025730921, 'sepal_width': 1.1910250852905595    }, 'rose'),
    generic_item({'petal_length': 1.2486411679038083, 'petal_width': 0.1822577828948292, 'sepal_length': 3.573032762297352, 'sepal_width': 2.273729883603161    }, 'rose'),
    generic_item({'petal_length': 2.6162127015036667, 'petal_width': 0.9293468490251668, 'sepal_length': 4.601315852784247, 'sepal_width': 2.267181936768208    }, 'rose'),
    generic_item({'petal_length': 1.172377184935379, 'petal_width': 0.5234414529606316, 'sepal_length': 4.946478176075985, 'sepal_width': 1.3076328367104617    }, 'rose'),
    generic_item({'petal_length': 1.2886244046412283, 'petal_width': 0.8432888937753571, 'sepal_length': 3.864848106154672, 'sepal_width': 1.564886452424418    }, 'rose'),
    generic_item({'petal_length': 1.8204404487966628, 'petal_width': 0.8477249422425585, 'sepal_length': 4.2104202050263435, 'sepal_width': 1.4936462141841116    }, 'rose'),
    generic_item({'petal_length': 1.1453617040070594, 'petal_width': 0.5634243763929525, 'sepal_length': 4.2607683475878195, 'sepal_width': 1.249930600548892    }, 'rose'),
    generic_item({'petal_length': 2.6946041426826257, 'petal_width': 0.2053142143787134, 'sepal_length': 3.995370468629826, 'sepal_width': 1.6319412605601993    }, 'rose'),
    generic_item({'petal_length': 2.9184620251021887, 'petal_width': 0.6292283203079004, 'sepal_length': 3.5434163219112333, 'sepal_width': 2.3251980636010003    }, ('rose'))
])
    
print(knn_cluster.categorize_item(generate_rose()))